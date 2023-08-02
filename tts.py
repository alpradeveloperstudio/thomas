import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 300)
engine.setProperty('volume',1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(text):
	engine.say(text)
	print(text)
	engine.runAndWait()
	engine.stop()
def speakp(text):
	engine.say(text)
	engine.runAndWait()
	engine.stop()
