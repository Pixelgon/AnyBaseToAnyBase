# Vytvoril Matej Matejka
# Prevod z jakekoliv soustavy do destikove

def split(word):
    return list(word)
def lettonum():
    for letter, n in enumerate(cislo_vstup):
        if ord(n) >= 65 and ord(n) <= 90:
            cislo_vstup[letter] = ord(n) - 55
        if ord(n) >= 97 and ord(n) <= 122:
            cislo_vstup[letter] = ord(n) - 87
cycl = 1
while cycl == 1:
    # Nacteme zaklad jako int
    zaklad = int(input("Zadejte číselnou soustavu ve které je vaše číslo: "))
    # Overime zda jsme zadali spravnou soustavu
    while zaklad < 2 or zaklad > 36:
            print("Zadali jste špatnou soustavu")
            zaklad = int(input("Zadejte soustavu znovu: "))
    # Nacteme cislo jako string
    cislo_vstup = str(input("Zadejte číslo, které chcete převést: "))
    # Odstranime mezeri na zacatku a na konci
    cislo_vstup = cislo_vstup.strip()
    # Z cislo_vstup udelame list, kazdy znak rovna se 1 item v listu
    cislo_vstup = split(cislo_vstup)

    # Prevedeme pismena ktera jsou v listu na cisla
    lettonum()
    # Itemi v listu prevedeme na int
    cislo_vstup_map = map(int, cislo_vstup)
    cislo_vstup = list(cislo_vstup_map)
    # Pokud list obsahuje cislo vetsi nez zaklad
    while max(cislo_vstup) > zaklad:
        print("Číslo se neshoduje se soustavou")
        cislo_vstup = str(input("Zadejte číslo znovu: "))
        cislo_vstup = cislo_vstup.strip()
        cislo_vstup = split(cislo_vstup)
        lettonum()
        cislo_vstup_map = map(int, cislo_vstup)
        cislo_vstup = list(cislo_vstup_map)

    cislo = 0
    mocnina = len(cislo_vstup) - 1
    cislice = 0
    # v cyklu pro i od 0 do delky_retezce:
    for i in range(0, len(cislo_vstup)):
        # Kdyz je cislo[i] mezi 0 a 9
        if cislo_vstup[i] >= 0 <= 9:
                cislice = int(cislo_vstup[i])
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
    print("Výsledek je:", vysledek)
    print("Chcete převést nové číslo?")
    print("     1. ANO")
    print("     2. NE")
    cycl = int(input(": "))
if cycl == 2:
    print("Bye...")

