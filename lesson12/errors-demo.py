listem = ["1" , "2", "5a", "10b", "abc", "10", "50"]
# 1: Listedeki elemanlar içindeki sayısal değerleri bulunuz
for i in range(len(listem)):
    try:
        result = int(listem[i])
        print(result)
    except ValueError:
        continue
    
    # 2: Kullanıcı 'q' değerini girmedikçe aldığınız her input'un
# sayısal değer olduğundan emin olunuz aksi halde hata mesajı yazınız.

while True:
    x = input("Bir değer giriniz: ")  # string
    if x ==  "q":
        break
    try:
        result = int(x)
        print("Girdiğiniz sayı: ", result)
    except:
        print("Geçersiz değer")

# 3: Girilen parola içerisinde türkçe karakter hatası veriniz
turkce_karakterler = "şçğüöıİ"
def checkPassword(parola):
    for i in parola:
        if i in turkce_karakterler:
            raise TypeError("Parola türkçe karakter içermemelidir.")
        else:
            pass
    print("Geçerli Parola!")
parola = input("Parola giriniz:") 
try: 
    checkPassword(parola)
except TypeError as err:
    print(err)