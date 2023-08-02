import os
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import tts
import stt

def off():
	text = stt.listen()
	if fuzz.ratio(text, 'да')>60 or fuzz.ratio(text, 'конечно')>60 or fuzz.ratio(text, 'выключай')>60:
		tts.speak('отключаю компьютер')
		os.system('systemctl poweroff')
	elif fuzz.ratio(text, 'нет')>60 or fuzz.ratio(text, 'не надо')>60 or fuzz.ratio(text, 'отмена')>60:
		tts.speak('отменяю выключение')
	
def reboot():
	text = stt.listen()
	if fuzz.ratio(text, 'да')>60 or fuzz.ratio(text, 'конечно')>60 or fuzz.ratio(text, 'перезагружай')>60:
		tts.speak('перезагружаю компьютер')
		os.system('systemctl reboot')
	elif fuzz.ratio(text, 'нет')>60 or fuzz.ratio(text, 'не надо')>60 or fuzz.ratio(text, 'отмена')>60:
		tts.speak('отменяю перезагрузку')
	
	
def gibirnation():
	os.system('systemctl suspend')
		
