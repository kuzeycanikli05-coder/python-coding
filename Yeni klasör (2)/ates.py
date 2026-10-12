print("Basit Hesap Makinesi")

sayi1 = float(input("Birinci sayiyi gir: "))
islem = input("İslem sec (+, -,*, /): ")
sayi2 = float(input("İkinci sayiyi gir:"))

if islem == "+":
    sonuc = sayi1 + sayi2
elif islem == "-":
    sonuc = sayi1 - sayi2
elif islem == "*":
    sonuc = sayi1 * sayi2
elif islem == "/":
    if sayi ==0:
        print("Bir sayi sifira bolunemez.")
    else:
        sonuc = sayi1 / sayi2
else:
    print("Geçersiz işlem girdin.")

if islem in("+","-","*") or (islem == "/" and sayi2 !=0)  
    print ("Sonuc:",sonuc) 