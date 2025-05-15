import requests
import json
api_key = "50907e5434094925bce8f852"
api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

bozulan_doviz = input("Bozulan döviz cincini giriniz:").upper() 
alinan_doviz = input("Alınacak Döviz cinsini giriniz: ").upper()
miktar = int(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz:"))
sonuc = requests.get(api_url + bozulan_doviz)
sonuc_json = json.loads(sonuc.text)
print("1 {0} = {1}{2}".format(bozulan_doviz, sonuc_json["conversion_rates"][alinan_doviz], alinan_doviz))
print("{0} {1} = {2} {3}".format(miktar, bozulan_doviz, miktar * sonuc_json["conversion_rates"][alinan_doviz], alinan_doviz))