try:
    a = int(input("a sayisi giriniz: "))
    b = int(input("b sayısını giriniz"))

    print("a/b =", a/b)

except ValueError:
    print("HATA Tamsayı girlmelisiniz.")

except ZeroDivisionError:
    print("HATA Hiçbir sayı sıfıra bölünemez")