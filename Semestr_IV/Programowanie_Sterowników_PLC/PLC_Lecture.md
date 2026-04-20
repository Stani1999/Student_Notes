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
**`Mikrokontroler`** | Układ scalony mający wszystko "na pokładzie"  | Dedykowany do autonomicznej pracy <br> (RAM, ROM wewnątrz)
**`Mikroprocesor`**  | Serce sterownika PLC                          | Współpracuje z zewnętrzną pamięcią i modułami I/O
**`Rejestr`**        | Komórka pamięci procesora                     | Służy do ogólnego przechowywania danych lub jako rejestr przesuwny
**`Licznik`**        | Inkrementacja impulsów                        | Zlicza do wartości zadanej, <br> wymaga instrukcji `RESET`
**`Timer`**          | Układ odmierzający czas w sterowniku          | Służy do programowania zwłoki<br> na włączenie lub wyłączenie urządzenia
**`Zmienna (Tag)`**  | Nazwa symboliczna konkretnego obszaru pamięci | Wskazuje na wyjście `Q`, wejście `I`, lub zmienną pomocniczą `M`
**Symbol odwrócony** | Specyficzny rysunek czujnika                  | Stosowany, gdy czujnik ma generować działanie, gdy nie jest pobudzony (np. krańcówka)

### **I. 7. Logika zabezpieczenia**

**Zabezpieczenie**    | **Opis**                                | **Zastosowanie, cecha**
--------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------
**Krańcówka**         | Element zabezpieczający<br> tor ruchomy | Zabezpiecza zakres ruchu mechanizmu (pozycja krańcowa - zazwyczaj przed końcem toru)
**Przycisk STOP**     | Zestyk bezpieczeństwa                   | Większość czasu zamknięty (`NC`),<br> rozwierny w sytuacji pobudzenia
**Przycisk START**    | Zestyk sterujący                        | Przycisk zwierny (`NO`),<br> pobudzenie uruchamia algorytm
**Logika Start/Stop** | Warunek `X0 i nie X1`                   | Start (`X0`) jest załączony oraz <br> Stop (`X1`) nie jest pobudzony

### **I. 8. Hardware i Software Siemens**

**Urządzenie/Soft**  | **Opis**                                  | **Zastosowanie, cecha**
-------------------- | ----------------------------------------- | -----------------------------------------------------------------------------------------------------------
**`S7-200 (Micro)`** | Wcześniejsze, <br> tanie rozwiązanie      | Dzielił drogie oprogramowanie z S7-300
**`S7-1200`**        | Nowoczesny,<br> ekonomiczny sterownik PLC | Oprogramowanie "prawie darmowe",<br> posiada pamięć wewnętrzną, <br> inne sterowniki wymagają karty pamięci
**`S7-300/400`**     | Zaawansowane, <br> droższe rozwiązanie    | Stosowane w dużych zakładach przemysłowych
**`S7-1500`**        | Najnowsza, zaawansowana seria sterowników | Wymaga odpowiednich licencji
**`TIA Portal`**     | Zintegrowane środowisko od Siemens        | Bardzo zasobożerne,<br> przechowuje wszystkie składowe projektu Siemens
**`Hot Swapping`**   | Wymiana modułów na gorąco                 | Uszkodzony komponent można wymienić <br> bez przerywania pracy systemu

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
**Częstotliwość sygnału**| 200 impulsów na sekundę                              |Wymaga szybkich wejść licznikowych (HSC)<br> ze względu na dynamikę sygnału
**Wybór wyjść**          | Układy szybko przełączające<br> (np. sterowanie PWM) | Stosowane są tam tranzystory,<br> bo przekaźniki są za wolne i mają zużycie mechaniczne

## **2026-03-10 Wykład III `TIA Portal`**

**III. 1. Środowisko `TIA Portal` i Sprzęt**

