# Default olarak reading atandığında r parametresi verilmeden kullanılabilir.
#file = open("myFile.txt" , "r")

file = open("myFile.txt")
print(file)

# Eğer dosya belirtilen konumda yoksa try-except ile hata fırlatma

try:
    file = open("myFile452.txt")
except FileNotFoundError:
    print("Dosya okuma hatası!!")
finally:
    print("Dosya kapandı")
    file.close()

    # 3.Adım
# Dosyayı r modunda açıp içeriğini de türkçe karakterleri okunabileceği UTF-8
file = open("myFile.txt", "r", encoding = "utf-8")
print("-For döngüsü ile dosya içeriğini yazdırma-")
# for döngüsü ile okuma
for i in file:
    print(i, end = "")  # end araya boş satır eklememesi için
file.close()


# read fonksiyonu ile okuma
print("\n","-read fonksiyonu ile okuma-")
# content -> içerik
file = open("myFile.txt", "r", encoding = "utf-8", errors = "ignore")
content1 = file.read()
print("İçerik 1")

# dosya bir defa read ile okundu imleç en sonda ve dosya kapatılmadan
# tekrar okunmaya çalışıldı. İmlecin bulunduğu yerden okuma yapınca okunacak veri yok. 
print("İçerik 2")
# seek metodu ile kürsorun (imleç) yerini değiştirebilirim
file.seek(3)
# tell metoduyla imlecin en son nerde kaldığını görebiliriz
print(file.tell())
content2 = file.read()
print(content2)
file.close()

# read ile bütün dosyayı okur ancak (size) karakter sayısı belirtilebilir
# Herbir karakter 1 byte'a karşılık gelir dolayısıyla size alanında 5 belirtince 5 byte'lık karakteri alır.
print("\n","-Karakter sayısı belirtme-")
file = open("myFile.txt", "r", encoding = "utf-8")
content = file.read(7)
# sonraki 6 karakter ile okumaya devam eder.
content = file.read(6)
print(content)
file.close()



print("\n" , "*** readline fonksiyonu ***")
# Her seferinde bir satırı okur

file = open("myFile.txt", "r", encoding = "utf-8")

print(file.readline(), end = "")
print(file.readline(), end = "")
print(file.readline(), end = "")

file.close()

# readlines ile her bir satır bilgiyi dizi elemanı olarak okutabiliriz
# Her bir bilgi bir satırda yer aldığı için sonuna \n ekler
file = open("myFile.txt", "r", encoding = "utf-8")
print("\n" ,"* readlines *")

liste = file.readlines()
print(liste)

print(liste[0], end = "")
print(liste[1])

file.close()