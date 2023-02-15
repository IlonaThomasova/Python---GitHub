vstup1= input("Zadej na jaké telefonní číslo se má zaslat zpráva: ")

pomocna_promenna1=vstup1[0:4]

pomocna_promenna2='+420'

def funkce1():
    
    if ((len(vstup1)==9) or ((len(vstup1)==13) and (pomocna_promenna2==pomocna_promenna1))):
        
        print('True') 
    
    else:
        print('Telefonní číslo je špatně zadané.')
        quit()

funkce1()

vstup2= input("Zadej text zprávy: ")

def funkce2():
    
    pocet=0
    for i in vstup2:
        pocet+=1 
    if pocet<=180:
        print("Cena SMS je 3 Kč")
    if pocet>180:    
        pomocna_promenna3 = pocet//180
        print("Cena SMS je ",3*pomocna_promenna3," Kč.")
    
funkce2()