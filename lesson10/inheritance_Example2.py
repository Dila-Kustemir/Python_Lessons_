class EvcilHayvan:
    self.isim = isim 
    self.yas = yas

def ses_cikar(self):
    return "Ses Çıkarıyorum"

def tanit(self):
    return f"Ben {self.isim}. {self.yas} yaşındayım."


class Kedi(EvcilHayvan):
    def __init__(self, isim, yas, tur="Van Kedisi"):
        super().__init__(isim, yas)

    def ses_cikar(self):
        return "Miyaw"
    


class Kopek(EvcilHayvan):
    def __init__(self, isim, yas, tur="Golden Retriever"):
        super().__init__(isim, yas)
        self.tur = tur

    def ses_cikar(self):
        return "Hav Hav"
    

tekir = Kedi("Tekir", 2)
karabas = Kopek("karabaş", 3)

print(tekir.tanit())
print(f"{tekir.isim} bir {tekir.tur}: {tekir.ses_cikar()}")
print(karabas.tanit())
print(f"{karabas.isim} bir {karabas.tur}: {karabas.ses_cikar()}")