# **Programowanie Sterowników PLC**
## **2026-02-24 Wykład I**

### **I. 1. Organizacyjna**

**Zasada**          | **Opis**                               | **Uwagi**
------------------- | -------------------------------------- | -------------------------------------------------
**Podziału grupy**  | Sala posiada 6 stanowisk komputerowych | Każda grupa<br> dzieli się na 6 podgrup
**Ocena z ćwiczeń** | Wejściówki z poprzednich ćwiczeń       | Brak instrukcji,<br> zajęcia komputerowe
**Ocena z wykładu** | Kolokwia w trakcie trwania semestru    | I Kolokwium w połowie,<br> II Kolokwium na koniec

### **I. 2. Fundamenty sterowania**

**Element**                  | **Charakterystyka**                                                        | **Logika i budowa**
---------------------------- | -------------------------------------------------------------------------- | --------------------------------------------------------------------------------------
**Przekaźnik**               | Służy do wyłączania i włączania pojedynczego toru prądowego                | Sterowanie fizyczne (elektromagnetyczne)
**Stycznik**                 | "Rozbudowany przekaźnik" do wielu torów prądowych (większe moce)           | Budowa zbliżona do przekaźnika,<br> ale z większą ilością styków
**Układy klasyczne**         | Połączenie przekaźników i styczników <br> Dobre dla prostych małych maszyn | *Wady* - duża ilość elementów, <br> skomplikowane okablowanie, <br> trudna diagnostyka
**Przekaźnik programowalny** | Podstawowy poziom cyfryzacji (tzw. sterownik "LOGO!")                      | Logika zaszyta w **prostym programie**,<br> ograniczonym do liczby wejść i wyjść (I/O)
**Sterownik PLC**            | Zaawansowane urządzenie mikroprocesorowe do dużych systemów                | Logika "przerzucona" do procesora <br> (realizowana przez procesor)

### **I. 3. Model działania i komunikacja rozproszona**

**Zagadnienie**    | **Opis**                                                            | **Wyjaśnienie**
------------------ | ------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------
**Cykl pracy**     | Pętla zamknięta, <br> generowanie wyjść na podstawie wejść          | Wykonywany w powtarzalnych odstępach czasu,<br> zmienna długość cyklu <br> uniemożliwia pełną synchroniczność<br> względem czasu rzeczywistego
**Próbkowanie**    | To sposób, w jaki sterownik "widzi" świat (stany) wewnątrz cyklu    | Cykliczne sprawdzanie stanów wejść i aktualizacji wyjść
**Brak ciągłości** | Fizyczny skutek próbkowania                                         | Wprowadza opóźnienia odczytu do reakcji
**Pozorny czas rzeczywisty** | Wynik bardzo szybkiego cyklu pracy                        | Milisekundowe opóźnienia, <br> praktycznie niezauważalne dla ludzkiego oka
**System DCS**     | To przykład systemu rozproszonego <br> Distributed Control System   | Stosowany w dużych zakładach <br> gdzie kontrolery rozproszone są po całym obiekcie, <br> system spięty siecią komunikacyjną
**Zdalne I/O**     | Czujniki i inne elementy oddalone od siebie                         | Połączone medium komunikacyjnym <br> umożliwiające odczyt stanów i sterowanie

### **I. 4. Technologie i protokoły komunikacyjne**

**Standard**     | **Opis**                                             | **Zastosowanie, cecha**
---------------- | ---------------------------------------------------- | ----------------------------------------------------------------------------------
**Modbus**       | Najstarszy i najprostszy standard przesyłania danych | Wykorzystuje porty szeregowe, nadal szeroko stosowany <br> "przetrwał do dziś i ma się dobrze"
**Profibus**     | Standard firmy Siemens                               | "Bardziej zaawansowany Modbus" 
**Can (CANbus)** | Sieć dwużyłowa, odporna na zakłócenia                | Standardowo wykorzystywana w motoryzacji magistrala szeregowa
**HART**         | Protokół do zdalnej konfiguracji urządzeń            | Umożliwia strojenie i diagnostykę czujników
**Ethernet**     | Technologia sukcesywnie wypierająca starsze łącza    | Wprowadzane z opóźnieniem ze względu na konieczność zapewnienia niezawodności
**Profinet**     | Standard firmy Siemens<br> oparty na łączu Ethernet  | Służy do komunikacji przemysłowej<br> opartej na Ethernet (PLC, I/O, HMI)

