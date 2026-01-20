baslangic_para = int(input("ana para şuan ne kadar ? : "))
while True:
    print("--- Basit Atm Simulasyonu ---\n",end="")
    print("1-Bakiye Görüntüleme\n2-Para Yatır\n3-Para Çek\n4-Çıkış\n",end="")
    secim = input("1-4 arası seçim yap : ")
    if secim=="1": # bakiye görüntüleme
        print(f"ana paran şuan : {baslangic_para}")
    elif secim=="2": # para yatır
        p_yatir = int(input("yatırılacak miktar gir : "))
        baslangic_para = baslangic_para + p_yatir
        print(f"güncel bakiye : {baslangic_para} ")
    elif secim=="3": # para çek
        p_cek = int(input("çekilecek miktar gir : "))
        if p_cek>baslangic_para:
            print(f"bakiye yetersiz , güncel bakiye : {baslangic_para}")
        else:
            baslangic_para = baslangic_para - p_cek
            print(f"para başarıyla çekildi , kalan bakiye : {baslangic_para}")
    elif secim=="4": # çıkış
        print("sistemden çıkış yapılıyor...")
        break
    else:
        print("1 ile 4 arası sayı seç ")