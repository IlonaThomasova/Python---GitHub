import json
with open('Python---GitHub/body.json', encoding ='utf-8') as soubor:
    data=json.load(soubor)

novy_slovnik={}
for jmeno in data:
    print(data[jmeno])
    if data[jmeno]>60:
        novy_slovnik[jmeno]='Pass'
    else:
        novy_slovnik[jmeno]='Fail'

print(novy_slovnik)

with open("prospech.json", mode="w", encoding="utf-8") as vystupni_soubor:
    json.dump(novy_slovnik, vystupni_soubor, ensure_ascii=False, indent=4)