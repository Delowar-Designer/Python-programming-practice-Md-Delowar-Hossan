#5 Text to Speech using python
import pyttsx3

text_speech = pyttsx3.init()
text = input("Please enter your Text- ")

text_speech.say(text)
text_speech.runAndWait()
