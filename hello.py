import random
import tts
import datetime

def hello():
    current_date_time = datetime.datetime.now()
    current_time = str(current_date_time.time())[:5]
    hours = current_time[3:]
    hours = int(hours)
    coin =  random.randint(1, 4)
    if coin ==1:
        tts.speak('привет')
    if coin ==2:
        tts.speak('хеллоу')
    if coin ==3:
        tts.speak('здравствуй')
    else:
        if hours >6 and hours <=12:
            tts.speak('доброе утро')
        elif hours >12 and hours <=18:
            tts.speak('добрый день')
        elif hours >18 and hours <=23:
            tts.speak('добрый вечер')	
        else:
            tts.speak('доброй ночи')	
