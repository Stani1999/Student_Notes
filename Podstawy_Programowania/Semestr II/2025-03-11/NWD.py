#Znajdowanie dzuekników które dzielą się bez reszty
import timeit, math

'''
#funkcja znajdz dzielnik(n:int)
# dla każdego elementu i od 1 do n+1
# jeżelie n % i == 0
## return i
'''
n = 10

def znajdz_dzielniki(n: int):
    dzielniki = []  # Lista do przechowywania dzielników
    for i in range(1, n + 1):  # 1, Gdyż nie dzieli się przez 0 n+1 bo python liczymy od 0
        if n % i == 0:  # Sprawdzamy, czy i jest dzielnikiem n
            dzielniki.append(i)  # Dodajemy i do listy dzielników
    return dzielniki  # Zwracamy listę dzielników

# Przykład użycia
n = 10
print(f"Dzielniki liczby {n}: {znajdz_dzielniki(n)}")


def znajdz_dzielniki2(n: int):
    return [i for i in range(1, n+1) if n % i == 0]


print(f"Dzielniki liczby {n}: {znajdz_dzielniki2(n)}", timeit.timeit(lambda: znajdz_dzielniki2(n), number = 1), "sekundy")


def znajdz_dzielnik3(n:int):
    return sorted({i for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0} | {n // i for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0})
print(f"Dzielniki liczby {n}: {znajdz_dzielnik3(n)}", timeit.timeit(lambda: znajdz_dzielnik3(n), number = 1), "sekundy")


def znajdz_nwd_mol(n):  # znajdz_najwiekszy_dzielnik_mniejszy_od_liczby
    return next(i for i in range(n // 2, 0, -1) if n % i == 0)

print(f"Największy dzielnik != liczby {n}: {znajdz_nwd_mol(n)}", timeit.timeit(lambda: znajdz_nwd_mol(n), number = 1), "sekundy")


'''
liczby pieresz
pseudokod

# funkcja liczby_pieresze(n):
#   jeżeli n<2 
#   return false
# loop dla każdego i od 2 do n
#   jeżeli n modulo i == 0
#       zwróc false
# zwróc true

'''


def czy_to_liczba_pierwsza(n):
    if n<2:
        return False, "Nie jest liczbą pierwszą"
    for i in range(2,n):
        if n % 1 == 0:
            return False, "Nie jest liczbą pierwszą"
    return True, "Jest liczbą pierwszą"

print(f"{n}: {czy_to_liczba_pierwsza(n)[1]}", timeit.timeit(lambda:  czy_to_liczba_pierwsza(n), number = 1), "sekundy")


#Do domu znalezienie liczb pierwszych od 0 do n w formie listy, Można użyć rekurencji
