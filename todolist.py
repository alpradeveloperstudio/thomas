import tts
import stt

def task():
    
    query = stt.listen()
        
    with open('todo-list.txt', 'a') as file:
        file.write(f'! {query}\n')
        
    tts.speak(f'Задача {query} добавлена в список дел')
