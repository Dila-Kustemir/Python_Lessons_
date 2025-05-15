# Dosyayı açmak ve oluşturmak için open() fonks. kullanırız
# Kullanımı -> open(dosya_adi, dosya_erişim_modu)
# dosya_erişim_modu: Dosyayı hangi amaçla açtığımızı belirtir.
# "w" : (write) yazma modu
# *** Dosyayı konumda oluşturur
# *** Dosya içeriğini siler ve yeniden ekleme yapar.

file = open("newFile.txt", "w")
print(file)
file.write("İbrahim Halil Demir")
file.close()
# Encoding: Dosya içerisine yazacağımız bilgiler kullanacağımız 
# işletim sisteminde karakter kodlama tipi
file = open("myFile.txt", "w" , encoding="utf-8")
file.write("İbrahim Halil Demir")
file.close()

file = open("myFile.txt", "w" , encoding="utf-8")
file.write("Dila")
file.close()

# "a" (Append) 
# Dosya yoksa belirtilen konumda dosyayı oluşturur.
# Dosya mevcutsa ve içeriği varsa ekleme yapar içeriği silmez

file = open("myFile.txt", "a" , encoding="utf-8")
file.write("\nHakan")
file.close()

# "x" : (create)
# Oluşturma. Dosya zaten varsa hata verir
# file = open("C:\\Users\\Ibrahim Halil Demir\\Desktop\\Python_Lessons\\lesson18\\File.txt", "x", encoding="utf-8")

# "r" : (read)
# Okuma. Varsayılan. Dosya belirtilen konumda yoksa hata verir
file = open("myFile.txt", "r" , encoding="utf-8")
print(file.read())
file.close()

file = open("benim_dosyam.txt", "w")
print(file)
file.write("uykum vaar!!!")
file.close()

file = open("benim_dosyam.txt", "a" , encoding="utf-8")
file.write("\nuykum vaar!!!")
file.close()

file = open("benim_dosyam.txt", "r" , encoding="utf-8")
print(file.read())
file.close()