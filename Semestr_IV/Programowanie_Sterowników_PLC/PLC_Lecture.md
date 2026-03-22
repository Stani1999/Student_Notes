# **Programowanie Sterowników PLC**
## **2026-02-24 Wykład I**

### **I. 1. Organizacyjna**

**Zasada**          | **Opis**                               | **Uwagi**
------------------- | -------------------------------------- | -----------------------------------
**Podziału grupy**  | Sala posiada 6 stanowisk komputerowych | Każda grupa<br> dzieli się na 6 podgrup
**Ocena z ćwiczeń** | Wejściówki z poprzednich ćwiczeń       | Brak instrukcji,<br> zajęcia komputerowe
**Ocena z wykładu** | Kolokwia w trakcie trwania semestru    | I Kolokwium w połowie,<br> II Kolokwium na koniec

### **I. 2. Fundamenty sterowania**

**Element**                 | **Charakterystyka**                                                        | **Logika i budowa**
--------------------------- | -------------------------------------------------------------------------- | -------------------
**Przekaźnik**              | Służy do wyłączania i włączanie pojedynczego toru prądowego                | Sterowanie fizyczne (elektromagnetyczne)
**Stycznik**                | "Rozbudowany przekaźnik" do wielu torów prądowych (większe moce)           | Budowa zbliżona do przekaźnika,<br> ale z większą ilością styków
**Układy klasyczne**        | Połączenie przekaźników i styczników <br> Dobre dla prostych małych maszyn | *Wady* - duża ilość elementów, <br> skomplikowane okablowanie, <br> trudna diagnostyka
**Przekaźnik progrmowalny** | Podstawowy poziom cyfryzacji (tzw. sterownik "logo")                       | Logika zaszyta w **prostym programie**,<br> ograniczonym do liczby wejść i wyjść (I/O)
**Sterownik PLC**           | Zaawansowane urządzenie mikroprocesorowe do dużych systemów                | Logika "przerzucona" do procesora <br> 

### **I. 3. Model działania i komunikacja rozproszona**

**Zagadnienie** | **Opis**                                                            | **Wyjaśnienie**
--------------- | ------------------------------------------------------------------- | ----------------
**Cykl pracy**  | Pętla zamknięta, <br> generowanie wyjść na podstawie wejść          | Wykonywany w powtarzalnych odstępach czasu,<br> zmienna długość cyklu <br> uniemożliwia pełną synchroniczność
**Próbkowanie** | To sposób, w jaki sterownik "widzi" świat (stany) wewnątrz cyklu    | Sporadyczne sprawdzenia stanów wejść i aktualizacji wyjść
**Brak ciągłości** | Fizyczny skutek próbkowania                                      | Wprowadza opóźnienia odczytu do reakcji
**Pozorny czas rzeczywisty** | Wynik bardzo szybkiego cyklu pracy                     | Milisekundowe opóźnienia, <br> praktycznie niezauważalne dla ludzkiego oka
**System DCS**  | To przykład systemu rozproszonego <br> Distributed Control System   | Stosowany w dużych zakładach <br> gdzie kontrolery rozproszone są po całym obiekcie, <br> system spięty siecią komunikacyjną
**Zdalne I/O**  | Czyjniki i inne elementy oddalone od siebie                         | Połączone medium komunikacyjnym <br> umożliwiający odczyt stanu i wysterowania

### **I. 4. Technologie i protokoły komunikacyjne**

**Standard**     | **Opis**  | **Zastosowanie, cecha**
---------------- | --------- | ---------------
**Modbus**       | Najstarszy i najprostszy standard przesyłania danych | Wykorzystuje porty szeregowe "przetrwał do dziś i ma się dobrze"
**Profibus**     | Standard firmy Simens                                | "Bardziej zaawansowany Modbus" 
**Can (CANbus)** | Sieć dwużyłowa, odporna na zakłócenia                | Standardowo wykorzystywana w motoryzacji
**HART**         | Protokół do zdalnej konfiguracji urządzeń            | Umożliwia strojenie i diagnostykę czujników
**Ethernet**     | Technologia sukcesywnie wypierająca starsze łącza    | Wprowadzane z opóźnieniem ze względu na konieczność zapernienia niezawodności
**Profinet**     | Standard firmy Simens<br> oparty na łączu Ethernet   | Służy do programowania sterowników<br> przez nadanie im<br> unikatowego adresu IP

