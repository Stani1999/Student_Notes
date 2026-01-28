# Programowanie Obiektowe I (Semestr III)

## 2025-10-08 - Wprowadzenie do programowania obiektowego

### Elementy programowania obiektowego

Element         | Opis
--------------- | --------------------------------------------------------------------------------
Obiekt          | Instancja klasy reprezentująca konkretne dane i zachowania
Klasa           | Szablon definiujący strukturę i zachowanie obiektów (metody i funkcje)
Abstrakcja      | Ukrywanie szczegółów implementacji i eksponowanie tylko niezbędnych cech obiektu
Dziedziczenie   | Mechanizm pozwalający na tworzenie nowych klas na podstawie istniejących
Polimorfizm     | Możliwość używania jednej nazwy metody dla różnych implementacji

### Budowa klasy

Element              | Opis
-------------------- | ------------------------------------------------------------------------
Atrybuty             | Zmienne przechowujące stan obiektu
Konstruktor          | Specjalna metoda wywoływana podczas tworzenia obiektu
Metody               | Funkcje definiujące zachowanie obiektu (settery, gettery, inne funkcje)
Modyfikatory dostępu | Określają widoczność atrybutów i metod (public, private, protected)

### Elementy środowiska Java

Skrót | Rozwinięcie              | Opis
----- | ------------------------ | ------------------------------------------------
JKD   | Java Development Kit     | zestaw narzędzi do tworzenia aplikacji w Javie
JRE   | Java Runtime Environment | środowisko uruchomieniowe dla aplikacji Java
JVM   | Java Virtual Machine     | wirtualna maszyna uruchamiająca kod bajtowy Javy

### Środowiska programistyczne (IDE)

Nazwa         | Opis
------------- | ------------------------------------------------
IntelliJ IDEA | Popularne IDE do programowania w Javie, oferujące zaawansowane funkcje
Eclipse       | Otwarte IDE z szerokim wsparciem dla różnych języków
NetBeans      | IDE zintegrowane z narzędziami do tworzenia aplikacji webowych plus, że pobiera sam program JDK

- **Ważne**: Kompilatory Javy podczas procesu kompilacji zostawiają w pliku binarnym rodzaj "znaku wodnego" <br>z informacją o licencji twórcy.

### Podstawy GUI (Swing)

Komponent | Opis i składnia
--------- | ---------------------------------------------------------------------------------------------------
JFrame    | Podstawowe okno aplikacji graficznej.
JButton   | Przycisk. Składnia: JButton(x, y, xdelta, ydelta) <br>określa położenie (x,y) oraz wymiary (szerokość, wysokość).

---

## 2025-10-15 - Język Java - podstawy

### Przykładowe operacje na danych

Funkcja / pojęcie | Opis
----------------- | ------------------------------------------------------
trim()            | Usuwa białe znaki z początku i końca łańcucha znaków
round()           | Zaokrągla liczbę do najbliższej wartości całkowitej
Java enumerated   | Typ wyliczeniowy

### Wartości specjalne i obiekty w Javie

Pojęcie       | Opis
------------- | ----------------------------------------------------------------------------------
`null`        | Wartość oznaczająca brak referencji do obiektu (obiekt nie jest z niczym powiązany)
`NaN`         | "Not a Number" - reprezentuje wartość, która nie jest liczbą
`infinity`    | Reprezentuje nieskończoność w obliczeniach
Wrapper Class | Klasy opakowujące typy proste (np. Integer, Double)

### Wejścia i wyjścia danych w Javie

Element  | Opis
-------- | -----------------------------------------------------------------------------------
Scanner  | Klasa do odczytu danych wejściowych z różnych źródeł (np. klawiatura)
System   | Klasa wbudowana do obsługi wejścia/wyjścia (System.in, System.out)
Console  | Metoda umożliwaijąca wprowadzaie danych bez wyświetlania ich na ekranie (np. hasła)

### Formatowanie wyjścia

