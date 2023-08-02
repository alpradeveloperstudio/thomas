import requests
from bs4 import BeautifulSoup
import tts
 
def fact():
    fact_url = "https://randstuff.ru/fact/"
    response = requests.get(fact_url)
    soup = BeautifulSoup(response.content, 'html.parser').findAll('td')
    items = list(soup)
    funny_fact = items[0]
    tts.speak(str(funny_fact).replace('<td>', '').replace('</td>', '').replace('  ', ' '))
