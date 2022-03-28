import gtts
import pyaudio
import subprocess
# import os

def speak(text):
# convert text to speech
    tts = gtts.gTTS(text, lang="en")
    tts.save("speak.mp3")
    # play the speech
    subprocess.call(["mpg321", "speak.mp3"])

        