Element   | Opis
--------- | --------------------------------------------------------------------
printf()  | Bardziej zaawansowany niż `cin` z C++, umożliwia formatowanie tekstu
Znaczniki | Specjalne symbole używane w `printf()` do określania formatu (np. %d, %f, %s)

### Sterowanie przepływem programu

Pojęcie                              | Opis
------------------------------------ | --------------------------------------------------------------------------
Zasięg blokowy (scope)               | Określony przez `{ }` – decyduje o widoczności zmiennych i instrukcji
Instrukcja warunkowa półpełna        | `if (warunek) { // kod }`
Instrukcja warunkowa pełna           | `if (warunek) { // kod } else { // kod }`
Instrukcje przerywające (Breakpoint) | `break;` (wyjście z pętli)
Instrukcje kontynuujące              | `continue;` (przejście do następnej iteracji)
Instrukcja wielokrotnego wyboru      | `switch (zmienna) { case wartość1: // kod;`<br>`break; ...`<br>`default: // kod; }`

---

## 2025-10-22 - Omówienie języka Java

### Cechy języka Java

Cechy                            | Opis
-------------------------------- | ------------------------------------------------------------------------
Java jako obiekt                 | Została napisana od zera jako obiektowy język programowania
Prosty                           | Brak wskaźników, automatyczne zarządzanie pamięcią (Garbage Collector)
Zorientowany obiektowo           | Zasada "wszystko jest obiektem"
Jest sieciowy                    | Można zbudować architekturę klient – serwer (java.net)
Jest niezawodny (Robust)         | Kładzie duży nacisk na sprawdzanie błędów na etapie kompilacji i uruchomienia
Jest bezpieczny                  | Kod jest weryfikowany przez JVM przed wykonaniem
Niezależny od architektury       | Zasada WORA (Write Once, Run Anywhere) - przenoszalna
Interpretowany                   | Nie jest trudny w nauczeniu aby zrozumieć <br>Interpreter Javy może wykonać każdy kod binarny…
Jest wysokowydajny, wielowątkowy | Potrafi sobie poradzić z wielordzeniowym procesorem
Jest dynamiczny                  | Potrafi doładowywać klasy w czasie rzeczywistym (runtime)
Referecnje (Bezpieczny wskaźnik) | Wydzielony obszar pamięci na obiekty, który jest nie do ruszenia<br> Każda pruba dostępu do pamięci jest kontrolowana
Dynamiczne rezerwowanie pamięci  | Przez co może "zamulać" sprzęt o małej ilości RAMu
Java jest stosunkowo niewielka   | Pomyślana dla małych urządzeń np. do zegarka
Garbage Collector                | Automatyczne zarządzanie pamięcią <br>Zwalnianie nieużywanych obiektów
Stosunkowo szybki <br>język programowania | W porównaiu do innych języków interpretowanych <br>Wolniejsza od języka C np. przy komunbikacji sieciowej <br>W niektórych przypadkach pojawia się z latencją (nie ma tego w C)
JNI - Java Native Interface      | Może kożystać z bibliotek napisanych w innych językach np. C/C++
Automatyczne pobierane  klas     | Środowiska wysokoprogramowe mogą automatycznie pobierać klasy z sieci <br>nawet w trakcie pisania programu
Kompilacja JIT - Just In Time    | Maszyna wirtualna może wykonywać kompilację "w locie" podczas Runtime'u
Plik binarny tworzony od razu    | W przypadku IntelliJ IDEA i Java
Jest bazą dla innych technologii | Android Studio Kotlin uruchamia się na środowisku Javy pod spodem
Wszechstronność interfejsu GUI   | Aplikacje desktopowe (graficzne): Swing, JavaFX, AWT <br>Zarządzanie projektem: Maven - środowisko działające w trybie konsoli
Współpraca z bazami danychq      | Najlepiej działa z Oracle (Oracle XE – darmowa wersja),<br>Wspiera też starsze bazy danych takie jak DB2
Zaawansowany przepływ sterowania | Możliwość definiowania przerwania pętli (etykiety) nawet przy jej zapętleniu
Obsługa wielkich liczb           | Klasy BigInteger i BigDecimal – precyzyjne obliczenia na bardzo dużych liczbach
API Stream                       |  Nowoczesne przetwarzanie danych (strumienie) do środowiska graficznego, <br>którego brakuje w standardowym języku C

