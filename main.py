from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import words
import tts
import stt
from timet import time
from coin import coin
from cube import cube
from music import music
import offpc
from todolist import task
from threading import Thread
from alarm import alarm
from wheather import OWMp
from randfact import fact
import opener
from hello import hello
import websearch

def recognize(data, vectorizer, clf):
    words = ('найди', 'найти', 'ищи', 'кто такой', 'что такое', 'открой', 'видео')
    data = str(data)
    trg = words.TRIGGERS.intersection(data.split(' '))
    if trg:
        data = data.replace(list(trg)[0], '').strip()
    else:
        return
    print(data.startswith(('поставь будильник', 'установи будильник', 'запусти будильник')))
        
    if data.startswith(('поставь будильник', 'установи будильник', 'запусти будильник')):
    	t = Thread(target=alarm, args=(data,))
    	t.start()
    	return	
    elif data.startswith(words):
    	websearch.web_search()
    	
    	
    else:
        text_vector = vectorizer.transform([data]).toarray()[0]
        answer = clf.predict([text_vector])[0]
        func_name = answer.split()[0]
        answer = answer.replace(func_name, '')
        tts.speak(answer)

        if func_name == 'coin':
            coin()
        elif func_name == 'cube':
            cube()
        elif func_name == 'music':
            music()
        elif func_name == 'time':
            time()
        elif func_name == 'pcoff':
            offpc.off()
        elif func_name == 'reboot':
            offpc.reboot()
        elif func_name == 'hibernation':
            offpc.gibirnation()
        elif func_name == 'todo':
            task()
        elif func_name == 'wheather':
            OWMp()
        elif func_name == 'fact':
            fact()   
        elif func_name == 'browser':
            opener.browser()
        elif func_name == 'systemmonitor':
            t = Thread(target=opener.systemmonitor, args=(data,))
            t.start()
        elif func_name == 'terminal': 
            opener.terminal()
        elif func_name == 'file':
            opener.filemenager()     
        elif func_name == 'hello':
            hello()       	    






def main():
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(list(words.data_set.keys()))

    clf = LogisticRegression()
    clf.fit(vectors, list(words.data_set.values()))

    del words.data_set
    while True:
        text = stt.listen()
        recognize(text, vectorizer,clf)

main()