**Zagadnienie**          | **Opis i funkcja**              | **Szczegóły**
------------------------ | ------------------------------- | ----------------------------------------------------------------------------------------------------------------
**Lokalizacja projektu** | `Documents\\Automation\`        | Domyślne miejsce zapisu,<br> Przy otwieraniu wyświetlana jest wersja oprogramowania pliku
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
`DQ`       | Digital Output                  | Wyjście cyfrowe <br> (np. sterujące cewką stycznika lub lampką)
`AI`       | Analog Input                    | Wejście analogowe <br> (np. czujnik temperatury, ciśnienia)
`I`        | Prądowe                         | Sygnał analogowy prądowy <br> (najczęściej standard 4-20 mA)
`U`        | Napięciowe                      | Sygnał analogowy napięciowy <br> (najczęściej 0-10 V)
`TC`       | Thermocouple                    | Termoelement, termopara <br> (napięcie w mV)
`RTD`      | Resistance Temperature Detector | Czujnik rezystancyjny <br> (np. Pt100)
`CP`       | Communication Processor         | Koprocesor / moduł komunikacyjny <br> (np. Modbus/RS485)
`PS`       | Power Supply                    | Źródło zasilania <br> (np. zasilacz DC)
`PM`       | Power Module                    | Moduł zasilania <br> (np. moduł zasilania 24V)   

## **2026-03-17 Wykład IV `TIA Portal` - c.d.**

### **IV. 1. `TIA Portal` - Rozszerzona Adresacja**

**Zagadnienie**              | **Opis**                                                               | **Szczegóły**
---------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------
**`Adres IP`**               | Podstawowy element komunikacji                                         | Unikalny adres w sieci Ethernet
**`Gniazda modułów`**        | W konfiguracji sprzętowej moduły<br> muszą być umieszczone w gniazdach | Puste przestrzenie pomiędzy slotami są niedozwolone
**`M0` (`Memory 0`)**        | Obszar pamięci bitowej (markerów)                                      | Można wykorzystać jedynie jako zmienne pomocnicze wewnątrz programu
**`M1` (Zmienne systemowe)** | Bajt pamięci, w którym znajdują się<br> flagi systemowe (np. `AlwaysTrue`, `AlwaysFalse`)<br> lub zegary taktujące (`Clock_Byte`) | Tylko jeśli zostały aktywowane w ustawieniach CPU
**Adresacja bit vs bajt**    | `M1.0` vs `M1`                                                         | `%M1.0` to konkretny bit, `%MB1` (lub samo `%M1`) to cały bajt danych
**Adresacja `M.2`**          | Określenie typu i rozmiaru danych                                      | Bitu (np. `%M0.2`),<br> Bajtu `%MB2`,<br> Słowa `%MW2`,<br> Podwójnego słowa `%MD2`
`QW/QI`                      | Word wyjściowy/wejściowy                                               | Stosowane do obsługi sygnałów analogowych lub szybkich liczników

### **IV. 2. Typy danych w PLC**

**Typ danych**   | **Rozmiar** |**Opis** 
---------------- | ----------- | ----------------------------------------------------------------------
**`SINT`**       | 8-bit       | Signed Integer (skrócona liczba całkowita ze znakiem)
**`INT`**        | 16-bit      | Integer (standardowa liczba całkowita)
**`DINT`**       | 32-bit      | Double Integer (liczba całkowita o podwójnej precyzji)
**`USINT`**      | 8-bit       | Unsigned Signed Integer (liczba całkowita dodatnia, bez znaku)
**`UINT`**       | 16-bit      | Unsigned Integer (liczba całkowita dodatnia, bez znaku)
**`REAL`**       | 32-bit      | Liczba zmiennoprzecinkowa (ułamkowa), adresowana zawsze jako `%MD`
**`Bool`**       | 1 bit       | Typ logiczny (`1`/`0` - `prawda`/`fałsz`)
**`B` (Byte)**   | 8 bitów     | Podstawowy bajt danych, np. `%MB10`
**`W` (Word)**   | 16 bitów    | Słowo danych, np. `%MW10` (zajmuje dwa bajty: `MB10` i `MB11`)
**`D` (Double)** | 32 bity     | Podwójne słowo, zajmuje cztery bajty (np. `%MD10` to bajty 10, 11, 12 i 13)
**`Char`**       | 8 bitów     | Znak ASCII, ale w PLC zajmuje cały bajt (nie można go adresować na poziomie bitu)


### **IV. 3. Zarządzanie zmiennymi - `PLC Tags`**

**Rodzaj zmiennej**      | **Symbol / Lokalizacja**  | **Charakterystyka**
------------------------ | ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------
**Zmienne globalne**     | Poprzedzone przez `%`     | Widoczne w całym programie związane z fizycznymi<br> wejściami/wyjściami (`I`,`Q`) lub pamięcią (`M`)
**Zmienne lokalne**      | Poprzedzone przez `#`     | Zdefiniowane wewnątrz konkretnego bloku,<br> np. `FC` lub `FB` używane jedynie w jego obrębie
**Zmienne Statyczne**    | Sekcja `Static`           | Zachowują swoją wartość pomiędzy cyklami programu, dostępne w `FB`
**Zmienne Tymczasowe**   | Sekcja `Temp`             | Zmienne dynamiczne, tracą swoją wartość po zakończeniu wykonanego bloku lub przy utracie zasilania<br> Brak dostępu dla `paneli HMI`
**`Retain`**             | Atrybut (`Checkbox`)      | Rezerwowane zazwyczaj na początku obszaru adresowania zmienne,<br> które zachowują swoją wartość nawet po utracie zasilania
**Export/Import**        | n.d.                      | Przenoszenie zmiennych poza projekty <br> Można eksportować listy zmiennych<br> np. do `Excel'a` i importować je z powrotem

