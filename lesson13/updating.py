# r+ -> Hem okuma hem yazma modu.
# as file, open fonksiyonundan gelen objeyi file değişkenine aktarır.

with open("myFile.txt", "r+", encoding = "utf-8") as file:
    print(file.read())

print("--- r+ modu ile yazma işlemi: ")
with open("myFile.txt", "r+", encoding="utf-8") as file:

    file.seek(21)
    file.write("deneme")

    # r+ modu ile yazma işlemi yapılırken imleç konumu belirtilmezse
# dosyadaki ilk veri üzerinden ekleme yapar.
with open("myFile.txt", "r+", encoding = "utf-8") as file:
    print(file.read())

print("--- Sayfa sonunda güncelleme işlemi:")
with open("myFile.txt", "a", encoding = "utf-8") as file:

    # a (append): Sondna ekleme yapar
    # w (write): Dosyayı temizler ve ekleme yapar. Yeni bir dosya açılmış gibi
    file.write("dila")

with open("myFile.txt", "r+", encoding = "utf-8") as file:
    print(file.read())

with open("myFile.txt", "r+", encoding = "utf-8") as file:
    content = file.read()
    content = "\nDosyalarla çalışmak\n" + content
    file.seek(0)
    file.write(content)

with open("myFile.txt", "r+", encoding = "utf-8") as file:
    print(file.read())