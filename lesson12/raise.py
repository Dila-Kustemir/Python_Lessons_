def check_password(psw):
    import re
    if (len(psw)) < 8:
        raise Exception("Parola en az 8 karakter olmalıdır.")
    elif not re.search("[a-z]",psw):
        raise Exception("Parola küçük harf içermelidir.")
    elif not re.search("[A-Z]", psw):
        raise Exception("Parola büyük harf içermelidir.")
    elif not re.search("[_@$!]", psw):
        raise Exception("Parola alpha numeric karakter içermelidir.")
    elif  re.search("\s", psw):
        raise Exception("Parola boşluk.")
    else:
        print("Geçerli parola")


while True:
    password = input("Parolanızı giriniz: ")

    try:
        check_password(password)
    except Exception as ex:
        print(ex)
    else:
        break
    finally:
     print("Validation tamamlandı")