### **I. 5. Język drabinkowy (Ladder)**

**Element**                   | **Opis**                                                                 | **Zastosowanie, cecha**
----------------------------- | ------------------------------------------------------------------------ | -----------------------------------------------------------------------------------------------------------
**Język drabinkowy (Ladder)** | Przykład języka graficznego                                              | Najbardziej dominujący<br> sposób programowania PLC
**Kierunek czytania**         | Od lewej do prawej <br>, od góry do dołu                                 | Wyznacza kolejność w jakiej <br> sterownik analizuje logikę programu
**Cewka przekaźnika**         | Zastępowana<br> symbolami `O` lub `( )`                                  | Łatwo w taki sposób<br> narysować logikę
**NO (Normally Open)**        | `\| \|` - Zestyk zwierny                                                 | Przewodzi prąd,<br> gdy wejście jest aktywne
**NC (Normally Closed)**      | `\|/\|` - Zestyk rozwierny                                               | Przewodzi prąd (logiczne 1),<br> gdy przypisana zmienna wynosi 0<br> (stan spoczynku)
**Rodzaje cewek**             | Cewka ustawienia <br> `(S)` od `Set`, <br> Cewka resetowania <br> `(R)` od `Reset` | Umożliwiają tworzenie pamięci stanu, <br> za cewkami mogą być tylko inne cewki
**Paradygmat na temat cewek** | Cewki typu `(S)` i `(R)`<br> tworzyć na zmiennych pomocniczych | Niezalecane bezpośrednio na wyjściach (błąd w sztuce),<br> lepiej interpretować: "jeżeli nie uruchomione, to uruchom"
**Budowa**                    | Oparta na koncepcji przekaźników                                         | Programowe odwzorowanie klasycznej automatyki stycznikowej
**FBD**                       | Function Block Diagram                                                   | Alternatywny język graficzny, <br> firmy Siemens

### **I. 6. Architektura wewnętrzna**

**Element**          | **Opis**                                      | **Zastosowanie, cecha**
-------------------- | --------------------------------------------- | --------------------------------------------------------------------------------------
**Mikrokontroler**   | Układ scalony mający wszystko "na pokładzie"  | Dedykowany do autonomicznej pracy <br> (RAM, ROM wewnątrz)
**Mikroprocesor**    | Serce sterownika PLC                          | Współpracuje z zewnętrzną pamięcią i modułami I/O
**Rejestr**          | Komórka pamięci procesora                     | Służy do ogólnego przechowywania danych lub jako rejestr przesuwny
**Licznik**          | Inkrementacja impulsów                        | Zlicza do wartości zadanej, <br> wymaga instrukcji `RESET`
**Timer**            | Układ odmierzający czas w sterowniku          | Służy do programowania zwłoki<br> na włączenie lub wyłączenie urządzenia
**Zmienna (Tag)**    | Nazwa symboliczna konkretnego obszaru pamięci | Wskazuje na wyjście `Q`, wejście `I`, lub zmienną pomocniczą `M`
**Symbol odwrócony** | Specyficzny rysunek czujnika                  | Stosowany, gdy czujnik ma generować działanie, gdy nie jest pobudzony (np. krańcówka)

### **I. 7. Logika zabezpieczenia**

**Zabezpieczenie**    | **Opis**                                | **Zastosowanie, cecha**
--------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------
**Krańcówka**         | Element zabezpieczający<br> tor ruchomy | Zabezpiecza zakres ruchu mechanizmu (pozycja krańcowa - zazwyczaj przed końcem toru)
**Przycisk STOP**     | Zestyk bezpieczeństwa                   | Większość czasu zamknięty (`NC`),<br> rozwierny w sytuacji pobudzenia
**Przycisk START**    | Zestyk sterujący                        | Przycisk zwierny (`NO`),<br> pobudzenie uruchamia algorytm
**Logika Start/Stop** | Warunek `X0 i nie X1`                   | Start (`X0`) jest załączony oraz <br> Stop (`X1`) nie jest pobudzony

### **I. 8. Hardware i Software Siemens**

