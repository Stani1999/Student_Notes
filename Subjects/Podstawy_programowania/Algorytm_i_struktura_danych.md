# 1. Algorytm

| **Cecha algorytmu**                     | **Opis**                                                                          |
|-----------------------------------------|-----------------------------------------------------------------------------------|
| **Skończony**                           | Algorytm ma określoną liczbę kroków i zawsze kończy swoje działanie.              |
| **Uporządkowany**                       | Algorytm składa się z kroków, które muszą być wykonywane w określonej kolejności. |
| **Ciąg jasno zdefiniowanych czynności** | Każdy krok algorytmu jest dokładnie określony i możliwy do zrozumienia.           |
| **Konieczny do wykonania zadania**      | Algorytm jest zaprojektowany w celu rozwiązania konkretnego problemu.             |

| **Warunki spełniane przez algorytm**    | **Opis**                                                                          |
|-----------------------------------------|-----------------------------------------------------------------------------------|
| **Wyróżniony początek**                 | Algorytm zaczyna się od jasno zdefiniowanego kroku początkowego.                  |
| **Jednoznaczność**                      | Każdy krok algorytmu ma jednoznaczne znaczenie i interpretację.                   |
| **Dyskretność**                       | Algorytm działa w sposób dyskretny, operując na pojedynczych krokach i wartościach. |
| **Uniwersalność**                       | Algorytm można zastosować w różnych przypadkach i dla różnych danych wejściowych. |
| **Efektywność**                         | Algorytm rozwiązuje problem w rozsądnym czasie i z użyciem ograniczonych zasobów. |
| **Wyróżniony koniec**                 | Algorytm kończy się w określonym momencie, gdy osiągnie swój cel lub warunek końca. |


# 2. Typy proste (w Python)  

| **Typ prosty**                | **Python**  | **Przykład**      | **Opis**                                                                 |
|-------------------------------|-------------|-------------------|--------------------------------------------------------------------------|
| **Liczba całkowita**          | `int`       | `42`              | Przechowuje liczby całkowite, zarówno dodatnie, jak i ujemne.            |
| **Liczba zmiennoprzecinkowa** | `float`     | `3.14`            | Przechowuje liczby rzeczywiste z częścią dziesiętną.                     |
| **Liczba zespolona**          | `complex`   | `1 + 2j`          | Liczby zespolone z częścią rzeczywistą i urojoną.                        |
| **Tekst (łańcuch znaków)**    | `str`       | `"Hello, World!"` | Przechowuje ciągi znaków (tekst) w Unicode.                              |
| **Wartość logiczna**          | `bool`      | `True`, `False`   | Typ logiczny reprezentujący wartości prawdy (`True`) i fałszu (`False`). |
| **Wartość pusta**             | `NoneType`  | `None`            | Specjalny typ reprezentujący brak wartości lub pusty obiekt.             |
| **Bajt**                      | `bytes`     | `b'hello'`        | Przechowuje ciąg bajtów (dane binarne).                                  |


# 3. Typy złożone (w Python).

| **Typ złożony**   | **Python**                | **Przykład**                                                                          | **Komentarz**                                                         |
|-------------------|---------------------------|---------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| **Tablica/Lista** | `list`                    | `[1, 2, 3, 4]`                                                                        | W Pythonie listy są dynamiczne i mogą przechowywać różne typy danych. |
| **Krotka**        | `tuple`                   | `(1, 2, 3)`                                                                           | Krotka jest niemodyfikowalna i przechowuje uporządkowane dane.        |
| **Zbiór**         | `set`                     | `{1, 2, 3}`                                                                           | Zbiór przechowuje unikalne wartości, bez powtórzeń.                   |
| **Słownik**       | `dict`                    | `{"klucz": "wartość", "wiek": 25}`                                                    | Słownik w Pythonie jest implementacją struktury klucz-wartość.        |
| **Rekord**        | `namedtuple`, `dataclass` | `from collections import namedtuple; Point = namedtuple("Point", "x y"); Point(1, 2)` | Używane do reprezentacji rekordów z polami dostępnymi po nazwie.      |
| **Stos**          | `list` lub `collections.deque` | `stos = []; stos.append(1); stos.pop()`                                          | Stos można zaimplementować za pomocą listy lub `deque`.               |
| **Kolejka**       | `queue.Queue`             | `q = Queue(); q.put(1); q.get()`                                                      | Kolejki FIFO dostępne w module `queue`.                               |
| **Drzewo**        | Brak wbudowanego          | `class Node: ...` lub `from anytree import Node; Node("root")`                        | Python nie ma wbudowanego typu drzewa, ale można go zaimplementować.  |
| **Plik**          | `open()` (obsługa plików) | `with open("plik.txt", "r") as f: dane = f.read()`                                    | Python obsługuje pliki za pomocą funkcji `open()` i metod na plikach. |

## 1. Porównanie typów złożonych 
### Różnice między listą, krotką, zbiorem i słownikiem w Pythonie


