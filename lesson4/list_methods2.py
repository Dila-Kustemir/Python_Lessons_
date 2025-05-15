yaslar = [10, 19, 27, 27, 45, 2, 27, 87, 4, 66, 10,  102]
isimler = ["Dila", "İbrahim", "Dila", "Çınar", "Eda", "Dila", "Zümra","Dila","Dila", "Deniz"]

# yaslar listesini küçükten büyüğe sıralayınız
yaslar.sort()
print(yaslar)

isimler.sort()
print(isimler)

# Listede 27 sayısının ve Dila isminin kaç defa tekrarladığını yazdırınız
print(yaslar.count(27))
print(isimler.count("Dila"))

# Listenin elemanlarını tersten yazdırın
yaslar.reverse()
print(yaslar)

isimler.append("Ali")
print(isimler) 

isimler.remove("Ali")
print(isimler)

isimler.reverse()
print(isimler)

isimler.clear()
print(isimler)