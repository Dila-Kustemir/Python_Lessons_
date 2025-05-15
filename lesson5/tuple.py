
liste = [1, 2, 3, 4, 5]
tuple = (1, True, 'dört')

print(type(liste))
print(type(tuple))

print(liste[2])

print(tuple[2])


print(len(liste))
print(len(tuple))

liste2 = ["Dila" , "Ayse"]
tuple2 = ("Ahmet", "Mehmet")

liste2[0] = "cenk"
print(liste2)

# Tuple sabittir, tanımlandıktan sonra ekleme çıkarma yapılamaz hata verir
# tuple2[0] = "Ceren"
# print(tuple2)

names = ("Dila", "İdil") + tuple2
print(names)




