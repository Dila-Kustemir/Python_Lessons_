x = "global x"

def function():
    global x
    x = "local x"
    print(x)

function()
print(x)  

print("**************************************************************************************")

name = "Dila"

def change_name(new_name):
    name = new_name
    print(name)

change_name("Hakan")
print(name)

print("************************************")

name = 'global string'

def greeting():
    name = "Dila"

    def hello():
        print("Hello " + name)

    hello()

greeting()

print("************************************************************************************")

x = 50

def test(sayi):
    global x
    print(f"x: {x}")

    x = 100
    print(f"Yeni x değeri: {x}")

test(x)
print(x)