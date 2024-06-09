import os

class Musteri():
    def __init__(self,TC,ISIM,SIFRE):
        self.tc = TC
        self.isim = ISIM
        self.sifre = SIFRE
        self.bakiye = 0


class Banka():
    def __init__(self):
        self.musteriler = list()
    
    def musteri_ol(self,TC,ISIM,SİFRE):
        self.musteriler.append(Musteri(TC,ISIM,SİFRE))
        print("İnternet bankacılığa kayıt olduğunuz için teşekkür ederiz...")

banka = Banka()
menu = "Ana menüye dönmek için enter'a basınız."
while True:
    os.system("cls")
    print("""
            ZALEF BANKASINA HOŞ GELDİNİZ
          
        0) Kapat
        1) Müşteriyim
        2) Müşteri Olmak İstiyorum
          
        """)
    secim = input("İşlemi seçiniz : ")
    if secim == "0":
        print("Çıkış yapılıyor...\nYine bekleriz...")
        exit(1)
    elif secim == "1":
        girilen_tc = input("TC no giriniz : ")
        tc_no = [a.tc for a in banka.musteriler]
        if girilen_tc in tc_no:
            for musteri in banka.musteriler:
                if girilen_tc == musteri.tc:
                    girilen_sifre = input("Şifrenizi girin : ")
                    if girilen_sifre == musteri.sifre:
                        while True:
                            os.system("cls")
                            print("""
                                        ZALEF BANKASINA HOŞ GELDİNİZ
                                    0) Çıkış
                                    1) Bakiye Sorgula
                                    2) Para Yatır
                                    3) Para Transfer Et
                                    4) Para Çek""")
                            secim2 = input("İşlem numarasını giriniz : ")
                            if secim2 == "0":
                                print("Hesabınızdan çıkış yapılıyor...")
                                input(menu)
                                break
                            elif secim2 == "1":
                                print("Bakiyeniz : {}".format(musteri.bakiye))
                                input(menu)
                            elif secim2 == "2":
                                yatirilan_tutar = int(input("Miktar : "))
                                onay = input("Kendi hesabınıza {} TL para yatırmayı onaylıyor musunuz? (E/H) : ")
                                if onay == "e"or onay=="E":
                                    musteri.bakiye += yatirilan_tutar
                                    print("Paranız yatırıldı.")
                                elif onay=="h"or onay=="H":
                                    print("İşleminiz iptal edildi.")
                                    input(menu)
                                else:
                                    print("Hatalı seçim yaptınız.")
                                    input(menu)
                            elif secim2 == "3":
                                hedef_TC = (input("Yatırılacak Hesabın TC : "))
                                if hedef_TC in tc_no:
                                    for musteri2 in banka.musteriler:
                                        if hedef_TC == musteri2.tc:
                                            yatirilan_tutar2 = int(input("Miktar : "))
                                            if yatirilan_tutar2 <= musteri.bakiye:
                                                onay=input("{} adlı müşterimize, {} TL tutarında parayı göndermeyi onaylıyor musunuz? (E/H) : ".format(musteri2.isim,yatirilan_tutar2))
                                                if onay == "e" or onay == "E":
                                                    musteri2.bakiye += yatirilan_tutar2
                                                    musteri.bakiye -= yatirilan_tutar2
                                                    print("Paranız yatırıldı.")
                                                    input(menu)
                                                elif onay == "h" or onay == "H":
                                                    print("İşleminiz iptal edildi.")
                                                    input(menu)
                                                else:
                                                    print("Hatalı seçim yaptınız.")
                                                    input(menu)
                                            else:
                                                print("Bakiyeniz yetersiz!")
                                                input(menu)
                                else:
                                    print("Müşteri bulunamadı!")
                                    input(menu)
                            elif secim2 == "4":
                                cekilecek_tutar = int(input("Miktar : "))
                                if cekilecek_tutar <= musteri.bakiye:
                                    musteri.bakiye -= cekilecek_tutar
                                    print("İşleminiz tamamlandı.")
                                    input(menu)
                                else:
                                    print("Bakiyeniz yeterli değil.\nLütfen yeterli bakiye giriniz : ")
                                    input(menu)
    elif secim == "2":
        t=input("TC giriniz : ")
        i=input("İsim giriniz : ")
        s=input("Şifre giriniz : ")
        banka.musteri_ol(t,i,s)
        input(menu)
    else:
        print("Geçerli işlem giriniz!")
        input(menu)
