| **Cecha/Właściwość**            | **Lista**                                         | **Krotka**                                                    | **Zbiór**                                        | **Słownik**                                   |
|---------------------------------|---------------------------------------------------|---------------------------------------------------------------|--------------------------------------------------|-----------------------------------------------|
| **Definicja**                   | Kolekcja elementów w określonej kolejności.       | Kolekcja elementów w określonej kolejności, ale niemutowalna. | Kolekcja unikalnych elementów, nieuporządkowana. | Kolekcja par klucz-wartość, nieuporządkowana. |
| **Typ mutowalności**            | Mutowalna (można zmieniać elementy)               | Niemutowalna (nie można zmieniać elementów)                   | Mutowalny (można dodawać/usunąć elementy)        | Mutowalny (można dodawać/usunąć elementy)     |
| **Indeksowanie**                | Tak (indeksowanie zaczyna się od 0)               | Tak (indeksowanie zaczyna się od 0)                           | Nie (nie ma indeksów)                            | Tak (indeksowanie przez klucze)               |
| **Duplikaty**                   | Dozwolone (można mieć powtarzające się elementy)  | Dozwolone (można mieć powtarzające się elementy)          | Niedozwolone (wszystkie elementy muszą być unikalne) | Niedozwolone (klucze muszą być unikalne)      |
| **Porządek**                    | Uporządkowane (elementy zachowują kolejność)      | Uporządkowane (od Python 3.7+)                                | Nieuporządkowane (do Python 3.6)                 | Nieuporządkowane (do Python 3.6)              |
| **Złożoność operacji**          | O(n) przy dodawaniu, usuwaniu, szukaniu           | O(n) przy szukaniu, dodawaniu (brak zmiany)                   | O(1) przy dodawaniu, usuwaniu, szukaniu          | O(1) przy dodawaniu, usuwaniu, szukaniu       |
| **Szerokość zastosowania**      | Dynamiczne kolekcje, gdzie kolejność ma znaczenie | Kolekcje stałe, kiedy dane nie mają się zmieniać | Operacje na unikalnych elementach, np. matematyczne operacje zbiorów | Przechowywanie danych w postaci klucz-wartość |
| **Tworzenie**                   | `lista = [1, 2, 3]`                               | `krotka = (1, 2, 3)`                                          | `zbior = {1, 2, 3}`                              | `slownik = {'a': 1, 'b': 2}`                  |
| **Zastosowanie**                | Kolekcje danych, do których będziesz często dodawać lub zmieniać elementy | Kolekcje stałe, takie jak dane konfiguracyjne | Przechowywanie unikalnych danych i operacje na zbiorach | Przechowywanie powiązanych danych w formie klucz-wartość |
| **Dostęp do elementów**         | Indeksowanie, np. `lista[0]`                      | Indeksowanie, np. `krotka[0]`                                 | Nie ma indeksowania, ale można iterować          | Dostęp przez klucz, np. `slownik['a']`        |
| **Przykład dodawania elementu** | `lista.append(4)`                                 | Nie można dodawać                                             | `zbior.add(4)`                                   | `slownik['c'] = 3`                            |
| **Przykład usuwania elementu**  | `lista.remove(2)`                                 | Nie można usuwać                                              | `zbior.remove(2)`                                | `del slownik['a']`                            |


## 2. Operacje na typach złożonych 

### 1. **Wycinki (*slices*)** 
#### Wycinki umożliwiają szybki i wygodny sposób pracy z sekwencjami (np. listami, stringami). Są przydatne do filtrowania, modyfikacji i odwracania danych.

**Uwaga!** : Wcinki przyjmóją zakres włącznie od (start), **wyłącznie** do (end)

```python
list = [1, 2, 3, 4, 5]

seq[start:end:step]
```

| **Funkcjonalność**         | **Składnia**              | **Opis**                                                                              | **Przykład**            | **Wynik**         |
|----------------------------|---------------------------|---------------------------------------------------------------------------------------|-------------------------|-------------------|
| **Podstawowy wycinek**     | `seq[start:end]`          | Pobiera elementy od indeksu `start` (włącznie) do `end` (wyłącznie).                  | `lista[1:4]`            | `[2, 3, 4]`       |
| **Domyślny początek**      | `seq[:end]`               | Pobiera elementy od początku sekwencji do indeksu `end` (wyłącznie).                  | `lista[:3]`             | `[1, 2, 3]`       |
| **Domyślny koniec**        | `seq[start:]`             | Pobiera elementy od indeksu `start` do końca sekwencji.                               | `lista[2:]`             | `[3, 4, 5]`       |
| **Cała sekwencja**         | `seq[:]`                  | Pobiera całą sekwencję (kopiuje ją).                                                  | `lista[:]`              | `[1, 2, 3, 4, 5]` |
| **Krok (co n-ty element)** | `seq[start:end:step]`     | Pobiera elementy od `start` do `end` z krokiem `step`.                                | `lista[::2]`            | `[1, 3, 5]`       |
| **Odwrócenie sekwencji**   | `seq[::-1]`               | Pobiera elementy w odwrotnej kolejności (od końca do początku).                       | `lista[::-1]`           | `[5, 4, 3, 2, 1]` |
| **Negatywne indeksy**      | `seq[-start:-end]`        | Używa ujemnych indeksów, które liczą od końca sekwencji.                              | `lista[-3:-1]`          | `[3, 4]`          |
| **Łączenie wycinków**      | `seq[:mid] + seq[mid:]`   | Łączy dwa wycinki w jedną całość (podzielić i złączyć listę).                         | `lista[:2] + lista[2:]` | `[1, 2, 3, 4, 5]` |
| **Modyfikacja wycinków**   | `seq[start:end] = values` | Zamienia elementy w podanym zakresie na nowe wartości (dla list, które są mutowalne). | `lista[1:3] = [8, 9]`   | `[1, 8, 9, 4, 5]` |

### Przykład kodu:
```python
lista = [1, 2, 3, 4, 5]

# Podstawowe wycinki
print(lista[1:4])    # [2, 3, 4]
print(lista[:3])     # [1, 2, 3]
print(lista[2:])     # [3, 4, 5]

# Krok i odwrócenie
print(lista[::2])    # [1, 3, 5]
print(lista[::-1])   # [5, 4, 3, 2, 1]

# Modyfikacja listy
lista[1:3] = [8, 9]  
print(lista)         # [1, 8, 9, 4, 5]
```

## 3. Tabele dotyczące typów złożonych

### **1. Listy (*list*):**

