while True:
    try: 
        x = int(input("x: "))
        y = int(input("y: "))
        print("x/y=", x/y)

    except Exception as ex:
        print("Yanlış değer girdiniz")
    
    else:
        break

    finally:
        print("try-except sonlandı.")