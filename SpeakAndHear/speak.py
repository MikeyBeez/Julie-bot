import gtts
import pyaudio
import subprocess

def speak(text):
    tts = gtts.gTTS(text, lang="en")
    tts.save("speak.mp3")
    subprocess.call(["mpg321", "speak.mp3"])

        