### **IV. 4. Złożone typy danych - Struktury i Tablice i Czas**

 **Typ danych**        | **Opis i zastosowanie**
---------------------- | --------------------------------------------------------------------------------------------
**Tablice**            | Zbiór elementów tego samego typu, np. 6 zmiennych typu `INT` pod jedną nazwą
**Struktura**          | Zbiór różnych elementów, może zawierać w środku wiele typów jednocześnie
**String**             | Ciąg znaków ASCII, domyślnie zajmuje 254 znaki + 2 bajty nagłówka
**WString**            | Łańcuch znaków o rozszerzonym kodowaniu (Unicode), pozwalający na zapis znaków specjalnych
**DT (Date_And_Time)** | Standardowy format daty i czasu (rok, miesiąc, dzień, godzina, minuty, sekundy, milisekundy)
**DTL**                | Data and Time Long, rozszerzony format daty i czasu (32-bitowy)
**T (Time)**           | Czas trwania (np. dla Timerów). Zapisywany w milisekundach (np. `T#5s`)

### **IV. 5. Błędy, Nazewnictwo i Pamięć**

**Zagadnienie**        | **Opis**                          | **Konsekwencja/Rozwiązanie**
---------------------- | --------------------------------- | --------------------------------------------------------------------------------------------
**Błąd N31.0**         | Deklaracja typu `char` w bicie    | Błąd "Za mało pamięci", <br> znak potrzebuje całego bajtu, nie zmieści się na bicie
**Nazwy symboliczne**  | Stosowane zamiast adresów         | Ułatwiają czytelność kodu zapisywane w tablicy tagów
**Duplikaty nazw**     | Dwie zmienne o tej samej nazwie   | `TIA Portal` automatycznie dodaje sufiks `_1`<br> do drugiej zmiennej tworząc kopie
**Konflikt obszarów**  | Nakładanie się adresów            | Powoduje niezgodność i błędy w działaniu logiki,<br> jedna zmienna nadpisuje drugą w pamięci

## **2026-03-24 Wykład V**

### **V. 1. Architektura i Pamięć (Uzupełnienie)**

**Zagadnienie**                     | **Zasada / Dobra praktyka** | **Szczegóły techniczne**
----------------------------------- | --------------------------- | --------------------------------------------------------------------------------------------
**Adresacja 32-bit**                | Rezerwacja dla typów z `D`  | Oznaczenie `D` (np. `%MD`) dotyczy zawsze typów 32-bitowych, w tym `Real` oraz `DINT`
**Wyjścia wysokoczęstotliwościowe** | Obsługa HSC/PWM             | Wyjścia wysokoczęstotliwościowe są wykorzystywane przy sterowaniu impulsowym (np. silniki)
**Pamięć systemowa**                | Pierwsze 2 bajty            | Dobre praktyki nakazują rezerwację początkowych bajtów pamięci `M` na potrzeby systemowe sterownika
**Rezerwacja pamięci**              | Przesunięcie adresacji      | Zalecenie rezerwowania pierwszych dwóch bajtów pamięci na potrzeby systemowe<br> i adresowanie zmiennych procesowych (markerów) od dalszych adresów


