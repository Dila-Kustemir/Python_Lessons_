sozcuk = '   hello world   '
print(sozcuk)
sonuc = sozcuk.strip()
print(sonuc)
 
link = "https://www.python.org/"
sonuc2 = link.strip("htps:/w.org")
print(sonuc2)


kurs = " Python Kursu: Baştan Sona Pyhton "

sonuc3 = kurs.lower()
print(sonuc3)
sonuc4 = kurs.upper()
print(sonuc4)

sonuc5 = kurs.count('p')
print(sonuc5)

kurs2 = "Python Kursu: Baştan Sona Pyhton "
sonuc6 = kurs2.strip()
sonuc7 = sonuc6.startswith("P")
print(sonuc7)

sonuc8 = kurs2.endswith('n')
print(sonuc8)

sonuc9 = kurs2.replace(' ' ,"-")
print(sonuc9)

sonuc10 = kurs2.split( ' ')
print(sonuc10)