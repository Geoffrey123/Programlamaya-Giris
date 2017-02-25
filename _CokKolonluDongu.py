# Liste ureticileri vasitasiyla listelerimizi  uretiyoruz 
list1 = [i for i in range(15, 100, 15)]
list2 = [i for i in range(5, 35, 5)]
list3 = [i for i in range(100, 40, -10)]
list4 = [(i *2) for i in range(1, 64) if 64 % i == 0]
# uretiktden sonra for dongusu ile ekranda yaziyoruz
for i in range(0, 6):
    print("{}\t{}\t{}\t{}".format(list1[i], list2[i], list3[i], list4[i]))