### **V. 2. Programowanie i struktura bloków**

**Typ bloku**           | **Opis**                  | **Zastosowanie**
----------------------- | ------------------------- | -----------------------------------------------------------------------------------------------------------------
**OB1 (Main)**          | Blok organizacyjny główny | Główna pętla programu wykonywana w nieskończoność,<br> częstotliwość zależy od ilości kroków wewnątrz tego typu bloków
**System Operacyjny**   | Interface sprzętowy       | Pośredniczy między kodem użytkownika a fizycznym sprzętem, wejściami/wyjściami 
**DB (Data Block)**     | Blok danych               | Globalny obszar pamięci dla komponentów programu, może przechowywać typy proste i złożone
**FC (Function)**       | Funkcja                   | Wykonuje kod korzystając ze zmiennych globalnych, nie posiada własnej pamięci
**FB (Function Block)** | Blok funkcyjny            | Posiada dodatkową bazę danych (Instancja DB), pozwala na parametryzację obiektową
**LAD / FBD / SCL**     | Języki programowania      | Wybór zależy od problemu, LAD (drabinka), FBD (bloki) lub SCL (tekst strukturalny)

### **V. 3. Struktura i zarządzanie blokami programowymi**

**Element**                    | **Opis i funkcja**                                          | **Szczegóły techniczne**
------------------------------ | ----------------------------------------------------------- | --------------------------------------------------------------------------------------------------
**Tworzenie DB**               | Bloki danych (Data Block) służą do przechowywania zmiennych | Mogą być tworzone ręcznie jako bloki globalne lub automatycznie jako <br> instancje przy zakładaniu `FB`
**Dodawanie bloków**           | `Add new block` w drzewie projektu pod `Program blocks`     | Pozwala na wybór typu bloku (`OB, FC, FB, DB`) oraz nadanie mu unikalnej nazwy i numeru
**Wybór języka**               | Określenie sposobu zapisu logiki wewnątrz bloku             | Można wymusić język programowania (`LAD, FBD, SCL`) 
**Wywoływanie bloków**         | Umieszczenie bloków `FC/FB` wewnątrz pętli głównej (`OB1`)  | Przeciąganie bloku do segmentu (`Network`) <br> Bloki mogą być predefiniowane lub stworzone przez użytkownika
**Powielanie bloków**          | Możliwość wielokrotnego użycia tej samej logiki             | Raz napisany blok FB można wywołać wielokrotnie, przypisując mu każdorazowo inną instancję DB
**Kompilacja i Optymalizacja** | Przetwarzanie kodu do formy binarnej                        | Aby mieć dostęp do stałej struktury danych (np. dla systemów zewnętrznych),<br> należy w ustawieniach bloku włączyć opcje `Optimized block access`

### **V. 4. Elementy graficzne w LAD**

**Element interfejsu**  | **Funkcjonalność**                          | **Zastosowanie**
----------------------- | ------------------------------------------- | ---------------------------------------------------------------------------------------
**Pasek ulubionych**    | Sekcja nad obszarem roboczym programu       | Zaleca się dodawanie tam najczęściej używanych instrukcji (styk NO, NC, Cewka) aby przyspieszyć tworzenie kodu
**Komentarze Network**  | Pole tekstowe nad każdym segmentem drabinki | Służy do opisu realizowanych funkcji, co jest niezbędne przy rozbudowanych programach dla łatwiejszej diagnostyki
**Podpowiedzi Tagów**   | System autouzupełniania nazw zmiennych      | Po wpisaniu pierwszych liter nazwy symbolicznej, `TIA Portal` wyświetla listę pasujących wpisów z tablicy PLC Tags
**Zamykanie Networków** | Ikona strzałek przy numerze segmentu        | Pozwala zwijać i rozwijać część kodu, co poprawia przejrzystość przy pracy z dużą liczbą instrukcji
### **V. 5. Zaawansowana logika: Przekaźniki i Zbocza**

