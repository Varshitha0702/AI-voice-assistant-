# AI-voice-assistant-
A mini Alexa-like voice assistant built using Python with real-time speech processing and automation.

# 🎙️ AI Voice Assistant

🚀 A Python-based intelligent voice assistant with automation, NLP, and real-world integrations

---

## 🌟 Project Vision

Traditional voice assistants are either too basic or too complex to build from scratch.

This project aims to:

* Build a **practical, scalable voice assistant**
* Combine **AI + automation + real-world APIs**
* Deliver a **hands-on Alexa/Siri-like experience using Python**

---

## 🧭 What This System Does

The assistant listens to voice commands, understands intent, and performs real-world actions like:

* Responding to queries
* Sending emails
* Setting reminders
* Fetching live weather data
* Performing web & knowledge searches
* Executing user-defined custom commands

---

## 🧠 Core Capabilities

### 🎤 Voice Input Processing

* Real-time speech capture via microphone
* Noise adjustment for better recognition
* Converts speech → normalized text

---

### 🧩 Intent Recognition Engine

* Rule-based NLP system using keyword matching
* Maps user queries to predefined intents
* Lightweight and efficient (no heavy ML models)

```python
INTENTS = {
    "hello": ["hello", "hi"],
    "time": ["time"],
    "email": ["send email"],
}
```

---

### 🔗 Custom Command Engine

* Dynamically loads commands from `commands.json`
* Enables extensibility without code changes

👉 Example:

* “open github” → opens GitHub
* “open youtube” → opens YouTube

---

### ⏳ Reminder Management System

* Voice-based reminder creation
* Supports AM/PM time parsing
* Periodic checker triggers reminders automatically

---

### 📬 Email Automation Module

* Sends emails using SendGrid API
* Converts spoken email into valid format
* Validates input before sending

---

### 🌍 External API Integrations

#### 🌦️ Weather Service

* Fetches real-time temperature using OpenWeather API
* Handles API failures gracefully

#### 📚 Knowledge Retrieval

* Wikipedia integration for quick summaries
* Returns concise 2-line answers

#### 🌐 Web Navigation

* Google search via voice
* Direct YouTube access

---

### 🔊 Response Generation (TTS)

* Converts text → speech using `pyttsx3`
* Adjustable speed and volume
* Provides real-time feedback

---

### 🛡️ Reliability & Logging

* Logs all user commands (`assistant.log`)
* Handles:

  * Speech recognition failures
  * Invalid inputs
  * API/network errors
* Prevents system crashes

---

### 🔐 Secure Configuration

* Uses environment variables for sensitive data:

  * `EMAIL_ADDRESS`
  * `SENDGRID_API_KEY`
  * `WEATHER_API_KEY`
* Ensures secure and clean codebase

---

## 🔄 Execution Flow

```text
Voice Input → Speech Recognition → Text Normalization  
→ Intent Detection → Task Execution → Voice Response
```

---

## 🧰 Technology Stack

* **Python**
* SpeechRecognition
* pyttsx3
* SendGrid API
* OpenWeather API
* Wikipedia API
* Requests
* JSON

---

## 📁 Project Layout

```text
voice_assistant/
│
├── voice_assistant.py   # Core assistant logic
├── commands.json        # Custom command mappings
├── assistant.log        # Runtime logs
├── README.md
```

---

## 🗣️ Example Interactions

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

## ⚙️ Getting Started

### 1️⃣ Install Dependencies

```
pip install speechrecognition pyttsx3 wikipedia requests sendgrid
```

---

### 2️⃣ Configure Environment Variables

```
setx EMAIL_ADDRESS "your_email"
setx SENDGRID_API_KEY "your_sendgrid_key"
setx WEATHER_API_KEY "your_weather_key"
```

Restart terminal after setup.

---

### 3️⃣ Run the Application

```
python voice_assistant.py
```

---

## 🔬 How It Works

1. User gives voice input
2. Speech is converted to text
3. Query is normalized and analyzed
4. Intent is detected
5. Corresponding module executes task
6. Assistant responds via voice

---

## 🏆 Key Strengths

* Real-time voice-based interaction
* Lightweight NLP intent system
* Multi-feature automation (Email, Weather, Reminders)
* JSON-based extensibility
* Robust error handling

---

## 🚀 Future Scope

* GUI / Web-based interface
* Multi-language voice support
* ChatGPT-based conversational AI
* Smart home (IoT) integration
* Continuous listening mode

---

## ⚠️ Important Notes

* Ensure microphone permissions are enabled
* Internet connection required for APIs
* Never expose API keys publicly

---

## 👨‍💻 About the Project

This project demonstrates:

* AI-driven interaction systems
* Voice-based UI design
* API integration & automation
* Modular Python architecture

---

## 📌 Bonus (For Resume Use)

This project is highly valuable for:

* AI/ML roles
* Software engineering interviews
* Hackathons (HackWithInfy 🔥)
