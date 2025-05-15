print("Lambda sayesinde fonksiyon adı olmadan anonim bir şekilde fonks. tanımlayabiliriz: ")
numbers = [1, 3, 5, 9]

result = list(map(lambda num: num ** 2, numbers))
print("Anonim fonksiyon tanımlama: ")


lambda num : num **2

print("Lamba expression ile liste elemanlarının küp'ünü alma: ")
cube = lambda num : num ** 3
result = list(map(cube, numbers))
print(result)