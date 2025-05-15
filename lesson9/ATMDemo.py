İbrahimHesap = {
    "ad" : "İbrahim Halil Demir",
    "hesapNo" : "245489655",
    "bakiye" : 350,
    "ekHesap" : 2000,
 }

DilaHesap = { 
    "ad" : "Dila Kustemir",
    "hesapNo" : "598856",
    "bakiye" : 10000000,
    "ekHesap" : 5000
     }

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print("Paranızı alabilirsiniz")
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']
        if (toplam >= miktar):
            ekHesapKullanilsinMi = input("Ek Hesap kullanılsın mı  (e/h)")

            if ekHesapKullanilsinMi == 'e':

                hesap['ekHesap'] -= miktar

                print("Paranızı alabilirsiniz")
            else:
                print(f"Toplam Bakiyeniz: {toplam}")

        else:
            print("Bakiye yetersiz")

paraCek(İbrahimHesap, 1000)


def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} Nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitsiz ise {hesap['ekHesap']} bulunmaktadır.")

bakiyeSorgula(İbrahimHesap)