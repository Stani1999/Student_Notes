## **Wykład V (20.03.2025)**  

### **V. 1. Wprowadzenie do STL**
Standard Template Library (STL) to zestaw gotowych szablonów klas i funkcji w C++ do pracy ze strukturami danych.

- **STL** w C++ zapewnia gotowe, bezpieczne rozwiązania

**Przykład w C (brak STL):**
```c
// Ręczna implementacja listy
typedef struct Node {
    int data;
    struct Node* next;
} Node;

Node* create_node(int value) {
    Node* new_node = (Node*)malloc(sizeof(Node));
    new_node->data = value;
    new_node->next = NULL;
    return new_node;
}
```

**Przykład w C++ (z STL):**
```cpp
#include <list>
std::list<int> ready_list; // Gotowa lista z STL
ready_list.push_back(10); // Automatyczne zarządzanie pamięcią
```

---

### **V. 2. Array vs Vector - porównanie**

| **Cecha**               | **std::array**                 | **std::vector**                 |
|-------------------------|--------------------------------|---------------------------------|
| **Rozmiar**             | Stały (określony w kompilacji) | Dynamiczny (może rosnąć)        |
| **Miejsce w pamięci**   | Stos                           | Sterta                          |
| **Dostęp**              | `arr[0]` lub `arr.at(0)`       | `vec[0]` lub `vec.at(0)`        |
| **Dodawanie elementów** | Nie możliwe                    | `push_back()`, `emplace_back()` |
| **Wydajność**           | Szybszy dostęp                 | Wolniejsze realokacje           |

---

### **V. 3. std::array - tablica statyczna**

- **std::array** to lepsza wersja tablic C-style

**W C:**
```c
int arr[5] = {1, 2, 3, 4, 5};
printf("Rozmiar: %zu\n", sizeof(arr)/sizeof(arr[0])); // Obliczanie rozmiaru
```

**W C++:**
```cpp
#include <array>
std::array<int, 5> arr = {1, 2, 3, 4, 5};
std::cout << "Rozmiar: " << arr.size(); // Wbudowana metoda size()
```

---

### **V. 4. std::vector - tablica dynamiczna**

- **std::vector** to uniwersalny kontener dynamiczny

**W C:**
```c
int* vec = (int*)malloc(5 * sizeof(int));
vec[0] = 10;
free(vec); // Wymagane ręczne zwolnienie
```

**W C++:**
```cpp
#include <vector>
std::vector<int> vec;
vec.push_back(10); // Automatyczne zarządzanie pamięcią
vec.reserve(100);  // Rezerwacja pamięci
```

---

### **V. 5. Metody na tablicach - porównanie**

| **Operacja**   | **C (tablica)**                          | **C++ (std::array)**                | **C++ (std::vector)**               |
|----------------|------------------------------------------|-------------------------------------|-------------------------------------|
| **Dostęp**     | `arr[i]`                                 | `arr[i]` lub `arr.at(i)`            | `vec[i]` lub `vec.at(i)`            |
| **Rozmiar**    | `sizeof(arr)/sizeof(arr[0])`             | `arr.size()`                        | `vec.size()`                        |
| **Kopiowanie** | `memcpy(dest, src, size)`                | `arr2 = arr1`                       | `vec2 = vec1`                       |
| **Sortowanie** | `qsort(arr, size, sizeof(int), compare)` | `std::sort(arr.begin(), arr.end())` | `std::sort(vec.begin(), vec.end())` |

**Zalecenie:** W nowoczesnym C++ preferuj rozwiązania STL zamiast ręcznych implementacji znanych z C.

---

### **V. 6. Iteratory**

**W C (wskaźniki):**
```c
int arr[] = {1, 2, 3};
for(int* ptr = arr; ptr < arr + 3; ptr++) {
    printf("%d ", *ptr);
}
```

**W C++:**
```cpp
std::vector<int> vec = {1, 2, 3};
for(auto it = vec.begin(); it != vec.end(); ++it) {
    std::cout << *it << " ";
}

// Range-based for loop (C++11)
for(const auto& element : vec) {
    std::cout << element << " ";
}
```

#### **Operatory iteratorów - porównanie C i C++**

