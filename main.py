import islemler
import arac_ekle
import arac_sil
import arac_goster
def main():
    
    while True:
        print("1.Sisteme araç ekle")
        print("2.Sistemden araç sil")
        print("3.İstediğin aracın ÖTV ve KDV fiyatını hesapla")
        print("4.Araçları göster")
        print("0.Çıkış yap")
        islem = input("Seçiminiz:")
        
        if islem == "1":
            arac_ekle.arac_ekle()
        
        elif islem == "2":
            arac_sil.arac_sil()
            
        elif islem == "3":
            islemler.islem()
            
        elif islem == "4":
            arac_goster.arac_goster()
        
        elif islem == "0":
            print("Programdan çıkılıyor...")
            break
            
        else:
            print("Hatalı seçim yaptınız. Lütfen tekrar deneyiniz.")
            
            
            
if __name__ == "__main__":
    main()