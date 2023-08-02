import datetime
import tts

def time():
	current_date_time = datetime.datetime.now()
	current_time = str(current_date_time.time())[:5]
	hours = current_time[3:]
	minuts = current_time[:2] 
	print('сейчас ' + current_time)
	tts.speakp('сейчас '+ hours +' часов'+ minuts + ' минут' )
