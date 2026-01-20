kitaplar = []
kullanicilar = []

stok = 0

while True:
    print("--- Kütüphane Sistemi ---\n",end="")
    print("1-Kitap Ekle\n2-Kitapları Listele\n3-Kitap Ödünç ver\n4-Kitap İade al\n5-Kullanıcı Listele\n6-Çıkış\n",end="")

    secim = input("1-6 arası seçim yap ? : ")

    if secim=="1": # kitap ekle
        k_adi = input("Kitap Adını girin : ")
        kitaplar.append(k_adi)
        stok += 1
        print(f"stok sayısı : {stok}")
        print("kitap başarıyla eklendi")

    elif secim=="2": # kitap listele
        if not kitaplar:
            print("maalesef kitap eklenmedi..")
        else:
            print("---kitap listeleri---\n",end="")
            for kitap in kitaplar:
                print(kitap)
            print("-------Finish-------")
    elif secim=="3": # kitap ödünç ver
        o_ver_kitap = input("ödünç verilecek kitap girin : ")
        if o_ver_kitap not in kitaplar:
            print(f"maalesef {o_ver_kitap}. kitap yok")
        else:
            o_ver_kisi = input("ödünç verilecek kişi girin : ")
            kitaplar.remove(o_ver_kitap)
            kullanicilar.append(o_ver_kisi)
            stok -= 1
            print(f"{o_ver_kitap}.kitap , {o_ver_kisi}.kişiye ödünç verildi.")

    elif secim=="4": # kitap iade al
        k_iade_al = input("hangi kitap iade alıncak ? : ")
        kitaplar.append(k_iade_al)
        print(f"{k_iade_al}.kitap iade alındı..")
        
    elif secim=="5": # kullanıcı listele
        print("---Kullanıcılar Listesi---\n",end="")
        print(f"{kullanicilar}\n",end="")

    elif secim=="6": # çıkış
        print("Kütüphane sisteminden çıkış yapılıyor...")
        break
    else:
        print("lütfen 1 ile 6 arası sayı seç ?")