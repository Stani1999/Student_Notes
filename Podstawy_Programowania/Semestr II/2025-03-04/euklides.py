'''
algorytm Euklidesa

funkcja euk(a:int,b:int)
pętla dpooki liczba a jest rozna od b 
    jesli a > b to od a odejmij b
    jesli a < b to od b odejmij a
zwroc a (lub b)
'''

def euklides(liczba_a:int,liczba_b:int)->int:
    while liczba_a != liczba_b:
        if liczba_a > liczba_b:
            liczba_a -= liczba_b
        elif liczba_a < liczba_b:
            liczba_b -= liczba_a
    return liczba_a
    
print(euklides(315, 504))


def reku_euklides(liczba_a, liczba_b):
    if liczba_a != liczba_b:
        if liczba_a > liczba_b:
            return reku_euklides(liczba_a - liczba_b, liczba_b)
        else:
            return (liczba_a, liczba_b - liczba_a)
    return liczba_a

## Wykonaj to dla opcji z dzieleniem przez liczby b(modulo) iteracyjnie i rekursywnie