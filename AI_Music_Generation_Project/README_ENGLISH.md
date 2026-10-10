# AI Music Generation with LSTM — Complete Project

## Project Objective
This project reads MIDI music files, extracts musical note sequences, trains an LSTM deep-learning model to predict the next note, and generates a new melody saved as a MIDI file.

## Project Files
- `main.py` — Loads MIDI files, preprocesses note sequences, trains the LSTM model, generates music, and exports a MIDI file.
- `create_demo_dataset.py` — Creates synthetic demo MIDI files for testing the project without downloading a dataset.
- `dataset/` — Place training `.mid` or `.midi` files here.
- `outputs/` — The generated MIDI file is saved here.
- `requirements.txt` — Lists the required Python libraries.
- `AI_Music_Generation.ipynb` — Google Colab notebook for running the project.
- `REPORT_ENGLISH.md` — Project report in English.

## Run in Google Colab
1. Download and extract the project ZIP on your computer.
2. Open https://colab.research.google.com/ and create a new notebook, or open `AI_Music_Generation.ipynb`.
3. If opening the supplied notebook, run the cells from top to bottom. When prompted, upload the project ZIP file.
4. The notebook installs the required libraries.
5. It creates demo MIDI files in `dataset/`. If you have your own MIDI files, place them in that folder instead or add them before running the training script.
6. Run the training cell:
   ```python
   !python main.py
   ```
7. Download `outputs/generated_music.mid` and open it in MuseScore or another compatible MIDI player.

## Run on Windows
1. Install Python 3.10 or 3.11.
2. Extract the ZIP file and open Command Prompt or Terminal in the project folder.
3. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
4. Install the libraries:
   ```bash
   pip install -r requirements.txt
   ```
5. Generate demo data:
   ```bash
   python create_demo_dataset.py
   ```
6. Train the model and generate music:
   ```bash
   python main.py
   ```

## Output
When execution completes successfully:
- Generated melody: `outputs/generated_music.mid`
- Trained model: `model/music_lstm.keras`
- Note mapping: `model/note_mapping.json`

## Dataset Notes
The included demo dataset is synthetic and intended to test the workflow. For better results, use a larger, varied MIDI dataset that you are permitted to use. Check the license or usage terms of any downloaded data.

## Limitations
This is an educational prototype. It learns pitch sequences but simplifies timing and note duration; it does not fully model rhythm, chords, multiple instruments, or complete song structure. Results depend on dataset quality and size. The generated MIDI is not guaranteed to sound like a polished song.
