# Vytvoril Matej Matejka
# Prevod z jakekoliv soustavy do destikove

def split(word):
    return list(word)
zaklad = int(input("Zadejte číselnou soustavu ve které je vaše číslo: "))
# Overime zda jsme zadali spravnou soustavu
while zaklad < 2 or zaklad > 36:
        print("Zadali jste špatnou soustavu")
        zaklad = int(input("Zadejte soustavu znovu: "))
cislo_vstup = str(input("Zadejte číslo, které chcete převést: "))
cislo_vstup = cislo_vstup.strip()
cislo_vstup = split(cislo_vstup)
# Pismena nahradime cisli
for a, n in enumerate(cislo_vstup):
    if n == 'A':
        cislo_vstup[a] = '10'
for b, n in enumerate(cislo_vstup):
    if n == 'B':
        cislo_vstup[b] = '11'
for c, n in enumerate(cislo_vstup):
    if n == 'C':
        cislo_vstup[c] = '12'
for d, n in enumerate(cislo_vstup):
    if n == 'D':
        cislo_vstup[d] = '13'
for e, n in enumerate(cislo_vstup):
    if n == 'E':
        cislo_vstup[e] = '14'
for f, n in enumerate(cislo_vstup):
    if n == 'F':
        cislo_vstup[f] = '15'
cislo_vstup_map = map(int, cislo_vstup)
cislo_vstup = list(cislo_vstup_map)
while max(cislo_vstup) > zaklad:
    print("Číslo se neshoduje se soustavou")
    cislo_vstup = str(input("Zadejte číslo znovu: "))
    cislo_vstup = cislo_vstup.strip()
    cislo_vstup = split(cislo_vstup)
    cislo_vstup_map = map(int, cislo_vstup)
    cislo_vstup = list(cislo_vstup_map)

cislo = 0
mocnina = len(cislo_vstup) - 1
cislice = 0
for i in range(0, len(cislo_vstup)):
        if cislo_vstup[i] >= 0 <= 9:
                cislice = int(cislo_vstup[i])
        elif cislo_vstup[i] >= "A" <= "Z":
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
