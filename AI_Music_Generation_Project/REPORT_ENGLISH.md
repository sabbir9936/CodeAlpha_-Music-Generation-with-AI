# Project Report: AI-Based Music Generation Using an LSTM Neural Network

## 1. Project Title
**AI Music Generation with LSTM**

## 2. Objective
The objective of this project is to process MIDI music files, extract musical note sequences, train an LSTM model to learn note patterns, and generate a new note sequence that can be saved and played as a MIDI file.

## 3. Introduction
Artificial Intelligence can learn patterns from musical data and use those patterns to generate new sequences. This project demonstrates a beginner-level AI music generation pipeline using MIDI files and a Long Short-Term Memory (LSTM) neural network. The model learns to predict the next note from a sequence of previous notes. The predicted notes are then combined into a new melody and exported as a MIDI file.

## 4. Tools and Technologies
- Python
- TensorFlow and Keras
- NumPy
- pretty_midi
- Google Colab or a local Python environment
- MuseScore or another compatible MIDI player

## 5. Dataset
The input dataset consists of `.mid` or `.midi` files. The project includes a script named `create_demo_dataset.py` that creates synthetic MIDI patterns for testing. For a stronger experiment, a larger and more diverse MIDI dataset should be used. Always check the license and permitted uses of downloaded datasets.

## 6. Methodology
1. **Data Collection:** MIDI files are placed in the `dataset/` directory.
2. **Data Preprocessing:** The program reads non-drum instruments and extracts note pitch values.
3. **Sequence Preparation:** A sequence of 16 notes is used as input, and the following note is used as the target.
4. **Model Building:** An LSTM neural network is created using Embedding, LSTM, Dropout, and Dense layers.
5. **Model Training:** The model learns to predict the next note from training sequences.
6. **Music Generation:** The trained model predicts notes one by one to create a new sequence.
7. **MIDI Export:** The generated pitches are converted into a simple piano melody and saved as a MIDI file.

## 7. System Architecture
**MIDI Dataset → Note Extraction → Sequence Preparation → LSTM Training → Note Prediction → MIDI Export → MIDI Player**

## 8. Expected Output
After successful execution, the program creates `outputs/generated_music.mid`. This file can be opened in MuseScore or another compatible MIDI player. The trained model is saved as `model/music_lstm.keras`, and the note mapping is saved as `model/note_mapping.json`.

## 9. Results and Discussion
The program reports the number of MIDI files and notes loaded, the number of training sequences, and the model training progress. If execution succeeds, a generated MIDI file is produced. The musical quality depends on the size and diversity of the training dataset. The included synthetic demo data is intended mainly to verify that the pipeline works; it is not expected to produce professional-quality music.

## 10. Limitations
- The model mainly learns pitch sequences.
- Rhythm, note duration, chords, and overall song structure are simplified.
- A small or repetitive dataset may lead to repetitive or unnatural melodies.
- TensorFlow must be installed in a compatible Python environment.

## 11. Future Improvements
- Represent note duration, timing, and velocity in addition to pitch.
- Train on a larger, clean, and appropriately licensed MIDI dataset.
- Add chord progressions and multiple instruments.
- Experiment with model architecture and sampling temperature.
- Convert the generated MIDI into WAV or MP3 audio for easier playback.

## 12. Conclusion
This project demonstrates an end-to-end educational pipeline for AI-based music generation. It includes MIDI data processing, LSTM model training, sequence generation, and MIDI export. The project provides a practical introduction to sequence modeling and deep learning for music.
