#to check your machines speaker
import pyttsx3

speaker = pyttsx3.init()
speaker.say('hey there , vinayak this side')
speaker.runAndWait()