### **I. 5. Język drabinkowy (Ladder)**

**Element**                   | **Opis**  | **Zastosowanie, cecha**
----------------------------- | ------------------------------------------------------------------------ | ---------------
**Język drabinkowy (Ladder)** | Przykład języka graficznego                                              | Najbardziej dominujący<br> sposób programowania PLC
**Kierunek czytania**         | Od lewej do prawej <br>, od góry do dołu                                 | Wyznacza kolejność w jakiej <br> sterownik analizuje logikę programu
**Cewka przekaźnika**         | Zastępowana<br> symbolami `O` lub `( )`                                      | Łatwo w taki sposób<br> narysować logikę
**NO (Normally Open)**        | `\| \|` - Zestyk zwierny                                                 | Przewodzi prąd,<br> gdy wejście jest aktywne
**NC (Normally Closed)**      | `\|/\|` - Zestyk rozwierny                                               | Przewodzi prąd,<br> gdy nie jest pobudzony
**Rodzaje cewek**             | Cewka ustawienia <br> `(S)` od `Set`, <br> Cewka resetowania <br> `(R)` od `Reset` | Umożliwiają tworzenie pamięci stanu, <br> za cewkami mogą być tylko inne cewki
**Paradygmat**                | Cewki typu `(S)` i `(R)`<br> tworzyć na zmiennych pomocniczych | Niezalecane bezpośrednio na wyjściach (błąd w sztuce),<br> lepiej interpretować: "jeżeli nie uruchomione, to uruchom"
**Budowa**                    | Oparta na koncepcji przekażników                                         | Programowe odwzorowanie klasycznej automatyki stycznikowej
**FBD**                       | Function Block Diagram                                                   | Alternatywny język graficzny, <br> firmy Simens

### **I. 6. Architektura wewnętrzna**

**Element**          | **Opis**  | **Zastosowanie, cecha**
-------------------- | --------- | ---------------
**Mikrokontroler**   | Układ scalony mający wszystko "na pokładzie" | Dedykowany do autonomicznej pracy <br> (RAM, ROM wewnątrz)
**Mikroprocesor**    | Serce sterownika PLC                         | Wspórpracuje z zewnętrzną pamięcią i modułami I/O
**Rejestr**          | Komórka pamięci procesora                    | Służy do ogólnego przechowywania danych lub jako rejestr przesówny
**Licznik**          | Inkrementacja impulsów                       | Zlicza do wartości zadanej, <br> wymaga instrukcji `RESET`
**Timer**            | Układ odmierzający czas w sterowniku         | Suży do programowania zwłoki<br> na włączenie lub wyłączenia urządzenia
**Zmienna (Tag)**    | Nazwa syboliczna konkretnego obszaru pamięci | Wskazuja na wyjście `Q`, wejście `I`, lub zmienną pomocniczą `M`
**Symbol odwrócony** | Specyficzny rysunek czujnika                 | Stosowany, gdy czyjnik ma generować działanie, gdy nie jest pobudzony (np. krańcówka)

### **I. 7. Logika zabezpieczenia**

**Zabezpieczenie**    | **Opis**                                | **Zastosowanie, cecha**
--------------------- | --------------------------------------- | ---------------
**Krańcówka**         | Element zabezpieczający<br> tor ruchomy | Zapobiega przegrzaniu silnika, <br> zatrzymuje go w wyznaczonym miejscu <br> (zazwyczaj przed końcem zakresu ruchu)
**Przycisk STOP**     | Zestyk bezpieczeństwa                   | Większość czasu zamknięty (`NC`),<br> rozwierny w sytuacji pobudzenia
**Przycisk START**    | Zestyk sterujący                        | Przycisk zwierny (`NO`),<br> pobudznie uruchamia algorytm
**Logika Start/Stop** | Warunek `X0 i nie X1`                   | Start (`X0`) jest załączony oraz <br> Stop (`X1`) nie jest pobudzony

### **I. 8. Hardware i Software Simens**