| **Cecha/Właściwość**               | **Opis**                                                                                           | **Konstrukcja**                        | **Wynik**                                                                        |
|------------------------------------|----------------------------------------------------------------------------------------------------|----------------------------------------|----------------------------------------------------------------------------------|
| **Definicja**                      | Lista to dynamiczna, uporządkowana struktura danych, która może przechowywać różne typy elementów. | `lista = [1, "tekst", 3.14]`           | Lista zawiera elementy w określonej kolejności: `[1, "tekst", 3.14]`.            |
| **Tworzenie**                      | Listę można utworzyć za pomocą nawiasów kwadratowych lub funkcji `list()`.                         | `lista = []` lub `lista = list()`      | Pusta lista: `[]`.                                                               |
| **Tworzenie wyrażeń listowych**    | Prosty sposób tworzenia list, np. potęg liczby lub liczb parzystych w zakresie.                    | `lista = [x ** 2 for x in range(3)]`   | Lista: `[0, 1, 4]`.                                                              |
| **Konwertowanie**                  | Można konwertować (z iterować) inne sekwencje na listę za pomocą funkcji `list()`.                 | `lista = list("abc")`                  | Lista: `['a', 'b', 'c']`.                                                        |
| **Dostęp do elementów**            | Dostęp do elementów listy odbywa się za pomocą indeksów (liczonych od 0).                          | `lista[0]` dla `[0, 1, 2, 3]`          | Pierwszy element: `0`.                                                           |
| **Modyfikowalność**                | Listy są mutowalne – można dodawać, usuwać i zmieniać elementy po ich utworzeniu.                  | `lista[1] = 2` dla `[0, 1, 3]`         | Lista po modyfikacji: `[0, 2, 3]`.                                               |
| **Dodawanie elementów**            | Elementy można dodawać za pomocą metod `append()`, dodanie argumentu na końcu listy.               | `lista.append(4)` dla `[0, 1, 2]`      | Lista po dodaniu elementu: `[0, 1, 2, 4]`.                                       |
|                                    | lub `insert()`, podaje się dwa argumenty: index na który wpisać wartość oraz wartość to wpisania.  | `lista.insert(3, 10)` dla `[0, 1, 4]`  | Lista po dodaniu elementu: `[0, 1, 10, 4]`.                                      |
| **Dodawanie kilku elementów**      | Kilka elementów można dodać za pomocą metody `extend`, dodanie argumentów na koniec listy          | `lista.extend(5,6)` dla `[6, 7, 8]`    |  Lista po dodaniu elementów: `[6, 7, 8, 5, 6]`                                   |  
|                                    | lup przez przypisanie wielu wartości do indeksów za pomocą wcinka `lista[:]` = [wartości]          | `lista[1:2] = [1,2]` dla `[6, 7, 8]`   | Lista po dodaniu elementów: `[6, 1, 2, 8]`.                                      |
| **Usuwanie elementów**             | Elementy usuwa się metodami `remove()`, usunięcie argumentu jeżeli znajduje się na liście;         | `lista.remove(4)` dla `[3, 4, 5]`      | Lista po usunięciu: `[3, 5]`.                                                    |
|                                    | `pop()`, argument to index do usunięcia, jężeli taki istnieje.                                     | `lista.pop(1)` dla `[3, 4, 5]`         | Lista po usunięciu: `[3, 5]`.                                                    |
| **Usuwanie kilku elementów**       | Polega na przypisaniu pustej listy do indeksów za pomocą wcinka `lista[:]` = [];                   | `lista[1:2] = []` dla `[5, 6, 7, 8]`   | Lista po usunięciu elementów: `[5, 7, 8]`.                                       |
|                                    | metodą `clear` czyści się całą list ę(staje się więc pusta). Do jej usunięcia służy metoda `del`   | `lista.clear()` dla `[3, 4, 5]`        | Lista po użyciu metody `clear` `[]`                                              |
| **Rozmiar listy**                  | Liczbę elementów w liście można sprawdzić za pomocą funkcji `len()`.                               | `len(lista)` dla `[0, 1, 2]`           | Liczba elementów: `3`.                                                           |
| **Iteracja**                       | Po elementach listy można iterować za pomocą pętli `for`.                                          | `for el in lista: print(el)`           | Wypisanie elementów, np. dla `[1, 2]`: `1`, `2`.                                 |
| **Iteracja z indeksem enimmerate** | Metoda `enumerate()` pozwa la na iterowanie po liście i jednoczesne uzyskanie indeksu elementu.	  | `for i, el in enumerate(lista):`       | W każdej iteracji indeks to numer bieżącego elementu, a element to jego wartość. |
| **Typy elementów**                 | Lista może przechowywać elementy różnych typów jednocześnie.                                       | `[1, "abc", 3.5, True]`                | Lista: `[1, "abc", 3.5, True]`.                                                  |
| **Sortowanie**                     | Listę można posortować metodą `sort()` z opcjonalnym argumentem reverse (od najmniejszej liczby)   | `lista.sort()` dla `[4, 2, 1]`         | Posortowana lista: `[1, 2, 4]`.                                                  |
| ***Sortowanie z kluczem**          | Sortowanie można dostosować za pomocą argumentu key.                                               |	`lista.sort(key=abs)` dla `[-3, 1, 2]` | Posortowana lista: `[1, 2, -3]`.                                                 |
| **Wyszukiwanie elementu**          | Metoda `index()` zwraca pierwszy indeks elementu podanego jako argument.	                          | `lista.index(2)` dla `[1, 2, 3]`	   | Indeks: `1`.                                                                     |
| **Liczba wystąpień elementu**      |	Metoda `count()` zwraca liczbę wystąpień elementu w liście.	                                      | `lista.count(2)` dla `[1, 2, 2, 3]`    | Liczba wystąpień: `2`.                                                           |
| **Kopiowanie**                     | Kopię listy można stworzyć za pomocą metody `copy()` lub wycinka `[:]`.                            | `kopia = lista.copy()`                 | Oryginalna i skopiowana lista: `[1, 2, 3]`.                                      |
| **Operacje na listach**            | Konkatenacja list za pomocą `+`, powielanie za pomocą `*`.                                         | `[1, 2] + [3, 4]` = `[1, 2, 3, 4]`     | Wynik: `[1, 2, 3, 4]` lub `[1, 2, 1, 2]` przy `[1, 2] * 2`.                      |
| **Podstawowe operacje numeryczne** | Funkcje `sum()`, `min()`, i `max()` działają na listach liczbowych.                                |	`sum([1, 2, 3])`                       | Suma elementów: `6`, `min` zwraca najmniejszą liczbę a `max` największą.         |
| **Gniazdowanie, macierze**         | Listy mogą zawierać inne listy jako elementy (listy zagnieżdżone).                                 | `lista = [[1, 2], [3, 4]]`             | Zagnieżdżona struktura: `[[1, 2], [3, 4]]`.                                      |