**Urządzenie/Soft** | **Opis**                                  | **Zastosowanie, cecha**
------------------- | ----------------------------------------- | -----------------------------------------------------------------------------------------------------------
**S7-200 (Micro)**  | Wcześniejsze, <br> tanie rozwiązanie      | Dzielił drogie oprogramowanie z S7-300
**S7-1200**         | Nowoczesny,<br> ekonomiczny sterownik PLC | Oprogramowanie "prawie darmowe",<br> posiada pamięć wewnętrzną, <br> inne sterowniki wymagają karty pamięci
**S7-300/400**      | Zaawansowane, <br> droższe rozwiązanie    | Stosowane w dużych zakładach przemysłowych
**S7-1500**         | Najnowsza, zaawansowana seria sterowników | Wymaga odpowiednich licencji
**TIA Portal**      | Zintegrowane środowisko od Siemens        | Bardzo zasobożerne,<br> przechowuje wszystkie składowe projektu Siemens
**Hot Swapping**    | Wymiana modułów na gorąco                 | Uszkodzony komponent można wymienić <br> bez przerywania pracy systemu

## **2026-02-24 Wykład II Realizowany podczas zajęć komputerowych za 2026-03-04**

### **II. 1. Układy logiczne**

**Zagadnienie**          | **Opis**  | **Zastosowanie, cecha**
------------------------ | --------------------------------------------------------------- | ---------------------------------------------------------------------------------------------
**Układ synchroniczny**  | Posiada wejście taktujące (clock)                               | Często oparte na kwarcu,<br> zapewnia jednoznaczność<br> i powtarzalność operacji
**Zegar**                | Generator impulsów                                              | Powstałe przebiegi okresowe są wykorzystywane do synchronizacji 
**Układ asynchroniczny** | Brak wspólnego sygnału zegarowego                               | Każda zmiana stanu na wejściu<br> może natychmiast wpływać na wyjście,<br> ryzyko braku stabilności
**Układ kombinowany**    | Wyjście zależy tylko od <br> aktualnego stanu wejść             | Służy do prostej minimalizacji funkcji logicznych
**Układ sekwencyjny**    | Wyjście zależy od wejść<br> oraz stanu poprzedniego             | Wymaga zastosowania elementów pamięciowych (np. przerzutników)
**Kod Gray'a**           | Kod, w którym<br> kolejne wartości<br> różnią się tylko o 1 bit | Zapobiega błędom odczytu,<br> przy zmianie stanu zmienia się<br> tylko jedna zmienna na raz

### **II. 2. Przerzutniki Flip-Flops budujące bloki pamięci**

**Typ przerzutnika**     | **Opis**                                                 | **Zastosowanie, cecha**
------------------------ | -------------------------------------------------------- | -----------------------------------------------------------------------------
**`SR` (Set-Reset)**     | Posiada wejście Set i Reset                              | Stan niedozwolony to<br> kombinacja 11 na wejściach (błędy logiczne)
**`D` (Data/Delay)**     | Przenosi stan wejścia <br> na wyjście przy takcie zegara | Służy jako element opóźniający sygnał lub podstawowa komórka pamięci rejestru
**`T` (Toggle)**         | Zmiana stanu na przeciwny przy każdym impulsie           | Wykorzystywane do dzielenia<br> częstotliwości sygnału przez 2
**`JK` (Jump Kill)**     | Połączenie cech przerzutnika `SR` i `T`                  | Najbardziej uniwersalny,<br> eliminuje stan niedozwolony przerzutnika `SR`
**Wyjście<br> `Q i Q'`** | Wyjście proste (`Q`) i zanegowane (`Q'` zwane "nie Q")   | `Q'` to negacja `Q` (stan przeciwny), który pojawia się w następnym takcie zegara

### **II. 3. Struktura bloku funkcyjnego**

**Element**                        | **Opis**                         | **Zastosowanie, cecha**
---------------------------------- | -------------------------------- | -------------------------------------------------------------------------------------------------------------------
**Blok funkcjonalny**              | Następny poziom układu cyfrowego | Realizuje narzuconą funkcjonalność,<br> oparty na układach sekwencyjnych,<br> komutacyjnych lub bramkach logicznych
**Wejścia/Wyjścia (X, Y)**         | Główne tory danych               | Wejścia (X) to sygnały sterujące,<br> Wyjścia (Y) to sygnały wynikowe
**Wejście<br> sterujące (S)**      | Sygnał wyboru lub trybu          | Określa, jak blok ma zareagować na dane (np. adres w multiplexerze)
**Wyjście<br> potwierdzające (P)** | Sygnał statusu operacji          | Potwierdza wykonanie zadania przez blok,<br>  kluczowe dla powtarzalności operacji
**Przełącznik cyfrowy**            | Ograniczony multiplexer          | Wykorzystywany w układach<br> zaawansowanych do sterowania<br> siłownikami komutacyjnymi

