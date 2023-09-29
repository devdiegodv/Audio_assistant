import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# listen our mic and give back the audio as text
def transform_audio_in_text():
    # save recognizer in var
    r = sr.Recognizer()

    with sr.Microphone() as origin:
        # cooldown
        r.pause_threshold = 0.8

        print("You can talk")

        # save audio
        audio = r.listen(origin)

        try:
            # search in google
            order = r.recognize_google(audio, lenguaje="es-ar")