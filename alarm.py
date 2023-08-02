import datefinder
from playsound import playsound
import datetime
import tts



def alarm(text):
	try:
		time = datefinder.find_dates(text)
		date_and_time = ''
		for date_and_time in time:
		    pass
		date_time = str(date_and_time)
		only_time = date_time[11:]
		tts.speak('будильник поставлен на ' + only_time[:-3])
		hour_time = int(only_time[:-6])
		min_time = int(only_time[3:-3])

		while True:
		    if hour_time == datetime.datetime.now().hour:
		        if min_time == datetime.datetime.now().minute:
		            playsound('alarm sound.mp3')
		        elif min_time <= datetime.datetime.now().minute:
		            break
		        else:
		            pass
		    else:
		        pass
	except:
		pass


