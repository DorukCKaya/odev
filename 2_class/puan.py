class Ogrenci:
    def __init__(self, ogrenciAdi, ogrenciSoyadi, ogrenciSinif):
        self.ogrenciAdi = ogrenciAdi
        self.ogrenciSoyadi = ogrenciSoyadi
        self.ogrenciSinif = ogrenciSinif
        
class Soru(): 
    def netSayisi(self, dogruSayisi, yanlisSayisi):
        net = (int(dogruSayisi))- (int(yanlisSayisi)/4)
        self.net = net

    def hesapla(self, net):
        puan = 2*(net)
        self.puan = puan

ogrenciAdi, ogrenciSoyadi, ogrenciSinif = "doruk","kaya","1a"
o1 = Ogrenci(ogrenciAdi, ogrenciSoyadi, ogrenciSinif)    

print('doğru sayısı?')
dogruSayisi = input()
print('yanlış sayısı')
yanlisSayisi = input()

s1 = Soru()
s1.netSayisi(dogruSayisi,yanlisSayisi)
s1.hesapla(net)

print(o1.ogrenciSinif + " sınıfından " + o1.ogrenciAdi + " " + o1.ogrenciSoyadi + ", sınavdan " + str(s1.puan) + " puan aldı")
