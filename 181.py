from tkinter import *
import speech_recognition as sr
import webbrowser
import pyttsx3
from datetime import datetime
import subprocess

root=Tk()
root.geometry("400x400")
root.config(bg="lightgreen")

label_1=Label(root,text="Bienvenido a tu asistente personal")
label_1.place(relx=0.5,rely=0.1,anchor=CENTER)
button_1=Button(root,text="Iniciar")
button_1.place(relx=0.5,rely=0.2,anchor=CENTER)

var1=pyttsx3.init()
def a (i):
    text_to_speech.say(i)
    text_to_speech.runAndWait() 

def b ():
    var2=sr.Recognizer()
    speak("Como puedo ayudarte")
    with sr.Microphone() as source:
        audio = speech_recognisor.listen(source)
        voice_data=''
        try:
            voice_data=  speech_recognisor.recognize_google(audio, language='es-mx')
        except sr.UnknownValueError:
            print('Por favor, repite. No entendí tu solicitud')
            
    print(voice_data)
    respond(voice_data)

def respond(voice_data):
    if "nombre" in voice_data:
        speak("Mi nombre es cortana")
        print("Mi nombre es cortana")
        
    if "hora" in voice_data:
        speak("La hora es ")
        var3=datetime.now()
        
    
    
    

root.mainloop()
