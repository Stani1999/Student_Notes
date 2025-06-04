# Ćwiczenia 25-03-04
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
import timeit, math


def lista_pierwszych(n: int) -> list:
    # Funkcja tworzy listę liczb pierwszych od 0 do n
    if n < 2:
        return []                   # Brak liczb pierwszych dla n < 2
    lista_liczb = [2]               # dodanie 2, jedynej parzystej liczby pierwszej
    for i in range(3, n + 1, 2):    # Sprawdzanie tylko nieparzyste liczby
        is_prime = True             # Przed sprawdzeniem zakładam, że liczba jest pierwszą
        sqrt_i = int(i**0.5) + 1    # Zaokrąglona wartość pierwiastka z liczby + 1 do sprawdzania czy liczba jest pierwsza
        for dzielnik in lista_liczb:# Sprawdzamy podzielność tylko przez znalezione liczby pierwsze
            if dzielnik > sqrt_i:   # Jeżeli dzielnik jest więlszy od zaokrąflonej wartości liczby
                break               # Wyjście z pętli
            if i % dzielnik == 0:   # Jeżeli nie ma reszty z dzielenia
                is_prime = False    # To nie jest to liczba pierwsza
                break               # Wyjście z pętli
        if is_prime:                # Czy jest liczbą pierwszą (po ww. warunkach)
            lista_liczb.append(i)   # Dodanie liczby do listy
    return lista_liczb              # Zwrócenie listy


print(lista_pierwszych(17), timeit.timeit(lambda:  czy_to_liczba_pierwsza(n), number = 1), "sekundy")  

def lista_pierwszych_sito(n: int) -> list:
    # Funkcja tworzy listę liczb pierwszych od 1 do n
    if n < 2:                                               # Jeżeli n jest mniejsze od 2
        return []                                           # Zwrócenie listy (pustą)
    lista_liczb = [2] + [i for i in range(3, n + 1, 2)]     # Tworzenie listy zawierającej 2 oraz liczby nieparzyste od 3 do n
    for i in lista_liczb:                                   # Sprawdzanie, czy liczba jest pierwsza
        if i > 1:                                           # Pomijanie 1, bo nie jest liczbą pierwszą
            for krotnosc in range(i * i, n + 1, i):         # Porównywanie krotności z kolejnymi potęgami
                if krotnosc in lista_liczb:                 # Szukanie krotności w liście
                    lista_liczb.remove(krotnosc)            # Usuwanie wartości, w których znaleziono krotność
    return lista_liczb                                      # Zwróceni listy


print(lista_pierwszych_sito(17), timeit.timeit(lambda:  czy_to_liczba_pierwsza(n), number = 1), "sekundy")  

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

# Ćwiczenia 2025-03-11
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
import timeit, math


def lista_pierwszych(n: int) -> list:
    # Funkcja tworzy listę liczb pierwszych od 0 do n
    if n < 2:
        return []                   # Brak liczb pierwszych dla n < 2
    lista_liczb = [2]               # dodanie 2, jedynej parzystej liczby pierwszej
    for i in range(3, n + 1, 2):    # Sprawdzanie tylko nieparzyste liczby
        is_prime = True             # Przed sprawdzeniem zakładam, że liczba jest pierwszą
        sqrt_i = int(i**0.5) + 1    # Zaokrąglona wartość pierwiastka z liczby + 1 do sprawdzania czy liczba jest pierwsza
        for dzielnik in lista_liczb:# Sprawdzamy podzielność tylko przez znalezione liczby pierwsze
            if dzielnik > sqrt_i:   # Jeżeli dzielnik jest więlszy od zaokrąflonej wartości liczby
                break               # Wyjście z pętli
            if i % dzielnik == 0:   # Jeżeli nie ma reszty z dzielenia
                is_prime = False    # To nie jest to liczba pierwsza
                break               # Wyjście z pętli
        if is_prime:                # Czy jest liczbą pierwszą (po ww. warunkach)
            lista_liczb.append(i)   # Dodanie liczby do listy
    return lista_liczb              # Zwrócenie listy


print(lista_pierwszych(17), timeit.timeit(lambda:  czy_to_liczba_pierwsza(n), number = 1), "sekundy")  

