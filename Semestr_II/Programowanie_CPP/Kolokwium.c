#include <stdio.h>    // funkcje wejścia/wyjścia: printf, scanf
#include <stdlib.h>   // funkcje: atoi, malloc, free, sscanf
#include <string.h>   // funkcje do obsługi napisów: strcmp, strcpy
#include <math.h>     // funkcje matematyczne: pow, sqrt
#include <ctype.h>    // funkcja tolower

/* 
* Definicja typu wyliczeniowego Operation:
** Przypisuje wartości numeryczne operacją kalkulatora
* Spsoób wywołania:
**  enum Operation OP
**  gdzie OP to zmienna, która przyjmuje następujące wartości:
*/
enum Operation{
    PLUS,       // Gdy PLUS:  OP = 0, dla: enum Operation OP
    MINUS,      // Gdy MINUS: OP = 1, dla: enum Operation OP
    RAZY,       // Gdy RAZY:  OP = 2, dla: enum Operation OP
    PRZEZ,      // Gdy PRZEZ: OP = 3, dla: enum Operation OP
    DOPOT,      // Gdy DOPOT: OP = 4, dla: enum Operation OP
    INVALID_OP  // Gdy Błąd:  OP = 5, dla: enum Operation OP
};

/*
* Parsowanie argumentu operacji na enumeracje
* arg:
**  op - tablica znaków zawierająca string wprowadzony przez użytkownika
* return:
**  Odpowiadające stringą wartości z enumeratora enum Operation
*/
enum Operation parse_operation(const char *op) {
    
    char lower_op[10]; // deklaracja tablicy przechowującej string zmieniony na małe litery
    for (int i = 0; op[i]; i++) {  // pętla przechodząca przez wszystkie litery w tablicy (string'u)
        lower_op[i] = tolower(op[i]); // zmiejszenie litery w aktualnej iteracji
    }
    lower_op[strlen(op)] = '\0'; // Ręczne dodanie null-terminatora na końcu nowego stringu

    // Jeżeli string pod zmienną op jest taki sam jak ten porównywany to strcmp == 0 więc: 
    if (strcmp(lower_op, "plus") == 0) return PLUS;   // Gdy warunek spełniony zwróć op = PLUS
    if (strcmp(lower_op, "minus") == 0) return MINUS; // --------------||-------------- = MINUS
    if (strcmp(lower_op, "razy") == 0) return RAZY;   // --------------||-------------- = RAZY
    if (strcmp(lower_op, "przez") == 0) return PRZEZ; // --------------||-------------- = PRZEZ
    if (strcmp(lower_op, "do") == 0) return DOPOT;    // --------------||-------------- = DOPT
    return INVALID_OP;                                // Jeżeli żaden ze stringów nie pasował prześlij błąd
}

/*
*Struktuta Calculation przechowująca składniki potrzebne do wykonania operacji 
*/
struct Calculation{

    double x;           // Liczba 1
    double y;           // Liczba 2
    enum Operation OP;  // Odpowiada operacji z typu wyliczeniowego Operation
};

/*
* Funkcja dokonująca obliczeń na podstawie podanej operacji
* arg:
**  Wskaźnik do struct Calculation pod zmienną c 
* return:
**  Wyniki operacji zależne do case'u
**  -1 w przypadku dzielenia przez 0 
**  -2 w przypadku nieokreślonym
*/
double calc(struct Calculation *c){

    switch (c->OP){ // Użycie przeniesienia wskaźnika struktury na element dotyczący enumeracji (c->OP) aby określał przypadki w konstrukcji switch case
        // Przeniesienie wskaźnika struktury na kolejne elementy przechowujące w niej wartości liczbowe (c->x oraz c->y):
        case PLUS: return c->x + c->y;      // Przekazanie wyniku dodawania
        case MINUS: return c->x - c->y;     // Przekazanie wyniku odejmowania
        case RAZY: return c->x * c->y;      // Przekazanie wyniku dodawania
        case PRZEZ:
            if (c->y == 0){                 // Uwzględnienie przypadku dzielenia przez 0 
                printf("BŁĄD: Nie można dzielić przez zero!\n");
                return NAN;                 // Zwróć "Not a Number" (wymaga <math.h>)
            }
            else{
                return c->x / c->y;         // Przekazanie wyniku dzielenia
            }
        case DOPOT: return pow(c->x,c->y);  // Przekazanie wyniku potengowania dzięki funkcjia pow z biblioteki math.h
        default:    return NAN;              // Domylśnie zwróć błąd (gdyby wystąpił nieokreślony przypadek po wywołaniu kosntruckji)
    }
}

