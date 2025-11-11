liczby = [3, 5, 2, 8, 1]
lista = [3, 5, 2, 8, 1]

print("START")
print(liczby)
print("----------------")
def sortmax(liczby:list[int]) -> list[int]:
    if liczby == []:
        return "Brak elementów w liście"
    else:
        for i in range(len(liczby)):
            for j in range(len(liczby)-1):
                if liczby[j] < liczby[j+1]:
                    liczby[j], liczby[j+1] = liczby[j+1], liczby[j]
                    print (liczby)
        return liczby

sortmax(liczby)
print("KONIEC")
print(liczby)

lista = []

def znajdzmax(lista:list[int]) ->int:
    if lista == []:
        return "Brak elementów w liście"
    else:
        max_liczba = lista[0]
        for i in range(1, len(lista)):
            if lista[i] > max_liczba:
                max_liczba = lista[i]
        return max_liczba

print(znajdzmax(lista))


def znajdzmax2(liczby2:list[int]) ->int:
    if not liczby2:
        return None
    
    max_liczba = liczby2[0]
    for i in liczby2:
        if i > max_liczba:
            max_liczba = i
    return max_liczba