def lista_pierwszych_sito(n: int) -> list:
    # Funkcja tworzy listę liczb pierwszych od 1 do n
    if n < 2:                                               # Jeżeli n jest mniejsze od 2
        return []                                           # Zwrócenie listy (pustą)
    lista_liczb = [2] + [i for i in range(3, n + 1, 2)]     # Tworzenie listy zawierającej 2 oraz liczby nieparzyste od 3 do n
    for i in lista_liczb:                                   # Sprawdzanie, czy liczba jest pierwsza
        if i > 1:                                           # Pomijanie 1, bo nie jest liczbą pierwszą
            for krotnosc in range(i * i, n + 1, i):         # Porównywanie krotności z kolejnymi potęgami
                if krotnosc in lista_liczb:                 # Szukanie krotności w liście
                    lista_liczb.remove(krotnosc)            # Usuwanie wartości, w których znaleziono krotność
    return lista_liczb                                      # Zwróceni listy


print(lista_pierwszych_sito(17), timeit.timeit(lambda:  czy_to_liczba_pierwsza(n), number = 1), "sekundy")  

# Ćwiczenia 25-03-18
bombelek = [5,3,7,2,1]
# Sortowanie ASC
# Sortowanie bombelkowe (bubble sort)
# Porównanie kolejnych par liczb
# jezeli elementy 1 jest większy od elementu 2 to (n-1):
#   zamiana miejsczami liczb

def bubble_sort(lista_do_posortowania):
    #Funkcja sortowania liczb (metoda przez bombelkowanie)
    n = len(lista_do_posortowania)  # Długość listy
    for i in range(n):  # Przejście przez listę n razy
        zmiana = False # Z założenia brak zmiay
        for j in range(0, n - i - 1):  # Przejście przez nieposortowaną część listy
            if lista_do_posortowania[j] > lista_do_posortowania[j + 1]:  # Porówywanie par elementów
                # Zamiana miejscami, jeśli elementy są w złej kolejności
                lista_do_posortowania[j], lista_do_posortowania[j + 1] = lista_do_posortowania[j + 1], lista_do_posortowania[j]
                zmiana = True # Była zmiana
            if not zmiana: # Jeżeli nie ma zmiany (Celem optymalizacji kodu)
                break
    return lista_do_posortowania


posortowana_lista = bubble_sort(bombelek)
print("Po sortowaniu:", posortowana_lista)

# ćwiczenie 2025-03-25
'''
lista = [3,2,1]

pivot = 3
mniejsze = [2,1]
większe_lub_rowne = []
sort = mniejsze + pivot + większe_lub_rowne
sort = [2,1] + [3] + []

lista = [2,1]
pivot = 2
mniejsze = [1]
większe_lub_rowne = []
sort = [1] + [2] + []

finish = [1,2] + 3 + [] =  [1,2,3]
'''

#   funkcja QuickShort(arr):
#       jezeli ilosc elementow arr >=1
#           zwroc arr
#       pivot = pierwszy element z listy
#       mniejse = lista liczb elemnetów miejsych od pivot
#       wienkse = lista liczb elementow wieksych od pivot
#       zwroc = quickShort(mniejse) + pivot + QuickShort(wiekse)
import timeit


def QuickSort(lista: list) -> list:
    #Funkcja sortowania metodą Quick Sort 
    if len(lista) <= 1:                                         # Jezeli ilość elementów listy jest mniejsza od 1
        return lista                                            # Zwróć listę jednoelementową
    mid = len(lista)//2                                         # Wyznaczenie srodka listy 
    pivot = lista[mid]                                          # Pobranie elementu środkowego
    mniejsze = [m for m in lista[:mid] + lista[mid+1:] if m <= pivot]  # Elementy mniejsze lub równe pivotowi
    wieksze = [w for w in lista[:mid] + lista[mid+1:] if w > pivot]    # Elementy większe od pivot'a
    return QuickSort(mniejsze) + [pivot] + QuickSort(wieksze)   # Łączenie posortowanych wartości

lista_przyklad = [8,4,5,6,8,69,69,76,4,105,75]
print (QuickSort(lista_przyklad), timeit.timeit(lambda:  QuickSort(lista_przyklad), number = 1), "sekundy")  

# Gdy mamy posortowaną listę -  najgorszy przypadek, ponieważ, wybierając pierwszy lub ostatni element działa nam jedna strona kodu, 
# optymalizacja przez dodanie srodka listy.