**Element logiczny**  | **Działanie w programie** | **Powiązanie fizyczne**
--------------------- | ----------------------------------------- | -----------------------------------------------------------------------------
**Wirtualna cewka**   | Programowe odwzorowanie stanu przekaźnika | W programie widzimy zestyki, ale ich stan (zwarty czy rozwarty) zależy od "wirtualnej cewki",<br> którą pobudza np. fizyczny przycisk lub czujnik"
**Czujniki Poziomu**  | Przykład wejścia binarnego                | Gdy woda zalewa czujnik, aktywuje on swój wewnętrzny mechanizm,<br> co sterownik interpretuje jak zmianę stanu zestyku
**Wykrywanie zboczy** | `P` (positive edge) i `N` (negative edge) | Wykrywają moment zmiany sygnału z 0 na 1 (zbocze narastające)<br> lub z 1 na 0 (zbocze opadające), sygnał aktywny tylko przez jeden cykl sterownika
**Pamięć Zbocza**     | Wymóg dwóch zmiennych pomocniczych        | Instrukcja musi przechowywać stan aktualny oraz stan z poprzedniego cyklu,<br> aby stwierdzić, czy nastąpiła zmiana

## **2026-03-31 Wykład VI**

### **VI. 1. Mechanizmy wykonywania programów i wykrywania zboczy**

**Zagadnienie**         | **Zasada/Działanie**         | **Szczegóły techniczne**
----------------------- | ---------------------------- | --------------------------------------
**Cykl pracy OB**       | Bardzo krótki czas wykonania | Blok OB jest aktywny przez bardzo krótki czas rzędu kilku milisekund
**Detekcja zboczy**     | Porównanie stanów sygnału    | Aby wykryć zbocze, sterownik porównuje aktualny stan sygnału z bieżącego cyklu programu ze stanem z poprzedniego cyklu
**Pamięć operacji**     | Wymóg zmiennej `Memory`      | Instrukcja zbocza musi posiadać przypisaną zmienną pamięciową (`marker`), która przechowuje stan z poprzedniego cyklu
**Opis zestyku zbocza** | Zapis dwuargumentowy         | Zestyk opisywany jest przez dwie zmienne: zmienną wejściową (u góry) oraz zmienną pamięciową (na dole)

### **VI. 2. Operacje i konwersja typów danych**

**Operacja**               | **Cel i opis**                                  | **Ograniczenia przyczynowo-skutkowe**
-------------------------- | ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------
**Interpretacja danych**   | Zależność od typu zmiennej                      | Dane w pamięci są odczytywane w charakterystyczny sposób dla przypisanego typu
**Automatyczna konwersja** | Wsparcie przez kompilator                       | Kompilator `TIA Portal` posiada funkcję automatycznej konwersji typów,<br> jeśli operacja tego wymaga
**Konwersja typów**        | Umożliwienie operacji na różnych typach         | Blok operacyjny wymaga, aby wszystkie argumenty były tego samego typu
**Konwersja `Real -> Int`**| Zamiana liczby zmiennoprzecinkowej na całkowitą | Podczas przekształcenia typu zmiennoprzecinkowego (`Real`)<br> na całkowity (`Int`),<br> wartość po przecinku zostaje obcięta
**Konwersja `w górę`**     | Przejście na typ o większym zakresie            | W przypadku ryzyka przekroczenia zakresu (np. `Int`),<br> dane są automatycznie konwertowane na typ o większym zakresie (np. `DINT`)
**Konwersja `w dół`**      | Przejście z typu większego na mniejszy          | Konwersja z typów większych na mniejsze jest możliwa jedynie,<br> gdy wartość mieści się w węższym zakresie


### **VI. 3. Skalowanie wartości analogowych**

