# Przeredagowana notatka z Wykładów Programowania w C++

## **Wykład I (20.02.2024)**  

### **I. 1. Cechy języka C++**  

| **Cecha**      | **Opis**                                           |
|----------------|----------------------------------------------------|
| Twórca         | Bjarne Stroustrup (lata 80. XX wieku)              |
| Typowanie      | Statyczne (typ zmiennej jest stały)                |
| Wykorzystanie  | Systemy embedded, mikroprocesory, wysoka wydajność |
| Blisko sprzętu | Optymalizacja pod kątem architektury komputera     |

#### **Podsumowanie różnic**  
| **Element**           | **C**                | **C++**                       |
|-----------------------|----------------------|-------------------------------|
| Nagłówki              | `#include <stdio.h>` | `#include <iostream>`         |
| Wyjście               | `printf`             | `std::cout`                   |
| Nowa linia            | `\n` w `printf`      | `std::endl` lub `\n`          |

---

### **I. 2. Typy danych w C/C++**  

| **Typ**                     | **C (Przykłady)**                  | **C++ (Przykłady)**    | **Format (`printf`)** | **Format (`cout`)** | **Rozmiar (typowy)** | **Zakres/Uwagi**                 |
|-----------------------------|------------------------------------|------------------------|-----------------------|---------------------|----------------------|----------------------------------|
| **Całkowite**               | `int`, `long`, `short`, `unsigned` | (jak w C)              | `%d`, `%ld`, `%u`     | `<< dec`/`hex`      | 4B, 4B/8B, 2B, 4B    | Zależne od systemu               |
| **Zmiennoprzecinkowe**      | `float`, `double`                  | (jak w C)              | `%f`, `%lf`           | `<<` (automatycznie)| 4B, 8B               | Precyzja: ~6–9, ~15–18           |
| **Znakowe**                 | `char`                             | (jak w C)              | `%c`                  | `<<` (automatycznie)| 1B                   | `-128`–`127` lub `0`–`255`       |
| **Logiczne**                | Brak (`int` z `0/1`)               | `bool` (`true`/`false`)| `%d`                  | `<< boolalpha`      | 1B (C++)             | W C: `0` (fałsz), `!=0` (prawda) |
| **Stringi C-style (char*)** | `char[]`, `char*`                  | –                      | `%s`                  | `<<` (dla `char*`)  | Dynamiczny           | Zakończony `'\0'`                |
| **String (C++)**            | –                                  | `std::string`          | `.c_str()` z `%s`     | `<<` (bezpośrednio) | Dynamiczny           | Bezpieczniejszy niż C-string     |

| **Kluczowe różnice**     | **Język C**                                         | **Język C++**                                                    |
|--------------------------|-----------------------------------------------------|------------------------------------------------------------------|
| **Łańcuchy znaków**      | `char tekst[] = "ABC";` (tablica znaków)            | `std::string tekst = "ABC";` (obiekt z metodami jak `.length()`) |
| **Typ logiczny**         | Brak `bool` (używany `int`: 0 = fałsz, ≠0 = prawda) | `bool` z wartościami `true`/`false`                              |
| **Wyświetlanie danych**  | `printf("%d", liczba);`                             | `std::cout << liczba;`                                           |

 ---

### **I. 3. Instrukcje warunkowe**  

| **Instrukcja**  | **Opis**                                           |
|-----------------|----------------------------------------------------|
| `if`            | Warunek podstawowy                                 |
| `else if`       | Dodatkowe warunki                                  |
| `else`          | Wykonuje się, gdy żaden warunek nie jest spełniony |
| Skrócona wersja | `(warunek ? wartość1 : wartość2)`                  |


#### **W stylu C**  
```c
    if (ile_masz_cm > 20) {
        printf("Ale z ciebie bydle!\n");
    } 
    else if (ile_masz_cm > 15) {
        printf("Średnia krajowa.\n");
    } 
    else {
        printf("Masz małe ego.\n");
    }

    // Skrócona wersja if (ternary operator)
    printf("Podsumowanie: %s\n", (ile_masz_cm > 15 ? "Nice." : "Bywało lepiej."));
```

#### **W stylu C++**  
```cpp
    if (ile_masz_cm > 20) {
        std::cout << "Ale z ciebie bydle!" << std::endl;
    } 
    else if (ile_masz_cm > 15) {
        std::cout << "Średnia krajowa." << std::endl;
    } 
    else {
        std::cout << "Masz małe ego." << std::endl;
    }

    // Skrócona wersja if (ternary operator)
    std::cout << "Podsumowanie: " << (ile_masz_cm > 15 ? "Nice." : "Bywało lepiej.") << std::endl;
```

---

### **I. 4. Pętle**  

### - **Pętla for**  

| **Element** | **Opis**                                                                  |
|-------------|---------------------------------------------------------------------------|
| `for`       | Pętla ze zdefiniowanym początkiem, warunkiem i krokiem                    |
| `break`     | Przerywa wykonanie pętli                                                  |
| `continue`  | Pomija aktualną iterację                                                  |

