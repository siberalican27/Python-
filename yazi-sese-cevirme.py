# cmd indirme komutu : pip install gTTS playsound
from gtts import gTTS
from playsound import playsound
import time
import os

def konusma(metin):
    tts = gTTS(text=metin, lang="tr",slow=False) # metni sese donusturme 
    tts.save("cevap.mp3") # dosya olusturma ve dosya adi ve uzantisi
    playsound("cevap.mp3") # otomatik cal 
    os.remove("cevap.mp3") # caldiktan sonra silme

metin = "Buraya girilecek metni seslendirir.." 
konusma(metin) 