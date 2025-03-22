def czy_pierwsza(liczba : int):
    liczba = 50
    for i in range (2, liczba):
        if liczba % i == 0:
            return False
        return True

if __name__ == '__main__':
    print(czy_pierwsza(50))