def kontrola_cisla(telefonni_cislo):
    
    if (len(telefonni_cislo)==9) or ((len(telefonni_cislo)==13 and '+420'==telefonni_cislo[0:4])):
        
        return True
          
    else:
        return False 
        

def cena_zpravy(zprava):
    
    pocet_sms=len(zprava)//180+1
    return pocet_sms*3
   
    
vstup1= input("Zadej na jaké telefonní číslo se má zaslat zpráva: ")

if kontrola_cisla(telefonni_cislo=vstup1):
    vstup2= input("Zadej text zprávy: ")
    cena=cena_zpravy(zprava=vstup2)
    print(f'Cena vaší SMS je {cena} Kč.')
else:
    print("Zadal jste nesprávné číslo.")