def QuickSortMediana(lista: list) -> list:
    #Funkcja sortowania metodą Quick Sort z wykorzystaniem mediany dla pivota
    if len(lista) <= 1:                     # Jezeli ilość elementów listy jest mniejsza od 1
        return lista                        # Zwróć listę jednoelementową
    
    # Wybór pivota jako mediany z:
    first = lista[0]                        # pierwszego,
    middle = lista[len(lista)//2]           # środkowego
    last = lista[-1]                        # i ostatniego elementu

    pivot = sorted([first, middle, last])[1] # Obliczenie mediany
    
    # Podział listy (pominięcie pivota jeśli występuje wielokrotnie)
    mniejsze = [x for x in lista if x < pivot] # Elementy mniejsze od pivotowi
    wieksze = [x for x in lista if x >= pivot] # Elementy większe lub równe pivotowi
    
    return QuickSort(mniejsze) + QuickSort(wieksze) # Łączenie posortowanych wartości

lista_przyklad = [8,4,5,6,8,69,69,76,4,105,75]
print(QuickSortMediana(lista_przyklad), timeit.timeit(lambda:  QuickSortMediana(lista_przyklad), number = 1), "sekundy")  

# Ćwiczenia 25-04-01
def QuickSort_Index(lista: list) -> list:
    """
    Sortuje listę algorytmem QuickSort z zachowaniem stabilności (kolejności elementów o tej samej wartości).
    
    Args:
        lista (list): Lista do posortowania
        
    Returns:
        list: Posortowana lista z zachowaną kolejnością elementów równych
    """
    if len(lista) <= 1:                     # Warunek końca rekurencji
        return lista
    
    # Tworzenie listy z indeksami (wartość, oryginalny_indeks)
    indexed_list = [(value, index) for index, value in enumerate(lista)]
    
    return QuickSort_Index_Helper(indexed_list)  # Wywołanie funkcji pomocniczej

def QuickSort_Index_Helper(indexed_list: list) -> list:
    """
    Funkcja pomocnicza realizująca właściwe sortowanie QuickSort.
    Operuje na liście krotek (wartość, oryginalny_indeks).
    
    Args:
        indexed_list (list): Lista krotek (wartość, indeks)
        
    Returns:
        list: Posortowane wartości z zachowaną kolejnością dla duplikatów
    """
    # Pomocnicza funkcja realizująca sortowanie
    if len(indexed_list) <= 1:              # Lista pusta lub 1-elementowa
        return [x[0] for x in indexed_list] # Zwróć same wartości
    
    # Wybór pivota jako mediany z trzech wartości
    first = indexed_list[0][0]              # Pierwszy element
    middle = indexed_list[len(indexed_list)//2][0] # Środkowy element
    last = indexed_list[-1][0]              # Ostatni element
    pivot = sorted([first, middle, last])[1] # Mediana
    
    # Podział na podlisty z uwzględnieniem indeksów
    mniejsze = [(val, idx) for val, idx in indexed_list if val < pivot]
    rowne = [(val, idx) for val, idx in indexed_list if val == pivot]
    wieksze = [(val, idx) for val, idx in indexed_list if val > pivot]
    
    # Sortowanie równych elementów po indeksach (dla stabilności)
    rowne_sorted = sorted(rowne, key=lambda x: x[1])
    # Łączenie posortowanych podlist
    return (QuickSort_Index_Helper(mniejsze) + 
            [x[0] for x in rowne_sorted] + 
            QuickSort_Index_Helper(wieksze))

lista_przyklad = [8,4,5,6,8,69,69,76,4,105,75]
print("Przed:", lista_przyklad)
print("Po:", QuickSort_Index(lista_przyklad))



## Counting sort, - każde wystąpienie elementu w zbiorze dodajemy do listy.
# Używamy kiedy jest duża ilość wtstąpień danej liczby.

def counting_sort(arr):
    max_val = max (arr)
    count = [0] * (max_val+1) #

    for num in arr:
        count[num] += 1

    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i]*count[i]) 

    return sorted_arr

# napisz funkcje, która sortuje oceny studentów w zakresie od 0 do 100
# watrosci wchodzące, lista ocen, min wart, max wartosc
# wyjsice posortowane oceny

oceny = [88, 92, 75, 83, 90, 92, 60, 85, 90]

def graduate_sort(grades, min_val=0, max_val=100):
    # Inicjalizacja listy zliczającej
    count = [0] * (max_val - min_val + 1)
    
    # Zliczanie wystąpień każdej oceny
    for grade in grades:
        if min_val <= grade <= max_val:
            count[grade - min_val] += 1
    
    # Budowanie posortowanej listy wynikowej
    sorted_grades = []
    for i in range(len(count)):
        sorted_grades.extend([i + min_val] * count[i])
    
    return sorted_grades


