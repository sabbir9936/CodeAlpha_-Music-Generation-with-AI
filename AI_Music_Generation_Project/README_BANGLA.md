# AI Music Generation with LSTM — সম্পূর্ণ প্রজেক্ট

## প্রজেক্টের উদ্দেশ্য
MIDI music dataset থেকে musical note-এর pattern শেখানো এবং LSTM deep-learning model ব্যবহার করে নতুন note sequence তৈরি করে MIDI ফাইল হিসেবে সংরক্ষণ করা।

## কী কী আছে?
- `main.py` — MIDI পড়া, data preprocessing, LSTM training, নতুন melody তৈরি এবং MIDI export।
- `create_demo_dataset.py` — পরীক্ষা করার জন্য synthetic demo MIDI ফাইল তৈরি করে।
- `dataset/` — এখানে training MIDI ফাইল রাখতে হবে।
- `outputs/` — generated MIDI ফাইল এখানে থাকবে।
- `requirements.txt` — প্রয়োজনীয় Python libraries।
- `REPORT_BANGLA.md` — assignment report-এর খসড়া।

## Google Colab-এ চালানোর সহজ পদ্ধতি
1. https://colab.research.google.com/ খুলে New Notebook তৈরি করো।
2. নিচের command চালিয়ে library install করো:
   ```python
   !pip install pretty_midi numpy tensorflow
   ```
3. এই ZIP-এর ফাইলগুলো Colab-এ upload করো অথবা Google Drive-এ project folder রাখো।
4. `create_demo_dataset.py` চালাও। এটি `dataset/` folder-এ demo MIDI বানাবে।
5. `main.py` চালাও:
   ```python
   !python main.py
   ```
6. তৈরি হওয়া `outputs/generated_music.mid` download করো এবং MuseScore বা MIDI player-এ শুনো।

## নিজের dataset ব্যবহার
`dataset/` folder-এ নিজের `.mid` অথবা `.midi` ফাইল যোগ করো। Demo file-গুলো সরিয়ে বা রেখে নিজের data দিয়ে experiment করতে পারো। Dataset-এর ব্যবহার-অনুমতি/লাইসেন্স নিশ্চিত করবে।

## Windows-এ চালানোর পদ্ধতি
1. Python 3.10 বা 3.11 install করো।
2. ZIP extract করো।
3. project folder-এ Command Prompt/Terminal খোলো।
4. চালাও:
   ```bash
   python -m venv .venv
   ```
   Windows:
   ```bash
   .venv\Scripts\activate
   ```
5. library install:
   ```bash
   pip install -r requirements.txt
   ```
6. demo data বানাও:
   ```bash
   python create_demo_dataset.py
   ```
7. train ও generate:
   ```bash
   python main.py
   ```

## Output
সফলভাবে চললে `outputs/generated_music.mid` তৈরি হবে। Model `model/music_lstm.keras` হিসেবে save হবে।

## Limitations
এটি শিক্ষামূলক beginner prototype। Model note pitch-এর sequence শেখে; note duration, tempo variation, chords ও musical structure পুরোপুরি শেখে না। Demo dataset synthetic ও ছোট, তাই ফলাফল পেশাদার গান হবে না। ভালো ফলাফলের জন্য অনুমোদিত, বৈচিত্র্যময় MIDI dataset ব্যবহার করতে হবে।
