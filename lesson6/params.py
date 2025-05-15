def topla(a, b, c = 0, d = 0):
    return a + b + c + d

sonuc = topla(10, 20, 50, 20)
sonuc2 = topla(5,5,20)
sonuc3 = topla(7, 3)

print(sonuc)
print(sonuc2)
print(sonuc3)
print("-" * 50)

def topla2(*params):
    return sum((params))

print(topla2(20,40))
print(topla2(50, 40, 30,))
print(topla2(50, 40, 30,30))
print(topla2(50, 40, 30,30 , 100))

def topla3(*params):
    toplam =  0

    for n in params:
        toplam = toplam + n
    
    return toplam

print(topla3(30, 40, 80))