import random
import tts

def cube():
	cube =  random.randint(1, 6)
	tts.speak('на кубике выпала цифра: '+ str(cube))

	
