from bardapi import Bard
import pyttsx3
import speech_recognition as sr
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('COOKIE_KEY')

bard = Bard(token=token)

#  initializing the recognizer class for recognizing speech
r = sr.Recognizer()
engine = pyttsx3.init()

engine.say("Hey, I am your assistant for the day. How can I help you?")
engine.runAndWait()

while True:
    # reading microphone as a source
    ans = ""
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        try:
            # Adjust for 1 second to capture ambient noise
            r.adjust_for_ambient_noise(source, duration=2)
            print("Recognizing...")
            audio_data = r.listen(source)
            # convert speech to text
            text = r.recognize_google(audio_data, language="en-US")

            ans = bard.get_answer(text)['content']

        except sr.UnknownValueError:
            print("Speech recognition could not understand audio")
            engine.say(
                "Sorry,I can not recognise your voice either be in a quite enviroment or you can come after some time!!!")
            engine.runAndWait()
        except sr.RequestError:
            engine.say(
                "Could not request results from Google Speech Recognition service")
            engine.runAndWait()
    answer = ans
    engine.say(answer)
    engine.runAndWait()