#### Przykład użycia listy:
```python
# Tworzenie listy
lista = [1, 2, 3, 4, 5]

# Dodawanie elementów
lista.append(6)        # Dodaje element na końcu listy
print(lista)            # [1, 2, 3, 4, 5, 6]

# Zmiana elementu
lista[0] = 10           # Zmienia pierwszy element
print(lista)            # [10, 2, 3, 4, 5, 6]

# Usuwanie elementu
lista.remove(4)         # Usuwa pierwszy napotkany element o wartości 4
print(lista)            # [10, 2, 3, 5, 6]

# Iterowanie po liście
for element in lista:
    print(element)      # Wydrukuje każdy element listy

# Łączenie list
lista2 = [7, 8, 9]
nowa_lista = lista + lista2  # Łączy dwie listy
print(nowa_lista)        # [10, 2, 3, 5, 6, 7, 8, 9]

# Wycinki (slicing)
fragment = lista[1:4]    # Wybiera elementy od indeksu 1 do 3 (nie włącznie z 4)
print(fragment)          # [2, 3, 5]

# Tworzenie macierzy
macierz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Dodawanie wiersza
macierz.append([10, 11, 12])  # Dodaje nowy wiersz na końcu macierzy
print(macierz)
# [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [10, 11, 12]
# ]

# Zmiana elementu
macierz[0][0] = 99  # Zmienia pierwszy element w pierwszym wierszu
print(macierz)
# [
#     [99, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [10, 11, 12]
# ]

# Usuwanie wiersza
macierz.remove([7, 8, 9])  # Usuwa pierwszy napotkany wiersz równy [7, 8, 9]
print(macierz)
# [
#     [99, 2, 3],
#     [4, 5, 6],
#     [10, 11, 12]
# ]

# Iterowanie po macierzy
for wiersz in macierz:
    for element in wiersz:
        print(element, end=" ")  # Wydrukuje każdy element w macierzy w jednej linii
    print()  # Przejście do nowej linii po każdym wierszu

# Łączenie macierzy
macierz2 = [
    [13, 14, 15],
    [16, 17, 18]
]
nowa_macierz = macierz + macierz2  # Łączy dwie macierze
print(nowa_macierz)
# [
#     [99, 2, 3],
#     [4, 5, 6],
#     [10, 11, 12],
#     [13, 14, 15],
#     [16, 17, 18]
# ]

# Wycinki (slicing)
fragment_macierzy = [wiersz[1:3] for wiersz in macierz]  # Wybiera elementy od indeksu 1 do 2 (nie włącznie z 3) z każdego wiersza
print(fragment_macierzy)
# [
#     [2, 3],
#     [5, 6],
#     [11, 12]
# ]

# Spłaszczanie list zagnieżdzonych za pomocą Rekursji
def sflaszcz_liste(zagniezdzona_lista):
    """
    Funkcja rekurencyjna do spłaszczania zagnieżdżonych list.
    """
    wynik = []
    for element in zagniezdzona_lista:
        if isinstance(element, list):  # Jeśli element jest listą, wywołaj funkcję rekurencyjnie
            wynik.extend(sflaszcz_liste(element))
        else:
            wynik.append(element)  # Jeśli element nie jest listą, dodaj go do wyniku
    return wynik

# Przykład użycia
zagniezdzona_lista = [1, [2, [3, 4], 5], [6, 7], 8]
spłaszczona_lista = sflaszcz_liste(zagniezdzona_lista)
print(spłaszczona_lista)  # [1, 2, 3, 4, 5, 6, 7, 8]

# Iteracja przy użyciu enumetate
owoce = ["jabłko", "banan", "gruszka"]
for indeks, owoc in enumerate(owoce):
    print(f"Owoc na pozycji {indeks+1}: {owoc}")

# Owoc na pozycji 1: jabłko
# Owoc na pozycji 2: banan
# Owoc na pozycji 3: gruszka
```


### **2. Krotki (*tuples*):**

#### Główne różnice między listami a krotkami:
- **Krotki są niemutowalne**, co czyni je bardziej wydajnymi i bezpiecznymi, ale mniej elastycznymi niż listy.
- Krotki są często używane, gdy dane są stałe i nie powinny być modyfikowane, np. współrzędne punktów czy klucze w strukturach danych.


| **Cecha/Właściwość**        | **Opis**                                                                                                  | **Konstrukcja**                     | **Wynik**                                                                          |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|-------------------------------------|------------------------------------------------------------------------------------|
| **Definicja**               | Krotka to niemutowalna, uporządkowana struktura danych, która może przechowywać różne typy elementów.     | `krotka = (1, "tekst", 3.14)`       | `(1, "tekst", 3.14)`                                                               |
| **Tworzenie**               | Krotkę można utworzyć za pomocą nawiasów okrągłych lub funkcji `tuple()`.                                 | `krotka = (1, 2, 3)` lub `tuple([1, 2])` | `(1, 2, 3)`                                                                   |
| **Konwertowanie**           | Można konwertować inne sekwencje na krotki za pomocą funkcji `tuple()`.                                   | `tuple({1, 2, 3})`                  | `(1, 2, 3)`                                                                        |
| **Dostęp do elementów**     | Dostęp do elementów krotki odbywa się za pomocą indeksów (liczonych od 0).                                | `krotka[0]` zwraca pierwszy element | Wartość pierwszego elementu, np. `1` dla `krotka = (1, 2, 3)`                      |
| **Niemodyfikowalność**      | Krotki są niemutowalne – po ich utworzeniu nie można dodawać, usuwać ani zmieniać elementów.              | Nie można wykonać `krotka[0] = 10`. | Operacja spowoduje błąd typu `TypeError`.                                          |
| **Dodawanie elementów**     | Nie można dodawać nowych elementów do istniejącej krotki.                                                 | Niedozwolone: `krotka.append(4)`    | Operacja spowoduje błąd typu `AttributeError`.                                     |
| **Usuwanie elementów**      | Nie można usuwać elementów z krotki.                                                                      | Niedozwolone: `del krotka[0]`       | Operacja spowoduje błąd typu `TypeError`.                                          |
| **Rozmiar krotki**          | Liczbę elementów w krotce można sprawdzić za pomocą funkcji `len()`.                                      | `len(krotka)`                       | Liczba elementów w krotce, np. `3` dla `krotka = (1, 2, 3)`.                       |
| **Iteracja**                | Po elementach krotki można iterować za pomocą pętli `for`.                                                | `for el in krotka: print(el)`       | Elementy krotki są wypisywane w kolejności, np. dla `(1, 2)`: `1` i `2`.           |
| **Typy elementów**          | Krotka może przechowywać elementy różnych typów jednocześnie.                                             | `(1, "abc", 3.5, True)`             | `(1, "abc", 3.5, True)`                                                            |
| **Sortowanie**              | Krotka nie może być posortowana w miejscu, ale można utworzyć posortowaną listę z krotki.                 | `sorted(krotka)`                    | Posortowana lista, np. `[1, 2, 3]` dla `krotka = (3, 1, 2)`.                       |
| **Kopiowanie**              | Krotka jest niemutowalna, więc kopiowanie zwykle nie jest wymagane – wszystkie odniesienia są bezpieczne. | `kopia = krotka`                    | `kopia` będzie odnosić się do tych samych danych, co `krotka`, np. `(1, 2, 3)`.    |
| **Operacje na krotkach**    | Konkatenacja krotek za pomocą `+`, powielanie za pomocą `*`.                                              | `(1, 2) + (3, 4)` = `(1, 2, 3, 4)`  | Wynik konkatenacji `(1, 2, 3, 4)` lub powielenia `(1, 2, 1, 2)` przy `(1, 2) * 2`. |
| **Gniazdowanie**            | Krotki mogą zawierać inne krotki jako elementy (krotki zagnieżdżone).                                     | `((1, 2), (3, 4))`                  | Zagnieżdżona struktura: `((1, 2), (3, 4))`.                                        |

