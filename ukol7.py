class Auto:
    def __init__(self, znacka, typ_vozidla, najete_km):
        self.znacka = znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = True
    
    def pujc_auto(self):
        if self.dostupne:
            self.dostupne=False
            return (f"Potvrzuji zapůjčení vozidla.")
        else:
            return (f"Vozidlo není k dispozici.")
    
    def get_info(self):
        return f"Značka{self.znacka} vozidla{self.typ_vozidla} má najeto{self.najete_km}."

auto1=Auto("4A23020", "Peugeot", "47534")
auto2=Auto("1P34747", "Škoda", "41253")
print(auto1.get_info())
print(auto1.pujc_auto())










