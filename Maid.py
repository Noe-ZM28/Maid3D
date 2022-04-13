from traceback import print_tb
import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia
import datetime
import keyboard

name = "computadora" 
listener = sr.Recognizer()
engine = pyttsx3.init()
KEY = None

voices = engine.getProperty('voices')
#ver voces instaladas
#for voice in voices:
#    print(voice) 

engine.setProperty('voice', voices[1].id) # 1 para español o 0 para ingles

engine.setProperty('rate', 178)
engine.setProperty('volume', 0.7)

def talk (text):
   engine.say(text)
   engine.runAndWait()
#

def listen():
    try:
        print('Escuchando...')
        with sr.Microphone() as source:
            voice = listener.listen(source)
            listener.adjust_for_ambient_noise(source, 0.5)
            rec = listener.recognize_google(voice,
                                            key=KEY,
                                            language='es-MX')
            rec = rec.lower()
        

    except sr.UnknownValueError:
        pass#talk("Disculpa, no te he entendido, ¿me lo puedes repetir?")
    except:
        pass
    return rec

def runVA():
    while True:
        try:
            rec = listen()   
            print(f"Escuchando>: {rec}")  
            if name in rec:
                rec = rec.replace(name, '')
                if 'reproduce' in rec:
                    music = rec.replace('reproduce','')
                    pywhatkit.playonyt(music)
                    print(f"Reproduciendo>: {music}")
                    talk(f"Reproduciendo {music}")
                elif 'repite' in rec:
                    repeat = rec.replace('repite','')
                    talk(repeat)
                elif "busca":
                    search = rec.replace('busca', '')
                    wikipedia.set_lang('es')
                    wiki = wikipedia.summary(search, 1)
                    talk(f'Buscando...{search}')
                    print(f"{search}>: {wiki}")
                    talk(wiki)
                # else:
                #     talk("Comando desconocido")
            elif "termina":
                talk("Hasta pronto")
                break

    
        except UnboundLocalError:
            #talk("No te entendí, intenta de nuevo...")
            continue


if __name__ == '__main__':
    runVA()
