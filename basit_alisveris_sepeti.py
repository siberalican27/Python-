sepettekiler = []
toplam_fiyat = 0
elma = 5
ekmek = 10
sut = 20
while True:
    print("=== Alışveriş Sepeti ===\n",end="")
    print("1-Ürünleri Görüntüle\n2-Sepete Ürün Ekle\n3-Sepeti Görüntüle\n0-Çıkış\n",end="")
    secim = input("Seçim yap : ")
    if secim=="1":
        print("---Mevcut Ürünler ---\n",end="")
        print("1-Elma = 5 TL\n2-Ekmek = 10 TL\n3-Süt = 20 TL\n",end="")
    elif secim=="2":
        print("---Mevcut Ürünler ---\n",end="")
        print("1-Elma = 5 TL\n2-Ekmek = 10 TL\n3-Süt = 20 TL\n",end="")
        sec = input("Sepete eklemek istediğiniz ürün numarası girin (çıkmak için 0) :")
        if sec=="1":
            print("Elma sepete eklendi")
            sepettekiler.append("elma")
            toplam_fiyat += elma
        elif sec=="2":
            print("Ekmek Sepete Eklendi")
            sepettekiler.append("ekmek")
            toplam_fiyat += ekmek
        elif sec=="3":
            print("Süt Sepete Eklendi")
            sepettekiler.append("süt")
            toplam_fiyat += sut
        elif sec=="0":
            continue
        else:
            print("maalesef seçtiğin seçenek liste de yok tekrar dene")
    elif secim=="3":
        print("---Sepetteki Ürünler---\n",end="")
        for sepet in sepettekiler:
            print(sepet)
        print(f"Toplam Tutar : {toplam_fiyat}")
    elif secim=="0":
        break
    else:
        print("lütfen yukarıdaki seçeneklerden birini seç")