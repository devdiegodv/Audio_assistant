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
            order = r.recognize_google(audio, language="es-ar")
            # test
            print("You have said: " + order)
            return order

        # if it can't hear the audio
        except sr.UnknownValueError:
            print("Oooops, i didn't understand.")
            return "I keep waiting"

        # if order is damaged
        except sr.RequestError:
            print("Oooops, no service (order).")
            return "I keep waiting"

        # unenspected error
        except:
            print("Oooops, there's something wrong.")
            return "I keep waiting"

# the assistant can be heard
def talk(message):

    # turn on pyttsx3's engine
    engine = pyttsx3.init()
    engine.setProperty('voice', english_voice_id)

    # pronounce message
    engine.say(message)
    engine.runAndWait()


spanish_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'
english_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

talk("What's going on son of a bitch, what you doing?")