/*
* Funkcja display_menu wyświetla się podczas uruchomienia - skrócona instrukcja
* arg:
**   name - nazwa programu 
* return:
**   jako void nie zwraca wartości
*/
void display_menu(char *name){

    printf("Witaj w programie %s\n", name);
    printf("Dla wybranej ilości obliczeń uzupełnij następujące dane N zadanych razy:\n");
    printf("<Liczba_1> <Operacja> <Liczba_2>\n");
    printf("Przyjmowany format liczb 2.5 (kropka zamiast przecinka)\n");
    printf("Dostępne operacje to : plus, minus, razy, przez, do\n");
}

/*
* Funkcja main jako Entry point uruchamia program
* arg:
**  argc - liczba argumentów
**  argv[] - tablica zawierająca argumenty
* return:
**  0 - program zakończony bez błędu
**  1 - program zakończony z błędem 
*/
int main(int argc,char *argv[]){

    if (argc != 2){ // Jeżeli liczba arguentów jest różna od 2 (nazwa programu + parametr liczby operacji N):
        printf ("Program kalkulator wymaga podania dokładnie jednego parametru (ilości obliczeń)\n");
        printf ("Aby wywołać program wprowadź następujące polecenie:\n");
        printf("%s N\n", argv[0]); // argv[0] - przekazanie nazyw programu do komunikatu
        printf("N - to liczba całkowita (typu intiger)");
        return 1;  // W przypadku wystąpienia zakończ z błędem
    }
    display_menu(argv[0]); // argv[0] - przekazanie nazyw programu do funkcji wyświetlającej menu
    const int N = atoi(argv[1]); // Pobranie parametru N jako stałej określającej ilość operacji 
    if (N <= 0) { // Sprawdzenie czy jest więcej iteracji niż 0
        printf("Liczba konwersji musi być większa niż zero.\n");
        return 1;
    }
    double *resoult = NULL; // Inicjalizowanie wskaźnika NULL'em

    resoult = (double *)malloc(N * sizeof(double)); // Utworzenie tablicy typu double zaalokowanej dynamicznie

    for (int i = 0; i < N; i++){ // Iteracja powtarzająca wprowadzenie operacji N-razy
        struct Calculation c;   // Inicjalizacja struktury jako zmienną c
        char operacja[10];     // deklaracja tablicy przechowującej string dla operacji
        printf("Wprowadź dane: ");
        if (scanf("%lf %9s %lf",&c.x, operacja, &c.y) != 3){ // Pobranie argumentów od użytkownik (sprawdzenie czy wprowadzono 3 argumenty)
            printf("Błędny format danych\n");
            printf("Poprawny format to:\n");
            printf("<Liczba_1> <Operacja> <Liczba_2>(kropka zamiast przecinka)\n");
            free(resoult);  // Zwolnienie zaalokowanej pamięci dla resoult
            return 1;       // Zakończenie programu z błędem
        }

        c.OP = parse_operation(operacja); // Parsowanie operacji i przypisanie jej do Operacji ze struktury c
        if (c.OP == INVALID_OP) {         // Jeżeli operacja jest błędna
            printf("Nieznana operacja: %s\n", operacja);
            printf("Dostępne operacje to : plus, minus, razy, przez, do\n");
            free(resoult); // Zwolnij zaalokowaną pamięć 
            return 1;      // Zakończ program z błędem
        }
        resoult[i] = calc(&c);   // Przekazanie wyniku z iteracji do tablicy resoult obliczonego na podstawie przekazania ADRESU (&) struktury
        if (isnan(resoult[i])) { // Sprawdzanie, czy wynik to NaN (dzielenie przez zero)
            free(resoult);       // Jeżeli tak zwolnij zaalokowaną pamięć na tablice resoult
            return 1;            // Zakończ z błędem
        }
    }

    printf("Wynik: ");
    double suma = 0;  // Inicjalizacja zmiennej przechowującej sumę wyników wszystkich operacji
    for (int i = 0; i < N; i++){ // Iteracja po tablicy resoult celem wydobycia wyników 
        printf("%.5f ", resoult[i]); // Wypisanie na ekran wyniku dla danej iteracji
        suma += resoult[i]; // Sumowanie wyników wszystkich operacji
    }

    double avr = suma / N; // Utworzenie zmiennej średniej z operacji na podstawie sumy wyników wszystkich operacji dzielonej przez N-operacji 
    printf("\nŚrednia: %.5f" , avr); // Wypisanie na ekran średniej z wszystkich operacji
    free (resoult); // Zwolnienie zaalokowanej pamięci dla tablicy resoult przy poprawnym zakończeniu programu

return 0; // Prawidłowe zakończenie programu

}