posortowane_oceny = graduate_sort(oceny)
print(posortowane_oceny)

# Ćwiczenia 25-04-08

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 1, 'C': 5},
    'C': {'D': 8, 'F': 2},
    'D': {'F': 2},
    'F': {} 
}

    #ustawiamy wieszchołki na nieskońconość
    # pierwszy element ustawiamy na 0

    #pętla while dla nie odwiedzonych elementów

        # wybieramy wierzchołek o najmniejszej wartości

        # jeżeli nie ma wierzchołków to koniec

        # sprawdzamy sąsiadów wybranego wierzchołka
            # jeżeli trasa jest krótsza to aktualizujemy

        # zaznaczamy wieszhołek odwiedzony

        # zwróc dystans
        
# wywołanie


def dijkstra(graph, start_node):
    # Ustawiamy wszystkie wierzchołki na nieskończoność
    distances = {node: float('infinity') for node in graph}
    # Pierwszy element ustawiamy na 0
    distances[start_node] = 0
    visited = set()
    
    # Pętla while dla nieodwiedzonych elementów
    while True:
        # Wybieramy wierzchołek o najmniejszej wartości
        current_node = None
        min_distance = float('infinity')
        for node in graph:
            if node not in visited and distances[node] < min_distance:
                min_distance = distances[node]
                current_node = node
        
        # Jeżeli nie ma wierzchołków to koniec
        if current_node is None:
            break
            
        # Sprawdzamy sąsiadów wybranego wierzchołka
        for neighbor, weight in graph[current_node].items():
            distance = distances[current_node] + weight
            # Jeżeli trasa jest krótsza to aktualizujemy
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                
        # Zaznaczamy wierzchołek jako odwiedzony
        visited.add(current_node)
    
    return distances

# Wywołanie
start_node = 'A'
shortest_distances = dijkstra(graph, start_node)
print(f"Najkrótsze ścieżki z węzła {start_node}:")
for node, distance in shortest_distances.items():
    print(f"Do {node}: {distance}")

# Ćwiczenia 25-04-15

## Lista jednokierunkowa

class Node:
    """Klasa reprezentująca pojedynczy węzeł listy jednokierunkowej.
        - data: przechowuje wartość danego węzła
        - next wskoźnik do następnego węzła (domylśnie NODE)"""

    def __init__(self, data):
        """Inicjalizacja data"""
        self.data = data  # Przechowuje wartość danego węzła
        self.next = None  # Ustaw next na None
        

class SingelyLinkedList: 
    """Klasa reprezentująca listę jednokierunkową."""
#     
    def __init__(self):
        """Inicjalizacja pustej listy"""
        # head: wskaźnik na pierwszy węzeł (domylśnie None)
        self.head = None   # - Inicjalizacja head jako None
    
    def append(self, data):
        """Dodaje nowy węzeł z danymi na koniec listy.
        
        Args:
            data: Wartość do dodania.
        """
        new_node = Node(data)  # Utwórz nowy wenzeł z wartością data
        
        if self.head is None:        # Jeśli Head jest None:
            self.head = new_node# Ustaw head na nowy węzeł
        else: # W przeciwnym razie:
        # Przejdź pezez listę do ostatniego węzła
            lastNode = self.head
            while lastNode.next is not None: 
                lastNode = lastNode.next
            lastNode.next = new_node # Ustaw next ostatniego węzłą na nowy węzeł

    def display(self):
        """Wyświetla zawartość listy"""
        if self.head is None: # Jeżeli hed jest Node:
            print("Lista jest puszta")# Wyświetl "Lista jest pusta"
        else: # W przeciwnym razie:
            i = self.head# zaczynając od head
            while i is not None: # Przejdź przez każdy węzeł
                print(i.data, end=" --> " if i.next else "")
                i = i.next# Wyświetl wartość każdego węzła po kolei
            print() #Nowa linia

    def delete(self, data):
        """Usuwa (pierwszą) pozycję z kolejki"""
        if self.head is None: # Jeżeli head jest Node:
            print("Lista jest pusta") # Wyświetl "Lista jest pusta"
            return # Zakończ operację

        if self.head == data: # Jeśli wartość head.data równa się data:
            self.head = self.head.next # Ustaw head na head.next (usuń pierwszy element)
            return # Zajkończ operację

        i = self.head
        #  Przejdź przez listę, szukając węzła z wartością data
        while i.next is not None and i.next.data != data:
            i = i.next
        
        if i.next is not None:  # Jeśli znajdziesz taki węzeł:
            i.next = i.next.next # Usuń go ustawiając wskaźnik poprzedniego węzłą na następny węzeł

