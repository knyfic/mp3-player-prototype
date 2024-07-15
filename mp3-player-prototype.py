from random import choice

class MP3calar():
  def __init__(self,sarkilistesi = []):
    self.CalanSarkı = ""
    self.ses = 50
    self.sarkilistesi = sarkilistesi
    self.durum = True


  def menugoster(self):
    print('''
    ---------- MP3calara Hos Gelndiniz ----------
    sarkı listesi: {}
    suan calan sarkı: {}
    ses duzeyi: {}
    ---------------------------------------------
    1) sarki sec
    2) ses arttır
    3) ses azalt
    4) ramdom sarkı cal
    5) sarkı ekle
    6) sarkı sil
    7) kapat'''.format(self.sarkilistesi, self.CalanSarkı, self.ses))


  def secimyap(self):
    sec = int(input("secim yapiniz: "))

    while sec < 1 or sec > 7:
      sec = int(input("girdiğiniz değer 1-7 arasında olmalı tekrar secım yapınız: "))

    return sec


  def calıstır(self):
    self.menugoster()
    secimyap = self.secimyap()


    if secimyap == 1:
      sayac = 1
      if len(self.sarkilistesi) == 0:
        print("\n","HATA: SARKI LİSTESI BOS")
      else:
        for sarkı in self.sarkilistesi:
          print("{}) {}".format(sayac, sarkı))
          sayac += 1

        secileceksarkı = int(input("secmek istediğiniz sarkı numarası: "))

        while secileceksarkı < 1 or secileceksarkı> len(self.sarkilistesi):
          secileceksarkı = int(input("secmek istediğiniz sarkı numarasını dogru girdiginizden emin olunuz ve tekrar giriniz: "))

        self.CalanSarkı = self.sarkilistesi[secileceksarkı - 1]


    if secimyap == 2:
      arttır = int(input("arttırmak istediğiniz ses miktarı: "))
      while arttır < 0:
        arttır = int(input("arttırmak istediğiniz ses miktarı negatif deger olamaz lutgen pozitif tam sayı girniz: "))
      if arttır > 100 - self.ses:
        self.ses = 100
      else:
        self.ses += arttır


    if secimyap == 3:
      azalt = int(input("azaltmak istediğiniz ses miktarı: "))
      while azalt < 0:
        azalt = int(input("lütfen azaltmak istediginiz büyüklüye karsılık gelen pozitif tamsayı girniz: "))
      if azalt > 0 + self.ses:
        self.ses = 0
      else:
        self.ses -= azalt


    if secimyap == 4:
      x = choice(self.sarkilistesi)
      self.CalanSarkı = x


    if secimyap == 5:
      sanatcı = input("sanatcının ismini giriniz: ")
      sarkı = input("sarkının ismini giriniz: ")
      self.sarkilistesi.append(sanatcı + " - " + sarkı)


    if secimyap == 6:
      sayac = 1
      for sarkı in self.sarkilistesi:
        print("{}) {}".format(sayac, sarkı))
        sayac += 1

      silineceksarkı = int(input("silmek istediğiniz sarkı numarası: "))

      while silineceksarkı < 1 or silineceksarkı > len(self.sarkilistesi):
        silineceksarkı = int(input("silmek istediğiniz sarkı numarasını dogru girdiginizden emin olunuz ve tekrar giriniz: "))
      self.sarkilistesi.pop(silineceksarkı - 1)
      
                          
    if secimyap == 7:
      self.kapat()


  def kapat(self):
    print("bb")
    self.durum = False


mp3calar = MP3calar()

while mp3calar.durum:
  mp3calar.calıstır()
