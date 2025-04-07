## **Wykład III (06.03.2025)**  

### **III 1. Stałe**  

| **Element**      | **C** | **C++**              | **Różnice i uwagi**                                                                     |
|------------------|-------|----------------------|-----------------------------------------------------------------------------------------|
| **`const`**      | ✅   | ✅ | W C++ ma szersze zastosowanie (np. w klasach). W C ograniczone głównie do zmiennych globalnych/lokalnych. |
| **`constexpr`**  | ❌   | ✅ (od C++11)        | C nie ma odpowiednika – stałe kompilacyjne definiuje się przez `#define` lub `enum`.    |
| **`#define`**    | ✅   | ✅ (ale niezalecane) | W C++ lepiej używać `constexpr` zamiast makr (bez sprawdzania typów).                   |

---

#### **Kluczowe różnice:**  
1. **`const` w C vs. C++**:  
   - **W C**:  
     - Zmienna `const` jest tylko **read-only**, ale nie zawsze jest stałą kompilacyjną (np. nie można jej użyć do rozmiaru tablicy).  
     ```c
     const int size = 10;  
     int array[size]; // Błąd w C (chyba że kompilator wspiera VLA)!  
     ```  
   - **W C++**:  
     - `const` dla typów prostych (np. `int`) jest stałą kompilacyjną, jeśli inicjalizowana jest literałem.  
     ```cpp
     const int size = 10;  
     int array[size]; // OK w C++!  
     ```  

2. **Brak `constexpr` w C**:  
   - W C stałe kompilacyjne definiuje się przez:  
     - `#define` (makra bez typu):  
       ```c
       #define SIZE 10  
       int array[SIZE];  
       ```  
     - `enum` (dla wartości całkowitych):  
       ```c
       enum { SIZE = 10 };  
       int array[SIZE];  
       ```  

3. **Zalecenia dla C++**:  
   - Zawsze preferuj `constexpr` zamiast `#define` (lepsza kontrola typów i zakresu).  
   - Używaj `const` dla zmiennych, które nie muszą być stałymi kompilacyjnymi.  

---

### **III 3. Alokacja pamięci w C i C++ - porównanie**

#### **1. Alokacja statyczna**
| **Opis**                                  | **Przykład**    | **Zalety/Wady**                                                   |
|-------------------------------------------|-----------------|-------------------------------------------------------------------|
| Rozmiar musi być znany podczas kompilacji | `int arr[100];` | ✅ Szybkie, brak narzutu<br>❌ Stały rozmiar, marnowanie pamięci |

#### **2. Alokacja dynamiczna w C**
| **Funkcja** | **Opis**                         | **Przykład**                                 | **Uwagi**                                          |
|-------------|----------------------------------|----------------------------------------------|----------------------------------------------------|
| `malloc`    | Alokuje pamięć bez inicjalizacji | `int* ptr = (int*)malloc(10 * sizeof(int));` | Wymaga rzutowania, sprawdzania NULL                |
| `calloc`    | Alokuje i zeruje pamięć          | `int* ptr = (int*)calloc(10, sizeof(int));`  | Wolniejszy niż malloc                              |
| `free`      | Zwalnia pamięć                   | `free(ptr); ptr = NULL;`                     | Zapobiega dangling pointer                         |
| `realloc` | Zmiana rozmiaru | `ptr = realloc(ptr, 20*sizeof(int));` | Przenoszenie danych do nowo zaalokowaniej pamięci (malloc -> memcpy -> free) |

**Dangling pointer** to wskaźnik wskazujący na zwolniony lub nieistniejący obszar pamięci, co może prowadzić do błędów wykonania programu.  
*"Prościej: Wskaźnik, który "wisi w powietrzu", bo pamięć, na którą pokazywał, już nie istnieje."*


#### **3. Alokacja dynamiczna w C++**
| **Operator** | **Opis**        | **Przykład**                   | **Uwagi**                          |
|--------------|-----------------|--------------------------------|------------------------------------|
| `new`        | Alokuje pamięć  | `int* ptr = new int;`          | Automatycznie wywołuje konstruktor |
| `new[]`      | Alokuje tablicę | `int* arr = new int[10];`      |                                    |
| `delete`     | Zwalnia pamięć  | `delete ptr; ptr = nullptr;`   |                                    |
| `delete[]`   | Zwalnia tablicę | `delete[] arr; arr = nullptr;` |                                    |