# Przykład użycia
if __name__ == "__main__":
    # Tworzymy listę
    singelist = SingelyLinkedList()
    
    # Dodajemy elementy
    singelist.append(6)
    singelist.append(9)
    singelist.append(20)
    
    # Wyświetlamy listę
    print("Lista przed usunięciem:")
    singelist.display()  # 6 -> 9 -> 20
    
    # Usuwamy element
    singelist.delete(20)
    print("\nLista po usunięciu 20:")
    singelist.display()  # 6 -> 9
    
    # Próba usunięcia nieistniejącego elementu
    print("\nPróba usunięcia 99:")
    singelist.delete(99)  # Nic się nie dzieje
    singelist.display()   # 6 -> 

# Ćwiczenia 25-04-29

''' 
Programowanie dynamiczne 
Metoda rozwiązywania problemu polegająca na rozbijaniu ich na mniejsze podproblemy.
Każdy problem rozwiązuje się tylko raz zapisując jego wyniki.
++ Optymalizacja pamięci

-- Problem plecakowy 
--- praremtry typu wielkość i waga
--- oblicza się na podstawie wzoru.
'''

def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    
    # Śledzenie wybranych przedmiotów
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i-1)  # Indeks przedmiotu
            w -= weights[i-1]
    
    selected_items.reverse()  # Aby zachować kolejność dodawania
    return dp[n][capacity], selected_items

def main():
    print("Problem plecakowy (0-1 Knapsack)")
    print("---------------------------------")
    
    values = list(map(int, input("Podaj wartości przedmiotów (oddzielone przecinkami): ").split(",")))
    weights = list(map(int, input("Podaj wagi przedmiotów (oddzielone przecinkami): ").split(",")))
    capacity = int(input("Podaj pojemność plecaka: "))
    
    if len(values) != len(weights):
        print("Błąd: Liczba wartości i wag musi być taka sama!")
        return
    
    if capacity < 0:
        print("Błąd: Pojemność plecaka nie może być ujemna!")
        return
    
    max_value, selected = knapsack(values, weights, capacity)
    
    print(f"\nMaksymalna wartość w plecaku: {max_value}")
    print("Wybrane przedmioty:")
    for idx in selected:
        print(f"- Przedmiot {idx+1}: wartość = {values[idx]}, waga = {weights[idx]}")
    
    print("\nPodsumowanie:")
    print(f"Liczba wybranych przedmiotów: {len(selected)}")
    print(f"Sumaryczna waga: {sum(weights[i] for i in selected)}/{capacity}")
    print(f"Sumaryczna wartość: {max_value}")

if __name__ == "__main__":
    main()

# Ćwiczenia 25-05-06

"""
W drzewach mniejsze elementy idą w lewo, a większe w prawo
np drzewo 3 1 2          2 3 1
"""
#        [3]              [2]
#        /                  \
#       /                    \
#     [1]                    [3]
#       \                    /
#        \                  /      
#        [2]              [2]   

"""
W drzewach BST
Służy do wyszukiwań w bazach danych
np drzewo 3 1 2          2 3 1    
"""    
#            [3]           [2]
#             /            / \
#            /            /   \
#          [1]          [1]   [3]
#           \
#            \
#           [2]


tree = [1, 2, 3, 4, 5, 6, 7]

def get_left_child(index):
    """Zwraca lewe dziecko o danym indeksie"""
    return 2 * index + 1

def get_right_child(index):
    """Zwraca prawe dziecko o danym indeksie"""
    return 2 * index + 2

def get_parent(index):
    """Zwraca rodzica węzła o podanym indeksie"""
    return (index-1) // 2

# Dostęp do elementów drzewa
index = 0 # Korzeń drzewa
left_child_index = get_left_child(index)
rigth_child_index = get_right_child(index)

print(f"Zawartość korzenia: {tree[index]}")
print(f"Lewe dziecko korzenia: {tree[left_child_index]}")
print(f"Prawe dziecko korzenia: {tree[rigth_child_index]}")


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.rigth = None
        self.parent = None

# lista [3, 5, 7, 10, 20]
root = Node(10)
root.left = Node(5)
root.rigth = Node(20)
root.left.left = Node(3)
root.left.rigth = Node(7)


