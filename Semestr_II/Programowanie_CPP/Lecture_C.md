# Notatka z języka C

### **Spis treści**  
1. [Kompilowanie programu](#i-kompilowanie-programu)  
2. [Zagadnienia języka C](#ii-zagadnienia-związane-z-językiem-c)  
   - [Argumenty wejściowe](#ii-1-argumenty-wejściowe-int-argc-char-argv)  
   - [Printf i scanf](#ii-2-printf-oraz-scanf)  
   - [Funkcje i wskaźniki](#ii-3-funkcje-i-wskaźniki)  
   - [Tablice](#ii-4-tablice)  
   - [Alokacja dynamiczna](#ii-5-alokacja-dynamiczna)  
   - [Stringi](#ii-6-stringi-c-style)  
   - [Struktury](#ii-7-struktury)  
   - [Wyliczenia (enum)](#ii-8-wyliczenia-enum)  
3. [Assembler NASM (x86_64)](#iii-4-assembler-nasm-x86_64)  
4. [Organizacja projektu](#iv-organizacja-projektu)  
   - [Podział na pliki `.c` i `.h`](#iv-1-podział-na-pliki-c-i-h)  
   - [Makefile i CMake](#iv-2-makefile-i-cmake)  
5. [Dynamiczne struktury danych](#v-dynamiczne-struktury-danych)  
   - [Kolejka (FIFO)](#v-1-kolejka-fifo)  
   - [Stos (LIFO)](#v-2-stos-lifo)  

## I. Kompilowanie programu

### [I 1. Instalacja kompilatora (VSC-WSL), kliknij tutaj](https://code.visualstudio.com/docs/cpp/config-wsl)

### I. 2. Aby poprawnie skompilować należy dołączyć do niego odpowiednie biblioteki poprzez #include, należy to robić na początku programu:
```c
#include <stdio.h>    // funkcje wejścia/wyjścia: printf, scanf
#include <stdlib.h>   // funkcje: atoi, malloc, free, sscanf
#include <string.h>   // funkcje do obsługi napisów: strcmp, strcpy
#include <math.h>     // funkcje matematyczne: pow, sqrt (jeśli potrzebne)
#include <ctype.h>    // funkcje takie jak tolower
```

### I. 3. Aby skompilować program za pomocą GCC należy zastosować składnie : 
```zsh
gcc <nazwa_programu>.c -o <nazwa_programu_po_skompilowaniu> -l 
```
- Bez `-o` kompilator domyślnie tworzy plik a.out (Linux/macOS) lub a.exe (Windows)
- Gdy używamy biblioteki math.h zamiast `-l` należy wpisać `-lm` 
- `-l` oznacza "link with library" (dołącz bibliotekę).
- `m` to skrót od biblioteki matematycznej
- Przykład 
    ```zsh
    gcc kod.c -o kod -lm
    ```

<a id="uruchomienie-programu"></a>
### I 4. Uruchomienie programu
```zsh
./<nazwa_programu_po_skompilowaniu> [argument_1] [argument_2] [argument_3] ... [argument_n-1] [argument_n]
```
- elementy opcjonalne oznaczane są za pomocą ubrania ich w `[ ]`.
- aby przekazać argument zawierający spacje, należy ująć go w cudzysłów

- Przykład 
    ```zsh
    ./kod "Politechnika Warszawska"
    ```

## II. Zagadnienia związane z językiem C.

### II. 1. Argumenty wejściowe `(int argc, char *argv[])`
- argc (argument count) – liczba argumentów (≥ 1, bo argv[0] to nazwa programu).
- argv (argument vector) – tablica wskaźników do napisów (zakończona NULL).
- parametry te są wprowadzane do programu podczas jego uruchamiania ([patrz punkt I 4.](#uruchomienie-programu))

#### II. 1. Przykład
```c
/*
* Funkcja main do uruchomienia programu
*   Stanowi Entry Point (bez niego kompilator nie wie od czego zacząć)
* Argumenty: 
* (przyjmowane z wiersza poleceń przy wywołaniu programu)
*   argc - liczba argumentów
*   argv - tablica napisów (ciągów znaków)
* Zwraca: 
*   0 - gdy program jest zakończony bez błedów
*   1 - gdy brak wymaganego argumentu lub jest niepoprawny
*/
int main(int argc, char *argv[]) {
    // Sprawdzenie minimalnej liczby argumentów
    if (argc < 2) {
        printf("Użycie: %s <liczba>\n", argv[0]);
        return 1;
    }

    // Konwersja pierwszego argumentu na liczbę całkowitą
    const int N = atoi(argv[1]);
    
    // Walidacja wyniku konwersji
    if (N <= 0) {
        printf("Błąd: argument musi być liczbą większą od 0 (podano: '%s')\n", argv[1]);
        return 1;
    }

    printf("Program uruchomiony z %d argumentami\n", argc);
    printf("Przekazana liczba: %d\n", N);
    
    // Wyświetlenie argumentów z indeksem
    for (int i = 0; i < argc; i++) {
        if (i == 0) { // argv[0] to zawsze nazwa programu
            printf("Nazwa programu: %s\n", argv[i]);
        }
        else {
            printf("Argument %d: %s\n", i, argv[i]);
        }
    }
    
    return 0;
}
```

### II 2. printf oraz scanf
| Funkcja | Pełna nazwa     | Tłumaczenie              | Działanie                  | Dodatkowo              |
|---------|-----------------|--------------------------|----------------------------|------------------------|
| printf  | print formatted | sformatowane wypisywanie | wypisuje tekst na ekran    | pokazuje wartości (x)  |
| scanf   | scan formatted  | sformatowane wczytywanie | wczytuje dane z klawiatury | wymaga wskaźników (&x) |

#### II 2. Tabela przykładowych specyfikatorów
| Specyfikator | Typ    |	Przykład             |
|--------------|--------|------------------------|
| %d           | int    | scanf("%d", &liczba);  |
| %f           | float  | scanf("%f", &zmienna); |
| %lf      	   | double | scanf("%lf", &x);      |
| %s           | char[] | scanf("%9s", bufor);   |

#### II. 2. Przykłady
```c
/*
* Funkcja input_output_example 
*   Przykładowe wypisywanie i wprowadzanie danych przez terminal 
* Argumenty: 
*   Deklarowane w programie i przyjmowane przez scanf (ich wartości) z terminala
* Zwraca: 
*   Typu void - funkcja nie zwraca żadnej wartości
*/
void input_output_example() {
    
    int age;        // Deklaracja zmiennej dla wieku
    char name[50];  // Tablica znaków dla imienia (max 49 znaków + '\0')
    
    // Wyświetlenie prośby o podanie imienia
    printf("Podaj swoje imię: ");
    // Odczytanie imienia - %49s ogranicza do 49 znaków (zapobiega przepełnieniu)
    // name - przekazujemy adres początku tablicy (bez &, bo tablice to wskaźniki)
    scanf("%49s", name);  
    
    // Wyświetlenie prośby o podanie wieku
    printf("Podaj swój wiek: ");
    // Odczytanie wieku - %d dla int, &age przekazuje adres zmiennej
    scanf("%d", &age);
    
    // Wyświetlenie wyniku - %s dla stringa, %d dla int
    printf("Witaj, %s! Masz %d lat.\n", name, age);
    
    /* Uwaga: scanf("%s") czyta tylko do pierwszej spacji.
       Aby przeczytać całą linię, lepiej użyć fgets():
       fgets(name, 50, stdin);
    */
    // Przykład - fgets czytający całą linię
    printf("Podaj ponownie imię i nazwisko: ");
    fgets(name, sizeof(name), stdin);
    
    // Usuwamy znak nowej linii z końca
    name[strcspn(name, "\n")] = '\0';
    
    // Wyświetlenie wyniku - %s dla stringa
    printf("fgets wczytał: '%s'\n", name);
} 
```

## II. 3. Funkcje i wskaźniki

### Funkcje w języku C
- Funkcja to blok kodu, który wykonuje określone zadanie.
- Deklaracja funkcji zawiera typ zwracany, nazwę i listę argumentów.
- Funkcje mogą zwracać wartości lub być typu `void` (nic nie zwracają).
- Argumenty mogą być przekazywane przez wartość (domyślnie) lub przez wskaźnik (aby umożliwić modyfikację danych w miejscu wywołania).

### Wskaźniki (`*`, `&`)
- Wskaźnik to zmienna przechowująca adres innej zmiennej.
- Operator `*` pozwala na dereferencję – uzyskanie wartości spod adresu.
- Operator `&` zwraca adres zmiennej.
- Przekazywanie wskaźników do funkcji pozwala modyfikować oryginalne zmienne.

#### II. 3. Przykład – funkcja zwiększająca wartość zmiennej

```c
/*
* Funkcja increment zwiększa wartość liczby o 1
* Argumenty:
*   int *x - wskaźnik do liczby całkowitej
* Zwraca:
*   void - nie zwraca wyniku, ale modyfikuje wartość przez wskaźnik
*/
void increment(int *x) {
    (*x)++;  // Zwiększenie wartości, do której prowadzi wskaźnik
}

/*
* Funkcja display_info wyświetla się podczas uruchomienia
* arg:
**   name - nazwa programu 
* return:
**   jako void nie zwraca wartości
*/
void display_info(char *name){

    printf("Witaj w programie %s\n", name);
}

int main(int argc, char *argv[]) {
    int liczba = 5;
    display_info(argv[0]); // argv[0] - przekazanie nazyw programu do funkcji wyświetlającej informacje
    printf("Przed: %d\n", liczba);

    
    increment(&liczba);  // Przekazanie adresu zmiennej

    printf("Po: %d\n", liczba);  // Wartość została zmieniona przez funkcję
    
    return 0;
}
```

#### II. 3. Przykład – funkcja zwracająca wskaźnik

```c
/*
* Funkcja get_max zwraca wskaźnik do większej z dwóch liczb
* Argumenty:
*   int *a, int *b - wskaźniki do liczb
* Zwraca:
*   int* - wskaźnik do większej liczby bez użycia funkcja będzie działać na kopi zmiennej
*/
int* get_max(int *a, int *b) { 
    return (*a > *b) ? a : b; // dowolne operacje logiczne operator warunkowy (trójargumentowy):
    // składnia : warunek ? wartość_jeśli_prawda : wartość_jeśli_fałsz;
}

int main() {
    int x = 10, y = 20;
    int *max_ptr = get_max(&x, &y);
    
    printf("Większa liczba to: %d\n", *max_ptr);
    
    return 0;
}
```

#### II. 3. Przykład – funkcja zamieniająca dwie zmienne przez wskaźniki
```c
/*
* Funkcja swap_numbers zamienia wartości dwóch zmiennych typu int
* Argumenty:
*   int *a - wskaźnik do pierwszej liczby
*   int *b - wskaźnik do drugiej liczby
* Zwraca:
*   void - zmienia wartości zmiennych bezpośrednio przez wskaźniki
*/
void swap_numbers(int *a, int *b) {
    int temp = *a;  // zapisujemy wartość spod adresu a
    *a = *b;        // przypisujemy wartość spod b do a
    *b = temp;      // przypisujemy wartość tymczasową do b
}

int main() {
    int x = 10, y = 20;
    
    printf("Przed zamianą: x = %d, y = %d\n", x, y);
    
    swap_numbers(&x, &y);  // przekazujemy adresy zmiennych
    
    printf("Po zamianie: x = %d, y = %d\n", x, y);
    
    return 0;
}
```

#### II. 3. Przykład – praca ze wskaźnikami (deklaracja, przypisanie, dereferencja)
```c
/*
* Funkcja pointer_example demonstruje użycie wskaźnika
* Argumenty:
*   brak - wszystkie zmienne są lokalne
* Zwraca:
*   void - wypisuje dane bez zwracania wartości
*/
void pointer_example() {
    int x = 42;
    int *ptr;       // deklaracja wskaźnika do int
    ptr = &x;       // przypisanie adresu zmiennej x
    
    *ptr = 100;     // zmiana wartości x przez wskaźnik
    
    int val = *ptr; // odczyt wartości spod adresu (dereferencja)
    
    printf("x = %d (po zmianie przez wskaźnik)\n", x);
    printf("val = %d (odczyt przez *ptr)\n", val);
}
```

## II. 4. Tablice

```c
#include <stdio.h>

void array_examples() {
    // Tablica jednowymiarowa - statyczna alokacja
    int numbers[5] = {1, 2, 3, 4, 5}; // Inicjalizacja
    
    // Tablica dwuwymiarowa 2x3 - wiersze x kolumny
    int matrix[2][3] = { {1, 2, 3}, 
                         {4, 5, 6} };
    
    // Wyświetlanie tablicy jednowymiarowej
    printf("Tablica jednowymiarowa:\n");
    for (int i = 0; i < 5; i++) {
        printf("%d ", numbers[i]); // Dostęp przez indeks
    }
    
    // Wyświetlanie tablicy dwuwymiarowej
    printf("\n\nTablica dwuwymiarowa:\n");
    for (int i = 0; i < 2; i++) {        // Pętla po wierszach
        for (int j = 0; j < 3; j++) {    // Pętla po kolumnach
            printf("%d ", matrix[i][j]);  // Dostęp przez 2 indeksy
        }
        printf("\n"); // Nowa linia po każdym wierszu
    }
    
    /* Ważne:
       - Indeksowanie od 0
       - Rozmiar musi być znany w momencie kompilacji (dla statycznych)
       - numbers[5] oznacza dostęp do 6. elementu (UB - undefined behavior) */
}
```

## II. 5. Alokacja dynamiczna

```c
#include <stdio.h>
#include <stdlib.h> // Dla malloc/free

void dynamic_allocation_example() {
    int *array = NULL; // Wskaźnik inicjalizowany NULLem
    int size = 5;
    
    if (array == NULL) { // Sprawdzenie czy alokacja się udała
        printf("Błąd alokacji pamięci!\n");
        return;
    }
    
    // Inicjalizacja tablicy 
    for (int i = 0; i < size; i++) { // przejście po wszystkich elementach tablicy
        array[i] = i * 10; // Dostęp jak do zwykłej tablicy
    }
    
    // Wyświetlanie
    printf("Dynamicznie alokowana tablica:\n");
    for (int i = 0; i < size; i++) {
        printf("%d ", array[i]);
    }
    
    // Zwolnienie pamięci - ABSOLUTNIE KONIECZNE!
    free(array);
    array = NULL; // Dobre praktyki - unikamy dangling pointer
    
    /* Uwaga:
       - malloc nie zeruje pamięci (zawartość losowa)
       - calloc(size, sizeof(int)) - alokuje i zeruje
       - realloc(array, new_size) - zmienia rozmiar istniejącej alokacji */
}
// Przykład tablicy w main
int main(int argc, char *argv[]){

    // Alokacja pamięci dla size intów
    // sizeof(int) - rozmiar typu int w bajtach
    // (int*) - rzutowanie void* na int*
    array = (int *)malloc(size * sizeof(int));

    // Alokacja pamięci na wyniki podwójnej precyzji z wywołaniem rozmiaru tablicy przed uruchomieniem programu
    const int N = atoi(argv[1]); // Pobranie parametru N jako stałej określającej ilość operacji z pierwszego parametru
    
    double *doubleArray = NULL; // Inicjalizowanie wskaźnika NULL'em

    doubleArray = (double *)malloc(N * sizeof(double)); // Utworzenie tablicy typu double zaalokowanej dynamicznie

    if (!doubleArray) {
        printf("Błąd alokacji pamięci\n");
        return 1;
    }
}
```

## II 6. Stringi C-style

```c
#include <stdio.h>
#include <string.h> // Dla funkcji operujących na stringach

void string_examples() {
    // Inicjalizacja stringów
    char str1[] = "Hello"; // Automatyczna alokacja (6 bajtów - +'\0')
    char *str2 = "World";  // Wskaźnik do stałego stringa
    
    // Tablica na wynik operacji
    char buffer[50] = {0}; // Inicjalizacja zerami
    
    // strlen - długość stringa (bez '\0')
    printf("Długość '%s': %lu\n", str1, strlen(str1));
    
    // strcpy - kopiowanie stringów (destination, source)
    strcpy(buffer, str1); // Kopiuje str1 do buffer
    
    // strcat - łączenie stringów (do destination dodaje source)
    strcat(buffer, " ");  // Dodaje spację
    strcat(buffer, str2); // Dodaje str2
    
    // strcmp - porównywanie stringów (0 jeśli równe)
    int cmp = strcmp(str1, str2);
    if (cmp < 0) printf("'%s' < '%s'\n", str1, str2);
    else if (cmp > 0) printf("'%s' > '%s'\n", str1, str2);
    else printf("Stringi są równe\n");
    
    /* Ważne:
       - Stringi kończą się znakiem '\0'
       - Zawsze alokować miejsce na '\0'
       - strncpy/strncat są bezpieczniejsze (ograniczają długość)
       - sprintf(buffer, format, ...) - formatowanie do stringa */
}
```

## II. 7. Struktury

#### II. 7. Przykład
```c
#include <stdio.h>
#include <string.h>

// Definicja struktury (typ złożony)
struct Student {
    int id;          // Pole typu int
    char name[50];   // Pole typu tablica znaków
    float gpa;       // Pole typu float
}; // Uwaga na średnik na końcu!

void structure_example() {
    // Tworzenie struktury - wersja 1
    struct Student student1;
    student1.id = 12345;
    strcpy(student1.name, "Jan Kowalski"); // Dla tablic znaków używamy strcpy
    student1.gpa = 4.5;
    
    // Tworzenie struktury - wersja 2 (inicjalizacja)
    struct Student student2 = {54321, "Anna Nowak", 4.8};
    
    // Dostęp do pól
    printf("Student 1: %d, %s, %.2f\n", 
           student1.id, student1.name, student1.gpa);
    
    // Wskaźnik do struktury
    struct Student *ptr = &student2;
    // Dostęp przez wskaźnik: (*ptr).name lub ptr->name
    printf("Student 2: %s\n", ptr->name);
    
    /* Typedef - tworzenie aliasu typu:
       typedef struct Student Student;
       Teraz można używać: Student student3; */
}
```
#### II. 7. Przykład z funkcją
```c
/*
* Struktura Conversion przechowująca dane potrzebne do wykonania konwersji
*/
struct Conversion {
    double value;           // Wartość do konwersji
    enum UnitConversion type; // Typ konwersji z enumeracji UnitConversion
};

/*
* Funkcja wykonująca konwersję jednostek
* arg:
**  c - wskaźnik do struct Conversion zawierającej wartość i typ konwersji
* return:
**  Wynik konwersji
**  NaN w przypadku nieznanej konwersji
*/
double perform_conversion(struct Conversion *c) {
    switch (c->type) {
        case M_TO_CM:     return c->value * 100;          // metry na centymetry
        case CM_TO_M:     return c->value / 100;          // centymetry na metry
        case KM_TO_MILES: return c->value * 0.621371;     // kilometry na mile
        case MILES_TO_KM: return c->value / 0.621371;     // mile na kilometry
        case INCH_TO_CM:  return c->value * 2.54;         // cale na centymetry
        default:
            printf("Błąd: Nieznana konwersja\n");
            return NAN; // Zwróć "Not a Number" w przypadku błędu
    }
}
int main(int argc, char *argv[]){
    // Pętla wykonująca N konwersji
    for (int i = 0; i < N; i++) {
        struct Conversion c;
        char type_str[20];
        
        printf("\n[%d] Podaj wartość i typ konwersji (np. 100 m_to_cm): ", i + 1);
        if (scanf("%lf %19s", &c.value, type_str) != 2) {
            printf("Błędne dane wejściowe.\n");
            free(results);
            return 1;
        }

        c.type = parse_conversion(type_str);
        if (c.type == INVALID_UNIT) {
            printf("Nieznany typ konwersji: %s\n", type_str);
            free(results);
            return 1;
        }

        results[i] = perform_conversion(&c);
        if (isnan(results[i])) {
            free(results);
            return 1;
        }
    printf("Wynik: ");
    double suma = 0;  // Inicjalizacja zmiennej przechowującej sumę wyników wszystkich operacji
    for (int i = 0; i < N; i++){ // Iteracja po tablicy results celem wydobycia wyników 
        printf("%.5f ", results[i]); // Wypisanie na ekran wyniku dla danej iteracji
        suma += results[i]; // Sumowanie wyników wszystkich operacji
        }

    double avr = suma / N; // Utworzenie zmiennej średniej z operacji na podstawie sumy wyników wszystkich operacji dzielonej przez N-operacji 
    printf("\nŚrednia: %.5f" , avr); // Wypisanie na ekran średniej z wszystkich operacji
    free (results); // Zwolnienie zaalokowanej pamięci dla tablicy results przy poprawnym zakończeniu programu
    }        

return 0; // Prawidłowe zakończenie programu
}
```

## II. 8. Wyliczenia (enum)

```c
#include <stdio.h>
#include <string.h> // dla strcmp
#include <ctype.h>  // dla tolower

/* 
* Definicja typu wyliczeniowego Weekday:
** przypisuje wartości numeryczne dnią tygodnia
* Spsoób wyołania:
* enum Weekday day
* gdzie day to zmienna, która przyjmuje następujące wartości:
*/
enum Weekday {

    MONDAY,      // Gdy MONDAY:    day = 0, dla wywołania: enum Weekday day (Jest to wartość domylśna)
    TUESDAY,     // Gdy TUESDAY:   day = 1, dla wywołania: enum Weekday day
    WEDNESDAY,   // Gdy WEDNESDAY: day = 2, dla wywołania: enum Weekday day
    THURSDAY,    // Gdy THURSDAY:  day = 3, dla wywołania: enum Weekday day
    FRIDAY,      // Gdy FRIDAY:    day = 4, dla wywołania: enum Weekday day
    SATURDAY,    // Gdy SATURDAY:  day = 5, dla wywołania: enum Weekday day
    SUNDAY,      // Gdy SUNDAY:    day = 6, dla wywołania: enum Weekday day
    INVALID_DAY  // Gdy Nieznany:  day = 7, dla wywołania: enum Weekday day
};

/*
* Funkcja zmieniająca dzień tygodnia z enumeracje w string
* arg:
*   enumeracja z zmienną przejmującą wartości wskazujące dzień
* return:
*   Wyniki operacji zależne do case'a:
*   String odpowiadający dniu z enumeracji
*   String "Nieznany dzień" domylśnie (jeżeli wystąpił nieznany dzień poza skalą enumeracji)
*/
const char* get_weekday_name(enum Weekday day) {
    // Switch dla typów wyliczeniowych
    switch (day) {
        case MONDAY:    return "Poniedziałek";
        case TUESDAY:   return "Wtorek";
        case WEDNESDAY: return "Środa";
        case THURSDAY:  return "Czwartek";
        case FRIDAY:    return "Piątek";
        case SATURDAY:  return "Sobota";
        case SUNDAY:    return "Niedziela";
        default:        return "Nieznany dzień";
    }
}

/*
* Funkcja zmieniająca dni tygodnia w postaci tablicy zanków (String C-style) na enumeracje
* arg:
**  day - tablica znaków zawierająca string wprowadzony przez użytkownika
* return:
**  Odpowiadające stringą wartości z enumeratora enum Weekday
*/
enum Weekday parse_weekday_name(const char *day) {
    // Konwersja na małe litery dla porównania bez uwzględniania wielkości
    char lower_day[20];                 // deklaracja tablicy przechowującej string zmieniony na małe litery
    for (int i = 0; day[i]; i++) {      // pętla przechodząca przez wszystkie litery w tablicy (string'u)
        lower_day[i] = tolower(day[i]); // zmiejszenie litery w aktualnej iteracji
    }
    lower_day[strlen(day)] = '\0';
    // Jeżeli string pod zmienną day jest taki sam jak ten porównywany to strcmp == 0 więc: 
    if (strcmp(lower_day, "poniedziałek") == 0) return MONDAY; // Gdy warunek spełniony zwróć day = MONDAY
    if (strcmp(lower_day, "wtorek") == 0) return TUESDAY;      // ---------------||-------------- = TUESDAY
    if (strcmp(lower_day, "środa") == 0) return WEDNESDAY;     // ---------------||-------------- = WEDNESDAY
    if (strcmp(lower_day, "czwartek") == 0) return THURSDAY;   // ---------------||-------------- = THURSDAY
    if (strcmp(lower_day, "piątek") == 0) return FRIDAY;       // ---------------||-------------- = FRIDAY
    if (strcmp(lower_day, "sobota") == 0) return SATURDAY;     // ---------------||-------------- = SATURDAY
    if (strcmp(lower_day, "niedziela") == 0) return SUNDAY;    // ---------------||-------------- = SUNDAY
    return INVALID_DAY;                                        // Jeżeli żaden ze stringów nie pasował prześlij błąd
}

void enum_example() {
    enum Weekday today = WEDNESDAY; // Zmienna typu enum
    
    printf("Dzisiaj jest %s (wartość: %d)\n", 
           get_weekday_name(today), today);
    
    // Iteracja przez wartości enum
    printf("\nDni tygodnia:\n");
    for (enum Weekday day = MONDAY; day <= SUNDAY; day++) {
        printf("%d: %s\n", day, get_weekday_name(day));
    }
    
}
//Wywałania 
int main() {
    char input[20]; // Inicjalizacja tablicy znaków na dane z klawiatury
    printf("Podaj dzień tygodnia: ");
    scanf("%19s", input); // %19s aby uniknąć przepełnienia bufora

    enum Weekday day = parse_weekday_name(input);

    if (day == INVALID_DAY) {
        printf("Nieznany dzień: %s\n", input);
        printf("Dostępne dni to: Poniedziałek, Wtorek, Środa, Czwartek, Piątek, Sobota, Niedziela\n");
        return 1;
    }

    printf("Wybrany dzień to: %s (wartość enum: %d)\n", get_weekday_name(day), day);

    return 0;
}
    /* Uwagi:
       - Wartości enum to po prostu liczby całkowite
       - Można ręcznie przypisać wartości: enum { JAN=1, FEB, MAR };
       - enum class w C++ jest bezpieczniejszy */
```


### III. 4. Assembler NASM (x86_64)

Assembler to niskopoziomowy język programowania, który jest bardzo bliski kodowi maszynowemu. NASM (Netwide Assembler) jest popularnym asemblerem dla architektury x86 (w tym x86_64). Format `elf64` jest używany w systemach Linux 64-bitowych.

#### III. 4. 1. Rejestry i kolejność przekazywania argumentów (System V AMD64 ABI)

W architekturze x86_64, przy wywoływaniu funkcji (konwencja System V AMD64 ABI, używana m.in. w Linuxie):

| Typ Argumentu/Wartości                               | Rejestry                                   |
| :--------------------------------------------------- | :----------------------------------------- |
| Argumenty całkowitoliczbowe lub wskaźniki            | `RDI`, `RSI`, `RDX`, `RCX`, `R8`, `R9`     |
| Argumenty zmiennoprzecinkowe (pierwsze 8)            | `XMM0` - `XMM7`                            |
| Wartość zwracana całkowitoliczbowa lub wskaźnik      | `RAX`                                      |
| Wartość zwracana zmiennoprzecinkowa                  | `XMM0`                                     |

* **Rejestry, które funkcja wołana może dowolnie modyfikować (caller-saved):**
    * `RAX`, `RCX`, `RDX`, `RSI`, `RDI`, `R8`, `R9`, `R10`, `R11`
    * Rejestry `XMM0` - `XMM15` (i `YMM`/`ZMM` jeśli używane)
* **Rejestry, których wartości funkcja wołana musi zachować (callee-saved):**
    * `RBX`, `RBP`, `RSP`, `R12`, `R13`, `R14`, `R15`
    * Jeśli funkcja ich używa, musi zapisać ich oryginalne wartości na stosie i przywrócić przed powrotem.
* `RSP`: Wskaźnik stosu.
* `RBP`: Wskaźnik bazowy ramki stosu (często używany, ale można go pominąć w prostych funkcjach).

#### III. 4. 2. Podstawowe Instrukcje Sterowania Przepływem w NASM

Poniższe instrukcje służą do kontrolowania kolejności wykonywania rozkazów w programie.

##### `call` - Wywołanie procedury
* **Działanie:** Wykonuje wywołanie procedury (funkcji)[cite: 2]. Polecenie to powoduje umieszczenie na stosie adresu następnego rozkazu (tego, który następuje zaraz po tej instrukcji) i przekazuje sterowanie programem do określonego przez operand miejsca[cite: 3].
* **Typy wywołań:**
    * **Bliskie (near call):** Na stosie umieszczany jest sam adres powrotu[cite: 5]. Jest to domyślny typ w płaskim modelu pamięci używanym przez systemy operacyjne Windows i Linux[cite: 6].
    * **Odległe (far call):** Jeśli procedura nie występuje w tym samym segmencie co jej wywołanie, na stosie umieszczany jest segment i adres rozkazu po `call`[cite: 4].
* **Operand (`A`):** Etykieta lub adres procedury zawarty w rejestrze lub komórce pamięci[cite: 7].
* **Przykład:**
    ```nasm
    call moja_procedura
    ```
    [cite: 7]

##### `ret`, `retn`, `retf` - Powrót z procedury
* **Działanie:** Instrukcja ta wykonuje powrót z procedury[cite: 13]. Polega to na zdjęciu ze stosu adresu powrotu umieszczonego przez polecenie `call`[cite: 13].
* **Warianty:**
    * `retn`: Służy do tzw. bliskiego powrotu (zdejmuje jedynie wartość rejestru IP/RIP)[cite: 14].
    * `retf`: Służy do odległego powrotu (najpierw zdejmowana jest wartość rejestru IP/RIP, potem CS)[cite: 14].
    * `ret`: Może być typu zarówno bliskiego jak i odległego, w zależności od tego, jak została zdefiniowana procedura, z której się powraca[cite: 15].
* **Opcjonalny operand (`A`):** Wszystkie trzy rozkazy opcjonalnie przyjmują jeden 8-bitowy operand bezpośredni (liczbę), który nakazuje procesorowi dodanie odpowiedniej ilości bajtów do rejestru wskaźnika stosu (`SP`/`RSP`) *po* zdjęciu adresu powrotnego[cite: 16, 17]. Służy to do usunięcia argumentów przekazanych przez stos (częściej spotykane w konwencjach 32-bitowych jak `stdcall` lub `cdecl` gdy funkcja wołana sprząta stos). W konwencji System V AMD64 ABI (Linux 64-bit) argumenty są przekazywane przez rejestry, więc ta forma `ret` jest rzadziej używana do czyszczenia argumentów.
* **Przykład:**
    ```nasm
    ret 4  ; Zdejmij adres powrotu, następnie dodaj 4 do RSP
    ```
    [cite: 17]

##### `jmp` - Skok bezwarunkowy
* **Działanie:** Polecenie wykonuje bezwarunkowy skok do etykiety[cite: 8].
* **Typy etykiet (operandu `A`):**
    * **short:** Skok o -128 do +127 bajtów od aktualnego położenia[cite: 8].
    * **near:** Skok w obrębie aktualnego segmentu kodu[cite: 8]. W płaskim modelu pamięci x86_64 jest to najczęstszy typ.
    * **far:** Skok do innego segmentu[cite: 8]. Rzadziej używane w nowoczesnych systemach operacyjnych z płaskim modelem pamięci.
* Instrukcja ta przyjmuje tylko jeden operand, którym jest etykieta, do której ma być wykonany skok[cite: 9].
* **Przykład:**
    ```nasm
    jmp etykieta_docelowa
    ```
    [cite: 10]

##### `jWarunek` - Skoki warunkowe
* **Działanie:** Wykonują skok do etykiety tylko wtedy, jeśli dany warunek (zależny od stanu flag procesora) jest spełniony[cite: 11].
* **Przykład:**
    ```nasm
    cmp rax, 0      ; Porównaj rax z 0 (ustawia flagi)
    jz jest_zero    ; Skocz do etykiety 'jest_zero' jeśli rax był równy 0 (ZF=1)
    ; ... kod jeśli nie jest zero
    jest_zero:
    ; ... kod jeśli jest zero
    ```
    [cite: 11]

* **Tabela Skoków Warunkowych:**

    | Mnemonik | Angielski (rozwinięcie skrótu)           | Skok (po polsku),                                   | Warunek (Flagi)            |
    | :------- | :--------------------------------------- | :-------------------------------------------------- | :------------------------- |
    | `JZ`     | Jump if Zero                             | Skok, jeśli zero                                    | $ZF=1$                     |
    | `JE`     | Jump if Equal                            | Skok, jeśli równe                                   | $ZF=1$                     |
    | `JNZ`    | Jump if Not Zero                         | Skok, jeśli nie zero                                | $ZF=0$ ($ZF=0$)            |
    | `JNE`    | Jump if Not Equal                        | Skok, jeśli nie równe                               | $ZF=0$ ($ZF=0$)            |
    | `JA`     | Jump if Above (unsigned)                 | Skok, jeśli większe (bez znaku)                     | $CF=0$ i $ZF=0$            |
    | `JNBE`   | Jump if Not Below or Equal (unsigned)    | Skok, jeśli nie mniejsze lub równe (bez znaku)      | $CF=0$ i $ZF=0$            |
    | `JNA`    | Jump if Not Above (unsigned)             | Skok, jeśli nie większe (bez znaku)                 | $CF=1$ lub $ZF=1$          |
    | `JBE`    | Jump if Below or Equal (unsigned)        | Skok, jeśli mniejsze lub równe (bez znaku)          | $CF=1$ lub $ZF=1$          |
    | `JB`     | Jump if Below (unsigned)                 | Skok, jeśli mniejsze (bez znaku)                    | $CF=1$                     |
    | `JNAE`   | Jump if Not Above or Equal (unsigned)    | Skok, jeśli nie większe lub równe (bez znaku)       | $CF=1$                     |
    | `JC`     | Jump if Carry                            | Skok, jeśli jest przeniesienie                      | $CF=1$                     |
    | `JNB`    | Jump if Not Below (unsigned)             | Skok, jeśli nie mniejsze (bez znaku)                | $CF=0$                     |
    | `JAE`    | Jump if Above or Equal (unsigned)        | Skok, jeśli większe lub równe (bez znaku)           | $CF=0$                     |
    | `JNC`    | Jump if No Carry                         | Skok, jeśli nie ma przeniesienia                    | $CF=0$                     |
    | `JG`     | Jump if Greater (signed)                 | Skok, jeśli większe (ze znakiem)                    | $ZF=0$ i $SF=OF$ ($ZF=C$ i $SF=OF$) |
    | `JNLE`   | Jump if Not Less or Equal (signed)       | Skok, jeśli nie mniejsze lub równe (ze znakiem)     | $ZF=0$ i $SF=OF$ ($ZF=C$ i $SF=OF$) |
    | `JNG`    | Jump if Not Greater (signed)             | Skok, jeśli nie większe (ze znakiem)                | $ZF=1$ lub $SF \neq OF$ ($ZF=1$ lub $SF<>OF$) |
    | `JLE`    | Jump if Less or Equal (signed)           | Skok, jeśli mniejsze lub równe (ze znakiem)         | $ZF=1$ lub $SF \neq OF$ ($SF<>OF$)  |
    | `JL`     | Jump if Less (signed)                    | Skok, jeśli mniejsze (ze znakiem)                   | $SF \neq OF$ ($SF<>OF$)    |
    | `JNGE`   | Jump if Not Greater or Equal (signed)    | Skok, jeśli nie większe lub równe (ze znakiem)      | $SF \neq OF$ ($SF<>OF$)    |
    | `JNL`    | Jump if Not Less (signed)                | Skok, jeśli nie mniejsze (ze znakiem)               | $SF=OF$                    |
    | `JGE`    | Jump if Greater or Equal (signed)        | Skok, jeśli większe lub równe (ze znakiem)          | $SF=OF$                    |
    | `JCXZ`   | Jump if CX is Zero                       | Skok, jeśli rejestr $CX=0$                          | $CX=0$                     |
    | `JECXZ`  | Jump if ECX is Zero                      | Skok, jeśli rejestr $ECX=0$                         | $ECX=0$                    |
    |          | (W x86_64 używa się `JRCXZ` dla `RCX=0`) | Skok, jeśli rejestr $RCX=0$                         | $RCX=0$                    |
    | `JP`     | Jump if Parity                           | Skok, jeśli parzystość                              | $PF=1$                     |
    | `JPE`    | Jump if Parity Even                      | Skok, jeśli parzystość (parzysta liczba bitów '1')  | $PF=1$                     |
    | `JNP`    | Jump if No Parity                        | Skok, jeśli nieparzystość                           | $PF=0$                     |
    | `JPO`    | Jump if Parity Odd                       | Skok, jeśli nieparzystość (nieparzysta liczba bitów '1') | $PF=0$                |
    | `JO`     | Jump if Overflow                         | Skok, jeśli przepełnienie                           | $OF=1$                     |
    | `JNO`    | Jump if No Overflow                      | Skok, jeśli nie ma przepełnienia                    | $OF=0$                     |
    | `JS`     | Jump if Sign                             | Skok, jeśli znak (ujemny)                           | $SF=1$                     |
    | `JNS`    | Jump if No Sign                          | Skok, jeśli nie ma znaku (dodatni)                  | $SF=0$                     |


##### Flagi Procesora Używane w Skokach Warunkowych

Skoki warunkowe działają na podstawie stanu flag w rejestrze flag procesora (np. `EFLAGS` w x86, `RFLAGS` w x86_64). Flagi te są ustawiane przez większość instrukcji arytmetycznych i logicznych, a także przez instrukcje porównania (`CMP`, `TEST`).

| Flaga | Nazwa Angielska | Nazwa Polska        | Opis                                                                                                |
| :---- | :-------------- | :------------------ | :-------------------------------------------------------------------------------------------------- |
| `ZF`  | Zero Flag       | Flaga Zera          | Ustawiana na 1, jeśli wynik ostatniej operacji był równy zero; w przeciwnym razie 0.                |
| `CF`  | Carry Flag      | Flaga Przeniesienia | Ustawiana na 1, jeśli operacja arytmetyczna na liczbach bez znaku spowodowała przeniesienie (nadmiar) z najbardziej znaczącego bitu lub pożyczkę do najbardziej znaczącego bitu. |
| `SF`  | Sign Flag       | Flaga Znaku         | Ustawiana na wartość najbardziej znaczącego bitu wyniku operacji (dla liczb ze znakiem: 1 oznacza ujemną, 0 dodatnią). |
| `OF`  | Overflow Flag   | Flaga Nadmiaru      | Ustawiana na 1, jeśli operacja arytmetyczna na liczbach ze znakiem spowodowała nadmiar, tj. wynik nie mieści się w docelowym operandzie i znak wyniku jest niepoprawny. |
| `PF`  | Parity Flag     | Flaga Parzystości   | Ustawiana na 1, jeśli najmniej znaczący bajt wyniku zawiera parzystą liczbę bitów ustawionych na 1; w przeciwnym razie 0. |

#### III. 4. 3. Wywoływanie funkcji zaimplementowanych w asemblerze z poziomu kodu w C

Aby funkcja napisana w NASM była widoczna dla C, musi:
1.  Być zadeklarowana jako `global` w pliku asemblera. Nazwa funkcji w asemblerze jest tą samą nazwą, której użyjemy w C.
2.  Przestrzegać konwencji wołania funkcji (ABI), czyli przyjmować argumenty w odpowiednich rejestrach (`RDI`, `RSI`, itd.) i zwracać wynik w `RAX` (lub `XMM0`).
3.  Zachowywać wartości rejestrów callee-saved (`RBX`, `RBP`, `R12`-`R15`), jeśli ich używa (poprzez zapisanie ich na stosie na początku funkcji i przywrócenie przed `ret`).

**Plik `asm_funkcje.asm`:**
```nasm
section .text
    global asm_prosta_funkcja

; Funkcja przyjmuje int w RDI, zwraca RDI + 5 w RAX
asm_prosta_funkcja:
    mov rax, rdi    ; Kopiuj argument z RDI do RAX
    add rax, 5      ; Dodaj 5 do RAX
    ret             ; Powrót, wynik w RAX
```

**Plik `main_asm.c`:**
```c
#include <stdio.h>

// Deklaracja funkcji zdefiniowanej w asemblerze
extern int asm_prosta_funkcja(int a);

int main() {
    int x = 10;
    int wynik;

    wynik = asm_prosta_funkcja(x);
    printf("Wynik z ASM dla %d to %d\n", x, wynik); // Oczekiwany wynik: 15

    return 0;
}
```

**Kompilacja i linkowanie (np. w Makefile):**
1.  Skompiluj plik asemblera do pliku obiektowego:
    `nasm -f elf64 asm_funkcje.asm -o asm_funkcje.o`
2.  Skompiluj plik C do pliku obiektowego:
    `gcc -c main_asm.c -o main_asm.o -Wall -Wextra -std=c11 -g`
3.  Zlinkuj pliki obiektowe w program wykonywalny:
    `gcc main_asm.o asm_funkcje.o -o program_z_asm`

---

#### **IV. Organizacja projektu**  
##### **IV. 1. Podział na pliki `.c` i `.h`**  
- **Nagłówki (`.h`)** – zawierają deklaracje funkcji, struktur i makr.  
- **Implementacje (`.c`)** – definiują logikę funkcji.  
- **Include guard** – chroni przed wielokrotnym dołączeniem:  
  ```c
  #ifndef NAZWA_PLIKU_H  
  #define NAZWA_PLIKU_H  
  // Kod  
  #endif  
  ```  

##### **IV. 2. Makefile i CMake**  

##  **Podstawowe elementy `Makefile`**

### 🔹 `CC` — kompilator

```makefile
CC = gcc
```

Określa, którego kompilatora używać (np. `gcc`, `clang`).

---

### 🔹 `CFLAGS` — flagi kompilatora

```makefile
CFLAGS = -Wall -Wextra -pedantic -std=c11
```

* `-Wall` – włącz wszystkie ważne ostrzeżenia
* `-Wextra` – dodatkowe ostrzeżenia
* `-pedantic` – wymuszaj standard języka
* `-std=c11` – użyj standardu C11

---

### 🔹 `SRC`, `OBJ`, `TARGET` — zmienne z plikami

```makefile
SRC = main.c stack.c
OBJ = $(SRC:.c=.o)
TARGET = program
```

* `SRC` — pliki źródłowe
* `OBJ` — odpowiadające im pliki obiektowe (`.o`)
* `TARGET` — nazwa programu wynikowego

---

##  **Reguły w Makefile**

### 🔹 Reguła domyślna (`all`)

```makefile
all: $(TARGET)
```

Domyślna reguła wykonywana przy `make`.

---

### 🔹 Reguła linkowania

```makefile
$(TARGET): $(OBJ)
	$(CC) $(CFLAGS) -o $@ $^
```

Tworzy plik wynikowy z plików `.o`.

* `$@` – oznacza nazwę celu (tu: `program`)
* `$^` – lista zależności (tu: wszystkie `.o`)

---

### 🔹 Reguła kompilowania pojedynczego `.c` do `.o`

```makefile
%.o: %.c
	$(CC) $(CFLAGS) -c $<
```

* `%.o: %.c` — wzorzec dla reguły (każdy `.c` → `.o`)
* `$<` – oznacza pierwszy plik zależny (tu: `.c`)

---

### 🔹 Reguła czyszczenia (`clean`)

```makefile
clean:
	rm -f *.o $(TARGET)
```

Czyści pliki tymczasowe. Uruchamiasz komendą:

```bash
make clean
```

---

## **Przykład pełnego Makefile**

```makefile
CC = gcc
CFLAGS = -Wall -Wextra -pedantic -std=c11

SRC = main.c stack.c
OBJ = $(SRC:.c=.o)
TARGET = program

all: $(TARGET)

$(TARGET): $(OBJ)
	$(CC) $(CFLAGS) -o $@ $^

%.o: %.c
	$(CC) $(CFLAGS) -c $<

clean:
	rm -f *.o $(TARGET)
```

---

##  **Najczęstsze zmienne specjalne w Makefile**

| Zmienna | Znaczenie                         |
| ------- | --------------------------------- |
| `$@`    | Cel (target)                      |
| `$<`    | Pierwsza zależność (np. `main.c`) |
| `$^`    | Wszystkie zależności              |
| `$?`    | Tylko zmienione zależności        |

---
