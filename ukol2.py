sklad = {
"1N4148": 250,
"BAV21": 54,
"KC147": 147,
"2N7002": 97,
"BC547C": 10
}

kod_soucastky=(input("Zadejte prosím kód součástky: "))
if kod_soucastky in sklad:
    pocet_kusu=int(input("Zadejte prosím počet kusů: "))
         
    if sklad[kod_soucastky]<(pocet_kusu):
        print("v omezeném množství")
        sklad.pop(kod_soucastky)
    else:
        print("v plné výši")
        sklad[kod_soucastky]=sklad[kod_soucastky]-(pocet_kusu)
else:
    print("Součástka není skladem")