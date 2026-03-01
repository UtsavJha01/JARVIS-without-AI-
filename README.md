# 🤖 JARVIS – Python Voice Assistant (Offline Version)

JARVIS is a simple Python-based voice assistant inspired by Iron Man’s AI, built **without any paid AI APIs** like OpenAI or Gemini.

This version works completely offline using:
- Speech Recognition
- Text-to-Speech (TTS)
- Basic command automation
- Web browsing automation
- Music playback

Perfect for beginners learning Python automation and voice control systems.

---

## 🚀 Features

- 🎤 Voice Command Recognition
- 🔊 Text-to-Speech Responses
- 🌐 Open Websites (Google, YouTube, etc.)
- 🎵 Play Music from Local Library
- ⏰ Tell Time
- 🧠 Basic Command Processing
- 💻 Lightweight & Offline (No API Cost)

---

## 🛠️ Technologies Used

- Python 3.11.9
- `speech_recognition`
- `pyttsx3`
- `webbrowser`
- `datetime`
- Custom music library module

---
---

---

## 📦 Installation

bash
### 1️⃣ Clone the repository


`git clone https://github.com/yourusername/JARVIS.git
cd JARVIS `
2️⃣ Create Virtual Environment (Recommended)
`python -m venv .venv`

Activate:

Windows

`.venv\Scripts\activate`

Mac/Linux

`source .venv/bin/activate`
3️⃣ Install Dependencies
`pip install -r requirements.txt`


▶️ Run JARVIS
`python main.py`

Make sure your microphone is connected and working.
## 🎯 Example Commands

- "Open Google"
- "Open YouTube"
- "Play music"
- "What is the time?"
- "Open Linkedin"

---

## 🧩 How It Works

1. Listens to your voice input using `speech_recognition`
2. Converts speech to text
3. Processes command using simple `if-else` logic
4. Responds using `pyttsx3` (offline TTS)
5. Executes tasks like opening browser or playing music

---


## 💡 Why No AI?

This version does not use OpenAI or Gemini APIs because:

- API keys require payment
- Free tiers are limited or unstable
- This project focuses on learning automation fundamentals first

Later versions may integrate AI when feasible.

---

## 👨‍💻 Author

**Utsav Kumar Jha**  
Student | Python Enthusiast | Future AI Developer  

---

## ⭐ Support

If you like this project:

- Star the repository ⭐
- Fork it 🍴
- Improve it 💡
- Share it 🚀

---

## 📜 License

This project is open-source and free to use for educational purposes.

---

> "Sometimes you don't need advanced AI to build something cool.  
> You just need curiosity and Python." 🐍