**Urządzenie/Soft** | **Opis**                                  | **Zastosowanie, cecha**
------------------- | ----------------------------------------- | ---------------
**S7-200 (Micro)**  | Wcześniejsze, <br> tanie rozwiązanie      | Dzialił drogie oprogramowanie z S7-300
**S7-1200**         | Nowoczesny,<br> ekonomiczny sterownik PLC | Oprogramowanie "prawie darmowe",<br> posiada pamięć wewnętrzną, <br> inne sterowniki wymagają karty pamięci
**S7-300/400**      | Zaawansowane, <br> droższe rozwiązanie    | Stosowane w dużych zakładach przemysłowych
**S7-1500**         | Najnowsza, zaawansowana seria sterowników | Wymaga odpowiednich licencji
**TIA Portal**      | Zintegrowane środowisko od Simens         | Bardzo zasobożerne,<br> przechowuje wszystkie składowe projektu Siemens
**Hot Swapping**    | Wymiana modułów na gorąco                 | Uszkodzony komponent można wymienić <br> bez przerywania pracy systemu

## **2026-02-24 Wykład II Realizowany podczas zajęć komputerowych**

### **II. 1. Układy logiczne**

**Zagadnienie**          | **Opis**  | **Zastosowanie, cecha**
------------------------ | --------------------------------------------------------------- | ---------------
**Układ synchroniczny**  | Posiada wejście taktujące (clock)                               | Często oparte na kwarcu,<br> zapewnia jednoznaczność<br> i powtarzalność operacji
**Układ asynchroniczny** | Brak wspólnego sygnału zegarowego                               | Każda zmiana stanu na wejściu<br> natychmiast wpływa na wyjście,<br> ryzyko braku stabilności
**Układ kombinowany**    | Wyjście zależy tylko od <br> aktualnego stany wejść             | Służy do prostej minimalizacji funkcji logicznych
**Układ sekwencyjny**    | Wejście zależy od wejść<br> oraz stanu poprzedniego             | Wymaga zastosowania elementów pamięciowych (np. przerzutników)
**Kod Gray'a**           | Kod, w którym<br> kolejne wartości<br> różnią się tylko o 1 bit | Zapobiega błędom odcztu,<br> przy zmianie stanu zmienia się<br> tylko jedna zmienna na raz

### **II. 2. Przerzutniki Flip-Flops budujące bloki pamięci**

**Typ przerzutnika**     | **Opis** | **Zastosowanie, cecha**
------------------------ | --------- | ---------------
**`SR` (Set-Reset)**     | Posiada wejście Set i Reset                              | Stan niedozwolony to<br> kombinacja 11 na wejściach (błędy logiczne)
**`D` (Data/Delay)**     | Przenosi stan wejścia <br> na wyjście przy takcie zegara | Służy jako element opóźniający sygnał lub podstawowa komórka pamięci rejestru
**`T` (Toggle)**         | Zmiana stanu na przeciw przy każdym impulsie             | Wykorzystywane do dzielenia<br> częstotliwości sygnały przez 2
**`JK` (Jump Kill)**     | Połączenie cech przerzutnika `SR` i `T`                  | Najbardziej uniwersalny,<br> eliminuje stan niedozwolony przerzutnika `SR`
**Wyjście<br> `Q i Q'`** | Wyjście proste (`Q`) i zanegowane (`Q'` zwane "nie Q")   | `Q'` reprezentuje stan wyjścia, który pojawia się w następnym takcie zegara

### **II. 3. Struktura bloku funkcyjnego**

**Element**                        | **Opis**                         | **Zastosowanie, cecha**
---------------------------------- | -------------------------------- | ---------------
**Blok funkcjonalny**              | Następny poziom układu cyfrowego | Realizuje narzuconą funkcjonalność,<br> oparty na układach sekwenchjnych,<br> komutacyjnych lub bramkach logicznych
**Wejścia/Wyjścia (X, Y)**         | Główne tory danych               | Wejścia (X) to sygnały sterujące,<br> Wyjścia (Y) to sygnały wynikowe
**Wejście<br> sterujące (S)**      | Sygnał wyboru lub trybu          | Określa, ak blok ma zareagować na dane (np. adres w multiplexerze)
**Wyjście<br> potwierdzające (P)** | Sygnał statusu operacji          | Potwierdza wykonanie zadania przez blok,<br>  kluczowe dla powtarzalności operacji
**Przełącznik cyfrowy**            | Ograniczony multiplexer          | Wykorzystywany w układach<br> zaawansowanych do sterowania<br> siłownikami komutacyjnymi

