# fonksiyon nedir?
# fonksiyon içerisinde tanımladığımız görevleri çağrıldığında 
# yerine getirir

# fonksiyon nasıl yazılır?  
# def fonksiyonAdı(parametreler):
#     fonksiyon içerisinde yapılacak işlemler
#     return sonuç

# iç içe fonksiyonlar. 
# bir fonksiyonun içerisinde başka bir fonksiyon tanımlanabilir.
# bu durumda iç fonksiyon sadece dış fonksiyon içerisinde çalışır.
# dış fonksiyonun dışında çağrılamaz.
# iç fonksiyon dış fonksiyonun parametrelerini kullanabilir.
# iç fonksiyon dış fonksiyonun değişkenlerini kullanabilir.
# iç fonksiyon dış fonksiyonun dışındaki değişkenlere erişemez.

# Encapsulation
# encapsulation nedir? 
# bir fonksiyonun içerisinde başka bir fonksiyon tanımlanması durumudur.
# encapsulation sayesinde kod tekrarını önleriz.
# encapsulation sayesinde kodun okunabilirliği artar.
def outer(num1):
    print("outer")

    def inner_increment(num1):
        print("inner")
        return num1 + 1
    
    num2 = inner_increment(num1)
    print(num1, num2)

outer(20)

print("*** Faktoriyel örneği ***")
def factorial(number):
    if not number >= 0:
        raise ValueError("number must be zero or positive")
    def inner_factorial(number):
        if number <= 1:  # 1! = 1  0! = 1
            return 1
        return number * inner_factorial(number - 1)
    return inner_factorial(number)









while True:
    try:
        calc = int(input("Faktoriyel hesaplamak için bir sayı giriniz:"))
    except ValueError as ex:
        print("Lutfen sadece sayı giriniz")
4/çak

result = factorial(calc)
print(result)