import MySQLdb
import time


class Uye():
    def __init__(self):
        self.db = MySQLdb.connect("localhost", "root", "sifre", "pythondeneme")
        self.cursor = self.db.cursor()
        self.cursor_2 = self.db.cursor()
        self._kullaniciIsim = ""
        self._kullaniciSoyIsim = ""
        self._kullaniciSifre = ""
        self._kullaniciEmail = ""

    
    #cursor.execute("""CREATE TABLE Uyeler(
    #isim char(20) NOT NULL,
    #soyisim char(20) NOT NULL,
    #sifre char(10) NOT NULL,
    #email char(40) NOT NULL)
    #""")
        
    def YeniUyeEkle(self, _isim, _soyIsim, _sifre, _email):
        self.cursor.execute("SELECT isim, soyisim, sifre, email FROM Uyeler WHERE isim = %s", (_isim,))
        self.cursor_2.execute("SELECT isim, soyisim, sifre, email FROM Uyeler WHERE email = %s", (_email,))
        _isimVerisi = self.cursor.fetchall()
        _emailVerisi = self.cursor_2.fetchall()

        if _isimVerisi != ():
            print("Bu isim daha önce alınmış ! \nTekrar üyelik sayfasına yönlendiriliyorsunuz...\n\n\n\n")
            time.sleep(1)
            self.YeniUyeSayfasi()
        elif _emailVerisi != ():
            print("Bu email daha önce alınmış ! \nTekrar üyelik sayfasına yönlendiriliyorsunuz...\n\n\n\n")
            time.sleep(1)
            self.YeniUyeSayfasi()
        else:
            self.cursor.execute("INSERT INTO Uyeler(isim, \
            soyisim, sifre, email) \
            VALUES ('%s', '%s', '%s', '%s')" % \
            (_isim, _soyIsim, _sifre, _email))
            self.db.commit()
        
            print("Üyelik Başarılı ! \nGiriş sayfasına yönlendiriliyorsunuz...\n\n\n\n")
            time.sleep(1)
            self.GirisSayfasi()

    def GirisYap(self, _isim, _sifre):
        self.cursor.execute("SELECT isim, soyisim, sifre, email FROM Uyeler WHERE isim = %s", (_isim,))
        _veriler = self.cursor.fetchall()

        if _veriler != ():
            for row in _veriler:
                self._kullaniciIsim = row[0]
                self._kullaniciSoyIsim = row[1]
                self._kullaniciSifre = row[2]
                self._kullaniciEmail = row[3]
            if _sifre == self._kullaniciSifre:
                print("Giriş Yapıldı :)")
            else:
                print("Giriş Yapılamadı :(")
        else:
            print("Böyle bir kullanıcı yok !")
            print("Kayıt için yönlendiriliyorsunuz...\n\n\n\n")
            time.sleep(1)
            self.YeniUyeSayfasi()


    def YeniUyeSayfasi(self):
        print("Girişlerden herhangi birine 'b' değeri girmeniz durumunda başlangıç sayfasına yönlendirilirsiniz.")
        _isim = input("İsminizi Giriniz : ")
        _soyIsim = input("Soyisminizi Giriniz : ")
        _sifre = input("Güçlü Bir Şifre Belirleyiniz : ")
        _email = input("Email Adresinizi Giriniz : ")

        if _isim == "b" or _soyIsim == "b" or _sifre == "b" or _email == "b":
            print("Başlangıç sayfasına yönlendiriliyorsunuz...")
            time.sleep(1)
            print("\n\n\n\n")
            self.OlaySecici()
        else:
            self.YeniUyeEkle(_isim, _soyIsim, _sifre, _email)

    def GirisSayfasi(self):
        print("Girişlerden herhangi birine 'b' değeri girmeniz durumunda başlangıç sayfasına yönlendirilirsiniz.")
        _isim = input("İsminizi Giriniz : ")
        _sifre = input("Şifrenizi Giriniz : ")
        if _isim == "b" or _sifre == "b":
            print("Başlangıç sayfasına yönlendiriliyorsunuz...")
            time.sleep(1)
            print("\n\n\n\n")
            self.OlaySecici()
        else:
            self.GirisYap(_isim, _sifre)

    def OlaySecici(self):
        print("""[1]Kayıt Ol
[2]Giriş Yap
[3]Çıkış Yap""")
        
        _olay = input("Ne yapmak istersiniz ? \n")

        if _olay == "1":
            print("\n\n\n\n")
            self.YeniUyeSayfasi()
        elif _olay == "2":
            print("\n\n\n\n")
            self.GirisSayfasi()
        elif _olay == "3":
            print("Çıkılıyor...")
            time.sleep(1)
            quit()
        else:
            print("Yanlış bir tuşlama yaptınız !")
            print("Çıkılıyor...")
            time.sleep(2)
            quit()


if __name__ == "__main__":
    uyelik = Uye()
    uyelik.OlaySecici()

        
        
