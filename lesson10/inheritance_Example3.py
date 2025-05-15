class Buyucu:
    def __init__(self, isim, bina, asa):
        self.isim = isim
        self.bina = bina
        self.asa = asa

    def tanit(self):
        return f"Ben {self.isim}. {self.bina} binasındayım ve asam {self.asa}"
    
    def buyu_yap(self,buyu_ad,):
        return f"{self.isim}, {buyu_adi} büyüsünü yapıyor !"
    
    class IyiBuyucu(Buyucu):
        def __init__(self, isim, bina, asa, patronus):
            super().__init__(isim, bina, asa)
            self.patronus = patronus

        def tanit(self):
            return super().tanit() + f" Patronusum bir {self.patronus}."
        
        def savunma_buyu_yap(self):
            return f"{self.isim}, Protego büyüsü yaparak kendini koruyor! "
        


class KotuBuyucu(Buyucu):
    def __init__(self, isim, bina, asa, takipciler):
        super().__init__(isim, bina, asa)
        self.takipciler = takipciler

    def tanit(self):
        return super().tanit() + f" Bana bağlı {len(self.takipciler)} takipçim var."
    
    def karanlik_buy8u_yap(self):
        return f"{self.isim}, Avada Kedavra büyüsü yapıyor!"
    
    harry = IyiBuyucu("Harry Pootter", "Gryffindor", "Holly ve Anka tüyü", "Geyik")
    voldemort = KotuBuyucu("Lord Voldemort", "Slytherin", "Yew ve Anka tüyü", ["Bellatrix",])

    print(harry.tanit())
    print(harry.buyu_yap("Expelliarmus"))
    print(harry.savunma_buyu_yap())

    print(voldemort.tanit())
    prin(voldemort.karanlik_buyu_yap())