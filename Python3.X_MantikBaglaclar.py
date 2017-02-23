a = int(input("Birinci Sayiyi (a) Giriniz :"))

b = int(input("Ikinci Sayiyi (b) Giriniz :"))

c = int(input("Ucuncu Sayiyi (c) Giriniz :"))

print("-"*40)

if (a < b and a > c):
    print("a, b ile c arasinda bir sayidir")
else:
    print("a, b ile c arasinda bir sayi degildir")

if a == b and a < c:
    print("a, b'ye esit ayni zamanda c'den kicikdir")
else:
    print("a, b'ye esit ayni zamanda c'den kicik degildir")

if a < b and a < c:
    print("a, b veya c'den daha buyuk degildir")

if (a != b and a != c) and b != c:
    print("Uc sayi birbirine esit degildir")
else:
    print("Uc sayi birbirine esitdir")
    
