################################
# Author: Ricardo V. M. Torres
# Created:  18/05/2021
################################

# ---WARNINGS---
# This is a Marvin my new Python son.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# IMPORTS
import speech_recognition as sr
import pyttsx3
from googlesearch import search

### FUNCTIONS ###
## Utils ##
def begin():
    x = 1

def google_search(command):
    for result in search()
        return "google"
    return 1

def build_phrase(words):
    frase: str = ''
    for word in words:
        frase += word
    return frase


## ROBOTO ##
# Acha função
def find_func(command):
    command_sliced = command.slice()
    if 'marvin' in command:
        print("Você disse: '" + command + "'")
        if command_sliced[1] == 'google':
            google_search(command)

    else:
        return 1
    return 0

# Abre o microfone e reconhece pt-BR
def ouvir_mic():
    try:
        with sr.Microphone() as source:
            # Chama um algoritmo de redução de ruídos na captura do som
            listener.adjust_for_ambient_noise(source)
            print('ouvindo...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='pt-BR')
            command = command.lower()
            # Quando for estudar erros e acertos, sempre marcar acerto
            # a não ser que o proximo comando indique leitura errada
            # print("Voce disse: "+command+"?")
            find_func(command)
    except sr.UnknownValueError:
        return "Não entendi humano... :? "
    finally:
        return 42

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Olá! Meu nome é {name}')  # Press Ctrl+F8 to toggle the breakpoint.

### MAIN ###
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # object speech recognition creation
    listener = sr.Recognizer()
    # object text to speech creation
    engine = pyttsx3.init()
    # start computing
    begin()
    # first interaction
    print_hi('Marvin')
    # start listening

    print(ouvir_mic())
