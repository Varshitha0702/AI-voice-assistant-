import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import time
import requests
import os
import json
import logging
import re
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# ------------------ ENVIRONMENT VARIABLES ------------------
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

# ------------------ LOGGING ------------------
logging.basicConfig(
    filename="assistant.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# ------------------ STORAGE ------------------
reminders = []

# ------------------ LOAD CUSTOM COMMANDS ------------------
try:
    with open("commands.json") as f:
        custom_commands = json.load(f)
except:
    custom_commands = {}

# ------------------ SPEAK ------------------
def speak(text):
    try:
        import pyttsx3
        engine = pyttsx3.init()
        engine.setProperty("rate", 170)
        engine.setProperty("volume", 1.0)
        print("Assistant:", text)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except Exception as e:
        print(e)

# ------------------ NORMALIZE ------------------
def normalize(text):
    return text.lower().replace(".", "").replace(":", " : ")

# ------------------ SPEECH INPUT ------------------
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)

    try:
        cmd = r.recognize_google(audio)
        print("You said:", cmd)
        return normalize(cmd)
    except:
        return ""

# ------------------ NLP INTENTS ------------------
INTENTS = {
    "hello": ["hello", "hi"],
    "time": ["time", "current time"],
    "date": ["date", "today date"],
    "email": ["send email", "send mail"],
    "weather": ["weather", "temperature"],
    "search": ["search", "google"],
    "youtube": ["youtube"],
    "wiki": ["who is", "what is", "tell me about"],
    "exit": ["exit", "quit", "stop"]
}

def get_intent(query):
    for intent, words in INTENTS.items():
        for w in words:
            if w in query:
                return intent
    return None

# ------------------ REMINDER ------------------
def parse_time_ampm(text):
    nums = [int(w) for w in text.split() if w.isdigit()]
    if len(nums) < 2:
        return None, None

    h, m = nums[0], nums[1]
    if "pm" in text and h < 12:
        h += 12
    if "am" in text and h == 12:
        h = 0

    if h > 23 or m > 59:
        return None, None

    return h, m

def check_reminders():
    now = datetime.datetime.now()
    for r in reminders[:]:
        if now.hour == r[0] and now.minute == r[1]:
            speak("Reminder. " + r[2])
            reminders.remove(r)

# ------------------ WEATHER ------------------
def get_weather():
    if not WEATHER_API_KEY:
        speak("Weather API key is missing")
        return

    city = "Hyderabad"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"

    try:
        res = requests.get(url, timeout=5)
        data = res.json()
        speak(f"The temperature in {city} is {data['main']['temp']} degree Celsius")
    except:
        speak("Unable to fetch weather")

# ------------------ EMAIL (SENDGRID) ------------------
def clean_email(text):
    text = text.lower().replace(" at ", "@").replace(" dot ", ".").replace(" ", "")
    return text

def send_email():
    if not SENDGRID_API_KEY or not EMAIL_ADDRESS:
        speak("Email service not configured")
        return

    try:
        speak("Tell me the receiver email address")
        receiver = clean_email(take_command())

        if not re.match(r"[^@]+@[^@]+\.[^@]+", receiver):
            speak("Invalid email. Please type it")
            receiver = input("Receiver email: ").strip().lower()

        speak("What is the subject")
        subject = take_command()

        speak("What should I say in the email")
        body = take_command()

        message = Mail(
            from_email=EMAIL_ADDRESS,
            to_emails=receiver,
            subject=subject,
            plain_text_content=body
        )

        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)

        if response.status_code == 202:
            speak("Email sent successfully")
        else:
            speak("Email failed")

    except Exception as e:
        print(e)
        speak("Unable to send email")

# ------------------ START ASSISTANT ------------------
speak("Hello, I am your voice assistant")

while True:
    try:
        query = take_command()
        if not query:
            continue

        logging.info(query)

        # Custom commands
        for cmd, link in custom_commands.items():
            if cmd in query:
                webbrowser.open(link)
                speak("Opening " + cmd)
                break

        # Reminder
        if "set reminder" in query and ("am" in query or "pm" in query):
            h, m = parse_time_ampm(query)
            if h is None:
                speak("Invalid time")
            else:
                speak("What should I remind you")
                msg = take_command()
                reminders.append((h, m, msg))
                speak("Reminder set")

        intent = get_intent(query)

        if intent == "hello":
            speak("Hello, how can I help you")

        elif intent == "time":
            speak(datetime.datetime.now().strftime("%H:%M:%S"))

        elif intent == "date":
            speak(str(datetime.date.today()))

        elif intent == "email":
            send_email()

        elif intent == "weather":
            get_weather()

        elif intent == "search":
            speak("What should I search")
            q = take_command()
            webbrowser.open("https://www.google.com/search?q=" + q)

        elif intent == "youtube":
            webbrowser.open("https://www.youtube.com")
        elif intent == "wiki":
            speak("Searching Wikipedia")
            try:
                topic = query
                for phrase in ["who is", "what is", "tell me about"]:
                    topic = topic.replace(phrase, "")
                topic = topic.strip()
                result = wikipedia.summary(topic, sentences=2)
                speak(result)
            except:
                speak("I could not find information")

        elif intent == "exit":
            speak("Goodbye")
            break

        check_reminders()
        time.sleep(5)

    except Exception:
        speak("Something went wrong. Please try again.")