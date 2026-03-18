# AI-voice-assistant-
A mini Alexa-like voice assistant built using Python with real-time speech processing and automation.


# 🎙️ AI Voice Assistant

🚀 A Python-based intelligent voice assistant with automation, NLP, and real-world integrations

---

## 💡 Why This Project?

Most beginner voice assistants only respond to fixed commands.

This project goes beyond that by implementing:

* **Intent-based command understanding**
* **Real-time voice interaction**
* **Task automation (Email, Weather, Web, Reminders)**
* **Custom command extensibility**

👉 It behaves like a **mini Alexa/Siri built from scratch using Python**.

---

## 🚀 Overview

This voice assistant listens to user commands via microphone, processes them using intent recognition, and performs tasks such as:

* Answering queries
* Sending emails
* Setting reminders
* Fetching weather updates
* Searching web & Wikipedia
* Executing custom commands

---

## ✨ Key Features

### 🎤 Speech Recognition

* Uses `SpeechRecognition` library
* Converts real-time voice → text
* Handles ambient noise for better accuracy

---

### 🧠 Intent-Based NLP System

* Custom intent mapping system:

```python
INTENTS = {
    "hello": ["hello", "hi"],
    "time": ["time"],
    "email": ["send email"],
    ...
}
```

* Matches user queries to actions dynamically
* Lightweight NLP without heavy frameworks

---

### 🔗 Custom Commands (Dynamic)

* Loads commands from JSON file
* Example: 

👉 You can add your own commands without changing code
(e.g., "open github", "open youtube")

---

### ⏰ Smart Reminder System

* Voice-based reminder creation
* Supports AM/PM parsing
* Background checker triggers reminders at exact time

---

### 📧 Email Automation (SendGrid API)

* Sends emails via voice commands
* Converts spoken email (e.g., “abc at gmail dot com”)
* Validates email format before sending

---

### 🌦️ Weather Integration

* Uses OpenWeather API
* Fetches real-time temperature
* Handles API failures gracefully

---

### 🌐 Web & Knowledge Search

* Google search via voice
* Wikipedia summaries (2-line concise answers)
* YouTube quick access

---

### 🔊 Text-to-Speech Response

* Uses `pyttsx3`
* Adjustable speech rate & volume
* Real-time voice feedback

---

### 🛡️ Error Handling & Logging

* Logs all commands (`assistant.log`)
* Handles:

  * Speech errors
  * API failures
  * Invalid inputs
* Prevents crashes with fallback responses

---

### 🔐 Environment-Based Security

* Uses environment variables:

  * `EMAIL_ADDRESS`
  * `SENDGRID_API_KEY`
  * `WEATHER_API_KEY`
* Keeps sensitive data secure

---

## 🧩 System Architecture

```text
Voice Input (Microphone)
        ↓
Speech Recognition
        ↓
Query Normalization
        ↓
Intent Detection
        ↓
Command Execution Engine
        ↓
API Calls / Automation
        ↓
Voice Response (TTS)
```

---

## 🛠️ Tech Stack

* Python
* SpeechRecognition
* pyttsx3
* SendGrid API
* OpenWeather API
* Wikipedia API
* Requests
* JSON (for custom commands)

---

## 📂 Project Structure

```text
voice_assistant/
│
├── voice_assistant.py   # Main logic
├── commands.json        # Custom commands
├── assistant.log        # Logs (auto-generated)
├── README.md
```

---

## 🎥 Sample Commands

```
User: Hello
Assistant: Hello, how can I help you

User: What is the time
Assistant: 14:32:10

User: Send email
Assistant: Tell me the receiver email address

User: Set reminder at 5 30 pm
Assistant: What should I remind you
```

---

## ⚙️ Setup & Run

### 1️⃣ Install Dependencies

```
pip install speechrecognition pyttsx3 wikipedia requests sendgrid
```

---

### 2️⃣ Set Environment Variables

```
setx EMAIL_ADDRESS "your_email"
setx SENDGRID_API_KEY "your_sendgrid_key"
setx WEATHER_API_KEY "your_weather_key"
```

Restart terminal after this.

---

### 3️⃣ Run the Assistant

```
python voice_assistant.py
```

---

## 🧪 Example Workflow

* User speaks command
* Speech → text
* Intent detected
* Corresponding function executed
* Response spoken back

---

## 🏆 Highlights

* Real-time voice interaction
* Intent-based NLP system
* Email + Weather API integration
* Custom command extensibility (JSON-based)
* Modular and scalable design

---

## 🔮 Future Improvements

* GUI / Web interface
* Multi-language support
* AI conversation (ChatGPT integration)
* Smart home control
* Continuous listening mode

---

## 📌 Note

* Ensure microphone permissions are enabled
* Internet connection required for APIs
* Keep API keys secure

---

## 👨‍💻 Author

Built as a practical project to demonstrate:

* **AI + Automation**
* **Voice Interfaces**
* **Real-world API integration**

