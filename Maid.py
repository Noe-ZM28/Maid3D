import pyttsx3
import pywhatkit
import speech_recognition as sr

name = "Maid" 
listener = sr.Recognizer()
engine = pyttsx3.init()


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
            print("Escuchando...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language='es-ES')
            rec = rec.lower()
            
            if name in rec:
                rec = rec.replace(name, '')
            
            elif 'reproduce' in rec:
                music = rec.replace('reproduce','')
                pywhatkit.playonyt(music)
                print("Reproduciendo " + music)
                talk("Reproduciendo " + music)
                
            else:
                talk("Disculpa, no te he enendido, ¿me lo puedes repetir?")
    except:
        pass
    return rec

def runVA():
    while True:
        try:
            rec = listen()
        except UnboundLocalError:
            talk("No te entendí, intenta de nuevo...")
            continue


if __name__ == '__main__':
    runVA()