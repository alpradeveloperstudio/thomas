import random
import tts

def coin():
	coin =  random.randint(1, 2)
	if coin ==1:
		tts.speak('выпал орёл')
	else:
		tts.speak('выпала решка')
	
