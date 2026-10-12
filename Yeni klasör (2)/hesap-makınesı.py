Sayi1=float(input("Birinci sayiyi giriniz "))
Sayi2=float(input("Ikinci sayiyi giriniz "))  
secim=input("+,-,*,/ islemlerden birini seciniz ")

if secim=="+":
    sonuc=Sayi1+Sayi2
    print(sonuc)
elif secim=="-":
    sonuc=Sayi1-Sayi2
    print(sonuc)
elif secim=="*":
    sonuc=Sayi1*Sayi2
    print(sonuc)
elif secim=="/":
    sonuc=Sayi1/Sayi2
    print(sonuc)