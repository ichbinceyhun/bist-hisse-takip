import requests
import json
def ilkdongu():
    print("Hisse adı girin:")
    hisse = input()
    hissex = hisse.upper()
    url = f"https://bigpara.hurriyet.com.tr/api/v1/borsa/hisseyuzeysel/{hissex}"
    response = requests.get(url)
    cikti = response.text
    dict_hali = json.loads(cikti)

    sembol = dict_hali["data"]["hisseYuzeysel"]["sembol"]
    fiyat = dict_hali["data"]["hisseYuzeysel"]["alis"]
    degisim = dict_hali["data"]["hisseYuzeysel"]["yuzdedegisimS1"]

    print(f"Hisse Adı: {sembol}")
    print(f"Güncel Fiyat: {fiyat}")
    print(f"Değisim: {degisim}")


while True:
    ilkdongu()