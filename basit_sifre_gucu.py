"""
Kullanıcıdan şifre al.
puan = 0 olarak başlat.
Eğer uzunluk ≥ 8 ise puan artır.
Döngü ile her karakteri kontrol et:
Büyük harf varsa puan artır.
Küçük harf varsa puan artır.
Rakam varsa puan artır.
Özel karakter varsa puan artır.
Puan aralığına göre:
0 - 2 → Zayıf
3 - 4 → Orta
5+ → Güçlü
Sonucu yazdır.
"""


sifre = input("Şifre Giriniz : ")
puan = 0

if len(sifre)>=8:
    puan += 1

if any(harf.isupper() for harf in sifre):
    puan+=1    

if any(harf.islower() for harf in sifre):
    puan+=1    

if any(harf.isdigit() for harf in sifre):
    puan+=1    

if any(not harf.isalnum() for harf in sifre):
    puan+=1    

print(f"{puan}.puan aldınız")

if puan<=2:
    print("Şifre Gücü Zayıf")
elif puan<=4:
    print("Şifre Gücü Orta")
elif puan>=5:
    print("Şifre Gücü Güçlü")
else:
    print("Puanın yok")


#SiberAlican