**Element układu**          |**Funkcja**                    |**Rola**                                                                   |**Sygnał**                                  
----------------------------|-------------------------------|---------------------------------------------------------------------------|-----------------------------------------------------------
**Czujnik (np. `PT100`)**   |Element pomiarowy (`TE`)       |Bezpośredni odczyt wartości procesowej z obiektu                           |**Fizyczny:** Rezystancja, ciśnienie, temperatura, przepływ 
**Przetwornik `TT`**        |Konwerter sygnału              |Standaryzacja surowego odczytu do standardu przemysłowego                  |**Elektryczny:** napięciowy `0-10 V` lub prądowy `4-20 mA`
**Przetwornik `ADC w PLC`** |Interpretacja analogowo-cyfrowa|Przekształcenie napięcia/prądu na liczbę całkowitą zrozumiałą dla procesora|**Cyfrowy:** Zakres liczbowy Siemens od `0` do `27648`    
**Normalizacja<br>`NORM_X`**|Przetwarzanie wstępne          |Sprowadzenie wartości `0-27648` do ułamka z zakresu `0.0 - 1.0`            |**Liczbowy:** Typ Real (zmiennoprzecinkowy)
**Skalowanie<br>`SCALE_X`** |Przetwarzanie końcowe          |Nadanie jednostki inżynierskiej (np. `bary`, `°C`) wartości ułamkowej      |**Inżynierski:** Wartość rzeczywista w skali czujnika (np. `0-10 bar`)
 
### **VI. 4. Gotowe biblioteki w systemie**

**Instrukcja**     | **Działanie i logika**         | **Zastosowanie**
------------------ | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------
**`CALCULATE`**    | Wykonywanie złożonych operacji | Pozwala na zapisanie skomplikowanego wzoru matematycznego w jednym bloku na wielu argumentach
**`MIN/MAX`**      | Wybór skrajnej wartości        | Bloki `MIN` i `MAX` zwracają odpowiednio najmniejszą lub największą wartość spośród podanych argumentów (zmiennych na wejściu)
**`LIMIT`**        | Ograniczenia zmiennej          | Blok `LIMIT` "pilnuje", aby zmienna nie przekroczyła zadanej wartości minimalnej i maksymalnej
**`IN_RANGE`**     | Sprawdzanie przedziału         | Blok `IN_RANGE` zwraca `TRUE/1`, jeśli badana zmienna znajduje się wewnątrz zdefiniowanego zakresu
**`OUT_RANGE`**    | Sprawdzanie poza zakresem      | Blok `OUT_RANGE` zwraca `TRUE/1`, jeśli badana zmienna znajduje się poza zdefiniowanym przedziałem

## **2026-04-14 Wykład VII**

### **VII. 1. Mechanizmy detekcji zboczy**

**Zagadnienie**        | **Opis i działanie**                                 | **Wymagania techniczne**
---------------------- | ---------------------------------------------------- | ---------------------------------------------------------------------------------------------
**Zbocze narastające** | Rosnący poziom sygnału - Zmiana sygnału z `0 na 1`   | Wymaga markera pamięci do przechowywania stanu z poprzedniego cyklu
**Zbocze opadające**   | Spadający poziom sygnału - Zmiana sygnału z `1 na 0` | Podobnie jak w przypadku zbocza narastającego, potrzebna jest zmienna pamięciowa
**Blok sprawdzający**  | Specjalna funkcja weryfikująca aktualny stan wejścia | Konieczność użycia zmiennej pomocniczej w `TIA Portal` (na dole bloku) 
**Zmienna pomocnicza** | Przechowuje stan z poprzedniego cyklu                | Bez tej zmiennej, instrukcja zbocza nie będzie w stanie poprawnie wykryć zmiany stanu sygnału

### **VII. 2. Przykład skalowania: Barometr (`4-20 mA`)**

**Wartość**            | **Barometr** | **Przetwornik** | **Przetwornik `ADC`** | `NORM_X` | `SCALE_X`
---------------------- | ------------ | --------------- | --------------------- | -------- | ----------
**Wartość minimalna**  | `0 bar`      | `4 mA`          | `0`                   | `0.0`    | `0.0`    
**Wartość pośrednia**  | `5 bar`      | `12 mA`         | `13824`               | `0.5`    | `5.0`   
**Wartość maksymalna** | `10 bar`     | `20 mA`         | `27648`               | `1.0`    | `10.0`  

