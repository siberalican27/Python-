import os

while True:
    print("********** KİŞİSEL NOT TUTMA **********\n",end="")

    print("1-Not Ekleme\n2-Not Görüntüleme\n3-Not Arama\n4-Not Güncelleme\n5-Not Silme\n6-Çıkış\n",end="")

    secim = input("alican burdan yapmak istediğin seçenek numarasını yaz : ")

    if secim=="1": # not ekleme
        klasor_adi = input("Alican klasör ismi gir oluşturalım : ")
        dosya_adi = input("Alican dosya ismini gir (örnek:dosya_adi.txt) şeklinde : ")

        os.makedirs(klasor_adi, exist_ok=True)

        dosya_yolu = os.path.join(klasor_adi,dosya_adi)

        with open(dosya_yolu,"a",encoding="utf-8") as f:
            f.write(input("Alican dosyaya ne eklemek istiyorsun : ") + "\n")
        print(f"{dosya_yolu} oluşturuldu alican")
    
    elif secim=="2": # not görüntüleme
        klasor_adi = input("klasör adını yaz alican içindeki dosyaları listelim : ")
        for dosya in os.listdir(klasor_adi):
            print(dosya)
        dosya_ac = input("hangi dosyayı açmak istiyorsun alican : ")
        dosya_yolu = os.path.join(klasor_adi,dosya_ac)
        with open(dosya_yolu,"r",encoding="utf-8") as f:
            icerik = f.read()
        print(icerik)
    
    elif secim=="3": # not arama
        klasor_adi = input("klasör adını gir alican : ")
        dosya_adi = input("dosya adını gir alican : ")
        dosya_yolu = os.path.join(klasor_adi,dosya_adi)
        if os.path.exists(dosya_yolu):
            arama = input("aranacak kelime gir alican : ")
            with open(dosya_yolu,"r",encoding="utf-8") as f:
                icerik = f.read()
            if arama in icerik:
                print(f"{arama}.metin dosya da bulundu alican")
            else:
                print(f"{arama} metni dosya da bulunamadı alican")
        else:
            print("belirtilen dosya bulunamadı alican")


   
    elif secim=="4": # not güncelleme
        klasor_adi = input("klasör adını gir alican : ")
        dosya_adi = input("dosya adını gir alican : ")

        dosya_yolu = os.path.join(klasor_adi,dosya_adi)

        if os.path.exists(dosya_yolu):
            eski_metin = input("güncellenecek metni gir alican : ")
            yeni_metin = input("yeni metni gir alican : ")

            with open(dosya_yolu,"r",encoding="utf-8") as f:
                icerik = f.read()
            icerik = icerik.replace(eski_metin,yeni_metin)
            
            with open(dosya_yolu,"w",encoding="utf-8") as f:
                f.write(icerik)
            print("dosya başarıyla degiştirildi alican")
        else:
            print("belirtilen dosya bulunamadı alican")
    
    elif secim=="5": # not silme
        klasor_adi = input("klasör adını gir alican : ")
        dosya_adi = input("dosya adını gir alican : ")

        dosya_yolu = os.path.join(klasor_adi,dosya_adi)

        if os.path.exists(dosya_yolu):
            silinecek = input("silinecek metni yaz alican : ")

            with open(dosya_yolu,"r",encoding="utf-8") as f:
                icerik = f.read()
            
            icerik = icerik.replace(silinecek + "\n", "")

            with open(dosya_yolu,"w",encoding="utf-8") as f:
                f.write(icerik)
            
            print(f"{silinecek} silindi alican ")
        else:
            print("belirtilen dosya yok alican kontrol et")
    
    elif secim=="6": # çıkış
        print("alican sistemden çıkış yapılıyor...")
        break





















