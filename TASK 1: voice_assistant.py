import speech_recognition as sr
import pyttsx3
import webbrowser
import requests
from datetime import datetime

recognizer= sr.Recognizer()
tts_engine=pyttsx3.init()

def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening..")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
        try:
            command=recognizer.recognize_google(audio)
            print(f"Recognized: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not hear that")
            return None
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return None

def open_chrome():
    speak("Opening Google Chrome")
    webbrowser.open("http://www.google.com")

def open_youtube():
    speak("Opening YouTube")
    webbrowser.open("https://www.youtube.com")

def get_time():
    now = datetime.now().strftime("%H:%M:%S")
    speak(f"The current time is {now}")

def open_weather():
    speak("Showing weather details")
    webbrowser.open("https://www.google.com/search?q=weather+now&oq=weather+now&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDM4NzJqMGoxqAIAsAIA&sourceid=chrome&ie=UTF-8")

def main():
    speak("Hello, how can I help you?")
    while True:
        command = listen()
        if command:
            if "open chrome" in command:
                open_chrome()
            elif "open youtube" in command:
                open_youtube()
            elif "what time is it" in command:
                get_time()
            elif "what is today's weather" in command:
                open_weather()
            elif "exit" in command or "quit" in command:
                speak("Goodbye!")
                break

if __name__ == "__main__":
    main()
