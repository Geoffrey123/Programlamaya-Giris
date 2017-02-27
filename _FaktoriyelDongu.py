def faktorial(sayi):
    cevab = 1
    for i in range(1, (sayi+1)):
        cevab *= i
    return cevab

if __name__ == "__main__":
    try:
        deger = int(input("Lutfen bir deger giriniz :"))
        print("Girdiyiniz degerin faktoriyeli {}".format(faktorial(deger)))
    except:
        print("Lutfen bir tam sayi giriniz !")
