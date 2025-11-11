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

**Źródło:** Wykład 1 - Programowanie w C++, Konrad Kosmatka

---