#### Przykład użycia krotki:
```python
# Tworzenie krotki
krotka = (1, 2, 3, 4, 5)

# Dostęp do elementów
print(krotka[0])         # 1
print(krotka[-1])        # 5 (ostatni element)

# Iterowanie po krotce
for element in krotka:
    print(element)       # Wydrukuje każdy element krotki

# Sprawdzanie, czy element jest w krotce
print(3 in krotka)      # True
print(6 in krotka)      # False

# Łączenie krotek
krotka2 = (6, 7, 8)
nowa_krotka = krotka + krotka2  # Łączy dwie krotki
print(nowa_krotka)      # (1, 2, 3, 4, 5, 6, 7, 8)

# Konwersja krotki na listę
lista_z_krotki = list(krotka)
print(lista_z_krotki)   # [1, 2, 3, 4, 5]

# Przykład nieudanej próby zmiany elementu (błąd)
# krotka[0] = 10  # Błąd: 'tuple' object does not support item assignment
```


### **3. Zbiory (*set*):**

| **Cecha/Właściwość**        | **Opis**                                                                                                             | **Konstrukcja**                            | **Wynik**                                                                                        |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------|--------------------------------------------|--------------------------------------------------------------------------------------------------|
| **Definicja**               | Zbiór to nieuporządkowana kolekcja unikalnych elementów. W Pythonie zbiory są implementowane za pomocą typu `set`.   | `zbior = {1, 2, 3}`                        | Zbiór zawiera unikalne elementy: `{1, 2, 3}`.                                                    |
| **Tworzenie**               | Zbiory tworzymy za pomocą nawiasów klamrowych `{}` lub funkcji `set()`.                                              | `zbior = {1, 2, 3}` lub `zbior = set([1, 2, 3])` | Zbiór `{1, 2, 3}` lub `{1, 2, 3}` (przy użyciu funkcji `set()`).                           |
| **Dostęp do elementów**     | Zbiory są nieuporządkowane, więc nie mają indeksów. Nie można bezpośrednio uzyskać dostępu do elementu przez indeks. | Brak dostępu przez indeks, np. `zbior[0]` jest niedozwolone. | Operacja typu `zbior[0]` spowoduje błąd `TypeError`.                           |
| **Dodawanie elementów**     | Elementy dodaje się za pomocą metody `add()`.                                                                        | `zbior.add(4)`                             | Zbiór po dodaniu elementu: `{1, 2, 3, 4}`.                                                       |
| **Usuwanie elementów**      | Elementy usuwa się za pomocą metody `remove()` lub `discard()`. Metoda `pop()` usuwa losowy element.                 | `zbior.remove(3)` lub `zbior.discard(3)`   | Zbiór po usunięciu elementu: `{1, 2}` (dla `zbior = {1, 2, 3}`).                                 |
| **Sprawdzanie przynależności** | Można sprawdzić, czy element należy do zbioru za pomocą operatora `in`.                                           | `3 in zbior` zwraca `True`                 | Wynik `True` lub `False`, np. `3 in {1, 2, 3}` zwraca `True`.                                    |
| **Operacje na zbiorach**    | Można wykonywać operacje takie jak: `union()`, `intersection()`, `difference()`, `symmetric_difference()`.           | `zbior1.union(zbior2)`                     | Wynik operacji, np. `zbior1 = {1, 2}`, `zbior2 = {2, 3}` → `zbior1.union(zbior2)` = `{1, 2, 3}`. |
| **Usunięcie wszystkich elementów** | Zbiory można opróżnić za pomocą metody `clear()`.                                                             | `zbior.clear()`                            | Zbiór po wyczyszczeniu: `set()` (pusty zbiór).                                                   |
| **Konwersja do/z innych struktur** | Zbiory można konwertować do list, krotek i innych struktur danych.                                            | `list(zbior)` lub `tuple(zbior)`           | Wynik konwersji, np. `list({1, 2, 3})` → `[1, 2, 3]`.                                            |
| **Zalety**                  | Zbiorów to szybkie sprawdzanie przynależności elementów, a także możliwość wykonywania matematycznych operacji na zbiorach. | -                                   | Wysoka wydajność dla operacji sprawdzania obecności elementów i operacji matematycznych.         |
| **Zastosowanie**            | Zbiory są często wykorzystywane w algorytmach, gdzie ważne jest unikanie duplikatów i szybkie operacje sprawdzające, czy dany element znajduje się w zbiorze. | - | Wygodne przechowywanie unikalnych danych, np. eliminowanie duplikatów z listy.                   |

#### Przykład użycia zbioru:
```python
# Tworzenie zbioru
zbior = {1, 2, 3, 4}

# Dodawanie elementów
zbior.add(5)   # Zbiór: {1, 2, 3, 4, 5}
zbior.add(2)   # Zbiór pozostaje bez zmian, ponieważ 2 już istnieje

# Usuwanie elementów
zbior.remove(3)   # Zbiór: {1, 2, 4, 5}
zbior.discard(10)  # Brak błędu, ponieważ 10 nie istnieje w zbiorze
print(zbior.pop()) # Usuwa losowy element, np. 1

# Operacje na zbiorach
zbior2 = {3, 4, 5, 6}
print(zbior.union(zbior2))          # Zbiór: {1, 2, 3, 4, 5, 6}
print(zbior.intersection(zbior2))   # Zbiór: {4, 5}
print(zbior.difference(zbior2))     # Zbiór: {1, 2}
print(zbior.symmetric_difference(zbior2))  # Zbiór: {1, 2, 6}
```

### 4. **Słownik** (*dict*ionary):

