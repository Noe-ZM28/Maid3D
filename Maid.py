import pyttsx3
import pywhatkit
import speech_recognition as sr

name = "computadora" 
listener = sr.Recognizer()
engine = pyttsx3.init()
KEY = None


voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # 1 para español o 0 para ingles
engine.setProperty('rate', 178)
engine.setProperty('volume', 0.7)

#ver voces instaladas
#for voice in voices:
#    print(voice) 

def talk (text):
   engine.say(text)
   engine.runAndWait()

#

def listen():
    try:
        with sr.Microphone() as source:
            voice = listener.listen(source)
            listener.adjust_for_ambient_noise(source, 0.5)
            rec = listener.recognize_google(voice,
                                            key=KEY,
                                            language='es-MX')
            rec = rec.lower()
            print("Escuchando>: "+rec)
            
            if name in rec:
                rec = rec.replace(name, '')
            
                if 'reproduce' in rec:
                    music = rec.replace('reproduce','')
                    pywhatkit.playonyt(music)
                    print("Reproduciendo>: " + music)
                    talk("Reproduciendo " + music)
                elif 'repite' in rec:
                    repeat = rec.replace('repite','')
                    talk(repeat)
                else:
                    talk("Comando desconocido")
            elif "finaliza": exit()

    except sr.UnknownValueError:
        talk("Disculpa, no te he entendido, ¿me lo puedes repetir?")
    except:
        pass
    return rec

def runVA():
    while True:
        try:
            rec = listen()
        except UnboundLocalError:
            #talk("No te entendí, intenta de nuevo...")
            continue


if __name__ == '__main__':
    runVA()