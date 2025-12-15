# cmd indirme komutu : pip install SpeechRecognition pyaudio
import speech_recognition as sr # SpeechRecognition modulunu iceri alir

def dinle(): 
    r = sr.Recognizer() # taniyici (recognizer) olusturur
    with sr.Microphone() as kaynak: # mikrofonu kaynak olarak kullanmaya baslar
        print("dinleniyor...") # kullaniciya mikrofonun dinlenmeye basladigini bildirir
        ses = r.listen(kaynak) # mikrofonu dinler ve sesi kaydeder
    try:
        audio = r.recognize_google(ses,language="tr-TR") # kaydedilen sesi google'a gonderir ve metne cevirir
        return audio # metni dondurur
    except: # eger hata olursa 
        return "anlayamadım.." # hata mesaji dondurur

metin = dinle() # dinle fonksiyonu calistirir ve sesli komutlari algilar
print("algılanan metin :",metin) # algilanan metni ekrana yazdirir

# ciktisi : algılanan metin : Merhaba