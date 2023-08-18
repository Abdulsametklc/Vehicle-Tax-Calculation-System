def arac_sil():
    while True:
        
        arac_sil_kodu_str = input("Silinecek aracın kodunu giriniz:")
        if not arac_sil_kodu_str.isdigit() or len(arac_sil_kodu_str) != 4: # silinmek istenen aracın kodunun 4 basamaklı ve sayısal değer olup olmadığını kullanarak kontrol ediyoruz.
            print("Girdiğiniz kod geçerli değildir. Lütfen 4 basamaklı ve araca ait kodu giriniz:")
            
        else:
            arac_sil_kodu = int(arac_sil_kodu_str) #yeni değişkene int olarak atıyoruz.
            arac_bulundu = False #bir değişkene false değeri atayarak koşullarımızı oluşturuyoruz.
            
            with open("arac_bilgileri.txt", "r",encoding="utf-8") as file:
                satirlar = file.readlines()
                
            with open("arac_bilgileri.txt", "w", encoding = "utf-8") as file:
                for satir in satirlar:
                    if str(arac_sil_kodu) not in satir:
                        file.write(satir) # eğer araç listede yok ise en alttaki if-else koşuluna girerek false değeri ile uyarı mesajı veriyor ve tekrar kodu istiyor.
                    else:
                        arac_bulundu = True # eğer ki kontroller sonucu araç var ise else bloğuna girip değişkene true atıyoruz ve alttaki if-else koşulunda aracın silindiğine dair bilgi veriyoruz.
                
                if arac_bulundu:
                    print(f"{arac_sil_kodu} numaralı araç listeden silinmiştir.")
                    break
                
                else:
                    print(f"{arac_sil_kodu} numaralı araç listede bulunmamaktadır.")                    
        
        
        