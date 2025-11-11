## **Wykład VI (27.03.2025)**  

### **VI. 1. Typy Wyliczeniowe (enum)**

- **enum/class enum**: Lepsza organizacja kodu, szczególnie w C++  

#### **Podstawowa składnia**

#### **W C:**
```c
#include <stdio.h>

// Klasyczny enum (globalna przestrzeń nazw)
enum Kolor {
    CZERWONY,    // 0
    ZIELONY,     // 1
    NIEBIESKI    // 2
};

int main() {
    enum Kolor k = ZIELONY;
    printf("Kolor: %d\n", k); // Wypisze: 1
    
    // Niejawna konwersja na int
    int i = CZERWONY; // i = 0
    return 0;
}
```

#### **W C++ (enum class):**
```cpp
#include <iostream>

// Enum class (lepsza hermetyzacja)
enum class Kolor {
    Czerwony,   // 0
    Zielony,    // 1
    Niebieski   // 2
};

int main() {
    Kolor k = Kolor::Zielony;
    
    // Konwersja wymaga static_cast
    std::cout << "Kolor: " << static_cast<int>(k) << std::endl; // Wypisze: 1
    
    // int i = Kolor::Czerwony; // Błąd kompilacji!
    return 0;
}
```

---

#### **Ręczne przypisywanie wartości**

#### **W C:**
```c
enum Status {
    SUCCESS = 0,
    FILE_NOT_FOUND = -1,
    PERMISSION_DENIED = -2
};

void check_status(enum Status s) {
    if (s == FILE_NOT_FOUND) {
        printf("Plik nie istnieje!\n");
    }
}
```

#### **W C++:**
```cpp
enum class Status {
    Success = 0,
    FileNotFound = -1,
    PermissionDenied = -2
};

void check_status(Status s) {
    if (s == Status::FileNotFound) {
        std::cout << "Plik nie istnieje!" << std::endl;
    }
}
```

---

#### **Porównanie C vs C++**

| **Cecha**               | **C (enum)**                            | **C++ (enum class)**                        |
|-------------------------|-----------------------------------------|---------------------------------------------|
| **Przestrzeń nazw**     | Wszystkie enums w globalnej przestrzeni | Każdy enum class ma własną przestrzeń       |
| **Konwersja na int**    | Automatyczna                            | Wymaga `static_cast`                        |
| **Bezpieczeństwo**      | Niskie (możliwość porównań między różnymi enum) | Wysokie (brak niejawnych konwersji) |
| **Rozmiar w pamięci**   | Zazwyczaj `int`                         | Możliwość określenia (`: short` itp.)       |

---

#### **Zaawansowane użycie w C++**

#### **Określanie typu bazowego:**
```cpp
enum class Status : short {
    Ok = 200,
    NotFound = 404,
    Error = 500
}; // Zajmuje tylko 2 bajty (short)
```

#### **Iteracja po wartościach (C++17):**
```cpp
enum class Dzien : int {
    Poniedzialek = 1,
    Wtorek,
    Sroda,
    // ...
    Niedziela = 7
};

// Konwersja na string
const char* to_string(Dzien d) {
    switch(d) {
        case Dzien::Poniedzialek: return "Poniedziałek";
        // ...
    }
}
```

---

#### **Kiedy używać enum w C vs enum class w C++**  

| **C-style enum**                           | **enum class (C++)**               |
|--------------------------------------------|------------------------------------|
| Pracujesz z kodem C                        | Piszesz nowy kod w C++             |
| Potrzebujesz prostych stałych numerycznych | Zależy Ci na bezpieczeństwie typów |
| Chcesz automatycznej konwersji na int      | Chcesz uniknąć kolizji nazw        |
|                                            | Potrzebujesz określić typ bazowy   |  

---

#### **Przykład użycia enum/class enum dla błędów datasetu**

#### **1. Wersja C (standard enum)**
```c
#include <stdio.h>

enum DatasetError {
    DATASET_ERROR_NONE = 1,
    DATASET_ERROR_MISSING = -1,
    DATASET_ERROR_OPEN = -2,
    DATASET_ERROR_READ = -3,
    DATASET_ERROR_FORMAT = -4
};

const char* dataset_error_message(enum DatasetError error) {
    switch (error) {
        case DATASET_ERROR_NONE:    return "No error";
        case DATASET_ERROR_MISSING: return "File does not exist";
        case DATASET_ERROR_OPEN:   return "Unable to open the file";
        case DATASET_ERROR_READ:   return "Failed to read the file";
        case DATASET_ERROR_FORMAT: return "Invalid file format";
        default:                   return "Unknown error";
    }
}

DatasetError load_dataset(const char *filename) {
    if (!file_exists(filename))
        return DATASET_ERROR_MISSING;
    
    if (!dataset_open(filename))
        return DATASET_ERROR_OPEN;
        
    return DATASET_ERROR_NONE;
}
```

