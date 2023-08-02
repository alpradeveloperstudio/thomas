from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
import tts

owm = OWM('de07f938cf0d4a14219686e5fc7d77d3')
mgr = owm.weather_manager()

def OWMp():
	observation = mgr.weather_at_place('Ферма')
	w = observation.weather
	status = w.detailed_status
	temp = w.temperature('celsius')['temp']
	temp1 = w.temperature('celsius')['feels_like']
	humidity = w.humidity
	
	tts.speak('В посёлке ферма сейчас ' + str(status) +
			  '\nТемпература ' + str(round(temp))+ '°c ощущается как '+str(round(temp1))+'°c' +
			  '\nВлажность ' + str(humidity) + "%" + 
			  '\nСкорость ветра ' + str(w.wind()['speed']) + " метров в секунду")
				
