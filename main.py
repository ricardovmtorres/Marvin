################################
# Author: Ricardo V. M. Torres
# Created:  18/05/2021
################################

# ---WARNINGS---
# This is a Marvin may new Python son.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# IMPORTS
import speech_recognition as sr
import pyttsx3


# FUNCTIONS
def begin():
    x = 1


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
            print("Voce disse: "+command+"?")
            if 'marvin' in command:
                print(command)
    except sr.UnknownValueError:
        return "Não entendi humano... :? "
    finally:
        return 42


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Olá! Meu nome é {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# MAIN
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # object speech recognition creation
    # habilita e configura o microfone
    listener = sr.Recognizer()
    # object text to speech creation
    engine = pyttsx3.init()
    begin()
    print_hi('Marvin')
    print(ouvir_mic())