| **Cecha/Właściwość**          | **Opis**                                                                                                   | **Konstrukcja**                           | **Wynik**                                                   |
|-------------------------------|------------------------------------------------------------------------------------------------------------|-------------------------------------------|-------------------------------------------------------------|
| **Definicja**                 | Słownik to struktura danych przechowująca pary klucz-wartość. Klucze muszą być unikalne i niemutowalne.    | `slownik = {'a': 1, 'b': 2, 'c': 3}`      | Słownik z parami klucz-wartość: `{'a': 1, 'b': 2, 'c': 3}`. |
| **Tworzenie**                 | Słownik tworzony jest za pomocą nawiasów klamrowych `{}`.                                                  | `slownik = {'klucz1': 'wartość1'}`        | Powstaje słownik: `{'klucz1': 'wartość1'}`.                 |
| **Dodawanie elementów**       | Elementy dodaje się, przypisując wartość do klucza. Jeśli klucz istnieje, wartość zostanie zaktualizowana. | `slownik['d'] = 4`                        | Dodanie elementu: `{'a': 1, 'b': 2, 'c': 3, 'd': 4}`.       |
| **Dostęp do elementów**       | Dostęp do wartości odbywa się za pomocą klucza.                                                            | `slownik['a']`                            | Zwracana wartość klucza `a`: `1`.                           |
| **Usuwanie elementów**        | Elementy usuwa się za pomocą metody `del` lub `pop()`.                                                     | `del slownik['b']` lub `slownik.pop('c')` | Po usunięciu: `{'a': 1, 'd': 4}`.                           |
| **Sprawdzanie przynależności** | Można sprawdzić, czy dany klucz istnieje w słowniku za pomocą operatora `in`.                             | `'a' in slownik`                          | Wynik: `True`, jeśli `a` istnieje w słowniku.               |
| **Iteracja**                  | Po słowniku można iterować, aby uzyskać dostęp do jego kluczy, wartości lub obu naraz.                     | `for klucz, wartosc in slownik.items():`  | Iteracja zwraca np. `('a', 1)`, `('b', 2)` itd.             |
| **Konwersja z innych struktur** | Słowniki można tworzyć z listy krotek (para klucz-wartość).                                              | `slownik = dict([('a', 1), ('b', 2)])`    | Powstaje słownik: `{'a': 1, 'b': 2}`.                       |
| **Metody**                    | Metody do manipulacji: `keys()`, `values()`, `items()`, `get()`, `update()`, `clear()`, `popitem()`.       | `slownik.keys()`                          | Zwraca obiekt widoku kluczy: `dict_keys(['a', 'b', 'c'])`.  |

#### Przykłady użycia słownika w Pythonie:
```python
# Tworzenie słownika
slownik = {'a': 1, 'b': 2, 'c': 3}

# Dodawanie elementu
slownik['d'] = 4       # Słownik: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Dostęp do elementu
print(slownik['a'])    # 1

# Sprawdzanie, czy klucz istnieje
print('a' in slownik)  # True
print('e' in slownik)  # False

# Usuwanie elementu
del slownik['b']       # Słownik: {'a': 1, 'c': 3, 'd': 4}
print(slownik)

# Iterowanie po słowniku
for klucz, wartosc in slownik.items():
    print(f'Klucz: {klucz}, Wartość: {wartosc}')

# Metoda get() do pobierania wartości
print(slownik.get('a'))  # 1
print(slownik.get('b', 'Brak'))  # 'Brak' (jeśli klucz nie istnieje)

# Konwersja z listy krotek
lista_krotek = [('x', 10), ('y', 20)]
nowy_slownik = dict(lista_krotek)   # {'x': 10, 'y': 20}
print(nowy_slownik)

# Aktualizacja słownika
slownik.update({'e': 5, 'f': 6})  # Słownik: {'a': 1, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
print(slownik)

# Usuwanie ostatniego elementu (metoda popitem)
ostatni_element = slownik.popitem()  # Usuwa ('f', 6)
print(ostatni_element)               # ('f', 6)
print(slownik)                       # {'a': 1, 'c': 3, 'd': 4, 'e': 5}

# Opróżnianie słownika
slownik.clear()  # Słownik jest teraz pusty: {}
print(slownik)
```

### **5. Stos (*stack*):** 

| **Cecha/Właściwość**        | **Opis**                                                                                                                                    | **Konstrukcja**           | **Wynik**                                                                 |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|---------------------------------------------------------------------------|
| **Definicja**               | Stos to struktura danych działająca na zasadzie LIFO (Last In, First Out) – ostatni element dodany jest pierwszym, który zostanie usunięty. | `stos = []`               | Powstaje pusty stos: `[]`.                                                |
| **Tworzenie**               | Stos można utworzyć jako listę lub używać specjalnych klas/stosów z modułów takich jak `collections.deque`.                                 | `stos = []`               | Utworzono pusty stos jako listę: `[]`.                                    |
| **Dodawanie elementów**     | Elementy dodaje się za pomocą metody `append()`.                                                                                            | `stos.append(1)`          | Dodanie elementu: `[1]`.                                                  |
| **Usuwanie elementów**      | Elementy usuwa się za pomocą metody `pop()`, która usuwa i zwraca ostatni element.                                                          | `stos.pop()`              | Po usunięciu elementu `[1, 2]`, stos to `[1]`, a zwrócona wartość to `2`. |
| **Podgląd szczytu**         | Aby zobaczyć ostatni dodany element (bez usuwania), można użyć `stos[-1]`.                                                                  | `stos[-1]`                | Jeśli stos to `[1, 2, 3]`, wynik to `3`.                                  |
| **Sprawdzanie pustego stosu**| Można sprawdzić, czy stos jest pusty za pomocą `len()` lub `not stos`.                                                                     | `len(stos) == 0`          | Wynik: `True` dla pustego stosu `[]`, `False` dla `[1]`.                  |
| **Kopiowanie stosu**        | Stos można skopiować za pomocą `copy()` lub wycinka.                                                                                        | `stos_copy = stos.copy()` | Oryginał: `[1, 2]`, kopia: `[1, 2]`.                                      |
| **Zalety**                  | Stos jest efektywny w przypadkach, gdzie ważna jest operacja dostępu do ostatnio dodanych danych, np. w rekurencji.                         | -                         | Szybki dostęp do ostatnio dodanego elementu i usuwanie w czasie O(1).     |
| **Zastosowanie**            | Stos jest używany w algorytmach przetwarzania wyrażeń, w systemach rekurencyjnych, zarządzaniu historią (np. w przeglądarkach).             | -                         | Stos może obsłużyć operacje typu "cofnij" w aplikacjach.                  |


#### Przykład użycia stosu za pomocą listy:
```python
# Tworzenie stosu
stos = []

# Dodawanie elementów
stos.append(1)  # Stos: [1]
stos.append(2)  # Stos: [1, 2]
stos.append(3)  # Stos: [1, 2, 3]

# Usuwanie elementów
print(stos.pop())  # Zwraca 3, Stos: [1, 2]
print(stos.pop())  # Zwraca 2, Stos: [1]

# Podgląd szczytu
print(stos[-1])    # Zwraca 1

# Sprawdzanie pustego stosu
print(len(stos) == 0)  # False, ponieważ stos nie jest pusty
```

