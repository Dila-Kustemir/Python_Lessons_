# Lambda expression ve map kullanımını öğrendik. 
#  fonksiyonumuzda yapılan işlem sonucunda filtreleme yapmak istiyorsak
# örneğin sadece sonucu çift olan sayıları geri döndürmek istiyorsak
# filter kullanırız

print("filtre kullanımı: ")

numbers = [1, 3, 5, 9, 10, 4]

def check_even(num):
    return num % 2 == 0

result = list(filter(check_even, numbers))
print(result)

print("Lambada ile filter kullanımı:")
result = list(filter(lambda num : num % 2 != 0, numbers))
print(result)