# Notatka z języka C

## Spis treści
- [I. Kompilowanie programu](#i-kompilowanie-programu)
- [II. Zagadnienia języka C](#ii-zagadnienia-związane-z-językiem-c)
    - [Argumenty wejściowe](#ii-1-argumenty-wejściowe-int-argc-char-argv)
    - [Printf i scanf](#ii-2-printf-oraz-scanf)
    - [Funkcje i wskaźniki](#ii-3-funkcje-i-wskaźniki)
    - [Tablice](#ii-4-tablice)
    - [Alokacja dynamiczna](#ii-5-alokacja-dynamiczna)
    - [Stringi](#ii-6-stringi-c-style)
    - [Struktury](#ii-7-struktury)
    - [Wyliczenia (enum)](#ii-8-wyliczenia-enum)


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