#### **W stylu C**  
```c
    // Pętla for wypisująca liczby 0-99
    for (int i = 0; i < 100; i++) {
        if (i == 69) continue;  // Pomija 69
        printf("%d ", i);
    }
```

#### **W stylu C++**  
```cpp
    // Pętla for wypisująca liczby 0-99
    for (int i = 0; i < 100; i++) {
        if (i == 69) continue;  // Pomija 69
        std::cout << i << " ";
    }
```

### - **Pętla while**

| **Element** | **Opis**                                                                  |
|-------------|---------------------------------------------------------------------------|
| `while`     | Wykonuje blok kodu dopóki warunek jest spełniony                          |
| `break`     | Przerywa wykonanie pętli                                                  |
| `continue`  | Pomija aktualną iterację                                                  |

#### **W stylu C**
```c
    // Pętla while wypisująca liczby 0-99
    while (i < 100) {
        if (i == 69) {
            i++;
            continue;  // Pomija 69
        }
        printf("%d ", i);
        i++;
    }
```

#### **W stylu C++**
```cpp
    // Pętla while wypisująca liczby 0-99
    while (i < 100) {
        if (i == 69) {
            i++;
            continue;  // Pomija 69
        }
        std::cout << i << " ";
        i++;
    }
```

### - **Pętla do...while**

| **Element** | **Opis**                                                                  |
|-------------|---------------------------------------------------------------------------|
| `do...while`| Wykonuje blok kodu przynajmniej raz, a następnie sprawdza warunek         |
| `break`     | Przerywa wykonanie pętli                                                  |
| `continue`  | Pomija aktualną iterację                                                  |

#### **W stylu C**
```c
    // Pętla do...while wypisująca liczby 0-99
    do {
        if (i == 69) {
            i++;
            continue;  // Pomija 69
        }
        printf("%d ", i);
        i++;
    } while (i < 100);
```

#### **W stylu C++**
```cpp
    // Pętla do...while wypisująca liczby 0-99
    do {
        if (i == 69) {
            i++;
            continue;  // Pomija 69
        }
        std::cout << i << " ";
        i++;
    } while (i < 100);
```

---

### **I. 5. Entry Point (punkt wejścia programu)**

#### **Najprostszy program w C/C++:**

```c
#include <stdio.h> // lub dla C++: #include <iostream>

int main() {
    return 0;
}
```

#### **W stylu C**

```c
#include <stdio.h>

// Z argumentami wiersza poleceń
int main(int argc, char *argv[]) {
    printf("Program: %s\n", argv[0]);
    printf("Liczba argumentów: %d\n", argc - 1);
    
    for(int i = 1; i < argc; i++) {
        printf("Argument %d: %s\n", i, argv[i]);
    }
    
    return 0;
}
```

#### **W stylu C++**
```cpp
#include <iostream>

// Z argumentami wiersza poleceń
int main(int argc, char *argv[]) {
    std::cout << "Program: " << argv[0] << std::endl;
    std::cout << "Liczba argumentów: " << argc - 1 << std::endl;
    
    for(int i = 1; i < argc; i++) {
        std::cout << "Argument " << i << ": " << argv[i] << std::endl;
    }
    
    return 0;
}
```

### **Kluczowe elementy entry point**

| **Element**      | **Opis**                                                  |
|------------------|-----------------------------------------------------------|
| `argc`           | Liczba argumentów (≥1, bo argv[0] to nazwa programu)      |
| `argv`           | Tablica ciągów znaków z argumentami                       |
| Wartość zwracana | 0 oznacza sukces, inne wartości oznaczają błędy           |

### **Różnice C vs C++**
| **Różnica** | **C** | **C++** |
|-------------|-------|---------|
| Nagłówki | `<stdio.h>` | `<iostream>` |
| Wyjście | `printf()` | `std::cout` |
| Przestrzeń nazw | Brak | `std::` |
| Typ void w main | `main(void)` | `main()` |

### **Uwagi:**
1. W C++ można pominąć `void` w `main()`
2. `argv[0]` może być pusty jeśli program uruchomiony bez ścieżki
3. W systemach UNIX wartości zwracane inne niż 0 oznaczają błędy
4. W C++ warto używać `std::vector<std::string>` zamiast `char*[]` dla bezpieczeństwa

---

### **I. 6. Funkcje**  

#### **1. Podstawowa struktura funkcji**

| **Element**       | **C**                          | **C++**                        |
|-------------------|--------------------------------|--------------------------------|
| **Deklaracja**    | `typ nazwa(argumenty);`        | `typ nazwa(argumenty);`        |
| **Definicja**     | `typ nazwa(argumenty) {...}`   | `typ nazwa(argumenty) {...}`   |
| **Wywołanie**     | `nazwa(argumenty);`            | `nazwa(argumenty);`            |

