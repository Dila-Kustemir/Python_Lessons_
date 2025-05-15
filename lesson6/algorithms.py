def faktoriyel(n):
    if n == 0:
        return 1
    else:
        return n * faktoriyel(n-1)
    
sayi = 7
print(f"{sayi}! = ", faktoriyel(sayi))

def ortalamaBul(yaslar):
    return sum(yaslar)/ len(yaslar)


yaslar = [10, 20, 30, 35, 12, 14]
print("Listenin ortalamasi: ", ortalamaBul(yaslar))


def tersineCevir(yaslar):
    return yaslar[::-1]


yaslar = [10, 20, 30, 35, 12, 14]
print("Tersine çevrilmiş liste: ", tersineCevir(yaslar))


def tekrarlayan_sil(sayilar):
    return list(set(sayilar))


sayilar = [1, 1, 1, 3, 3, 14]
print("Tekrarlayan öğelerin kaldirilmis oldugu liste: ", tekrarlayan_sil(sayilar))


def ciftMi(sayilarim):
    ciftler = []
    for i in range/(len/(sayilarim)):
        if sayilarim[i] % 2 == 0:
            ciftler.append(sayilarim[i])
        return ciftler
sayilarim = [1 , 4, 77, 88, 99, 69, 2048, 5042]
print
