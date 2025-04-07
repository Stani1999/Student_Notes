## **Wykład II (27.02.2025)**  

### **II. 1. Podział na pliki**  

| **Element**   | **Opis**                                             |
|---------------|------------------------------------------------------|
| Pliki `.hpp`  | **deklaracje** funkcji, klas, zmiennych globalnych   |
| Pliki `.cpp`  | **implementacje** funkcji zadeklarowanych w nagłówku |
| Include guard | Zabezpiecza przed wielokrotnym dołączaniem plików    |

#### **Plik nagłówkowy (`.hpp` lub `.h`)**  
Stosuje **Include Guard** <br>
Zabezpiecza przed wielokrotnym dołączaniem tego samego nagłówka, co mogłoby prowadzić do błędów kompilacji. <br>Działa w następujący sposób:
- Sprawdza, czy unikalny identyfikator (np. OPERATIONS_H) nie został zdefiniowany (#ifndef).
- Jeśli nie – definiuje go (#define) i przetwarza zawartość pliku.
- Jeśli identyfikator już istnieje, kompilator pomija kod do #endif.

- Składnia
```cpp
#ifndef NAZWA_PLIKU_H
#define NAZWA_PLIKU_H
// Deklaracje
#endif
```  
Przykład (`operations.hpp`):  
```cpp
#ifndef OPERATIONS_H
#define OPERATIONS_H
double add(double, double);
double sub(double, double); 
#endif
```  

#### **Plik źródłowy (`.cpp`)**  

Dołącza odpowiadający mu plik nagłówkowy:  
```cpp
#include "operations.hpp"
```  
Przykład (`operations.cpp`):  
```cpp
double add(double a, double b) { return a + b; }
double sub(double a, double b) { return a - b; }
```  

#### **Zasady**  
Funkcje używane tylko w jednym pliku `.cpp` należy deklarować lokalnie (np. na początku pliku), a nie w nagłówku.  
Dołączanie plików:  
`#include "plik.hpp"` – dla plików w projekcie (przeszukuje katalog bieżący).  
`#include <iostream>` – dla bibliotek standardowych.  

#### **Korzyści**  
Lepsza organizacja kodu.  
Szybsza kompilacja (tylko zmienione pliki są rekompilowane).  
Łatwiejsza współpraca w zespołach.  

---  

### **II. 2. Operatory (w tym inkrementacji/dekrementacji)**  

| **Typ operatora**           | **Przykłady**                         | **Przykłady użycia w kodzie**                                                                 |
|-----------------------------|---------------------------------------|-----------------------------------------------------------------------------------------------|
| **Arytmetyczne**            | `+`, `-`, `*`, `/`, `%`               | ```cpp int x = 5 + 3; // 8  double y = 10.0 / 3.0; // 3.333...  int z = 10 % 3; // 1 ```      |
| **Porównania**              | `==`, `!=`, `<`, `>`, `<=`, `>=`      | ```cpp bool isEqual = (5 == 5); // true  bool isGreater = (10 > 7); // true ```               |
| **Logiczne**                | `&&` (AND), `\|\|` (OR), `!` (NOT)    | ```cpp bool result = (true && false); // false  bool check = (5 > 3 \|\| 2 < 1); // true ```  |
| **Inkrementacji/dekrementacji** | `++`, `--` (pre i post)           | ```cpp int a = 5;  int b = a++; // b = 5, a = 6  int c = ++a; // c = 7, a = 7 ```             |

#### **Tabela operatorów inkrementacji i dekrementacji w C++**  

| **Typ operatora**       | **Składnia** | **Działanie**                                                                 | **Przykład użycia**                     | **Wartość po operacji** |
|-------------------------|--------------|-------------------------------------------------------------------------------|-----------------------------------------|-------------------------|
| **Pre-inkrementacja**   | `++a`        | Najpierw zwiększa wartość `a` o 1, potem zwraca nową wartość                  | `int b = ++a;` (gdzie `a = 5`)          | `a = 6`, `b = 6`        |
| **Post-inkrementacja**  | `a++`        | Najpierw zwraca bieżącą wartość `a`, potem zwiększa `a` o 1                   | `int b = a++;` (gdzie `a = 5`)          | `a = 6`, `b = 5`        |
| **Pre-dekrementacja**   | `--a`        | Najpierw zmniejsza wartość `a` o 1, potem zwraca nową wartość                 | `int b = --a;` (gdzie `a = 5`)          | `a = 4`, `b = 4`        |
| **Post-dekrementacja**  | `a--`        | Najpierw zwraca bieżącą wartość `a`, potem zmniejsza `a` o 1                  | `int b = a--;` (gdzie `a = 5`)          | `a = 4`, `b = 5`        |

#### **Przykłady kodu**  
```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 5;
    
    // Pre-inkrementacja
    int b = ++a;
    cout << "Pre-inkrementacja: a = " << a << ", b = " << b << endl;  // a = 6, b = 6
    
    // Post-inkrementacja
    int c = a++;
    cout << "Post-inkrementacja: a = " << a << ", c = " << c << endl;  // a = 7, c = 6
    
    // Pre-dekrementacja
    int d = --a;
    cout << "Pre-dekrementacja: a = " << a << ", d = " << d << endl;  // a = 6, d = 6
    
    // Post-dekrementacja
    int e = a--;
    cout << "Post-dekrementacja: a = " << a << ", e = " << e << endl;  // a = 5, e = 6
    
    return 0;
}
```

#### **Kilka ważnych uwag dotyczących operatorów inkrementacji/dekrementacji**

| **Zasada**                               | **Przykład problematyczny**    | **Poprawne użycie**            | **Konsekwencje**                                                                     |
|------------------------------------------|--------------------------------|--------------------------------|--------------------------------------------------------------------------------------|
| **Unikaj mieszania w jednym wyrażeniu**  | `int x = (a++) + (++a);`       | `++a; int x = a + a;` lub rozdziel operacje | Niezdefiniowane zachowanie (`UB`), różne wyniki w różnych kompilatorach |
| **Preferuj pre-inkrementację w pętlach** | `for(int i=0; i<n; i++) {...}` | `for(int i=0; i<n; ++i) {...}` | Lepsza wydajność dla złożonych typów (iteratory)                                     |
| **Nie stosuj do wartości tymczasowych**  | `5++`, `(a+b)++`               | `int temp = a+b; temp++;`      | Błąd kompilacji: "lvalue required as increment operand"                              |
| **Uważaj na kolejność ewaluacji**        | `arr[i++] = i;`                | `arr[i] = i; i++;`             | Nieokreślona wartość `i` w trakcie przypisania                                       |
| **Unikaj wielokrotnego użycia w jednej instrukcji** | `func(i++, i++, i++);` | `func(i, i+1, i+2); i+=3;`  | Kolejność ewaluacji argumentów niezdefiniowana                                       |

**Dodatkowe wyjaśnienia:**
1. W przypadku iteratorów STL, pre-inkrementacja (`++it`) jest ogólnie zalecana, ponieważ nie tworzy tymczasowej kopii obiektu
2. Problem z kolejnością ewaluacji jest szczególnie istotny przy przekazywaniu argumentów do funkcji
3. W prostych typach (jak `int`) różnica między `i++` a `++i` jest minimalna, ale dobre praktyki sugerują używanie `++i` dla spójności
4. `UB (Undefined Behavior)` – to sytuacja w C/C++, <br>gdy kod wykonuje operację niezgodną ze standardem języka (np. modyfikacja tej samej zmiennej wielokrotnie w jednym wyrażeniu), <br>co może powodować nieprzewidywalne efekty (od błędów po dziwne działanie programu, w zależności od kompilatora/systemu).

---

### **II 3. Wskaźniki i referencje w C**  

| **Element**           | **Definicja**                                                                | **Przykład użycia**                          | **Kluczowa różnica**                             |
|-----------------------|------------------------------------------------------------------------------|----------------------------------------------|--------------------------------------------------|
| **Wskaźnik (`*`)**    | Zmienna przechowująca adres innej zmiennej w pamięci                         | `int* ptr = &x;`<br>`*ptr = 10;`             | Może być `nullptr`, można zmieniać adres         |
| **Referencja (`&`)**  | Alias (alternatywna nazwa) dla istniejącej zmiennej                          | `int& ref = x;`<br>`ref = 20;`               | Musi być inicjalizowana, nie może być `null`     |
| **Operator `&`**      | Zwraca adres pamięci zmiennej                                                | `int* addr = &x;`                            | Używany zarówno w wskaźnikach jak i referencjach |
| **Dereferencja `*`**  | Pozwala dostać się do wartości przechowywanej pod adresem (tylko wskaźniki)  | `int value = *ptr;`                          | Działa tylko na wskaźnikach                      |

**Najważniejsze różnice:**  
1. Referencja **musi** być zainicjalizowana podczas tworzenia, wskaźnik może być `nullptr` (wskaźnik pusty)  
2. Referencji **nie można** przekierować na inną zmienną, wskaźnik - tak  
3. Składnia referencji jest czystsza (nie potrzeba operatora `*` do dostępu do wartości)  

**Przykład praktyczny:**  
```cpp
int main() {
    int x = 5;
    
    // Wskaźnik
    int* ptr = &x;  // przechowuje adres x
    *ptr = 10;      // zmienia wartość x
    
    // Referencja
    int& ref = x;   // ref to teraz alias x
    ref = 20;       // zmienia wartość x
    
    return 0;
}
```
### **II 4. Tablice**

| **Typ tablicy**       | **Deklaracja**              | **Zalety**                                                  | **Wady**                                           | **Typowe zastosowania**                                       |
|-----------------------|-----------------------------|-------------------------------------------------------------|----------------------------------------------------|---------------------------------------------------------------|
| **Statyczna**         | `int tab[5];`               | - Szybki dostęp<br>- Prosta składnia                        | - Stały rozmiar<br>- Brak sprawdzania zakresu      | Małe, znane z góry struktury danych                           |
| **Dynamiczna**        | `int *tab = new int[5];`<br>`delete[] tab;` | - Zmienny rozmiar (można realokować)<br>- Zarządzanie pamięcią | - Konieczność ręcznego zwalniania<br>- Ryzyko wycieków pamięci | Struktury o zmiennym rozmiarze |
| **Wielowymiarowa**    | `int matrix[3][3];`         | - Prosta reprezentacja macierzy<br>- Szybki dostęp          | - Stałe wymiary<br>- Zajmuje ciągły obszar pamięci | Grafika, obliczenia macierzowe                                |
| **std::array (C++11)**| `std::array<int, 5> arr;`   | - Bezpieczeństwo (sprawdzanie zakresu)<br>- Metody STL      | - Stały rozmiar<br>- Wymaga C++11                  | Nowoczesne zastępstwo tablic statycznych                      |
| **std::vector**       | `std::vector<int> vec(5);`  | - Dynamiczny rozmiar<br>- Automatyczne zarządzanie pamięcią | - Nieznacznie wolniejszy dostęp                    | Główna struktura danych w nowoczesnym C++                     |

#### **Przykłady praktyczne:**

1. **Tablice statyczne:**
```cpp
int grades[5] = {4, 5, 3, 4, 5};
cout << grades[0]; // Wypisze 4
```

2. **Tablice dynamiczne:**
```cpp
int size = 10;
int *dynamicArray = new int[size];
dynamicArray[0] = 100;
delete[] dynamicArray; // Pamiętaj o zwolnieniu!
```

3. **Tablice wielowymiarowe:**
```cpp
char tictactoe[3][3] = {{'X', 'O', 'X'},
                        {'O', 'X', 'O'},
                        {'X', ' ', 'O'}};
```

4. **Nowoczesne alternatywy (C++11):**
```cpp
std::array<int, 3> modernArr = {1, 2, 3};
std::vector<int> dynamicVec = {1, 2, 3, 4};
dynamicVec.push_back(5); // Rozszerzanie w runtime
```

**Ważne ostrzeżenia:**
- Tablice statyczne i dynamiczne nie sprawdzają zakresu - dostęp do `tab[100]` może powodować błędy pamięci
- Zawsze zwalniaj pamięć po `new[]` za pomocą `delete[]`
- W nowoczesnym C++ preferuj `std::vector` i `std::array` nad surowymi tablicami

**Źródło:** Wykład 2 - Programowanie w C++, Konrad Kosmatka

---