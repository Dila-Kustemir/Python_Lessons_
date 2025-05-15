yaslar = [5, 12, 14, 11, 47, 28, 26, 49, 78, 67, 78, 80, 14, 6, 3 ,1 , 2, 45, 92, 72]
harfler = ["z", "c", "f", "g", "h", "t", "i", "w", "x", "a", "c"]

enKucuk = min(yaslar)
print(enKucuk)

enBuyuk = max(yaslar)
print(enBuyuk)



enKucukharf = min(harfler)
print(enKucukharf)

enBuyukharf = max(harfler)
print(enBuyukharf)


yaslar.append(77)
print(yaslar)

yaslar.insert(2, 13)
print(yaslar)

yaslar.append(14)
print(yaslar)

yaslar.insert(0, 1)
print(yaslar)

yaslar.pop(4)
print(yaslar)

yaslar.remove(5)
print(yaslar)

yaslar.remove(12)
print(yaslar)