### **II. 4. Rejestry**

**Element**           | **Opis**  | **Zastosowanie, cecha**
--------------------- | --------- | ---------------
**Multiplexer**       | Posiada wejście adresowe i wiele wejść danych | Działa jak cyfrowy przełącznik,<br> wybiera jedno z wielu wejść<br> i przekazuje je na wyjście
**Komparator**        | Układ porównujący dwa sygnały                 | Służy do sprawdzania relacji między liczbami<br> (większy, mniejszy, równy)  
**Rejestr**           | Zbiór przerzutników (zazwyczaj D)             | Służy do przechowywania zawartości<br> danych w pamięci<br> (funkcja: załaduj/zpamiętaj)
**Rejestr przesuwny** | Przesuwa bity w szeregu                       | Przesunięcie w lewo/prawo,<br> skutkuje 2x większą <br> lub 2x mniejszą watością liczby 
**Licznik**           | Specyficzny rodzaj rejestru                   | Posiada możliwość liczenia <br> w górę lub w dół <br> (inkrementacji/dekrementacji)
**Dekoder**           | Przekształca kod binarny na sygnał `1 z N`    | W pamięci ROM pełni rolę układu odczytu<br> (np. z 3 bitów robi 8 kombinacji) 

### **II. 5. Konfiguracja sprzętowa (Simens S7-1200)**

**Element**      | **Opis**                                     | **Zastosowanie, cecha**
---------------- | -------------------------------------------- | ---------------
**Nasze modele** | S7-1211, S7-1212, S7-1215                    | Na wyposażeniu sali komputerowej
**Oznaczenia**   | Zapisywane jako DC/AC/RYL                    | Określają kolejno<br> zasilacnie procesra, zasilanie wejścia, typ wyjścia
**Wejście DC**   | Standardowe wejście cyfrowe (24V DC)         | Jedyny typ wekścia w S7-1200,<br> Zasilacz przetwarza 230V AC na 24V DC
**Wejście AC**   | Wejście na prąd przemienny (230V)            | W S7-1200 wymagają przekaźników 
**Wyście DC**    | Wyjście tranzystorowe<br> (półprzewodnikowe) | Bardzo mała bezwładność,<br> bardzo szybkie przełączanie,<br> brak zużycia mechanicznego
**Wyjście AC**   | Wyjscie triakowe                             | W S7-1200 nie występują,<br> zamiast nich jest RYL
**Wyjście RYL**  | Skrót od Relay, wyjście przekaźnikowe        | Elektromechaniczne wolniejsze ale o większym prądzie

### **II. 6. Adresacja komponentów**

**Element**               | **Opis**      | **Zastosowanie, cecha**
------------------------- | ------------- | ---------------
**Symbol adresu**         | `%` (procent) | Każdy adres zmiennej w sterownikach Simens<br> musi być nim poprzedzony
**Zapis bitu i bajtu**    | Znak `.` pomiędzy | Jest separatorem między bajtem a bitem  
**Struktura adresu**      | `Bajt.Bit`    | Przykład `%I0.1` oznacza **0 bajt** oraz **1 bit** na wejściu

### **II. 7. Przykład obliczeniowy (Impulsowanie)**

**Parametr**             | **Wartość / Obliczenie** | **Aspekty techniczne**
------------------------ | ---------------------    | -----------------
**Prędkość obiektu**     |36 km/h = 10 m/s          |Prędkość liniowa przeliczona na jednostki SI
**Charakterystyka koła** |Obwód = 1 m               |Przy 20 impulsach na jeden obrót koła
**Częstotliwość sygnału**|200 impulsów na sekundę   |Wymaga szybkich wejść licznikowych (HSC) ze względu na dynamikę sygnału
**Wybór wyjść**          | Układy szybko przełączające (np. sterowanie PWM) | Stosowane są tam tranzystory,<br> bo przekaźniki są za wolne i mają zużycie mechaniczne

