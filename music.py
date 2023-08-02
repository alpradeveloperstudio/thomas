import os
import random
import tts

def music():
    files = os.listdir('music')
    random_file = f'music/{random.choice(files)}'
    os.system(f'xdg-open {random_file}')
    tts.speak(f'включаю {random_file.split("/")[-1]}')
    
