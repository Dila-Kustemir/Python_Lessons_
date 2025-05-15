def gunluk_ekle():
    tarih = input("Günlük tarihi (YYYY-MM-DD)")
    not_icerik = input("Bugünkü notun: ")
    with open("gunluk.txt", "a", encoding = "utf-8") as file:
        file.write(f"{tarih}: {not_icerik}/n")
    print("günlük kaydedildi!\n")

def gunluk_oku():
    try:
        with open("gunluk.txt", "r", encoding = "utf-8") as file:
            dosya_icerigi = file.read()
            if dosya_icerigi == "":
                print("henüz günlük kaydı yok")
            else:
                print("\n--- Günlük Kayıtları ---")
                file.seek(0)
                print(file.read())
    except FileNotFoundError:
        print("Bu isimde bir dosya mevcut değil\n")

def gunluk_ara():
    aranan_tarih = input("Hangi tarihi arıyorsun) (YYYY-MM-DD): ")
    bulundu = False
    try:
        with open("gunluk.txt", "r", encoding ="utf-8") as file:
            for satir in file:
                if satir.startswith(aranan_tarih):
                    print(satir.strip())
                    bulundu = True
        if not bulundu:
            print("bu tarihte bir kayıt bulunamadı")
    except FileNotFoundError:
        print("Bu isimde bir dosya mevcut degil\n")


while True:
    print("\n1 -Gunluk Ekle\n2 - Gunlugu Oku\n3 - Tarihe Göre Ara\n4 - çıkış")
    secim = input("Lütfen komut seçin: ")

    if secim == "1":
        gunluk_ekle()
    elif secim == "2":
        gunluk_oku()
    elif secim == "3":
        gunluk_ara()
    elif secim == "4":
        print("Görüşmek üzere")
        break
    else:
        print("Geçersiz seçim tekrar dene")


















