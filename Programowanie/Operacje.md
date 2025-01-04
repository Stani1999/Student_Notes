# 1. Operacje na typach złożonych 

## 1. **Wycinki (*slices*)** 
### Wycinki umożliwiają szybki i wygodny sposób pracy z sekwencjami (np. listami, stringami). Są przydatne do filtrowania, modyfikacji i odwracania danych.

```python
list = [1, 2, 3, 4, 5]

seq[start:end:step]
```

| **Funkcjonalność**         | **Składnia**            | **Opis**                                                             | **Przykład** | **Wynik**          |
|----------------------------|-------------------------|----------------------------------------------------------------------|--------------|--------------------|
| **Podstawowy wycinek**     | `seq[start:end]`        | Pobiera elementy od indeksu `start` (włącznie) do `end` (wyłącznie). | `lista[1:4]` | `[2, 3, 4]`        |
| **Domyślny początek**      | `seq[:end]`             | Pobiera elementy od początku sekwencji do indeksu `end` (wyłącznie). | `lista[:3]`  | `[1, 2, 3]`        |
| **Domyślny koniec**        | `seq[start:]`           | Pobiera elementy od indeksu `start` do końca sekwencji.              | `lista[2:]`  | `[3, 4, 5]`        |
| **Cała sekwencja**         | `seq[:]`                | Pobiera całą sekwencję (kopiuje ją).                                 | `lista[:]`   | `[1, 2, 3, 4, 5]`  |
| **Krok (co n-ty element)** | `seq[start:end:step]`   | Pobiera elementy od `start` do `end` z krokiem `step`.               | `lista[::2]` | `[1, 3, 5]`        |
| **Odwrócenie sekwencji**   | `seq[::-1]`             | Pobiera elementy w odwrotnej kolejności (od końca do początku).      | `lista[::-1]` | `[5, 4, 3, 2, 1]` |
| **Negatywne indeksy**      | `seq[-start:-end]`      | Używa ujemnych indeksów, które liczą od końca sekwencji.             | `lista[-3:-1]` | `[3, 4]`         |
| **Łączenie wycinków**   | `seq[:mid] + seq[mid:]` | Łączy dwa wycinki w jedną całość (podzielić i złączyć listę). | `lista[:2] + lista[2:]` | `[1, 2, 3, 4, 5]` |
| **Modyfikacja wycinków**   | `seq[start:end] = values` | Zamienia elementy w podanym zakresie na nowe wartości (dla list, które są mutowalne). | `lista[1:3] = [8, 9]` | `[1, 8, 9, 4, 5]` |

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

