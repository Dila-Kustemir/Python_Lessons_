class Circle:
    # Attributes -> Class attributes, object attributes
    # Methods
    # Çemberin çevresi: 2 * pi * r
    # pi = 3.14 sabit bir değer
    # r değeri çemberin yarıçapı
    # class attribute
    pi = 3.14

    def __init__(self, yaricap = 3):
        self.yaricap = yaricap

    def cevreHesapla(self):
        return 2 * self.pi * self.yaricap
    
    def alanHesapla(self):
        return self.pi * self.yaricap ** 2
    
c1 = Circle()
c2 = Circle(20)
print(f"C1 Objesi \n Çevresi: {c1.cevreHesapla()} \n Alanı: {c1.alanHesapla()}")
print("********************************")
print(f"C2 Objesi \n Çevresi: {c2.cevreHesapla()} \n Alanı: {c2.alanHesapla()}")