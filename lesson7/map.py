def square(num):
    return num ** 2

result = square(3)

print(result)

print("------------------------")

numbers = [1, 3, 5, 9]

for i in range(len(numbers)):
    result = square(number[i])
    print(result)

print("Map kullanarak kare alma: ")
result = map(square, numbers)
print(result)

result = list(map(square, numbers))
print(result)

print("liste kullanmadan enumerate (sıralı çağırma ile map kullanımı):")
for item in map(square, numbers):
    print(item)