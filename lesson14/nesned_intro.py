def dis_fonksiyon():
    print("Dış fonksiyon çalıştı")

    def ic_fonksiyon():
        print("ic fonksiyon çalıştı")

    ic_fonksiyon()
        
dis_fonksiyon()

def dis_fonksiyon(sayi):
    print("Dış fonksiyon çalıştı")
    
    def ic_fonksiyon(sayi):
        return sayi + 5
    
    sonuc =  ic_fonksiyon(sayi)
    print("İç fonksiyon sonucu: ", sonuc)
dis_fonksiyon(10)