#### **2. Wersja C++ (enum class)**
```cpp
#include <iostream>
#include <string>

enum class DatasetError {
    None = 1,
    Missing = -1,
    Open = -2,
    Read = -3,
    Format = -4
};

std::string dataset_error_message(DatasetError error) {
    switch (error) {
        case DatasetError::None:   return "No error";
        case DatasetError::Missing: return "File does not exist";
        case DatasetError::Open:   return "Unable to open the file";
        case DatasetError::Read:   return "Failed to read the file";
        case DatasetError::Format: return "Invalid file format";
        default:                  return "Unknown error";
    }
}

DatasetError load_dataset(const std::string& filename) {
    if (!file_exists(filename))
        return DatasetError::Missing;
    
    if (!dataset_open(filename))
        return DatasetError::Open;
        
    return DatasetError::None;
}
```

---

### **VI. 2. Kolejka (queue) i Stos (stack)**

- **Kolejki/stosy**: Idealne gdy ważna jest kolejność przetwarzania  

| **Kolejka w C (ręczna implementacja)**                         | **std::queue w C++**                                |
|----------------------------------------------------------------|-----------------------------------------------------|
| Pracujesz z istniejącym kodem C                                | Piszesz nowy kod w C++                              |
| Potrzebujesz pełnej kontroli nad zarządzaniem pamięcią         | Chcesz gotowe, bezpieczne rozwiązanie               |
| Wymagasz minimalnego narzutu pamięciowego                      | Zależy Ci na wygodzie i czytelności kodu            |
| Implementujesz specjalizowaną strukturę danych                 | Potrzebujesz standardowej implementacji FIFO        |
| Optymalizujesz pod kątem specyficznych wymagań wydajnościowych | Chcesz uniknąć błędów ręcznego zarządzania pamięcią |

#### **Metody:**
| **Struktura** | **Metoda** | **Działanie**             | **Przykład C++**         |
|---------------|------------|---------------------------|--------------------------|
| **queue**     | push       | Dodaje element na koniec  | ```q.push(10);```        |
|               | pop        | Usuwa element z początku  | ```q.pop();```           |
|               | front      | Zwraca pierwszy element   | ```int x = q.front();``` |
|               | back       | Zwraca ostatni element    | ```int y = q.back();```  |
| **stack**     | push       | Dodaje element na wierzch | ```s.push(20);```        |
|               | pop        | Usuwa element z wierzchu  | ```s.pop();```           |
|               | top        | Zwraca wierzchołek stosu  | ```int z = s.top();```   |

**Przykład użycia w C**:
```c
#define MAX_SIZE 100
int queue[MAX_SIZE];
int front = 0, rear = -1;

void enqueue(int item) {
    if (rear >= MAX_SIZE-1) return;
    queue[++rear] = item;
}

int dequeue() {
    if (front > rear) return -1;
    return queue[front++];
}
```

**Przykład użycia w C++**:
```cpp
#include <queue>
std::queue<int> q;

q.push(10);     // Dodanie elementu
int val = q.front(); // Podgląd pierwszego elementu
q.pop();        // Usunięcie elementu
```

#### **Kluczowe różnice:**

| **Kryterium**       | **Implementacja w C**                                    | **std::queue w C++**                     |
|---------------------|----------------------------------------------------------|------------------------------------------|
| **Bezpieczeństwo**  | Wymaga ręcznego zarządzania pamięcią i zakresami         | Automatyczne zarządzanie przez RAII      |
| **Funkcjonalność**  | Podstawowe operacje (enqueue/dequeue)                    | Gotowe metody (push/pop/front/back)      |
| **Wydajność**       | Może być lepiej zoptymalizowana pod specyficzne potrzeby | Zoptymalizowana ogólna implementacja     |

---

### **VI. 3. Listy (list i forward_list)**

- **Listy**: Szybkie modyfikacje, ale wolny dostęp  

| **Kryterium**       | **Lista w C (ręczna implementacja)**     | **std::list w C++**                  | **std::forward_list w C++**          |
|---------------------|------------------------------------------|--------------------------------------|--------------------------------------|
| **Bezpieczeństwo**  | Wymaga ręcznego zarządzania pamięcią     | Automatyczne zarządzanie przez RAII  | Automatyczne zarządzanie przez RAII  |
| **Wskaźniki**       | Tylko next (jednokierunkowa)             | next + prev                          | Tylko next                           |
| **Metody**          | Ręczna implementacja wszystkich operacji | push_back, push_front, pop_back      | Tylko push_front                     |
| **Pamięć**          | Minimalny narzut                         | Większy narzut                       | Mniejszy narzut                      |
| **Wydajność**       | Może być zoptymalizowana pod potrzeby    | Zoptymalizowana ogólna implementacja | Zoptymalizowana ogólna implementacja |
| **Zastosowanie**    | Gdy potrzebna pełna kontrola             | Gdy potrzebny dostęp w obie strony   | Gdy ważna oszczędność pamięci        |

