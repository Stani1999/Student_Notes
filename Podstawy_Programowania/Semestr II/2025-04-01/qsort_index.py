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