| **Operacja**               | **Przykład w C (wskaźniki)**      | **Przykład w C++ (iteratory STL)**       | **Wyjaśnienie**                                                                 |
|----------------------------|-----------------------------------|------------------------------------------|---------------------------------------------------------------------------------|
| **Wyłuskanie**             | `int value = *(ptr + i);`         | `int value = *it;`                       | Pobranie wartości spod iteratora/wskaźnika                                      |
| **Pre-inkrementacja**      | `for(; ptr < end; ++ptr)`         | `for(; it != end; ++it)`                 | Przejście do następnego elementu (bez tworzenia kopii)                          |
| **Pre-dekrementacja**      | `for(; ptr > start; --ptr)`       | `for(; it != begin; --it)`               | Przejście do poprzedniego elementu (bez tworzenia kopii)                        |
| **Przesunięcie o n**       | `ptr += 3;`                       | `it += 3;`                               | Przeskoczenie o 3 elementy do przodu                                            |
| **Dostęp indeksowany**     | `int val = ptr[2];`               | `int val = *(it + 2);`                   | Dostęp do elementu z przesunięciem (tylko iteratory dostępu swobodnego)         |
| **Post-inkrementacja**     | `int val = *ptr++;`               | `int val = *it++;`                       | Pobranie wartości, potem inkrementacja (tworzy kopię iteratora)                 |
| **Porównanie**             | `if(ptr1 == ptr2)`                | `if(it1 == it2)`                         | Sprawdzenie czy wskazują na ten sam element                                     |

#### **Przykłady praktyczne**

#### **W C (wskaźniki):**
```c
int arr[] = {10, 20, 30, 40, 50};
int *ptr = arr;

// Pre-inkrementacja
while(ptr < arr + 5) {
    printf("%d ", *ptr);
    ++ptr;  // Bez kopii
}

// Przesunięcie
ptr = arr;
printf("\nElement 3: %d", *(ptr + 2));  // Równoważne ptr[2]
```

#### **W C++ (iteratory STL):**
```cpp
#include <vector>
#include <iostream>

int main() {
    std::vector<int> vec = {10, 20, 30, 40, 50};
    auto it = vec.begin();

    // Pre-dekrementacja
    auto end = vec.end();
    while(it != end) {
        std::cout << *it << " ";
        ++it;  // Bez kopii
    }

    // Przesunięcie
    it = vec.begin();
    std::cout << "\nElement 3: " << *(it + 2);  // Równoważne vec[2]

    return 0;
}
```

#### **Porównanie wskaźników w C i iteratorów STL w C++**

| **Kryterium**      | **Wskaźniki (C)**                          | **Iteratory STL (C++)**                        |
|--------------------|--------------------------------------------|------------------------------------------------|
| **Bezpieczeństwo** | Wymagana ręczna kontrola zakresów          | Sprawdzanie zakresów w wersjach debug          |
| **Uniwersalność**  | Specyficzne dla tablic                     | Działają tak samo dla różnych kontenerów       |
| **Wydajność**      | W optymalizacji podobny kod maszynowy      | W optymalizacji podobny kod maszynowy          |
| **Zalecenia**      | Pre-inkrementacja zalecana (`++ptr`)       | Pre-inkrementacja zalecana (`++it`)            |

- **Iteratory** zapewniają jednolity interfejs dostępu

---

### **V. 7. std::pair**

- **std::pair** ułatwiaja pracę z parą wartości

**W C (struktura):**
```c
typedef struct {
    int first;
    char second[20];
} Pair;

Pair p = {1, "test"};
printf("%d %s", p.first, p.second);
```

**W C++:**
```cpp
#include <utility>
auto p = std::make_pair(1, "test");
std::cout << p.first << " " << p.second;

// Structured binding (C++17)
auto [first, second] = p;
```

---

### **V. 8. std::tuple**

- **std::tuple** ułatwiaja pracę z wieloma wartościami

**W C (struktura):**
```c
typedef struct {
    int id;
    char name[50];
    float salary;
} Tuple;

Tuple t = {1, "Stani", 6900.50f};
printf("%d %s %.2f", t.id, t.name, t.salary);
```

**W C++:**
```cpp
#include <tuple>
auto t = std::make_tuple(1, "Stani", 6900.50);
std::cout << std::get<0>(t) << " " << std::get<1>(t);

// Structured binding (C++17)
auto [id, name, salary] = t;
```

**Źródło:** Wykład 5 - Programowanie w C++, Konrad Kosmatka

---