#### **Przykłady implementacji:**

**W C (lista jednokierunkowa):**

- Implementacja w C wymaga ręcznego zarządzania pamięcią

```c
struct Node {
    int data;
    struct Node* next;
};

void insert_front(struct Node** head, int value) {
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    new_node->data = value;
    new_node->next = *head;
    *head = new_node;
}
```

**W C++ (std::list):**

- Kontenery C++ zapewniają gotowe metody i bezpieczeństwo
- **std::list** oferuje pełną funkcjonalność listy dwukierunkowej

```cpp
#include <list>
std::list<int> my_list;
my_list.push_back(10);
my_list.push_front(20);
my_list.pop_front();
```

**W C++ (std::forward_list):**

- **std::forward_list** jest bardziej efektywna pamięciowo

```cpp
#include <forward_list> 
std::forward_list<int> f_list;
f_list.push_front(30);
```

---

### **VI. 4. Tablice (array/vector) vs Kolejki/Stosy**

| **Kryterium**      | **Tablice w C**                 | **std::array/vector w C++**         | **std::queue/stack w C++**   |
|--------------------|---------------------------------|-------------------------------------|------------------------------|
| **Bezpieczeństwo** | Brak kontroli zakresów          | Sprawdzanie zakresów (at())         | Pełna kontrola dostępu       |
| **Dostęp**         | O(1) - dostęp losowy            | O(1) - dostęp losowy                | O(1) - tylko końce           |
| **Wstawianie**     | Brak wbudowanej funkcjonalności | O(n) - w środku                     | O(1) - push/push_back        |
| **Usuwanie**       | Brak wbudowanej funkcjonalności | O(n) - w środku                     | O(1) - pop/pop_back          |
| **Pamięć**         | Statyczna (stack)               | Ciągła (stack/heap)                 | Zależy od kontenera bazowego |
| **Rozmiar**        | Stały                           | Dynamiczny (vector) / Stały (array) | Dynamiczny                   |
| **Typowe użycie**  | Przechowywanie danych           | Gdy potrzebny dostęp losowy         | Gdy ważna kolejność operacji |

#### **Przykłady implementacji:**

**W C (tablica statyczna):**
```c
int arr[10];  // Tablica statyczna
arr[0] = 5;   // Dostęp
```

**W C++ (std::vector):**
```cpp
#include <vector>
std::vector<int> vec = {1, 2, 3};
vec.push_back(4);  // Wstawianie
int val = vec[1];  // Dostęp
```

**W C++ (std::queue):**
```cpp
#include <queue>
std::queue<int> q;
q.push(10);        // Wstawianie
int front = q.front(); // Dostęp
q.pop();           // Usuwanie
```

#### **Porównanie tablic/wektorów vs kolejek/stosów**

| **Kryterium**           | **array/vector**                                        | **queue/stack**                                  |
|-------------------------|---------------------------------------------------------|--------------------------------------------------|
| **Optymalizacja**       | optymalne dla dostępu losowego                          | specjalizowane dla operacji na końcach           |
| **Implementacja w C**   | wymaga ręcznego zarządzania                             | wymaga ręcznego zarządzania                      |
| **Implementacja w C++** | oferują gotowe metody i bezpieczeństwo typów            | oferują gotowe metody i bezpieczeństwo typów     |
| **Zalecenia**           | Używaj vector gdy potrzebujesz dynamicznej tablicy      | Wybierz queue/stack gdy implementujesz FIFO/LIFO |
|                         | Array dla stałych rozmiarów znanych w czasie kompilacji | -                                                |

---

### **VI. 5. Zbiory (set i unordered_set)**

- **Zbiory**: std::set - gdy ważna kolejność, unordered - gdy ważna szybkość  

| **Kryterium**      | **Zbiory w C**                | **std::set w C++**              | **std::unordered_set w C++**  |
|--------------------|-------------------------------|---------------------------------|-------------------------------|
| **Bezpieczeństwo** | Brak wbudowanej implementacji | Automatyczne zarządzanie        | Automatyczne zarządzanie      |
| **Złożoność**      | N/A (zależy od implementacji) | O(log n)                        | O(1) średnia                  |
| **Kolejność**      | N/A                           | Posortowana                     | Nieposortowana                |
| **Wymagania**      | N/A                           | Własny komparator lub operator< | Hash i operator==             |
| **Zastosowanie**   | Rzadko używane                | Gdy potrzebne sortowanie        | Gdy ważna szybkość dostępu    |