### **II. 4. Rejestry**

**Element**           | **Opis**                                      | **Zastosowanie, cecha**
--------------------- | --------------------------------------------- | ----------------------------------------------------------------------------------------------
**Multiplexer**       | Posiada wejście adresowe i wiele wejść danych | Działa jak cyfrowy przełącznik,<br> wybiera jedno z wielu wejść<br> i przekazuje je na wyjście
**Komparator**        | Układ porównujący dwa sygnały                 | Służy do sprawdzania relacji między liczbami<br> (większy, mniejszy, równy)  
**Rejestr**           | Zbiór przerzutników (zazwyczaj D)             | Służy do przechowywania zawartości<br> danych w pamięci<br> (funkcja: załaduj/zapamiętaj)
**Rejestr przesuwny** | Przesuwa bity w szeregu                       | Przesunięcie w lewo/prawo,<br> skutkuje 2x większą <br> lub 2x mniejszą wartością liczby 
**Licznik**           | Specyficzny rodzaj rejestru                   | Posiada możliwość liczenia <br> w górę lub w dół <br> (inkrementacji/dekrementacji)
**Dekoder**           | Przekształca kod binarny na sygnał `1 z N`    | W pamięci ROM pełni rolę układu odczytu<br> (np. z 3 bitów robi 8 kombinacji) 

### **II. 5. Konfiguracja sprzętowa (Siemens S7-1200)**

**Element**      | **Opis**                                     | **Zastosowanie, cecha**
---------------- | -------------------------------------------- | ------------------------------------------------------------------------------------------
**Nasze modele** | S7-1211, S7-1212, S7-1215                    | Na wyposażeniu sali komputerowej
**Oznaczenia**   | Zapisywane jako DC/AC/RLY                    | Określają kolejno<br> Zasilanie procesora,<br> Typ wejść `Input`,<br> Typ wyjść (`Output`)
**Wejście DC**   | Standardowe wejście cyfrowe (24V DC)         | Jedyny typ wejścia w S7-1200,<br> Zasilacz przetwarza 230V AC na 24V DC
**Wejście AC**   | Wejście na prąd przemienny (230V)            | W S7-1200 wymagają przekaźników 
**Wyjście DC**   | Wyjście tranzystorowe<br> (półprzewodnikowe) | Bardzo mała bezwładność,<br> bardzo szybkie przełączanie,<br> brak zużycia mechanicznego
**Wyjście AC**   | Wyjście triakowe                             | W S7-1200 nie występują,<br> zamiast nich jest RLY
**Wyjście RLY**  | Skrót od Relay, wyjście przekaźnikowe        | Elektromechaniczne wolniejsze ale o większym prądzie

### **II. 6. Adresacja komponentów**

**Element**               | **Opis**          | **Zastosowanie, cecha**
------------------------- | ----------------- | ------------------------------------------------------------------------
**Symbol adresu**         | `%` (procent)     | Każdy adres zmiennej w sterownikach Siemens<br> musi być nim poprzedzony
**Zapis bitu i bajtu**    | Znak `.` pomiędzy | Jest separatorem między bajtem a bitem  
**Struktura adresu**      | `Bajt.Bit`        | Przykład `%I0.1` oznacza **0 bajt** oraz **1 bit** na wejściu

### **II. 7. Przykład obliczeniowy (Impulsowanie)**

**Parametr**             | **Wartość / Obliczenie**                             | **Aspekty techniczne**
------------------------ | ---------------------------------------------------- | ---------------------------------------------------------------------------------------
**Prędkość obiektu**     | 36 km/h = 10 m/s                                     |Prędkość liniowa przeliczona na jednostki SI
**Charakterystyka koła** | Obwód = 1 m                                          |Przy 20 impulsach na jeden obrót koła
**Częstotliwość sygnału**| 200 impulsów na sekundę                              |Wymaga szybkich wejść licznikowych (HSC) ze względu na dynamikę sygnału
**Wybór wyjść**          | Układy szybko przełączające<br> (np. sterowanie PWM) | Stosowane są tam tranzystory,<br> bo przekaźniki są za wolne i mają zużycie mechaniczne