### Tablice w Java

- Słowo kluczowe `new` w Javie służy do dynamicznego alokowania pamięci dla obiektów/klas i tablic

Zagadnienie                | Przykład / Uwagi                  | Opis
-------------------------- | --------------------------------- | -----------------------------------------------------------
Deklaracja                 | `int[] lista;` lub `int lista[];` | Obie formy są poprawne
Powołanie <br>(Alokacja)   | `int[] lista = new int[10];`      | Rezerwacja oktreślonej liczby elementów (tu 10'ciu)
Tablice <br>anonimowe      | `int[] lista = {1, 2, 3, 4, 5};`  | Inicjalizacja tablicy z wartościami bez określania rozmiaru <br>Tablice są więc tworzone dynamicznie
Indeksowanie               | `lista[0] = 1`                    | Indeks pierwszego elementu to 0, ostatniego to n-1
Pętla foreach              | `for (int zmienna : lista)`       | Przeszukuje kolekcje/listy; brak słowa `in`,<br> ze względu na kolizję z `System.in.`<br> Warto dodać tekst aby było wiadomo, że pętla się wykonała<br> Wyświetlanie zmienntch: `System.out.println(zmienna);` <br>Przetwarza elementy listy a nie ich wartości
Kopiowanie <br> tablicy    | `b = lista;`                      | Tworzy referencję do tej samej tablicy (nie kopiuje jej),<br>Działa to tak samo jak w przypadku obiektów/klas
Sortowanie <br> tablicy    | `Arrays.sort(lista);`             | Sortuje tablicę rosnąco (w miejscu) <br>Jest to metoda algorytmu QuickSort
Tablice <br>wielowymiarowe | `int[][] tab2D = new int[3][4];`  | Tworzy tablicę 2D o wymiarach 3x4 <br>Indeksowanie: `tab2D[wiersz][kolumna]` <br> W C występuje tablica wielowymiarowa posiadająca podtablice <br> W Javie tablice wielowymiarowe są tablicami tablic <br> To znaczy, że w Javie nie ma prawdziwych tablic wielowymiarowych,<br>są one symulowane przez tablice tablic
Tablica postrzępiona       | `int[][] tab = { {1,2}, {3,2,1}};`| Tablica, której każda "podtablica" może mieć różną długość <br>I-ta tablica jest częścią Y-tej tablicy, <br>Przykład: `tab[0]` ma 2 elementy, `tab[1]` ma 3 elementy

---

## 2025-10-29 - Obiektowość w Javie

### Relacja Klasa – Obiekt

Pojęcie       | Opis
------------- | ---------------------------------------------------------------------------------------------------
`Klasa`       | Szablon (wzór), z którego tworzy się obiekty. Definiuje wspólne cechy i zachowania
`Obiekt`      | Instancja klasy (konkretny "egzemplarz" stworzony według szablonu)
`Nazewnictwo` | W Javie nazwa pliku **musi** pokrywać się z nazwą klasy publicznej
`Biblioteki`  | Java posiada ogromną liczbę predefiniowanych klas, co pozwala unikać powielania kodu

### Kluczowe cechy obiektów

Cecha          | Opis
-------------- | ---------------------------------------------------------------------------------------------------
**Stan**       | Aktualne wartości pól obiektu (jak obiekt wygląda w danej chwili). Zmienia się w czasie
**Zachowanie** | Definiowane przez metody – określa, jak obiekt reaguje na polecenia i zmienia swój stan
**Tożsamość**  | Unikalność obiektu – sposób, w jaki system odróżnia go od innych instancji tej samej klasy

### Hermetyzacja (Encapsulation)

Pojęcie        | Opis
-------------- | ---------------------------------------------------------------------------------------------------
Definicja      | W przypadku programowania to ukrywanie danych (implementacji) przed użytkownikiem zewnętrznym
Mechanizm      | Grupowanie danych i metod w jednym pakiecie (klasie)
Zasada dostępu | Składowe klasy nie powinny być dostępne bezpośrednio – dostęp tylko przez metody obiektu
Bezpieczeństwo | Obiekt może odmówić wykonania metody (np. nie wyśle pustego zamówienia) <br>Bezpośrednia zmiana pola bez metody to "włamanie" (złamanie hermetyzacji)
Utrzyaminie    | Jeżeli metoda jest uznana za niebezpieczną, to wtedy powinna być napisana od nowa,<br> Użytkownik powinien zaprzestać kożystania z niej (odpowiednia adnotacja `@Deprecated`)

### Rozszerzanie klas i dziedziczenie

Słowo kluczowe | Opis
-------------- | ---------------------------------------------------------------------------------------------------
Dziedziczenie  | Nowa klasa przejmuje wszystkie cechy i metody klasy nadrzędnej
`extends`      | Służy do budowania nowej klasy na podstawie istniejącej (rozszerzanie)
`super`        | Odwołanie do klasy nadrzędnej (np. wywołanie konstruktora klasy bazowej)
Nowe pola      | Metody i pola zdefiniowane w klasie rozszerzonej są dostępne tylko w niej
`@Override`    | Klasa potomna może nadpisać metody klasy bazowej, używając adnotacji `@Override` <br> Nienadpisene metody z klasy bazowej działają bez zmian w klasie potomnej

### Dodatkowe pojęcia i narzędzia

Pojęcie / Narzędzie | Opis
------------------- | ---------------------------------------------------------------------------------------------------
Dezasemblacja       | Proces odwracania kompilacji – zamiana kodu bajtowego z powrotem na formę czytelną dla człowieka.
Netykieta           | Zbiór zasad kulturalnego zachowania w sieci (dotyczy też komunikacji między programistami).
Java Form Designer  | Zalecany dodatek do IDE ułatwiający wizualne projektowanie formularzy i interfejsów GUI.
Main w Javie        | W przeciwieństwie do C, kod Javy opiera się na klasach, a plik musi mieć strukturę klasową.

---

## 2025-11-12 

### Porównanie architektury Proceduralnej i Obiektowej

Aspekt         | Programowanie Proceduralne                      | Programowanie Obiektowe
-------------- | ----------------------------------------------- | ----------------------------------------------
Wymagania      | Kompilator zawsze wymaga jawengo punktu wejścia | Kod opiera się na definicjach klas i ich metod
Punkt startowy | Zaczyna się od funkcji `main()` (góry)          | System współpracujących klas bez sztywnej góry
Struktura      | Sekwencja instrykcji wykonywanych kolejno       | Zbiór obiektów wymieniających się komunikatami 
Zależności     | Funkcje operują bezpośrednio na danych          | Obiekty delegują zadania między sobą <br> Niczym podwykonwcy w firmach zleceniobiorczych <br> Rzadkie jest głębokie zagnieżdżenie klas np. potrójne

### Konwencje nazewnictwa w Javie

Element            | Zasada nazewnictwa | Przykład
------------------ | ------------------ | ---------
Klasa (Class)      | Przeważnie rzeczownik, z wielkiej litert                                           | `Student`, `Auto`
Stała (Constant)   | Wszystkie litery wielkie, słowa oddzielone podkreśleniami                          | `MAX_VALUE`, `PI` 
Zmienne (Variable) | Małe litery, wieloczłonowe z wielką literą na początku każdego członu (camelCase)  | `studentName`, `totalScore`
Metoda (Method)    |Małe litery, wieloczłonowe z wielką literą na początku każdego członu (camelCase)   | `nextLine()`, `getStudentName()`
Interfejs          | Przymiotnik lub rzeczownik, z wielkiej litery                                      | `Comparable`, `Runnable`
Pakiet (Package)   | Małe litery, często odwrócona domena                                               | `com.example.project`

### Relacje między klasami

Relacja                            | Opis                                                        | Przykład                                | Uwagi
---------------------------------- | ----------------------------------------------------------- | ----------------------------------------- | --------------------------
**Zależność**<br>*Użycie*               |  Metody jednej klasy<br>*używają* obiektów drugiej klasy    | Klasa `Zamowienie` używa klasy `Konto`,<br> aby sprawdzić czy klient jest wypłacalny <br> `Produkt` nie jest powiązany z klasą `Konto`,<br> nie potrzebuje ona informacji,<br> do którego klienta należy produkt | Liczbę klas należy minimalizować<br>W oprogramowaniu<br>jest to stopioeń powiązań<br>między klasami: <br>Zmiany w jednej w klasie `B`<br>nie wpływają na klasę `A`
**Agregacja**<br>*Zawiera*             | Klasa *zawiera* inne klasy<br>jako swoje elementy             | `Samochód` *zawiera* `Silnik` | Może to być zwizek tabel
**Asocjacja**<br>*Powiązanie*          | Stały *związek między* klasami                                | Klasa `Student` jest *powiązany* z klasą `Kurs` | *Powiązanie* może być<br>jednokierunkowe lub dwukierunkowe
**Dziedziczenie**<br>*Jest rodzajem* | *Jest* to wyrażenie związku <br>między klasą ogólną a specjalną | Klasa `SzybkieZamowienie` może *dziedziczyć*<br> po klasie `Konto`, metody dotyczące zamówieniń | W Java klasa dziedzicząca może mieć<br>większe możliwości od klasy bazowej

### Diagramy klas języka UML (Unified Modeling Language)

- Diagramy te stosuje się przy projektowaniu i przekazywaniu kodu,<br >aby zwizualizować strukturę systemu bez wchodzenia w detale implementacji


Symbol | Znaczenie                   | Opis 
------ | --------------------------- | ------------------------------------------------------------------------------
—▷    | Dziedziczenie (Inheritance) <br> Generalizacja | Kierunek grotu jest skierowany od podklasy (Subclass) do nadklasy (Superclass) <br> Przykład: Student —▷ Osoba
---▷  | Realizacja (Implementation) | Klasa implementuje interfejs (Interface implementation)
--->   | Zależność (Dependency)     | Luźny związek "używa". Linia przerywana z otwartym grotem
——     | Asocjacja (Association)    | Trwały związek (pole w klasie). Linia ciągła
—>     | Asocjacja skierowana       | Wskazuje kierunek powiązania (np. Klient zna swoje Zamówienie)
—♢     | Agregacja (Aggregation)    | Związek *zawiera*. Części mogą istnieć bez całości
«…»    | Stereotyp (Stereotype)     | Oznaczenie rodzaju klasy lub relacji (np. «include», «extend»)

---

## 2025-11-19

### Klasy predefiniowane w Javie

Element                 | Opis                              | Przykład 
----------------------- | --------------------------------- | -----------------------------------------------------
Klasy predyfinowane     | Gotowe klasy dostarczone z Java   | `String`, `Math`, `ArrayList`
Tworzenie własnej klasy | Najpierw należy sprawdzić, czy klasa istnieje i dopiero wtedy ją tworzyć | `class NazwaKlasy {...}`

### Definiowanie klasy w Javie

Zagadnienie 	| Opis
--------------- | --------------------------------------------------------------------------------
Definicja klasy | Każda klasa zawiera pola, konstruktory i metody
Wiele klas	    | Program może składać się z więcej niż jednej klasy
Klasa główna    | Zawsze musi istnieć jedna klasa z metodą main 

### Prosta struktura klasy

Element	    | Opis                         | Cechy i Właściwości
----------- | ---------------------------- | --------------------------------------------------
Nazwa klasy | Identyfikator klasy          | Zaczyna się z wielkiej litury najlepiej CamelCase
Pola	    | Przechowują stan obiektu     | Klasa może mieć wiele pól różnego typu
Konstruktor | Inicjalizuje obiekt          | Można tworzyć wiele konstruktorów (przeciążanie)<br>Nazwa konstruktora musi być taka sama jak nazwa klasy
Metody	    | Definiują zachowanie obiektu | Może być ich wiele mogą przyjmować parametry i zwracać wartości

### Mechanizmy kompilacji i wykonania w Java

Kategoria                |Opis mechanizmu / Zasada                                                                                                          
-------------------------|-------------------------------------------------------------------------------------------------------------------------------------
Kompilacja               |Kompilator buduje pliki wyjściowy z rozszerzeniem .class zawierające bytecode<br>dla klasy main oraz każdej innej zdefiniowanej klasy
Zależności               |Zmiana nazwy klasy po kompilacji powoduje błąd przy próbie odwołania,<br> gdyż interpreter nie znajdzie odpowiedniego pliku binatnego
Logowanie                |Zaleca się zapisywanie wszystkich błędów do pliku z logami oraz dodawanie<br> własnych komentarzy do wyjątków
Interpreter              |Interpreter uruchamia najpierw metodę main, a obiekty tworzy dynamicznie<br> dopiero w momencie ich wywołania
Symbole wieloznaczne     |Użycie symbolu `*` pozwala kompilatorowi dopasować i skompilować<br> wszystkie pliki pasujące do wzorca `np import java.util.*;`
Poszukiwanie źródeł      |Jeśli kompilator napotka brakujący plik .class,<br> automatycznie szuka pliku źródłowego .java, aby go skompilować
Aktualizacja             |Kompilator sprawdza sygnatury i daty plików<br> Jeśli wykryje różnice, skompiluje plik ponownie
Optymalizacja            |Klasy, do których nie ma żadnego odwołania (np. przez referencję),<br> nie są poddawane procesowi kompilacji
Składnia                 |Metody powinny zaczynać się małą literą <br> użycie wielkiej litery może zostać potraktowane przez kompilator jako błąd
Zarządzanie pamięcią     |Obiekty w Javie są zawsze przechowywane na stercie (heap)                      
Tworzenie obiektów       |Konstruktor jest wywoływany zawsze przy użyciu operatora `new`,<br> o czym kompilator często sam przypomina
Przesłanianie (Shadowing)|Zmienne lokalne w konstruktorze o tych samych nazwach co pola klasy <br>**"przesłaniają"** te pola, czyniąc je niedostępnymi bez słowa `this`
Debugowanie              |Niezamierzone przesłanianie pól jest trudne do wykrycia,<br>można do zrobić poprzez zastawianie tzw. "pułapek" podczas testowania
### Przykładowa klasa Pracownik

```java
import java.util.Date;
import java.util.GregorianCalendar;


class Pracownik {
    // pola
    private String imie;
    private double waga;
    private int id;
    private Date godzinaUrodzenia;
    private GregorianCalendar dataUrodzenia;


    // konstruktor
    public Pracownik(String s, double w, int i_d, Date hdb, GregorianCalendar bd) {
        // Operator this - Odwołuje się do pola klasy
        this.imie = s;  
        this.waga = w;
        this.id = i_d;
        this.godzinaUrodzenia = hdb;
        this.dataUrodzenia = bd;
    }


    // metody 
    public String getImie() { // get(ter) - Odczytuje wartość pola
        return imie;
    }
        
    public int setWaga(double w) { // set(ter) - Ustawia wartość pola
        this.waga = w;
        return 0;
}
```

---

## 2025-11-26

---

## 2025-12-10

---

## 2025-12-17

---

## 2026-01-14

---

## 2026-01-21

---

## 2026-01-28 - Zaliczenie