#### **Metody dla std::set i std::unordered_set**

| **Metoda** | **Działanie**                       | **Przykład użycia**            |
|------------|-------------------------------------|--------------------------------|
| **insert** | Dodaje element                      | ```s.insert(42);```            |
| **erase**  | Usuwa element                       | ```s.erase(42);```             |
| **find**   | Wyszukuje element (zwraca iterator) | ```auto it = s.find(42);```    |
| **size**   | Zwraca liczbę elementów             | ```size_t count = s.size();``` |
| **empty**  | Sprawdza czy kontener jest pusty    | ```if (s.empty()) { ... }```   |
| **clear**  | Usuwa wszystkie elementy            | ```s.clear();```               |

#### **Przykłady implementacji:**

**W C (brak natywnej implementacji):**
```c
// Typowa ręczna implementacja przez tablicę
int set[100];
int set_size = 0;

void insert(int value) {
    if (!contains(value)) {
        set[set_size++] = value;
    }
}
```

**W C++ (std::set):**
```cpp
#include <set>
std::set<int> s;
s.insert(10);
if (s.find(10) != s.end()) { /*...*/ }
```

**W C++ (std::unordered_set):**
```cpp
#include <unordered_set> 
std::unordered_set<int> us;
us.insert(20);
```

**Uwagi**:
- Metody mają identyczne nazwy i działanie w obu kontenerach
- `find` zwraca iterator do elementu lub `end()` jeśli nie znajdzie
- `insert` nie dodaje duplikatów (zbiory przechowują tylko unikalne wartości)


#### **Porównanie zbiorów w C++**

| **Kryterium**         | **std::set**                                    | **std::unordered_set**               |
|-----------------------|-------------------------------------------------|--------------------------------------|
| **Struktura danych**  | drzewo BST, elementy posortowane                | tablica hashująca, szybszy dostęp    |
| **Implementacja w C** | brak bezpośredniego odpowiednika                | brak bezpośredniego odpowiednika     |
| **Bezpieczeństwo**    | gotowe metody i bezpieczeństwo typów            | gotowe metody i bezpieczeństwo typów |
| **Zalecenia**         | Używaj gdy potrzebujesz posortowanych elementów | Wybierz dla lepszej wydajności       |

---

### **IV. 6. Mapy (map i unordered_map)**

- **Mapy**: std::map - gdy ważna kolejność, unordered - gdy ważna szybkość   

| **Cecha**     | **std::map** (drzewo)     | **std::unordered_map** (hash) |
|---------------|---------------------------|-------------------------------|
| **Złożoność** | O(log n)                  | O(1) (średnia)                |
| **Kolejność** | Posortowana               | Losowa                        |
| **Wymagania** | Operator < lub komparator | Hash i operator ==            |

#### **Metody dla std::map i std::unordered_map** 

| **Metoda**     | **Działanie**                        | **Przykład użycia**                    |
|----------------|--------------------------------------|----------------------------------------|
| **insert**     | Dodaje parę klucz-wartość            | ```m.insert({123, "Jan Kowalski"});``` |
| **erase**      | Usuwa element po kluczu              | ```m.erase(123);```                    |
| **find**       | Wyszukuje element (zwraca iterator)  | ```auto it = m.find(123);```           |
| **size**       | Zwraca liczbę elementów              | ```size_t count = m.size();```         |
| **empty**      | Sprawdza czy kontener jest pusty     | ```if (m.empty()) { ... }```           |
| **clear**      | Usuwa wszystkie elementy             | ```m.clear();```                       |
| **operator[]** | Dostęp/utworzenie wartości po kluczu | ```m[123] = "Nowa wartość";```         |

#### **Przykłady implementacji:**

#### **Przykład w C (tablica asocjacyjna):**
```c
typedef struct {
    int key;
    char value[50];
} MapEntry;
MapEntry map[100];
```

#### **Przykład w C++**  
```cpp
std::map<int, std::string> students;

// insert
students.insert({12345678, "Jan Kowalski"});
students[58371975] = "Adam Nowak";

// find
auto it = students.find(2234567);
if (it == students.end()) {
    std::cout << "Nie ma takiego studenta" << std::endl;
}

// erase
students.erase(12345678);
```

**Uwagi**:  
1. Metody identyczne dla `std::map` i `std::unordered_map`  
2. `operator[]` tworzy nowy element jeśli klucz nie istnieje  
3. `find` zwraca `end()` gdy element nie zostanie znaleziony  


**Źródło:** Wykład 6 - Programowanie w C++, Konrad Kosmatka

---