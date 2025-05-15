def yasHesapla(dogumYili):
    return 2024 - dogumYili

yas = yasHesapla(2010)
print(yas) 

def emeklilikYasi(dogumYili, isim):
    '''
    DOCSTRİNG: doğum yiliniza göre emekliğinize kaç yil kaldi.
    INPUT:Dogum yili
    OUTPUT: Hesaplanan yil
    '''
    yas = yasHesapla(dogumYili)
    emeklilik = 50 - yas

    if emeklilik > 0:
        print(f'emekliliginize {emeklilik} yil kaldi.')
    else:
        print("Zaten emekli oldunuz")


emeklilikYasi(1984, "Ali")

help(emeklilikYasi)