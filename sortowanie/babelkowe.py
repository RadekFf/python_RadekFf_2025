def sortuj_babelkowe(dane):
    n = len(dane)

    for i in range (0, n-1):
        for j in range (0, n-1-i):
            if dane[j] > dane[j+1]:
               dane[j], dane[j+1] = dane[j+1], dane[j]

if __name__ == '__main__':
    dane = [5,78,2,56,5,26]
    sortuj_babelkowe(dane)
    print(dane)