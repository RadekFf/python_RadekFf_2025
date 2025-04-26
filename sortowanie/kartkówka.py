alfabet = "aąbcćdeęfghijklłmnopqrsśtuvwxyzźż"
dlugosc_alfabetu = len(alfabet)

szyfrogram = "eax toćę ksbax khlwex, fhsmws?"
def odszyfruj(szyfr, przesuniecie):
    wynik = ""
    for znak in szyfr:
        if znak in alfabet:
            indeks = alfabet.index(znak)
            nowy_indeks = (indeks - przesuniecie) % dlugosc_alfabetu
            wynik += alfabet[nowy_indeks]
        else:
            wynik += znak
    return wynik

for i in range(1, dlugosc_alfabetu + 1):
    odszyfrowane = odszyfruj(szyfrogram, i)
    print(f"[{i}] {odszyfrowane}")