#!/bin/env python3
from re import A
import time
from SpeakAndHear import 


# use SpeakAndHear modules to speak text, listen for speech, and convert speech to text.


def __main__():
    SpeakAndHear.speak("What is your name?")
    time.sleep(3)
    Tools.listen()
    text = Tools.C
    print(text)


if __name__ == "__main__":
    __main__()
