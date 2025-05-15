'''
    ogrenciler = {        
        '120' : {
            'ad' : 'Ali',
            'soyad': 'Yılmaz,
            'telefon': '05555555'
        },
        '125' : {
            'ad': 'Can',
            'Soyad':'Korkmaz',
            'telefon':'0444444444'
        },
        '182' : {
            'ad' : 'Ece',
            'soyad': 'Yüksel',
            'telefon' : '0532321'
        },
    }
    sozluk_ornegi = { key : value, key2: value2}

    1- Bilgileri verilen öğrencileri kullanicidan aldginiz bilgilerle dictioanary içinde saklayiniz.
    2-Öğrenci numarasini kullanicidan alip ilgili öğrencinin bilgisini gösteriniz.
'''
ogrenciler = {}

for i in range(2):
    number = input("Öğrenci no: ")
    name = input("Ögrenci adi:")
    surname = input("Ögrenci soyadi:")
    phone = input("Ögrenci telefonu:")

    ogrenciler.update({})
    number : {}
AD : Na