## **2026-03-10 Wykład III TIA Portal**

**III. 1. Środowisko TIA Portal i Sprzęt**

**Zagadnienie**          | **Opis i funkcja**              | **Szczegóły**
------------------------ | ------------------------------- | ----------------------------------------------------------------------------------------------------------------
**Lokalizacja projektu** | `Documents\\Automation\`        | Domyślne miejsce zapisu,<br> Przy otwieraniu wyświetlana jest wersja oprogramowania, w której powstał plik
**Kompatybilność**       | Migracja projektów              | Możliwość otwierania starszych <br> projektów w nowszych wersjach 
**Adres MAC**            | Unikalny identyfikator fizyczny | Kluczowy dla konfiguracji<br> w warstwie sprzętowej Ethernet
**Aktualizacja systemu** | Kompilacja <br> Wgranie         | `Compile` stworzenie pliku binarnego<br> `Download` wysłanie go do sterownika
**Tryb Offline**         | Praca konfiguracyjna            | Zmiana parametrów,<br> pisanie kodu bez połączenia z PLC
**Tryb Online**          | Podgląd pracy sterownika        | Pozwala widzieć aktualne stany wejść/wyjść i flag
**Systemowe Flagi**      | `AlwaysTrue` /<br>`AlwaysFalse` | Zestyki zawsze przewodzą <br> lub zawsze blokują sygnał
**First SCAN**           | Flaga pierwszego cyklu          | Wykonuje się tylko raz<br> przy przejściu ze STOP do RUN<br> Służy do inicjalizacji zmiennych
**Zmiany częściowe**     | Compile changes - tylko zmiany  | Przy drobnych korektach można wykonać tylko kompilację zmian <br> i wgrać je bez zatrzymywania całego sterownika

### **III. 2. Symbolika i Typy sygnałów**

**Symbol** | **Pełna nazwa**                 | **Opis i funkcja**
---------- | ------------------------------- | ---------------------------------------------------------------
`DI`       | Digital Input                   | Wejście cyfrowe (binarne) <br> (np. przycisk, krańcówka)
`DQ`       | Digital output                  | Wyjście cyfrowe <br> (np. sterujące cewką stycznika lub lampką)
`AI`       | Analog Input                    | Wejście analogowe <br> (np. czujnik temperatury, ciśnienia)
`I`        | Prądowe                         | Sygnał analogowy prądowy <br> (najczęściej standard 4-20 mA)
`U`        | Napięciowe                      | Sygnał analogowy napięciowy <br> (najczęściej 0-10 V)
`TC`       | Thermocouple                    | Termoelement, termopara <br> (napięcie w mV)
`RTD`      | Resistance Temperature Detector | Czujnik rezystancyjny <br> (np. Pt100)
`CP`       | Communication Processor         | Koprocesor / moduł komunikacyjny <br> (np. Modbus/RS485)
`PS`       | Power Supply                    | Źródło zasilania <br> (np. zasilacz DC)
`PM`       | Power Module                    | Moduł zasilania <br> (np. moduł zasilania 24V)   

## **2026-03-17 Wykład IV TIA Portal - c.d.**

### **IV. 1. TIA Portal - Rozszerzona Adresacja**

**Zagadnienie**                   | **Opis**                                                           | **Szczegóły**
--------------------------------- | ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------
**Adres IP**                      | Podstawowy element komunikacji                                     | Unikalny adres w sieci Ethernet
**Gniazda modułów**               | W konfiguracji sprzętowej moduły muszą być umieszczone w gniazdach | Puste przestrzenie pomiędzy slotami są niedozwolone
**`M0` (Memory 0)**               | Obszar pamięci bitowej (markerów)                                  | Można wykorystać jedynie jako zmienne pomocnicze wewnątrz programu
**`M1` (Zmienne systemowe)**      | Bajt pamięci, w którym znajdują się<br> flagi systemowe (np. `AlwaysTrue`, `AlwaysFalse`)<br> lub zegary taktujące (`Clock_Byte`) | Tylko jeśli zostały aktywowane w ustawieniach CPU
**Adresacja <br> `M1.0` vs `M1`** | `%M1.0` odnosi się <br> do pojedynczego bitu `0` w bajcie `1`      | Samo `%M1` lub (`%MB1`) odnosi się do całego bajtu danych
**Adresacja `M.2`**               | Określenie typu i rozmiaru danych                                  | Bitu (np. `%M0.2`),<br> Bajtu `%MB2`,<br> Słowa `%MW2`,<br> Podwójnego słowa `%MD2`
`QW/QI`                           | Word wyjściowy/wejściowy                                           | Stosowane np do obsługi sygnałów analogowych 

### **IV. 2. Liczbowe typy danych w PLC**

**Typ danych**   | **Rozmiar** |**Opis** 
---------------- | ----------- | ----------------------------------------------------------------------
**SINT**         | 8-bit       | Signed Integer (liczba całkowita ze znakiem)
**INT**          | 16-bit      | Integer (standardowa liczba całkowita)
**DINT**         | 32-bit      | Double Integer (liczba całkowita o podwójnej precyzji)
**UINT**         | 16-bit      | Unsigned Integer (liczba całkowita dodatnia, bez znaku)
**REAL**         | 32-bit      | Zmiennoprzecinkowa reprezentacja liczb (liczby z ułamkiem)
**`B` (Byte)**   | 8 bitów     | Podstawowy bajt danych, np. `%MB10`
**`W` (Word)**   | 16 bitów    | Słowo danych, np. `%MW10` (zajmuje dwa bajty: `MB10` i `MB11`)
**`D` (Double)** | 32 bity     | Podwójne słowo, np. `%MD10` (zajmuje cztery bajty od `MB10` do `MB13`)

### **IV. 3. Zarządzanie zmiennymi - PLC Tags**

**Rodzaj zmiennej**      | **Symbol / Lokalizacja**  | **Charakterystyka**
------------------------ | ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------
**Zmienne globalne**     | Poprzedzone przez `%`     | Widoczne w całym programie związane z fizycznymi wejściami/wyjściami (`I`,`Q`) lub pamięcią (`M`)
**Zmienne lokalne**      | Poprzedzone przez `#`     | Zdefiniowane wewnątrz konkretnego bloku (np. FC lub FB), używane jedynie w jego obrębie
**Zmienne Statyczne**    | Sekcja Static             | Zachowują swoją wartość pomiędzy cyklami programu, dostępne w FB
**Zmienne Tymczasowe**   | Sekcja Temp               | Zmienne dynamiczne, tracą swoją wartość po zakończeniu wykonanego bloku lub przy utracie zasilania<br> Brak dostępu dla paneli HMI
**Retain**               | Atrybut (Checkbox)        | Rezerwowane zazwyczaj na początku obszaru adresowania zmienne, które zachowują swoją wartość nawet po utracie zasilania
**Export/Import**        | n.d.                      | Przenoszenie zmiennych poza projekty <br> Można eksportować listy zmiennych<br> np. do Excela i importować je z powrotem

