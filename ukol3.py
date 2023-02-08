import json
with open('Python---GitHub/body.json', encoding ='utf-8') as soubor:
    data=json.load(soubor)

novy_slovnik = data.copy()

novy_slovnik = dict((key, values) for key, values in novy_slovnik.items() if values >= 60)

for key in novy_slovnik.keys():
    print(key, ': PASS')
    
novy_slovnik = data.copy()

novy_slovnik = dict((key, values) for key, values in novy_slovnik.items() if values < 60)

for key in novy_slovnik.keys():
    print(key, ': FAIL')

with open("prospech.json", mode="w", encoding="utf-8") as vystupni_soubor:
    json.dump(data, vystupni_soubor, ensure_ascii=False, indent=4)
