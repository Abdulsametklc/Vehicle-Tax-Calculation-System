import main
def arac_ekle():
    
    while True:
        arac_marka =input("Araç Markası: ")
        arac_model =input("Araç Modeli: ")
        arac_yili =input("Araç Yılı: ")
        arac_rengi =input("Araç Rengi: ")
        arac_tipi = input("Araç Tipi: ")
        arac_fiyati = input("Aracın Fiyatı: ")
        arac_kodu_str = input("Aracınıza özel 4 basamaklı kod veriniz: ") #input ile kullanıcıdan araç bilgilerini istiyoruz.
        
        if not arac_kodu_str.isdigit() or len(arac_kodu_str) != 4: #girilen araç kodunun sayı ve 4 basamaklı koddan oluştuğunu inceliyoruz.
            print("Lütfen araç kodunu 4 basamaklı sayıdan oluşacak şekilde giriniz.")
        
        else:
            arac_kodu = int(arac_kodu_str) #araç kodunu int'e çevirip yeni değişkene atıyoruz
            
            
            with open("arac_bilgileri.txt", "r", encoding = "utf-8") as file: #Girilen araç kodunun listede mevcut olan araçlarda var olup olmadığını kontrol ediyoruz.
                satirlar = file.readlines()
                for satir in satirlar:
                    if "Kodu: "+ str(arac_kodu) in satir:
                        print(f"{arac_kodu} numaralı kod sistemde bulunmaktadır. Lütfen farklı kod ile kaydediniz.")
                        break
                
                else: #araç kodu listede başka bir araçta yok ise aracı listeye ekliyoruz.
                    with open("arac_bilgileri.txt", "a", encoding = "utf-8") as file:
                       file.write("Markası: " + arac_marka+  ", " + "Modeli: " + arac_model + ", " + "Üretim Yılı: " + arac_yili + ", " + "Rengi: " + arac_rengi + ", " + "Tipi: " + arac_tipi + ", " + "Fiyatı: " + arac_fiyati + ", " + "Kodu: " + str(arac_kodu) + "\n")
                       print(f"{arac_marka} markalı aracınız {arac_kodu} numaralı araç kodu ile sisteme yüklenmiştir.")
                    main.main() #dönüde tekrar araç eklemesin diye main fonksiyonunu çağırarak meniye geri dönüyoruz.

                   