#### **2. Przykład podstawowej funkcji**

**W stylu C:**
```c
#include <stdio.h>

// Deklaracja
int dodaj(int a, int b);

int main() {
    int wynik = dodaj(6, 9);
    printf("Wynik: %d\n", wynik);
    return 0;
}

// Definicja
int dodaj(int a, int b) {
    return a + b;
}
```

**W stylu C++:**
```cpp
#include <iostream>

// Deklaracja
int dodaj(int a, int b);

int main() {
    int wynik = dodaj(6, 9);
    std::cout << "Wynik: " << wynik << std::endl;
    return 0;
}

// Definicja
int dodaj(int a, int b) {
    return a + b;
}
```

#### **3. Zaawansowane funkcje (tylko C++)**

| **Funkcjonalność**     | **Przykład**                                        |
|------------------------|-----------------------------------------------------|
| **Przeciążanie**       | `void funkcja(int x);`<br>`void funkcja(double x);` |
| **Argumenty domyślne** | `void funkcja(int x = 0);`                          |
| **Referencje**         | `void zamien(int &a, int &b) {...}`                 |
| **Szablony**           | `template<typename T> T max(T a, T b) {...}`        |

**Przykład:**
```cpp
#include <iostream>

// Przeciążanie
void wypisz(int x) {
    std::cout << "Liczba całkowita: " << x << std::endl;
}

void wypisz(double x) {
    std::cout << "Liczba zmiennoprzecinkowa: " << x << std::endl;
}

// Referencje
void podwoj(int &x) {
    x *= 2;
}

int main() {
    int a = 5;
    double b = 3.14;
    
    wypisz(a);  // Wersja dla int
    wypisz(b);  // Wersja dla double
    
    podwoj(a);
    std::cout << "Podwojone a: " << a << std::endl;
    
    return 0;
}
```

#### **4. Różnice między C a C++**

| **Cecha**              | **C**       | **C++**               |
|------------------------|-------------|-----------------------|
| **Przeciążanie**       | Niedostępne | Dostępne              |
| **Referencje**         | Niedostępne | Dostępne (`&`)        |
| **Argumenty domyślne** | Niedostępne | Dostępne              |
| **Szablony**           | Niedostępne | Dostępne (`template`) |

#### **5. Uwagi**
1. W C++ preferuje się przekazywanie przez referencję zamiast wskaźników
2. Przeciążanie funkcji pozwala używać tej samej nazwy dla różnych typów
3. Argumenty domyślne muszą być podawane od prawej strony
4. Wartość zwracana `void` oznacza, że funkcja nic nie zwraca

---

### **I. 7. Dyrektywy preprocesora**  

| **Dyrektywa**       | **Opis**                  |
|---------------------|---------------------------|
| `#include`          | Dołącza pliki nagłówkowe  |
| `#define`           | Definiuje stałe           |
| `#ifdef`, `#ifndef` | Warunkowa kompilacja      |
| Generowanie błędów  | error w czasie kompilacji |

```cpp
#include <iostream>
#define SHOW_DEBUG_INFO

int main() {
    #ifdef SHOW_DEBUG_INFO
        std::cout << "Rozpoczęcie programu" << std::endl;
    #endif
    
    std::cout << "Hello World!" << std::endl;
    
    return 0;
}
```

---

### **I. 8. Namespace (Przestrzenie nazw) w C++**  

| **Element**            | **Opis**                            |
|------------------------|-------------------------------------|
| Przestrzeń nazw        | Zapobiega kolizjom nazw             |
| Odwołanie              | `nazwa_przestrzeni::funkcja()`      |
| `using namespace std;` | Pozwala pominąć przedrostek `std::` |
| `std`      |  to przestrzeń nazw biblioteki standardowej C++ |

```cpp
#include <iostream>

namespace Matematyka {
    const double PI = 3.14159;
    
    double kwadrat(double x) {
        return x * x;
    }
}

int main() {
    std::cout << "PI wynosi: " << Matematyka::PI << std::endl;
    std::cout << "Kwadrat 5: " << Matematyka::kwadrat(5) << std::endl;
    
    return 0;
}
```

---

### **I. 9. Komentarze**   

| **Typ**          | **Składnia** | **Zastosowanie**                          | **Przykład**                                 |
|------------------|--------------|-------------------------------------------|----------------------------------------------|
| **Jednoliniowy** | `//`         | Krótkie wyjaśnienia w kodzie              | `// To jest komentarz`                       |
| **Wieloliniowy** | `/* ... */`  | Dłuższe opisy, tymczasowe wyłączanie kodu | `/*`<br>`To jest dłuższy komentarz `<br>`*/` |

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

---

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

---

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

---

## **Wykład IV (13.03.2025)**  

### **Stringi**  

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

## **Wykład V (20.03.2025)**  

### **STL (Standard Template Library)**  

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

## **Wykład VI (27.03.2025)**  

### **Typy wyliczeniowe**  

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