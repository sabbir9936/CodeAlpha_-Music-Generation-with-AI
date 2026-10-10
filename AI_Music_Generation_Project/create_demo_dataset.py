"""
Create small, synthetic MIDI files so the project can be tested without
downloading a dataset. These are simple generated note patterns, not real songs.
"""
from pathlib import Path
import random

try:
    import pretty_midi
except ImportError:
    raise SystemExit("Install dependencies first: pip install -r requirements.txt")

OUT_DIR = Path("dataset")
OUT_DIR.mkdir(exist_ok=True)

random.seed(7)

# Several simple note patterns in a comfortable piano range.
patterns = [
    [60, 62, 64, 67, 64, 62, 60, 55, 60, 64, 67, 72],
    [60, 64, 67, 64, 62, 65, 69, 65, 60, 64, 67, 72],
    [67, 69, 71, 72, 71, 69, 67, 64, 62, 64, 67, 60],
    [60, 60, 67, 67, 69, 69, 67, 65, 65, 64, 64, 62, 62, 60],
    [60, 63, 65, 68, 65, 63, 60, 56, 60, 65, 68, 72],
    [62, 64, 65, 69, 65, 64, 62, 57, 62, 65, 69, 74],
    [65, 67, 69, 72, 69, 67, 65, 60, 65, 69, 72, 77],
    [60, 64, 67, 71, 67, 64, 62, 65, 69, 72, 67, 60],
]

for idx, base_pattern in enumerate(patterns, start=1):
    midi = pretty_midi.PrettyMIDI(initial_tempo=100 + idx * 2)
    piano = pretty_midi.Instrument(program=0)
    time = 0.0
    for j, pitch in enumerate(base_pattern * 5):
        # Small variation makes the demo data less repetitive.
        varied_pitch = max(48, min(84, pitch + random.choice([-1, 0, 0, 0, 1])))
        duration = random.choice([0.25, 0.3, 0.4])
        piano.notes.append(
            pretty_midi.Note(
                velocity=random.randint(75, 105),
                pitch=varied_pitch,
                start=time,
                end=time + duration
            )
        )
        time += duration + random.choice([0.03, 0.05, 0.08])
    midi.instruments.append(piano)
    midi.write(str(OUT_DIR / f"demo_{idx:02d}.mid"))

print(f"Created {len(patterns)} demo MIDI files in: {OUT_DIR.resolve()}")
print("These are synthetic demo patterns. Replace/add your own MIDI files for better results.")
