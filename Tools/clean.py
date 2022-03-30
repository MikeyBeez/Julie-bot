import subprocess


def clean():
    subprocess.call(["rm", "listen.wav"])
    subprocess.call(["rm", "reversed.wav"])
    subprocess.call(["rm", "silenced.wav"])
    subprocess.call(["rm", "speech.wav"])
    subprocess.call(["rm", "speak.mp3"])
