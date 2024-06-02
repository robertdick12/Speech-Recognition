import speech_recognition as sr
import webbrowser
from time import ctime

r = sr.Recognizer()

def record_audio(ask = False):
        with sr.Microphone() as source:
            if ask:
                 print(ask)
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            voice_data = ''

            try:
                voice_data = r.recognize_google(audio)
            except sr.UnknownValueError:
                print("Sorry, I did not get that")
            except sr.RequestError as e:
                print(f"Sorry, Could not request results {e}")
            except OSError as e:
                print(f"Could not access the microphone; {e}")
            return voice_data
        
def respond(voice_data):
     if 'what is your name' in voice_data:
          print('My name is ROBDOTCOM')        
     if 'what time is it' in voice_data:
          print(ctime())  
     if 'search' in voice_data:
       search = record_audio('what do you want to search for?') 
       url = 'https://google.com/search?q=' + search
       webbrowser.get().open(url)
       print('Here is what i found on ' + search)  
     if 'find location' in voice_data:
       location = record_audio('what is the location?') 
       url = 'https://google.nl/maps/place/' + location + '/&amp'
       webbrowser.get().open(url)
       print('Here is the location of ' + location)  



print("How may i assist you today")  
voice_data = record_audio()
respond(voice_data)


