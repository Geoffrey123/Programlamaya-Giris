def main():
    try:
        no = int(input("Notunuzu Giriniz :"))
        
        if no > 0 and no <= 100:
            
            if no > 90 and no <= 100:
                print("Harf notunuz A")
            elif no > 80 and no <= 90:
                print("Harf notunuz B")
            elif no > 70 and no <= 80:
                print("Harf notunuz C")
            elif no <= 70:
                print("Harf notunuz F")
                
        else:
            print("Hata aldiniz !\nLutfen notunuzu dogru giriniz !")
    
    except:
        print("Hata aldiniz !\nLutfen bir sayi giriniz !")

if __name__ == "__main__":
    main()
