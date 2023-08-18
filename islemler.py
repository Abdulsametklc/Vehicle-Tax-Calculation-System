def islem():
    
    arac_kodu_str= input("Lütfen işlem yapacağınız aracın kodunu giriniz:")
    

    if  arac_kodu_str.isdigit() and len(arac_kodu_str) != 4:
        print("Girdiğiniz kod hatalı. Lütfen 4 basamaklı araç kodunuzu giriniz.")
    else:    
        arac_kodu = int(arac_kodu_str)
       
        with open("arac_bilgileri.txt", "r",encoding ="utf-8") as file:
            arac_bulundu = any(f"Kodu: {arac_kodu}" in satir for satir in file)  #kodu aratarak o koda sahip aracın olup olmadığını inceliyoruz.
        
        if arac_bulundu:
            print("Araç bulundu, hesaplama yapılabilir.")
            
            arac_verisi = None
            
            with open("arac_bilgileri.txt", "r", encoding = "utf-8") as file:
                for satir in file:
                    if f"Kodu: {arac_kodu}" in satir:
                        arac_verisi = satir
                        break #arac verisine satır bilgilerini aktarıyoruz
            
            
            if arac_verisi:
                veri_parcalari = arac_verisi.split(", ")
                arac_fiyati = float(veri_parcalari[-2].split(": ")[1]) #atanan verilerden fiyatı bulmak için [-2] kullanıyoruz. Ardından fiyatı ifadesini ayırmak için split(":")[1] kullanıyoruz. Ve float ile değeri alırız.
        
                otv_orani = 0.45
                kdv_orani = 0.18
        
                otv = arac_fiyati * otv_orani
                kdv = (arac_fiyati + otv) * kdv_orani
                toplam = arac_fiyati + otv + kdv
        
                print(f"ÖTV: {otv:.2f} TL")
                print(f"KDV: {kdv:.2f} TL")
                print(f"Toplam Vergiler: {otv + kdv:.2f} TL")
                print(f"Toplam Fiyat: {toplam:.2f} TL")
    
            else: print("Belirtilen araç koduyla eşleşen bir veri bulunamadı.")

        else: 
            print("Belirtilen araç koduyla eşleşen bir veri bulunamadı.")