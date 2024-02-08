import speech_recognition as sr
from gtts import gTTS
import random
from os import remove
from playsound import playsound
from time import sleep
import response_list
import enterlist
import time
import webbrowser
import pygame
from tkinter import *

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice = r.recognize_google(audio,language="tr-TR")
        return voice




def speak(enter):
    tts = gTTS(text= enter,lang="tr")
    file = "name"+str(random.randint(1,1000))+".mp3"
    tts.save(file)
    playsound(file)
    remove(file)

#print("dinleniyor")
#metin = listen()
#print(metin)

def examination(el,rl,yazı):#el enterlistteki listeyi,rl responselistteki listeyi,yazı dinlenilen şeyi dikkatli bak
    for i in el:
        if i in yazı:
            speak(random.choices(rl)[0])
            break






def reply(texture):

    examination(el=enterlist.selam,rl=response_list.selam,yazı=texture)                       #selam

    for i in enterlist.arama:                                                                 #arama
        if i in texture:
            speak(random.choices(response_list.arama)[0])
            while True:
                try:
                    enter_url = listen()
                    break
                except sr.UnknownValueError:
                    speak("sizi tam anlayamadım bir daha söyler misiniz ?")
                    print("Dinlemede")

            url = "https://www.google.com/search?q="+enter_url
            webbrowser.open(url)
            speak("{}{}".format(enter_url,random.choices(response_list.arama_1)[0]))
            break

    for i in enterlist.kapatma:                                                                #kapatma
        if i in texture:
            speak(random.choices(response_list.kapatma)[0])
            exit()

    for i in enterlist.müzik:
        if i in texture:
            speak(random.choices(response_list.müzik)[0])
            print("Dinlemede")
            while True:
                try:
                    name = listen()+".mp3"
                    name = name.lower()
                    break
                except sr.UnknownValueError:
                    speak("sizi tam anlayabildiğimi düşümüyorum tekrar dener misiniz")
                    print("Dinlemede")

            root = Tk()
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load("{}".format(name))
            pygame.mixer.music.play()
            sleep(5)
            pygame.mixer.music.stop()


            root.mainloop()
            break

    for i in enterlist.dosya:
        if i in texture:
            speak("Dosyanın adı ne olsun")
            print("Dinlemede")
            while True:
                try:
                    ad = listen()
                    break
                except sr.UnknownValueError:
                    speak("sizi duyamadım tekrar eder misiniz")
                    print("Dinlemede")



            speak("Dosyanın uzantısı ne olsun")
            tip = "."+input("Lütfen bu alana giriniz:")
            doc = open(ad+tip,"w")
            doc.close()
            speak(random.choices(response_list.dosya)[0])
            break



speak("Limon sistemi başlatılıyor")
speak("selamu aleyküm ben Limon sizi dinliyorum. Nasıl yardım edebilirim")
sleep(0.5)
while True:
    try:
        print("Dinlemede")
        metin = str(listen())
        print("Siz: "+metin)
        reply(str(metin).lower())
        metin = ""
    except sr.UnknownValueError:
        speak("anlayamadım")


