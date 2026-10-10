# 🎵 AI Music Generation using LSTM

An AI-powered **Music Generation System** built with Python and Deep Learning. This project uses Long Short-Term Memory (LSTM) neural networks to learn musical note patterns from MIDI files and generate new melodies using Artificial Intelligence.

---

## 📌 Project Overview

- **Project:** AI Music Generation using LSTM
- **Domain:** Artificial Intelligence & Deep Learning
- **Task:** Music Generation with AI
- **Model:** Long Short-Term Memory (LSTM)
- **Output:** AI-generated MIDI music files

---

## ✨ Features

- 🎹 **MIDI Dataset Processing:** Loads MIDI files and extracts musical note sequences for training.
- 🧹 **Data Preprocessing:** Converts musical notes into numerical sequences suitable for deep learning.
- 🧠 **LSTM Neural Network:** Trains a deep learning model to learn patterns in musical sequences.
- 🎼 **AI Music Generation:** Predicts new musical notes based on previously learned patterns.
- 💾 **MIDI File Export:** Saves generated melodies as MIDI files for playback.
- 📊 **Model Saving:** Saves the trained model for future experiments.
- ☁️ **Google Colab Support:** Supports running the project in Google Colab or a local Python environment.

---

## 🛠️ Tech Stack

- **Programming Language:** Python 3.x
- **Deep Learning:** TensorFlow, Keras
- **Data Processing:** NumPy
- **MIDI Processing:** pretty_midi
- **Development Environment:** Google Colab / VS Code
- **Music Playback:** MuseScore or a compatible MIDI player

---

## ⚙️ How It Works

1. **Data Collection:** Collect MIDI music files for training.
2. **Preprocessing:** Extract note pitches from MIDI files.
3. **Sequence Preparation:** Convert notes into numerical sequences.
4. **Model Training:** Train an LSTM neural network to predict the next musical note.
5. **Music Generation:** Generate new note sequences using the trained model.
6. **MIDI Conversion:** Export the generated melody as a MIDI file.
7. **Playback:** Open the generated MIDI file in compatible music software.

---

## 📂 Project Structure

```text
AI-Music-Generation/
├── dataset/
├── outputs/
├── model/
├── main.py
├── create_demo_dataset.py
├── requirements.txt
├── AI_Music_Generation.ipynb
└── README.md
```

---

## 🚀 Installation & Usage

**1. Clone the repository**

```bash
git clone https://github.com/YOUR-USERNAME/AI-Music-Generation.git
cd AI-Music-Generation
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Create demo MIDI data**

```bash
python create_demo_dataset.py
```

**4. Train the model and generate music**

```bash
python main.py
```

**5. Listen to the generated music**

After successful execution, the generated MIDI file will be saved at:

```text
outputs/generated_music.mid
```

Open the file in MuseScore or another compatible MIDI player to listen to the generated melody.

---

## 📈 Future Improvements

- Improve rhythm and note-duration generation.
- Generate chord progressions and multi-instrument music.
- Train with larger and more diverse MIDI datasets.
- Convert generated MIDI files into WAV or MP3 audio.
- Develop a graphical user interface for interactive music generation.
- Experiment with advanced deep learning architectures.

---

## ⚠️ Limitations

This project is an educational prototype. The current implementation primarily learns note-pitch sequences and simplifies rhythm and timing. The quality of generated music depends on the size and diversity of the training dataset.

---

## 🎯 Learning Outcomes

- Understanding Artificial Intelligence and Deep Learning.
- Learning how LSTM neural networks process sequential data.
- Working with MIDI files and musical note sequences.
- Applying data preprocessing and model training techniques.
- Exploring AI-based creative applications.

---

## 👨‍💻 Author

**Sabbir Ahmed**

- **GitHub:** [@sabbir9936](https://github.com/sabbir9936)
- **LinkedIn:** [Sabbir Ahmed](https://www.linkedin.com/in/sabbirahmed9936)

---

⭐ If you find this project interesting, consider giving the repository a star!