class BST:
    def  __init__(self, value):
        self.value = value
        self.left = None
        self.rigth = None
        self.parent = None

    def insert(self, new_value):
        if new_value < self.value:
            if self.left is None:
                self.left = BST (new_value)
                self.parent = self 
            else:
                self.left.insert(new_value)
        else:
            if self.rigth is None:
                self.rigth = BST (new_value)
                self.parent = self
            else:
                self.rigth.insert(new_value)

## do domy jak zrobić drzewo obliczjące (2+4)*7/4

    def search(self, search_value):
        if search_value == self.value:
            return self
        elif search_value < self.value and self.left is not None:
            return self.left.search(search_value)
        elif search_value > self.value and self.right is not None:
            return self.right.search(search_value)
        return None
    
    def find_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current
    
    def find_max(self):
        current = self
        while current.rigth is not None:
            current = current.rigth
        return current
    
    def delate(self, value):
        if value < self.value:
            if self.left is not None:
                self.left = self.left.delate(value)
        elif value > self.value:
            if self.rigth is not None:
                self.rigth = self.rigth.delate(value)
        
        else:
            # Usuwanie węzła 
            if self.left is None and self.rigth is None:
                return None
            elif self.left is None:
                self.left.parent = self.parent
                return self.left
            else:
                # węzeł z dwam dziaćmi
                min_node = self.rigth.find_min()
                self.value = min_node.value
                self.rigth = self.rigth.delate(min_node.value)
            return self

# Ćwiczenia 25-05-13

# Drzewa zbalanmsowane
# Drzewa AVL (modyfikacja drzewa BST. tak aby były) 


#Napisz drzewo AVL, które będzie miało następujące metordy
# Pre order
# In order
# Post order

# Wyskoość drzewa n-elemenowego drzewa AVL wynosi O(log n)
# Drzewo AVL jest drzewem BTS, które jest zbalanbsiowane 

# Rodzaje rotacji w drzewach AVL
## Ruch w lewo LL (left-left)
# Chodzi w niej o to, że węzeł jest dodawany do lewego poddrzewaa

# Ruch w prawo RR (rigth-rigth)
# Chodzi w niej o to, że węzeł jest dodawany do prawego poddrzewia

# Ruch w lewo-prewo LR (left-rigth)
# Chodzi w niej o to, że węzeł jest dodawany do prawego poddrzewia lewego węzłą.

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None 
        self.right = None
        self.height = 1

class AVLTree:
    # Get height of a node
    def get_height(self, node):
        if not node:
            return 0
        return node.height
    
    # Get balance factor of a node
    def get_balance(self, node):
        if not node:
            return 0 
        return self.get_height(node.left) - self.get_height(node.right)
    
    # Right rotation for LL case
    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y 
        y.left = T2 

        # Update heights
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x
    
    # Left rotation for RR case
    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y
    
    def insert(self, root, key): 
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Check balance
        balance = self.get_balance(root)
        
        # LL Case
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        
        # RR Case
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        
        # LR Case
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        
        # RL Case
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root
    
    # Tree traversal methods
    def preorder(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
    
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)
    
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end=" ")


# Test the AVL tree
if __name__ == "__main__":
    tree = AVLTree()
    root = None
    keys = [10, 20, 30, 40, 50, 25]
    
    for key in keys:
        root = tree.insert(root, key)
    
    print("Preorder AVL tree is:")
    tree.preorder(root)
    print("\nInorder AVL tree is:")
    tree.inorder(root)
    print("\nPostorder AVL tree is:")
    tree.postorder(root)

# Ćwiczenia 25-05-27

import hashlib

# Użycie SHA-256 do hashowania tekstu
text_to_hash = "Każdy byle nie Trszaskowski"

hash_object = hashlib.sha256(text_to_hash.encode())  # Dane wejściowe muszą być typu bytes
hash_value = hash_object.hexdigest()  # Zwraca wartość hash jako ciąg znaków szesnastkowych

print(hash_value)


import os
import hashlib

def hash_password(password):
    sale = os.urandom(16)  
    key = hashlib.pbkdf2_hmac('sha256', password.encode(), sale, 100000)
    return sale + key

# Hashing hasła
password = "safePassword123"
password_hashed = hash_password(password)
print(password_hashed)


def own_hash(word):
    return hash(word)

haslo = "tajne123"
print(f"Hash 256: {haslo} : {own_hash(haslo)} ")

def simple_hash(password, table_size=10):
    return sum(otd(c) for c in password) % table_size

words = ["kod", "pies"]


