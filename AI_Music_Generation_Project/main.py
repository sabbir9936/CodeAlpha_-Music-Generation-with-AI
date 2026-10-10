"""
AI Music Generation with LSTM
- Reads MIDI files from ./dataset
- Trains a small next-note prediction model
- Generates ./outputs/generated_music.mid
- Saves the trained model and note mapping
"""
from pathlib import Path
import json
import random
import numpy as np

try:
    import pretty_midi
    import tensorflow as tf
    from tensorflow.keras import Sequential
    from tensorflow.keras.layers import LSTM, Dense, Dropout, Embedding
    from tensorflow.keras.callbacks import EarlyStopping
except ImportError as exc:
    raise SystemExit(
        "Missing dependency. Run: pip install -r requirements.txt\n"
        f"Details: {exc}"
    )

DATA_DIR = Path("dataset")
OUTPUT_DIR = Path("outputs")
MODEL_DIR = Path("model")
OUTPUT_DIR.mkdir(exist_ok=True)
MODEL_DIR.mkdir(exist_ok=True)

SEQUENCE_LENGTH = 16
EPOCHS = 30
BATCH_SIZE = 32
GENERATED_NOTES = 160
TEMPERATURE = 0.9
RANDOM_SEED = 42

random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)
tf.random.set_seed(RANDOM_SEED)


def load_midi_notes(folder: Path):
    """Read note pitches from non-drum instruments in all MIDI files."""
    midi_files = sorted(list(folder.glob("*.mid")) + list(folder.glob("*.midi")))
    if not midi_files:
        raise FileNotFoundError(
            f"No MIDI files found in '{folder}'. Run "
            "'python create_demo_dataset.py' or add your own .mid files."
        )

    all_notes = []
    loaded = 0
    for path in midi_files:
        try:
            midi = pretty_midi.PrettyMIDI(str(path))
            file_notes = []
            for instrument in midi.instruments:
                if not instrument.is_drum:
                    # Sort by start time so notes follow the melody timeline.
                    for note in sorted(instrument.notes, key=lambda n: n.start):
                        file_notes.append(int(note.pitch))
            if file_notes:
                all_notes.extend(file_notes)
                loaded += 1
                print(f"Loaded {path.name}: {len(file_notes)} notes")
        except Exception as exc:
            print(f"Skipping unreadable file {path.name}: {exc}")

    if len(all_notes) <= SEQUENCE_LENGTH:
        raise ValueError(
            f"Only {len(all_notes)} notes were found. Add more/larger MIDI files."
        )
    print(f"\nLoaded {loaded} MIDI files; total notes: {len(all_notes)}")
    return all_notes


def prepare_sequences(notes):
    """Convert pitch values to integer IDs and build training windows."""
    unique_notes = sorted(set(notes))
    note_to_id = {pitch: idx for idx, pitch in enumerate(unique_notes)}
    encoded = [note_to_id[pitch] for pitch in notes]

    X, y = [], []
    for i in range(len(encoded) - SEQUENCE_LENGTH):
        X.append(encoded[i:i + SEQUENCE_LENGTH])
        y.append(encoded[i + SEQUENCE_LENGTH])

    X = np.asarray(X, dtype=np.int32)
    y = np.asarray(y, dtype=np.int32)
    return X, y, unique_notes, encoded


def build_model(vocab_size: int):
    model = Sequential([
        Embedding(input_dim=vocab_size, output_dim=64),
        LSTM(128, return_sequences=True),
        Dropout(0.2),
        LSTM(64),
        Dense(vocab_size, activation="softmax")
    ])
    model.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"]
    )
    return model


def sample_next_note(probabilities, temperature=1.0):
    """Sample a note with temperature; lower values are more predictable."""
    probabilities = np.asarray(probabilities, dtype=np.float64)
    probabilities = np.log(np.maximum(probabilities, 1e-8)) / max(temperature, 1e-3)
    probabilities = np.exp(probabilities - np.max(probabilities))
    probabilities /= probabilities.sum()
    return int(np.random.choice(len(probabilities), p=probabilities))


def generate_music(model, seed, unique_notes, count=GENERATED_NOTES):
    generated = list(seed[-SEQUENCE_LENGTH:])
    for _ in range(count):
        window = np.asarray([generated[-SEQUENCE_LENGTH:]], dtype=np.int32)
        probabilities = model.predict(window, verbose=0)[0]
        generated.append(sample_next_note(probabilities, TEMPERATURE))
    return [unique_notes[note_id] for note_id in generated[len(seed[-SEQUENCE_LENGTH:]):]]


def save_as_midi(pitches, path: Path):
    """Write generated pitches as a simple piano melody MIDI."""
    midi = pretty_midi.PrettyMIDI(initial_tempo=110)
    piano = pretty_midi.Instrument(program=pretty_midi.instrument_name_to_program("Acoustic Grand Piano"))
    start = 0.0
    for pitch in pitches:
        duration = 0.30
        piano.notes.append(
            pretty_midi.Note(
                velocity=90,
                pitch=int(pitch),
                start=start,
                end=start + duration
            )
        )
        start += 0.34
    midi.instruments.append(piano)
    midi.write(str(path))


def main():
    print("=" * 56)
    print("AI MUSIC GENERATION WITH LSTM")
    print("=" * 56)
    notes = load_midi_notes(DATA_DIR)
    X, y, unique_notes, encoded = prepare_sequences(notes)

    print(f"Training sequences: {len(X)}")
    print(f"Unique pitches: {len(unique_notes)}")

    model = build_model(len(unique_notes))
    model.summary()
    callbacks = [
        EarlyStopping(monitor="loss", patience=5, restore_best_weights=True)
    ]
    model.fit(
        X, y,
        epochs=EPOCHS,
        batch_size=BATCH_SIZE,
        validation_split=0.1 if len(X) >= 30 else 0.0,
        callbacks=callbacks,
        verbose=1
    )

    model_path = MODEL_DIR / "music_lstm.keras"
    model.save(model_path)
    with open(MODEL_DIR / "note_mapping.json", "w", encoding="utf-8") as f:
        json.dump({"unique_notes": unique_notes, "sequence_length": SEQUENCE_LENGTH}, f)

    seed = encoded[-SEQUENCE_LENGTH:]
    generated_pitches = generate_music(model, seed, unique_notes)
    output_path = OUTPUT_DIR / "generated_music.mid"
    save_as_midi(generated_pitches, output_path)

    print("\nDONE!")
    print(f"Model saved to: {model_path}")
    print(f"Generated MIDI saved to: {output_path}")
    print("Open the MIDI file with MuseScore or another MIDI player to listen.")
    print("\nImportant: this beginner model learns pitch sequences only; timing and")
    print("chords are simplified. More varied MIDI training data improves results.")


if __name__ == "__main__":
    main()
