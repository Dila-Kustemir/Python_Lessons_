def validate_login(username, password):
    if username == "admin" and password == "123":
        return True
    else:
        return False
    
username = input("Kullanci Adi: ") 
password = input("Şifre: ")

if validate_login(username, password):
    print("Giriş Başarili")
else:
    print("Hatali kullanici adi veya sifre")