### 6. **Kolejka (*queue*)**:

| **Cecha/Właściwość**        | **Opis**                                                                                            | **Konstrukcja**                            | **Wynik**                                                                       |
|-----------------------------|-----------------------------------------------------------------------------------------------------|--------------------------------------------|---------------------------------------------------------------------------------|
| **Definicja**               | Kolejka to struktura danych działająca na zasadzie FIFO (First In, First Out).                      | `kolejka = []`                             | Powstaje pusta kolejka: `[]`.                                                   |
| **Tworzenie**               | Kolejkę można tworzyć jako listę lub, dla lepszej wydajności, za pomocą `collections.deque`.        | `kolejka = deque()`                        | Utworzono pustą kolejkę z `deque`: `deque([])`.                                 |
| **Dodawanie elementów**     | Elementy dodaje się na końcu kolejki za pomocą `append()` (dla `deque`) lub `list.append()`.        | `kolejka.append(1)`                        | Po dodaniu elementu `1`, kolejka to `[1]`.                                      |
| **Usuwanie elementów**      | Elementy usuwa się z początku kolejki za pomocą `pop(0)` (dla listy) lub `popleft()` (dla `deque`). | `kolejka.pop(0)` lub `kolejka.popleft()`   | Po usunięciu pierwszego elementu `[1, 2, 3]`, kolejka to `[2, 3]`.              |
| **Sprawdzanie pustej kolejki** | Można sprawdzić, czy kolejka jest pusta za pomocą `len()` lub `not kolejka`.                     | `len(kolejka) == 0`                        | Wynik: `True` dla pustej kolejki `[]`, `False` dla `[1]`.                       |
| **Iteracja**                | Po kolejce można iterować, aby uzyskać dostęp do jej elementów w kolejności ich dodania.            | `for element in kolejka:`                  | Elementy `[1, 2, 3]` zostaną wypisane w kolejności: `1, 2, 3`.                  |
| **Zalety**                  | Kolejki są użyteczne w zadaniach, które wymagają przetwarzania elementów w kolejności ich dodania, np. w symulacjach, procesach kolejkowych. | - | Obsługa procesów w kolejności ich zgłoszenia, np. w drukarce lub systemie FIFO. |

#### Przykład użycia kolejki za pomocą listy:
```python
# Tworzenie kolejki (lista)
kolejka = []

# Dodawanie elementów do kolejki
kolejka.append(1)   # Kolejka: [1]
kolejka.append(2)   # Kolejka: [1, 2]
kolejka.append(3)   # Kolejka: [1, 2, 3]

# Usuwanie elementów z kolejki
print(kolejka.pop(0))  # Usuwa i zwraca 1, Kolejka: [2, 3]
print(kolejka.pop(0))  # Usuwa i zwraca 2, Kolejka: [3]

# Sprawdzanie pustej kolejki
print(len(kolejka) == 0)  # False, Kolejka zawiera elementy
```


### **AD. 5. 6. Stos i kolejka za pomocą `deque`:**

Dzięki zastosowaniu **`deque`** z biblioteki `collections`, zarówno stos, jak i kolejka, oferują szybkie operacje dodawania i usuwania elementów, co czyni je bardziej wydajnymi niż używanie tradycyjnych list w Pythonie.

| **Cecha/Właściwość**          | **Stos (Stack)**                                                                                                        | **Kolejka (Queue)**                                                                                                          |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| **Definicja**                 | Stos działa na zasadzie **LIFO** (Last In, First Out) – ostatni element dodany jest pierwszym, który zostanie usunięty. | Kolejka działa na zasadzie **FIFO** (First In, First Out) – pierwszy element dodany jest pierwszym, który zostanie usunięty. |
| **Tworzenie**                 | Tworzony za pomocą `deque()`.                                                                                           | Tworzony za pomocą `deque()`.                                                                                                |
| **Dodawanie elementów**       | Dodawanie elementów za pomocą `append()`.                                                                               | Dodawanie elementów za pomocą `append()`.                                                                                    |
| **Usuwanie elementów**        | Usuwanie elementów za pomocą `pop()`.                                                                                   | Usuwanie elementów za pomocą `popleft()`.                                                                                    |
| **Sprawdzanie pustej struktury** | Sprawdzanie, czy stos jest pusty: `len(stos) == 0`.                                                                  | Sprawdzanie, czy kolejka jest pusta: `len(kolejka) == 0`.                                                                    |
| **Iteracja**                  | Można iterować po stosie, ale elementy są zwracane w odwrotnej kolejności.                                              | Można iterować po kolejce, aby uzyskać elementy w kolejności dodania.                                                        |
| **Zalety**                    | Szybki dostęp do ostatnio dodanego elementu.                                                                            | Szybki dostęp do pierwszego dodanego elementu.                                                                               |
| **Zastosowanie**              | Przechowywanie danych, które muszą być przetwarzane w odwrotnej kolejności (np. operacje nawiasowe, wycofywanie zmian). | Przechowywanie danych, które muszą być przetwarzane w kolejności ich dodania (np. w algorytmach BFS).                        |

#### 1. **Stos (*LIFO*) za pomocą `deque`:**
```python
from collections import deque

# Tworzenie stosu
stos = deque()

# Dodawanie elementów do stosu
stos.append(1)   # Stos: deque([1])
stos.append(2)   # Stos: deque([1, 2])
stos.append(3)   # Stos: deque([1, 2, 3])

# Usuwanie elementów ze stosu
print(stos.pop())  # Usuwa 3, Stos: deque([1, 2])
print(stos.pop())  # Usuwa 2, Stos: deque([1])

# Sprawdzanie pustego stosu
print(len(stos) == 0)  # False, Stos zawiera elementy
```

#### 2. **Kolejka (*FIFO*) za pomocą `deque`:**
```python
from collections import deque

# Tworzenie kolejki
kolejka = deque()

# Dodawanie elementów do kolejki
kolejka.append(1)   # Kolejka: deque([1])
kolejka.append(2)   # Kolejka: deque([1, 2])
kolejka.append(3)   # Kolejka: deque([1, 2, 3])

# Usuwanie elementów z kolejki
print(kolejka.popleft())  # Usuwa 1, Kolejka: deque([2, 3])
print(kolejka.popleft())  # Usuwa 2, Kolejka: deque([3])

# Sprawdzanie pustej kolejki
print(len(kolejka) == 0)  # False, Kolejka zawiera elementy
```

