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