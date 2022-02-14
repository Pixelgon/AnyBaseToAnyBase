# Vytvoril Matej Matejka
# Prevod z jakekoliv soustavy do destikove


zaklad = int(input("Zadejte číselnou soustavu ve které je vaše číslo: "))
while zaklad < 2 or zaklad > 36:
        print("Zadali jste špatnou soustavu")
        zaklad = int(input("Zadejte prosím soustavu znovu: "))

cislo_vstup = str(input("Zadejte číslo, které chcete převést: "))
cislo_vstup = cislo_vstup.strip()

def split(word):
        return list(word)

cislo_vstup = split(cislo_vstup)

# TODO
#provedeme kontrolu pismen ve cislo_vstupni zda jsou mensi nez zaklad_vstup

# =A * 16^4 + B * 16^3 + 1 * 16^2 + 2 * 16^1 + F * 16^0

# = cislice_v_danem_radu * zaklad ** pozice_dane_cislice

cislo = 0
mocnina = len(cislo_vstup) - 1

for i in range(0, len(cislo_vstup)):
        if cislo_vstup[i] >= '0' <= '9':
                cislice = int(cislo_vstup[i])
        elif cislo_vstup[i] >= 'A' <= 'Z':
                cislice = ord(cislo_vstup[i]) - 55
        else:
                print("Chyba ve vstupním čísle")
                exit()
        cislo = cislo + cislice * zaklad ** mocnina
        mocnina = mocnina - 1

zaklad = int(input("Do jaké soustavy chcete číslo převést?: "))
vysledek = ""
# Dokud cislo je vetsi nez nula
while cislo > 0:
    # Zbytek je roven zbytku po deleni cisla zakladem
    zbytek = int(cislo % zaklad)
    # Pokud je zbytek mensi nez 10
    if zbytek < 10:
        # Zbytek priradime do vysledku
        vysledek += str(zbytek)
    else:
        # Zbytek nahradime cislem a priradime do vysledku
        vysledek += chr(ord('A')+zbytek-10)
    # Cislo vydelime zakladem
    cislo //= zaklad
vysledek = vysledek[::-1]
# Vysledek vypiseme
print(vysledek)
exit()