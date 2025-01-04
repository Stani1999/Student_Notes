# Dokumentacja do programu 24-11-12-Rezerwacje.py w Python.
## Wprowadzenie 
Program służy do zarządzania rezerwacjami miejsc w kinie. Obsługuje takie funkcje jak :
 - dodawanie, 
 - usuwanie,
 - modyfikowanie rezerwacji, 
 - zapis i odczyt danych z pliku CSV.

 Użyanie globalnych zmiennych, takich jak `n` i `filename`, łatwo można dostosować liczbę miejsc oraz lokalizację pliku z danymi.
 
 - Uwaga zmiejszenie wartości zmiennej `n` może skrućić listę o rezerwacje o wyższych niż ona indeksach.


## Instalacja Python
Aby uruchomić poniższy kod python musisz najpierw zainstalować python.
Możesz to zrobić w następujący sposób:

# Windows 
|1. Pobierz instalator z linku klikając jego ikone poniżej.|
|---|
| [![Python](image-1.png)](https://www.python.org/downloads/)|
2. Uruchom instalator i upewnij się, że zaznaczyłeś opcję "Add Python to PATH"
3. Kliknij "Install Now"

### Linux (Debian/Bash)
|Wykkonaj poniższe instrukcje w terminalu:|
|---|

```bash
sudo apt update
sudo apt install python3
```

# Tworzenie środowiska wirtualnego
Zaleca się korzystanie ze środowisk wirtualnych, aby odizolować zależności projektu od globalnych pakietów Pythona.

## Tworzenie i aktywowanie środowiska wirtualnego

- **Windows**
    1. Utwórz środowisko wirtualne:
        ```bash
        python -m venv <nazwa_katalogu>
        ```
    2. Aktywuj środowisko:
        ```bash
        <nazwa_katalogu>\Scripts\activate
        ```

- **Linux/macOS**
    1. Utwórz środowisko wirtualne:
        ```bash
        python3 -m venv <nazwa_katalogu>
        ```
    2. Aktywuj środowisko:
        ```bash
        source <nazwa_katalogu>/bin/activate
        ```

Po aktywacji środowiska wirtualnego możesz instalować zależności, np. za pomocą `pip`, które będą izolowane w obrębie tego środowiska.


## Wymagania

- Python 3.12 lub nowszy (dotyczy wersji 3.x.x)


## Struktura programu

## 1. Biblioteka CSV

```python
import csv
```
Biblioteka csv jest używana do operowania na plikach (zapisu i odczytu danych) w formacie CSV.

## 2. Globalne zmienne

```python
n = 10
filename = "kino.csv"
```
## 3. Funkcje.

### 1. Funkcje pobierające numery miejsc : `value_check` oraz `which_seat`.
#### Walidują numery i sprawdzają czy są one poprawne, dane wprowadza użytkownik.
---
Funkcja `value_check` 

* Przetważany jest pojedynczy numer miejsca

```python
def value_check(action, n): 
    ...
```
Funkcja `which_seat`

* Przetwarzana jest lista miejsc (np. "1,2,3").
```python
def which_seat(action):
    ...
```

* Parametry:  
    * `action`: 
        * Umożliwia stosowanie wyżej wymienionych funkcji wewnątrz innych, które działają na ich wynikach, do różnych potrzeb.
        * Przykład zawartości "usunąć", "zmodyfikować"
    * `n`: Liczba miejsc w kinie (dotyczy jedynie `value_check`)
* `value_check` Zwraca: Indeks miejsca (liczba całkowita) lub 'None', jeśli dane wejściowe są niepoprawne.

### 2. Funkcje działające z listą
#### Wykonują operacje modyfikujące zawartość listy w czasie trwania programu.
---
Funkcja: `print_seats` 

* Wyświetla aktualny stan rezerwacji.

```python
def print_seats(seats):
    ...
```
---
Funkcja: `add_reservation`

* Dodaje rezerwację na wybrane miejsce
```python
def add_reservation(seats):
    ...
```
---
Funkcja: `remove_reservation`

* Usuwa rezerwację na wybrane miejsce.
```python
def remove_reservation(seats):
    ...
```
---
Funkcja: `mod_reservation`

* Modyfikuje istniejącą rezerwację
```python
def mod_reservation(seats):
    ...
```
---
Funkcja: `check_availability`

* Sprawdza dostępność miejsc.
```python
def check_availability(seats):
    ...
```
---
Funkcja: `add_multiple_reservations`

* Dodaje rezerwacje na kilka miejsc jednocześnie.
```python
def add_multiple_reservations(seats):
    ...
```
---
Funkcja: `cancel_all_reservations`

* Usuwa wszystkie rezerwacje dla podanej osoby.
```python
def cancel_all_reservations(seats):
    ...
```

* Parametr 
    * `seats` : Lista miejsc.

### 3. Funkcje odczytu i zapisu listy w pliku 
---
#### Dodane po to aby zachować listę po zamknięciu i ponownnym otwarciu programu
Funkcja: `load_seats_from_file`

* Ładuje rezerwacje z pliku CSV.

```python
def load_seats_from_file():
    ...
```

* Zwraca: Lista miejsc.
---
Funkcja: `save_seats_to_file`

* Zapisuje rezerwacje do pliku CSV.

```python
def save_seats_to_file(seats):
    ...
```

* Parametr:
    * `seats`: Lista miejsc.

### 4. Funkcja gółwna programu
#### Umożliwia operacje na funkcjach wbudowanych w progra.
----
Funkcja: `main`
* Główna pętla programu obsługująca menu użytkownika.

```python
def main():
    ...
```

## Plik cvs
* Nagłówki: Miejsce, Rezerwacja
* Struktura danych:

```cvs
Miejsce,Rezerwacja
1,Jakub
2,Anna
3,None
...
```

# Obsługa Programu
## Uruchomienie:
Program rozpoczyna działanie od załadowania danych z pliku CSV lub stworzenia pustej listy miejsc.
## Menu:
    Dostępne opcje:
    1. Wyświetl rezerwacje
    2. Dodaj rezerwację
    3. Usuń rezerwację
    4. Modyfikuj rezerwację
    5. Zapisz i wyjdź
    6. Wyświetl dostępność miejsc
    7. Dodaj rezerwacje na kilka miejsc
    8. Usuń wszystkie rezerwacje dla...

## Best Practice

1. Stosowanie środowisk wirtualnych
2. Aby uniknąć skrócenia listy nie zmniejszaj wartości zmiennej `n` poniżej liczby uzupełnionych mniejsc, lub twórz nową listę (podając inny plik do zmiennej `filename`)
3. Staraj się nie wprowadzać znaków innych niż liczby kiedy program prosi o wybór opcji czy miejsca.
4. Gdy w opcji 7. używaj znaku "," zamiast ".".

## Podsumowanie

## Linki

## Autorzy
 - [Stani1999](https://github.com/Stani1999)