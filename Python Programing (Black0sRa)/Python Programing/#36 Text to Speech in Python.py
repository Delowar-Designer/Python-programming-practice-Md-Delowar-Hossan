# Text to Speech in Python
import pyttsx3

blackosra = pyttsx3.init()

voices = blackosra.getProperty('voices')
blackosra.setProperty('voice', voices[0].id)

name = "I am a Programmeer Delowar.Designer"
blackosra.save_to_file(name, 'blackosraTestSound.mp3')

blackosra.say(name)
blackosra.runAndWait()