### **IV. 4. Złożone typy danych - Struktury i Tablice**

**Tablica - ARRAY**                                                              | **Struktura - STRUCT**
-------------------------------------------------------------------------------- | ----------------------------------------------------------------------------
Zbiór elementów tego samego typu <br> Np. 6 zmiennych typu `INT` pod jedną nazwą | Zbiór różnych elementów <br> Może zawierać w środku wiele typów jednocześnie

### **IV. 5. Błędy, Nazewnictwo i Pamięć**

**Zagadnienie**       | **Opis**                          | **Konsekwencja/Rozwiązanie**
--------------------- | --------------------------------- | -----------------------------------------------------------------------------------
**Błąd N31.0**        | Deklaracja typu `char` w bicie    | Błąd "Za mało pamięci", <br> znak potrzebuje całego bajtu, nie zmieści się na bicie
**Nazwy symboliczne** | Stosowane zamiast adresów         | Ułatwiają czytelność kodu zapisywane w tablicy tagów
**Duplikaty nazw**    | Dwie zmienne o tej samej nazwie   | TIA Portal automatycznie dodaje sufiks `_1`<br> do drugiej zmiennej tworząc kopie
**Konflikt adresów**  | Dwie zmienne na tym samym adresie | Powoduje niezgodność i błędy w działaniu logiki