### **7. Drzewo (*tree*):**

| **Cecha/Właściwość** | **Opis**                                                                                                                                             | **Konstrukcja**           |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| **Definicja**        | Drzewo to struktura danych składająca się z węzłów, gdzie każdy węzeł ma jedno połączenie z rodzicem i może mieć zero lub więcej połączeń z dziećmi. | `root = Node(1)`          |
| **Węzeł**            | Węzeł to jednostka drzewa, zawierająca wartość i wskazania do swoich dzieci oraz (opcjonalnie) do rodzica.                                           | `class Node:`             |
| **Rodzic i dzieci**  | Każdy węzeł w drzewie ma rodzica (poza korzeniem) oraz może mieć wiele dzieci (w zależności od typu drzewa).                                         | `node.left = Node(2)`     |
| **Typy drzew**       | Wyróżniamy różne typy drzew, takie jak: drzewo binarne, drzewo binarne wyszukiwania, drzewo AVL, drzewo B.                                           | -                         |
| **Tworzenie**        | Drzewo tworzy się poprzez definicję klasy węzła, gdzie każdy węzeł ma wartość oraz wskaźniki na dzieci.                                              | `class Node:`             |
| **Dodawanie elementów** | Dodawanie dzieci do węzła może być realizowane przez przypisanie nowego węzła do listy dzieci.                                                    | `node.left = Node(2)`     |
| **Usuwanie elementów** | Usuwanie węzłów odbywa się poprzez usuwanie odniesień do danego węzła, co może prowadzić do usunięcia go z drzewa.                                 | `node.left = None`        |
| **Iteracja**         | Drzewa są zazwyczaj przetwarzane w sposób rekurencyjny lub za pomocą algorytmów przechodzenia drzewa, takich jak preorder, inorder, postorder.       | `def preorder(node): ...` |
| **Zastosowanie**     | Drzewa są wykorzystywane w strukturach takich jak drzewa decyzyjne, drzewa binarne, drzewa wyszukiwań, w bazach danych (np. B-drzewa), itp.          | -                         |
| **Zalety**           | Drzewa pozwalają na efektywne przechowywanie danych i przechodzenie po nich w sposób hierarchiczny, umożliwiając szybkie wyszukiwanie, dodawanie oraz usuwanie elementów.    | - |
| **Brak wbudowanego typu w Pythonie** | W Pythonie nie ma wbudowanego typu dla drzewa, ale można je łatwo zaimplementować za pomocą klas i struktur danych, takich jak listy, słowniki czy `deque`.  | - |

#### Przykład implementacji prostego drzewa binarnego w Pythonie:

```python
class Node:
    def __init__(self, value):
        self.value = value    # Wartość węzła
        self.left = None      # Lewy potomek
        self.right = None     # Prawy potomek

# Tworzenie węzłów
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Drzewo wygląda teraz tak:
#         1
#        / \
#       2   3
#      / \
#     4   5

# Przechodzenie drzewa w preorder (root, left, right)
def preorder(node):
    if node:
        print(node.value, end=" ")  # Odwiedzamy węzeł
        preorder(node.left)         # Przechodzimy do lewego poddrzewa
        preorder(node.right)        # Przechodzimy do prawego poddrzewa

# Wywołanie preorder dla korzenia
preorder(root)  # Wynik: 1 2 4 5 3
```
### **8. Plik (*file*):**

Plik w Pythonie jest strukturą umożliwiającą przechowywanie danych na dysku. Pliki mogą zawierać tekst, liczby lub inne dane i są wykorzystywane do odczytu i zapisu danych w aplikacjach. Python oferuje prostą obsługę plików, pozwalając na wykonywanie różnych operacji, takich jak otwieranie, czytanie, zapisywanie czy zamykanie pliku.

| **Cecha/Właściwość**           | **Opis**                                                                                          | **Konstrukcja**           |
|---------------------------------|--------------------------------------------------------------------------------------------------|---------------------------|
| **Definicja**                  | Plik to zbiór danych przechowywanych na dysku, który może zawierać tekst lub dane binarne. W Pythonie do obsługi plików używamy wbudowanych funkcji i metod. | `file = open('example.txt', 'r')`             |
| **Rodzaje plików**             | Pliki mogą być tekstowe (zawierające dane w formacie tekstowym) lub binarne (zawierające dane w postaci binarnej). | `file = open('image.png', 'rb')` |
| **Tryb otwierania pliku**      | Pliki można otwierać w różnych trybach: do odczytu (`'r'`), zapisu (`'w'`), dopisywania (`'a'`), w trybie binarnym (`'rb'`, `'wb'`). | `file = open('example.txt', 'w')`            |
| **Odczyt z pliku**             | Odczyt danych z pliku można przeprowadzić za pomocą metod takich jak `read()`, `readline()` lub `readlines()`. | `content = file.read()`                      |
| **Zapis do pliku**             | Zapis danych do pliku odbywa się za pomocą metody `write()` lub `writelines()`. | `file.write('Hello, World!')`                |
| **Zamykanie pliku**            | Po zakończeniu operacji na pliku należy go zamknąć za pomocą metody `close()`, aby uwolnić zasoby systemowe. | `file.close()`                               |
| **Zarządzanie plikami w kontekście** | Użycie konstrukcji `with` umożliwia automatyczne zamknięcie pliku po zakończeniu pracy. | `with open('example.txt', 'r') as file: ...`  |
| **Przykładowe operacje**       | 1. Odczyt całego pliku: `content = file.read()`<br> 2. Zapis do pliku: `file.write('text')`<br> 3. Dopisanie do pliku: `file.write('more text')` | - |

#### Przykład użycia pliku:
##### 1. **Otwieranie pliku pliku:**

```python
# Otwieranie pliku w trybie odczytu
with open('example.txt', 'r') as file:
    content = file.read()  # Odczyt zawartości pliku
    print(content)         # Wyświetlenie zawartości pliku

# Otwieranie pliku w trybie zapisu
with open('example.txt', 'w') as file:
    file.write('Hello, Python!')  # Zapis do pliku
```

##### 2. **Dodawanie do pliku (dopisywanie):**

```python
with open('example.txt', 'a') as file:
    file.write('\nAppended text!')  # Dopisanie do pliku
```

##### 3. **Odczyt linii z pliku:**

```python
with open('example.txt', 'r') as file:
    lines = file.readlines()  # Odczyt wszystkich linii w pliku
    for line in lines:
        print(line.strip())  # Wyświetlanie każdej linii
```