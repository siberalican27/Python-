d_sayisi = 0
y_sayisi = 0

print("===Mini Quiz ===\n",end="")
# soru 1
s1 = input("1- Python bir programlama dili midir ? (e/h) : ")
s1_cevap = "e"
if s1==s1_cevap:
    d_sayisi +=1
    print("Doğru Cevap!")
else:
    y_sayisi +=1
    print("Yanlış Cevap")
# soru 2
s2 = input("2- 2:2+5 = 6 midir ? (e/h) : ")
s2_cevap = "e"
if s2==s2_cevap:
    d_sayisi +=1
    print("Doğru Cevap!")
else:
    y_sayisi +=1
    print("Yanlış Cevap")

# soru 3
s3 = input("3- siyah şapkalı hacker kötü biri midir ? (e/h) : ")
s3_cevap = "e"
if s3==s3_cevap:
    d_sayisi +=1
    print("Doğru Cevap!")
else:
    y_sayisi +=1
    print("Yanlış Cevap")

print(f"3 sorudan {d_sayisi} dogru , {y_sayisi} yanlış var")