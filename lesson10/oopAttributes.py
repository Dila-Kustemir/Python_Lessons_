class Person:
    # Class Attributes
    address = "No information"

    # Constructor (Yapıcı) Method
    def __init__(this, name, year):
        # Objec Attributes
        this.name = name
        this.year = year
        print("init metdotu çalıştı")

    def intro(self):
        print("Hello There")

    def calculateAge(self):
        return 2024 - self.year


p1 = Person(name = "Dila", year = 2012)
p2 = Person(name = "Yiğit", year = 2014)
p3 = Person(name = "Ceren", year = 1985)

p1.intro()
p2.intro()

print(f"Benim adım: {p1.name} ve {p1.calculateAge()} yaşındayım")

print(f"Benim adım: {p2.name} ve {p2.calculateAge()} yaşındayım") 

p2.name = "Zehra"
p2.year = 2018
p2.address = "Ankara"

print(f"p1: name: {p1.name} year: {p1.year} address: {p1.address}")
print(f"p2: name: {p2.name} year: {p2.year} address: {p2.address}")