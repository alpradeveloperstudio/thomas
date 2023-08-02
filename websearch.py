import webbrowser
import tts
import stt
from pywhatkit import playonyt
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def web_search(search):
    mode = ''

    youtube = ['найди видео', 'найди на ютубе', 'найти на ютубе', 'найди на youtube','найти видео', 'ищи видео', 'ищи на ютубе', 'ютуб', 'ютюбе', 'найди на ютюбе' 'видео', 'открой на ютубе', 'открой видео']

    words = ['найди', 'найти', 'ищи', 'кто такой', 'что такое', 'открой']
    remove = ["пожалуйста", "ладно", "давай", "сейчас", '']

    try:
        if mode == '':
            for i in range(len(youtube)):
                if youtube[i] in search:
                    mode = 'youtube'

        if mode == '':
            for i in range(len(words)):
                if words[i] in search:
                    mode = 'web'
    except:
    	pass

    if mode == 'youtube':
        for i in youtube:
            search = search.replace(i, '')
            for j in remove:
                search = search.replace(j, '')
                search = search.strip()

        tts.speak(f'Ищу {search} на ютубе')
        webbrowser.open(f'https://www.youtube.com/results?search_query={search}')
        tts.speak("Желаете сразу открыть первое видео?")
        text = stt.listen()
        print(text)
        if (fuzz.ratio(text, 'давай') > 60) or (fuzz.ratio(text, 'да') > 60) or (fuzz.ratio(text, "открой") > 60) or (fuzz.ratio(text, "открывай") > 60):
            tts.speak('Открываю видео')
            playonyt(search)
        elif fuzz.ratio(self.text, 'нет') > 60 or (fuzz.ratio(self.text, "не надо") > 60):
                tts.speak("Как пожелаете")
        
    elif mode == 'web':
        for i in words:
            search = search.replace(i, '')
            for j in remove:
                search = search.replace(j, '')
                search = search.strip()
        tts.speak(f"Ищу {search}")
        webbrowser.open(f'https://www.google.com/search?q={search}&oq={search}81&aqs=chrome..69i57j46i131i433j0l5.2567j0j7&sourceid=chrome&ie=UTF-8')
    pass
     
    
 
 
