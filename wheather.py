from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
import tts

owm = OWM('Ваш  API key')
mgr = owm.weather_manager()

def OWMp():
	observation = mgr.weather_at_place('Город')
	w = observation.weather
	status = w.detailed_status
	temp = w.temperature('celsius')['temp']
	temp1 = w.temperature('celsius')['feels_like']
	humidity = w.humidity
	
	tts.speak('В '+ 'Город'+' сейчас ' + str(status) +
			  '\nТемпература ' + str(round(temp))+ '°c ощущается как '+str(round(temp1))+'°c' +
			  '\nВлажность ' + str(humidity) + "%" + 
			  '\nСкорость ветра ' + str(w.wind()['speed']) + " метров в секунду")
				