#### **Kluczowe różnice w alokacji pamięci: C vs C++**  

| **Cecha**                | **C**                                         | **C++**                                     |
|--------------------------|-----------------------------------------------|---------------------------------------------|
| **Podstawowe operatory** | `malloc`, `calloc`, `free`                    | `new`, `new[]`, `delete`, `delete[]`        |
| **Typowanie**            | Wymaga rzutowania (`(int*)`)                  | Nie wymaga rzutowania                       |
| **Inicjalizacja**        | Tylko alokacja (brak inicjalizacji domyślnej) | Automatycznie wywołuje konstruktory         |
| **Zwalnianie pamięci**   | `free` (nie wywołuje destruktorów)            | `delete` (wywołuje destruktory)             |
| **Obsługa błędów**       | Zwraca `NULL`                                 | Rzuca wyjątek `std::bad_alloc`              |
| **Zalecane użycie**      | Tylko w C                                     | Preferowane w C++ (lepsza integracja z OOP) |  

#### **Zalecenia**
- W C++ zawsze używaj `new/delete` zamiast `malloc/free`
- Po zwolnieniu pamięci ustawiaj wskaźniki na `nullptr`
- Dla tablic używaj odpowiednich operatorów (`new[]/delete[]`)

---

### **III 4. Tablice wielowymiarowe - alokacja i zwalnianie**

#### **1. Alokacja statyczna (C i C++)**
```c
// Tablica 3x4 (12 elementów)
int arr[3][4]; 
```
- **Plusy**: Prosta składnia, automatyczne zarządzanie pamięcią  
- **Minusy**: Stały rozmiar, marnowanie pamięci  

#### **2. Alokacja dynamiczna w C**  
*(metoda "spłaszczona" - jedna alokacja)*  
```c
int rows = 3, cols = 4;
int *matrix = (int*)malloc(rows * cols * sizeof(int));

// Dostęp: matrix[row * cols + col] = wartość;
free(matrix);
```
**Uwaga**: Brak naturalnej składni `[i][j]`.

*(metoda "wskaźnikowa" - wielokrotne alokacje)*  
```c
int **matrix = (int**)malloc(rows * sizeof(int*));
for (int i = 0; i < rows; i++) {
    matrix[i] = (int*)malloc(cols * sizeof(int));
}

// Dostęp: matrix[row][col] = wartość;

// Zwalnianie:
for (int i = 0; i < rows; i++) free(matrix[i]);
free(matrix);
```
**Uwaga**: Złożoność alokacji, ale naturalny dostęp.

#### **3. Alokacja dynamiczna w C++**  
*(metoda "spłaszczona")*  
```cpp
int rows = 3, cols = 4;
int *matrix = new int[rows * cols];

// Dostęp: matrix[row * cols + col] = wartość;
delete[] matrix;
```

*(metoda "wskaźnikowa")*  
```cpp
int **matrix = new int*[rows];
for (int i = 0; i < rows; i++) {
    matrix[i] = new int[cols];
}

// Dostęp: matrix[row][col] = wartość;

// Zwalnianie:
for (int i = 0; i < rows; i++) delete[] matrix[i];
delete[] matrix;
```

*(metoda "nowoczesna" - std::vector)*  
```cpp
#include <vector>
std::vector<std::vector<int>> matrix(rows, std::vector<int>(cols));

// Dostęp: matrix[row][col] = wartość;
// Automatyczne zwalnianie!
```

#### **Podsumowanie różnic**  
| Cecha              | C                                | C++                                         |
|--------------------|----------------------------------|---------------------------------------------|
| **Składnia**       | `malloc`/`free`, wymaga rzutowań | `new`/`delete`, czystsza składnia           |
| **Bezpieczeństwo** | Brak ochrony przed wyciekami     | Możliwość użycia RAII (np. `vector`)        |
| **Wydajność**      | Spłaszczona: lepsza              | Spłaszczona: lepsza, ale `vector` ma narzut |

**Zalecenie w C++**: Używaj `std::vector` zamiast surowych wskaźników dla prostoty i bezpieczeństwa!

**Źródło:** Wykład 3 - Programowanie w C++, Konrad Kosmatka

---