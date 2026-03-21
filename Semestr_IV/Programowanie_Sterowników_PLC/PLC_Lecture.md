# Programowanie Sterowników PLC

## 2026-02-24 Wykład I

### **I. 1. Organizacyjna**

**Zasada**         | **Opis**                               | **Uwagi**
------------------ | -------------------------------------- | -----------------------------------
**Podziału grupy** | Sala posiada 6 stanowisk komputerowych | Każda grupa dzieli się na 6 podgrup
**Oceniania**      | Ćwiczenia: wejściówki z zajęć          | Wykład 2 kolokwia

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
**System DCS**  | To przykład systemu rozproszonego <br> (Distributed Control System) | Stosowany w dużych zakładach <br> gdzie kontrolery rozproszone są po całym obiekcie, <br> system spięty siecią komunikacyjną
**Zdalne I/O**  | Czyjniki i inne elementy oddalone od siebie                         | Połączone medium komunikacyjnym <br> umożliwiający odczyt stanu i wysterowania

### **I. 4. Technologie i protokoły komunikacyjne**

**Standard**     | **Opis**  | **Zastosowanie, cecha**
---------------- | --------- | ---------------
**Modbus**       | Najstarszy i najprostszy standard przesyłania danych | Wykorzystuje porty szeregowe "przetrwał do dziś i ma się dobrze"
**Profibus**     | Standard firmy Simens                                | "Bardziej zaawansowany Modbus" 
**Can (CANbus)** | Sieć dwużyłowa, odporna na zakłócenia                | Standardowo wykorzystywana w motoryzacji
**HART**         | Protokół do zdalnej konfiguracji urządzeń            | Umożliwia strojenie i diagnostykę czujników
**Ethernet**     | Technologia sukcesywnie wypierająca starsze łącza    | Wprowadzane z opóźnieniem ze względu na konieczność zapernienia niezawodności

### **I. 5. Język drabinkowy (Ladder)**

**Element** | **Opis**  | **Zastosowanie, cecha**
----------- | --------- | ---------------
**Język drabinkowy (Ladder)** | Przykład języka graficznego | Najbardziej dominujący sposób programowania PLC
**Kierunek czytania** | Od lewej do prawej <br>, od góry do dołu | Wyznacza kolejność w jakiej sterownik analizuje logikę programu
**Cewka przekaźnika** | Zastępowana symbolami `O` lub `( )` | Łatwo w taki sposób narysować logikę
**NO (Normally Open)** | `\| \|` - Zestyk zwierny | Przewodzi prąd, gdy wejście jest aktywne
**NC (Normally Closed)** | `\|/\|` - Zestyk rozwierny  | Przewodzi prąd, gdy nie jest pobudzony
**Rodzaje cewek** | Cewka ustawienia `(S)` od `Set`, <br> cewka resetowania `(R)` od `Reset` | Umożliwiają tworzenie pamięci stanu, <br> za cewkami mogą być tylko inne cewki
**Paradygmat** | Cewki typu `(S)` i `(R)` tworzyć na zmiennych pomocniczych | Niezalecane bezpośrednio na wyjściach (błąd w sztuce), lepiej interpretować: "jeżeli nie uruchomione, to uruchom"
**Budowa** | Oparta na koncepcji przekażników | Programowe odwzorowanie klasycznej automatyki stycznikowej
**FBD** | Function Block Diagram | Alternatywny język graficzny, <br> firmy Simens

### **I. 6. Architektura wewnętrzna**

**Element** | **Opis**  | **Zastosowanie, cecha**
----------- | --------- | ---------------
**Mikrokontroler** | Układ scalony mający wszystko "na pokładzie" | Dedykowany do autonomicznej pracy <br> (RAM, ROM wewnątrz)
**Mikroprocesor** | Serce sterownika PLC | Wspórpracuje z zewnętrzną pamięcią i modułami I/O
**Rejestr** | Komórka pamięci procesora | Służy do ogólnego przechowywania danych lub jako rejestr przesówny
**Licznik** | Inkrementacja impulsów | Zlicza do wartości zadanej, <br> wymaga instrukcji `RESET`
**Timer**   | Układ odmierzający czas w sterowniku | Suży do programowania zwłoki<br> na włączenie lub wyłączenia urządzenia
**Zmienna** | Adresowanie przekaźników | Do każdego przekaźnika w programie musi by zawsze dopisana konktetna zmienna
**Symbol odwrócony** | Specyficzny rysunek czujnika | Stosowany, gdy czyjnik ma generować działanie, gdy nie jest pobudzony (np. krańcówka)

### **I. 7. Logika zabezpieczenia**

**Zabezpieczenie** | **Opis**  | **Zastosowanie, cecha**
----------------- | --------- | ---------------
**Krańcówka** | Element zabezpieczający tor ruchomy | Zapobiega przegrzaniu silnika, <br> zatrzymuje go w wyznaczonym miejscu <br> (zazwyczaj przed końcem zakresu ruchu)
**Przycisk STOP** | Zestyk bezpieczeństwa | Większość czasu zamknięty (`NC`),<br> rozwierny w sytuacji pobudzenia
**Przycisk START** | Zestyk sterujący | Przycisk zwierny (`NO`),<br> pobudznie uruchamia algorytm
**Logika Start/Stop** | Warunek `X0 i nie X1` | Start (`X0`) jest załączony oraz <br> Stop (`X1`) nie jest pobudzony

### **I. 8. Hardware i Software Simens**

**Urządzenie/Soft** | **Opis**  | **Zastosowanie, cecha**
------------------ | --------- | ---------------
**S7-200 (Micro)** | Wcześniejsze, <br> tanie rozwiązanie | Dzialił drogie oprogramowanie z S7-300
**S7-1200** | Nowoczesny,<br> ekonomiczny sterownik PLC | Oprogramowanie "prawie darmowe",<br> posiada pamięć wewnętrzną, <br> inne sterowniki wymagają karty pamięci
**S7-300/400** | Zaawansowane, <br> droższe rozwiązanie | Stosowane w dużych zakładach przemysłowych
**S7-1500** | Najnowsza, zaawansowana seria sterowników | Wymaga odpowiednich licencji
**TIA Portal** | Zintegrowane środowisko od Simens | Bardzo zasobożerne,<br> przechowuje wszystkie składowe projektu Siemens
**Hot Swapping** | Wymiana modułów na gorąco | Uszkodzony komponent można wymienić <br> bez przerywania pracy systemu
