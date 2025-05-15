class Person():
    def __int__(self, fname, Iname):
        self.firstName = fname
        self.lastName = Iname
        print("Person Created")

    def who_am_i(self):
        print("im a Person")

    def eat(self):
        print("im eating")

class Student(Person):
    def __int__(self, fname, Iname):
        Person.__İnit__(self, fname, lname)
        print("Person Created")

    def who_am_i(self):
        print("im a student")

    def eat(self):
        print("im chocolate eating")

        
p1 = Person("Eymen kaan", "Kaplan")
p1.who_am_i()

s1 = Student("Ece", "Demir")
s1.who_am_i

p1.eat()
s1.eat()

print(p1.firstName + " " + p1.lastName)
print(s1.firstName + " " + s1.lastName)

        