### **VII. 3. Monitorowanie i diagnostyka online**

**Zagadnienie**              | **Opis i działanie**                              | **Uwagi techniczne**
---------------------------- | ------------------------------------------------- | -------------------------------------------------------------------------------------------------
**Status bloków**            | Tryb `Monitoring` (ikona okularów) w `TIA Portal` | Cewki `Set`/`Reset` mogą mylnie wskazywać stan aktywny,<br> należy zwracać uwagę na zestyki 
**Nadpisywanie bloków**      | Wgrywanie `Download` komponentów do sterownika    | Jeżeli w projekcie istnieją już bloki o tych samych numerach, zostaną one zastąpione nową wersją
**Diagnostyka<br> zestyków** | Wizualizacja przepływu sygnału w drabince (`LAD`) | Kolor zielony oznacza przewodzenie logiczne sygnału w danym cyklu

### **VII. 4. Karta Pamięci (`SMC`) i Zasoby sprzętowe**

**Element**             | **Opis**                                                  | **Szczegóły techniczne**
----------------------- | --------------------------------------------------------  | -----------------------------------------------------------------------
**Sterownik `S7-1200`** | Posiada wbudowaną pamięć typu `Load Memory`               | Karta pamięci jest opcjonalna (używana do transferu lub backupu)
**Sterownik `S7-1500`** | Nie posiada zintegrowanej pamięci ładowania               | Karta pamięci `SMC` jest niezbędna do pracy sterownika i wgrania programu
**`Timer`**             | Blok funkcjonalny oparty na cyklach procesora lub zegarze | Wykorzystuje wewnętrzny generator impulsów (zegar systemowy) do odmierzania czasu
**`Licznik`**           | Blok funkcjonalny oparty na cyklach procesora lub zegarze | Wykorzystuje zliczanie impulsów zewnętrznych (np. z czujnika, enkodera)
Uwaga ogólna            | `Timer` i `licznik` to często ten sam układ sprzętowy     | Różnica polega wyłącznie na źródle impulsów: wewnętrzne (czas) vs zewnętrzne (zdarzenia)

### **VII. 5. Obsługa Timerów (`TP`, `TON`)**

**Element<br>Typ `Timera`**| **Sposób (działania)**                   | **Logika**                                                                                                                 | **Specyfikacja parametrów i zapisu**
-------------------------- | ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------
**`TP`<br>(Impuls)**       | Generowanie impulsu<br> o stałym czasie  |  Po wykryciu zbocza narastającego na wejściu `IN`,<br> wyjście `Q` zostaje załączone na czas określony przez parametr `PT` | **Niezależność od wejścia:**<br> Raz wyzwolony impuls trwa zadany czas, nawet jeśli sygnał `IN` zostanie przerwany<br> Parametr czasu zapisujemy jako np. `T#4s`
**`TON`<br>(On-Delay)**    | Opóźnienie<br>załączenia                 | Wyjście `Q` zostaje aktywowane dopiero po upływie czasu `PT`,<br> pod warunkiem stałej obecności sygnału na wejściu `IN`   | **Reset automatyczny:**<br> Zanik sygnału na wejściu `IN` przed upływem czasu `PT`<br> powoduje wyzerowanie odliczania
**Sposób zapisu**          |  1. Blok (`Box`):<br> 2. Cewka (`Coil`): | Pełny blok funkcjonalny z wejściami/wyjściami<br>Uproszczony zapis w drabince                                              | `IN`, `PT`, `Q`,`ET` <br> `Timer` jest przypisany bezpośrednio do operacji na końcu linii logicznej
**Instancja `DB`**         | Automatyczne tworzenie                   | Każdorazowe wrzucenie timera do drabinki<br> generuje unikalny blok danych instancyjnych (`Instance DB`)                   | **Przechowywanie danych:**<br> `DB` przechowuje aktualny czas odliczania oraz nastawy,<br> co pozwala na dostęp do tych danych z innych części programu
