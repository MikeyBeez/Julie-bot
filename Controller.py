#!/bin/env python3
import time
import SpeakAndHear

# use SpeakAndHear modules to speak text, listen for speech, and convert speech to text.


def main():

    SpeakAndHear.speak("Hello, world!")
    time.sleep(3)
    SpeakAndHear.speak("What is your name?")
    time.sleep(3)
    SpeakAndHear.listen()
    text = SpeakAndHear.C
    print(text)


main()
