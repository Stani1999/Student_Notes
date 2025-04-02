## Notatka z Wykładów Programowania w C++  

### **Wykład I (20.02.2024)**  

#### **Cechy języka C++**  

| **Cecha**      | **Opis**                                           |
|----------------|----------------------------------------------------|
| Twórca         | Bjarne Stroustrup (lata 80. XX wieku)              |
| Typowanie      | Statyczne (typ zmiennej jest stały)                |
| Wykorzystanie  | Systemy embedded, mikroprocesory, wysoka wydajność |
| Blisko sprzętu | Optymalizacja pod kątem architektury komputera     |

#### **Typy danych w C++**  

| **Typ**            | **Przykłady**                          |
|--------------------|----------------------------------------|
| Całkowite          | `int`, `long`, `short`, `unsigned int` |
| Zmiennoprzecinkowe | `float`, `double`                      |
| Znakowe            | `char`                                 |
| Logiczne           | `bool` (`true`/`false`)                |
| Złożone            | `std::string`                          |

#### **Instrukcje warunkowe**  

| **Instrukcja**  | **Opis**                                           |
|-----------------|----------------------------------------------------|
| `if`            | Warunek podstawowy                                 |
| `else if`       | Dodatkowe warunki                                  |
| `else`          | Wykonuje się, gdy żaden warunek nie jest spełniony |
| Skrócona wersja | `(warunek ? wartość1 : wartość2)`                  |

### **Pętle w C++**  

| **Pętla**    | **Opis**                                              | **Zastosowanie**                                                                |  
|--------------|-------------------------------------------------------|---------------------------------------------------------------------------------|  
| `for`        | Wykonuje się określoną liczbę razy                    | `for (int i = 0; i < N; i++)` – iteruje od `0` do `N-1`                         |  
| `while`      | Wykonuje się, dopóki warunek jest spełniony           | `while (warunek)` – sprawdza warunek przed wykonaniem                           |  
| `do...while` | Wykonuje się przynajmniej raz, potem sprawdza warunek | `do { ... } while (warunek);` – zawsze wykonuje blok przed sprawdzeniem warunku |  
| `break`      | Przerywa pętlę                                        | Przerywa najbliższą otaczającą pętlę                                            |  
| `continue`   | Pomija aktualną iterację                              | Przechodzi do następnej iteracji w najbliższej pętli                            |  

#### **Dodatkowe uwagi:**  
- **`for`** – domyślnie używa inkrementacji (`i++`), ale można zmienić na np. `i += 2`.  
- **`while`** – jeśli warunek początkowo jest fałszywy, pętla nie wykona się ani raz.  
- **`do...while`** – zawsze wykona się co najmniej raz, nawet jeśli warunek jest fałszywy.  

#### **Funkcje**  

| **Element** | **Opis**                                                                    |
|-------------|-----------------------------------------------------------------------------|
| Deklaracja  | Informuje kompilator o nazwie, typie zwracanym i parametrach (pliki `.hpp`) |
| Definicja   | Implementacja funkcji (pliki `.cpp`)                                        |
| `void`      | Funkcja nie zwraca wartości                                                 |

#### **Dyrektywy preprocesora**  

| **Dyrektywa**       | **Opis**                 |
|---------------------|--------------------------|
| `#include`          | Dołącza pliki nagłówkowe |
| `#define`           | Definiuje stałe          |
| `#ifdef`, `#ifndef` | Warunkowa kompilacja     |

#### **Namespaces**  

| **Element**            | **Opis** |
|------------------------|-------------------------------------|
| Przestrzeń nazw        | Zapobiega kolizjom nazw             |
| Odwołanie              | `nazwa_przestrzeni::funkcja()`      |
| `using namespace std;` | Pozwala pominąć przedrostek `std::` |

---

### **Wykład II (27.02.2025)**  

#### **Podział na pliki**  

| **Element**   | **Opis**                                          |
|---------------|---------------------------------------------------|
| Pliki `.hpp`  | Deklaracje funkcji                                |
| Pliki `.cpp`  | Definicje funkcji                                 |
| Include guard | Zabezpiecza przed wielokrotnym dołączaniem plików |

#### **Operatory**  

| **Typ operatora**           | **Przykłady**                         |
|-----------------------------|---------------------------------------|
| Arytmetyczne                | `+`, `-`, `*`, `/`, `%`               |
| Porównania                  | `==`, `!=`, `<`, `>`, `<=`, `>=`      |
| Logiczne                    | `&&` (AND), `\|\|` (OR), `!` (NOT)    |
| Inkrementacji/dekrementacji | `++`, `--` ([++/--]pre i post[++/--]) |

