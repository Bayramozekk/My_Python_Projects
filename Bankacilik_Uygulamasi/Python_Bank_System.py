hesaplar = {}   # yapılacak nesneleri içeri almak için açılan sözlük

#--banka class ını oluşturulduğu kısım--#
class BankaHesabi:
    def __init__(self, kullanici, bakiye, ParaBirimi, sifre):
        self.kullanici = kullanici
        self.bakiye = bakiye
        self.ParaBirimi= ParaBirimi
        self.sifre = sifre
        self.history = []

    def ParaCekme(self, miktar):
        if miktar <= 0 :
            print("Girdiğiniz tutar pozitiv olmalıdır.")
        elif miktar > self.bakiye :
            print ("Yetersiz bakiye :(")
        else:
            self.bakiye -= miktar
            self.history.append(f"{miktar} {self.ParaBirimi} hesabınızdan çekildi. Güncel bakiyeniz:{self.bakiye} {self.ParaBirimi}")
     
    def ParaYatirma(self, miktar):
        if miktar <=0:
            print("Girdiğiniz tutar pozitiv olmalıdır.")
        else:
            self.bakiye += miktar
            self.history.append(f"{miktar} {self.ParaBirimi} hesabınıza yatırıldı. Güncel bakiyeniz:{self.bakiye} {self.ParaBirimi} ")

    def gecmis(self):
        return(self.history) 


print("Bankamıza hoşgeldiniz ;)\n")

while True:    
    print("Hesap oluşturmak için '1' \nVar olan hesabınıza giriş yapmak için '2' yazınız.")
    veri = input("hangi işlemi yapmak istiyorsunuz: ")

#--kullanıcıdan veri alarak her kullanıcıya bir banka hesabı nesnesi tanımlama kısmı--#

    if veri =="1" :
        while True:
            KullaniciAdi = input("Lütfen bir kullanıcı adı yazın (kullanıcı adınız türkçe karakter ve boşluk içermesin): ")
            if KullaniciAdi in hesaplar:
                print("girdiğiniz kullanıcı adı zaten mevcut  lütfen başka bir kullanıcı adı deneyiniz")
            else:
                break
        Kullanici = input("Adınız ve soyadınız: ")
        parabirimi = input("hesabınızda kullanacağınız para birimi: ")

        while True:    
            parola = input("Şifre giriniz: ")
            parola_kontrol = input("Şifreyi tekrar giriniz: ")
            if parola != parola_kontrol:
                print("girdiğiniz parolalar uyuşmuyor  lütfen tekrar deneyiniz.")
            else:
                break
        
        yeni_hesap= BankaHesabi(Kullanici, 0, parabirimi, parola) #yeni_hesap artık nesneyi sözlüğe taşıyacağımız araç
        hesaplar[KullaniciAdi] = yeni_hesap 
        print("\n")
        print("Hesabınız başarılı bir şekilde oluşturuldu \n")

    #--kullanıcının hesabına girip işlem yapmasını sağlayan kısım--#
        
    elif veri == "2":

        while True:
            kullanici_sorgula = input("Lütfen kullanıcı adnızı yazın: ")
            if kullanici_sorgula not in hesaplar:
                print("girdiğiniz kullanıcı adı sistemimize tanımlı değil lütfen tekrar deneyiniz deneyiniz")
            else:
                break
        guncel_kullanici=hesaplar[kullanici_sorgula]
        while True:
            parola_sorgula = input("Lütfen şifrenizi giriniz.")
            if parola_sorgula != guncel_kullanici.sifre:
                print("girdiğiniz şifre eksik veya hatalıdır lütfen tekrar deneyiniz")
            else:
                break

        while True:
            print("lütfen yapmak istediğiniz işlemi girin \n")
            print("para yatırmak için = 1 \n" \
            "para çekmek için = 2 \n" \
            "hesap hareketleri için = 3 \n" \
            "hesabınızdan çıkmak için = 4")
            islem = input("yapacağınız işlem: ")
            if islem == "1" :
                miktar= float(input("ne kadar para yatıracaksınız: "))
                guncel_kullanici.ParaYatirma(miktar)

            elif islem == "2" :
                miktar= float(input("ne kadar para çekeceksiniz: "))
                guncel_kullanici.ParaCekme(miktar)

            elif islem == "3" :
                Gecmis = guncel_kullanici.gecmis()
                print("-------İşlem Geçmişi-------")
                for degisim in Gecmis:
                    print(degisim)
            else :
                break 
    else:
        break
