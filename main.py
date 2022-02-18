# Vytvoril Matej Matejka
# Prevod z jakekoliv soustavy do destikove

def split(word):
    return list(word)
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

    # Pokud je zaklad vetsi nebo rovno 11, tak prevedeme pismena ktera jsou v listu na cisla
    if zaklad >= 11:
        for letter, n in enumerate(cislo_vstup):
            if n == 'A':
                cislo_vstup[letter] = '10'
            if n == 'B':
                cislo_vstup[letter] = '11'
            if n == 'C':
                cislo_vstup[letter] = '12'
            if n == 'D':
                cislo_vstup[letter] = '13'
            if n == 'E':
                cislo_vstup[letter] = '14'
            if n == 'F':
                cislo_vstup[letter] = '15'
            if n == 'G':
                cislo_vstup[letter] = '16'
            if n == 'H':
                cislo_vstup[letter] = '17'
            if n == 'I':
                cislo_vstup[letter] = '18'
            if n == 'J':
                cislo_vstup[letter] = '19'
            if n == 'K':
                cislo_vstup[letter] = '20'
            if n == 'L':
                cislo_vstup[letter] = '21'
            if n == 'M':
                cislo_vstup[letter] = '22'
            if n == 'N':
                cislo_vstup[letter] = '23'
            if n == 'O':
                cislo_vstup[letter] = '24'
            if n == 'P':
                cislo_vstup[letter] = '25'
            if n == 'Q':
                cislo_vstup[letter] = '26'
            if n == 'R':
                cislo_vstup[letter] = '27'
            if n == 'S':
                cislo_vstup[letter] = '28'
            if n == 'T':
                cislo_vstup[letter] = '29'
            if n == 'U':
                cislo_vstup[letter] = '30'
            if n == 'V':
                cislo_vstup[letter] = '31'
            if n == 'W':
                cislo_vstup[letter] = '32'
            if n == 'X':
                cislo_vstup[letter] = '33'
            if n == 'Y':
                cislo_vstup[letter] = '34'
            if n == 'Z':
                cislo_vstup[letter] = '35'
    # Itemi v listu prevedeme na int
    cislo_vstup_map = map(int, cislo_vstup)
    cislo_vstup = list(cislo_vstup_map)
    # Pokud list obsahuje cislo vetsi nez zaklad
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
    # v cyklu pro i od 0 do delky_retezce:
    for i in range(0, len(cislo_vstup)):
        # Kdyz je cislo[i] mezi 0 a 9
        if cislo_vstup[i] >= 0 <= 9:
                cislice = int(cislo_vstup[i])
            # kdyz je cislo mezi A a Z
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
    print("Výsledek je:", vysledek)
    print("Chcete převést nové číslo?: ")
    print("     1. ANO")
    print("     2. NE")
    cycl = int(input(": "))
if cycl == 2:
    print("Bye...")