#### **Wskaźniki i referencje**  

| **Element**           | **Opis**                                   |
|-----------------------|--------------------------------------------|
| Wskaźnik (`*`)        | Przechowuje adres zmiennej                 |
| Referencja (`&`)      | Bezpieczniejsza alternatywa dla wskaźników |
| Operator adresu (`&`) | Zwraca adres zmiennej                      |
| Dereferencja (`*`)    | Pobiera wartość spod adresu                |

#### **Tablice**  

| **Typ tablicy** | **Opis**                 |
|-----------------|--------------------------|
| Statyczna       | `int tab[5];`            |
| Dynamiczna      | `int *tab = new int[5];` |
| Wielowymiarowa  | `int matrix[10][10];`    |

---

### **Wykład III (06.03.2025)**  

#### **Stałe**  

| **Element** | **Opis**                          |
|-------------|-----------------------------------|
| `const`     | Zmienna nie może być modyfikowana |
| `constexpr` | Wartość znana podczas kompilacji  |

#### **Alokacja pamięci**  

| **Typ alokacji** | **Opis**                         |
|------------------|----------------------------------|
| Statyczna        | Rozmiar znany podczas kompilacji |
| Dynamiczna (C)   | `malloc`, `calloc`, `free`       |
| Dynamiczna (C++) | `new`, `delete`                  |

#### **Tablice wielowymiarowe**  

| **Element**         | **Opis**                         |
|---------------------|----------------------------------|
| Alokacja dynamiczna | Wymaga wskaźników do wskaźników  |
| Przykład            | `int **matrix = new int*[rows];` |

---

### **Wykład IV (13.03.2025)**  

#### **Stringi**  

| **Element** | **Opis**                                                |
|-------------|---------------------------------------------------------|
| W C         | Tablice `char` zakończone `\0`                          |
| W C++       | Klasa `std::string` (automatyczne zarządzanie pamięcią) |

#### **Struktury i klasy**  

| **Element**          | **Opis**                                 |
|----------------------|------------------------------------------|
| Struktura (`struct`) | Grupowanie danych                        |
| Klasa (`class`)      | Dane + metody, konstruktory, destruktory |
| RAII                 | Zasoby zwalniane przez destruktor        |

---

### **Wykład V (20.03.2025)**  

#### **STL (Standard Template Library)**  

| **Kontener**        | **Opis**                   |
|---------------------|----------------------------|
| `std::array`        | Tablica o stałym rozmiarze |
| `std::vector`       | Tablica dynamiczna         |
| `std::list`         | Lista dwukierunkowa        |
| `std::forward_list` | Lista jednokierunkowa      |

#### **Metody STL**  

| **Metoda**  | **Opis**                            |
|-------------|-------------------------------------|
| `push_back` | Dodaje element na koniec            |
| `pop_back`  | Usuwa ostatni element               |
| `size`      | Zwraca rozmiar kontenera            |
| `at()`      | Bezpieczny dostęp (sprawdza zakres) |

---

### **Wykład VI (27.03.2025)**  

#### **Typy wyliczeniowe**  

| **Element**  | **Opis**                                          |
|--------------|---------------------------------------------------|
| `enum`       | Zestaw stałych liczbowych                         |
| `enum class` | Bezpieczniejsza wersja (ogranicza zakres stałych) |

#### **Kontenery STL**  

| **Kontener**         | **Opis**                                    |
|----------------------|---------------------------------------------|
| `std::queue`         | FIFO (First In, First Out)                  |
| `std::stack`         | LIFO (Last In, First Out)                   |
| `std::set`           | Zbiór unikalnych elementów (posortowany)    |
| `std::unordered_set` | Zbiór unikalnych elementów (nieposortowany) |
| `std::map`           | Mapa (klucz-wartość, posortowana)           |
| `std::unordered_map` | Mapa (klucz-wartość, nieposortowana)        |

#### **Pary i krotki**  

| **Element**  | **Opis**              |
|--------------|-----------------------|
| `std::pair`  | Para dwóch wartości   |
| `std::tuple` | Krotka wielu wartości |

---

**Strona prowadzącego**: [kosmatka.pl/pw/](http://kosmatka.pl/pw/)