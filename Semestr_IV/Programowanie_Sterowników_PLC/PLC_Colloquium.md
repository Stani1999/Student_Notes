`# **Programowanie Sterowników PLC**

## **Zagadnienia do kolokwium**

## 1. Funkcjonowanie timera i licznika w sterowniku PLC

### 1. Budowa sprzętowa i zasada działania

**Zagadnienie**                                         | **Budowa / Zasada działania**
---                                                     | ---
**Układ bazujący na<br> dwóch 16-bitowych rejestrach**  | Rejestr wartości stałej (zadanej)<br> oraz Rejestr wartości bieżącej (licznika)
**Zrównanie wartości<br> obu rejestrów**                | Powoduje zmianę stanu logicznego zestyków<br> przypisanych do bloku (NO zamyka się, NC otwiera)
**Timer**                                               | **Timer zlicza impulsy z wewnętrznego generatora<br> sprzętowego generatora zegarowego** (np. co 100ms)
**Licznik**                                             | **Licznik zlicza zewnętrzne zdarzenia/impulsy**<br> (np. zbocza sygnału z czujnika)
**Z punktu widzenia CPU**                               | Jest to często tan sam układ fizyczny

### 2. Rodzaje i obsługa timerów (układów czasowych)

**Typ Timera**                     | **Opis**
---                                 | ---
**`TP`**<br>(Impuls)                | Po wykryciu zbocza narastającego na wejściu `IN`,<br> wyjście `Q` przyjmuje stan wysoki(1)<br> na ściśle określony czas `PT` (Preset Time np. `T#5s`), <br> Zanik sygnału `IN` w trakcie odliczania<br> **nie przerywa** działania układu. <br> Impuls trwa dokładnie `PT`
**`TON`**<br>(Opóżnione załączenie) | Opóźnia aktywacje wyjścia `Q`.<br> Wymaga ciągłego nieprzerwanego sygnału `IN`.<br> Zanik sygnału przed upływem `PT`<br> automatycznie resetuje upływający czas (`ET` = 0).
**`TONR`**<br>(Z podtrzymaniem)     | Odlicza czas na wyjściu `ET` tylko gdy<br> sygnał `IN` ma stan wysoki.<br> Zanik sygnału wstrzymuje odliczanie,<br> ale układ zapamiętuje wartość (brak auteresetu).<br> Wymaga fizycznego podania sygnału<br> na dedykowane wejście R (Reset),<br> aby wyzerować układ.
**Generowanie<br> instancji**       | Każde użycie bloku czasowego w programie<br> generuje unikalny dla niego<br> blok danych instancyjnych (Instance DB)<br> do przechowywania czasu i nastaw.

### 3. Rodzaje i obsługa liczników

**Typ Licznika**                | **Główna cecha**                                          | **Szczegóły**
---                             | ---                                                       | ---
**Standardowe liczniki**        | Są obsługiwane w ramach<br> głównego cyklu programu (OB1) | Domyślny sprzętowy filtr wejść cyfrowych w sterowniku (ok. 10ms)<br> oraz czas wykonywania pętli ograniczają ich częstotliwość<br> do zaledwie kilkunastu Hz.
**HSC (High Speed Counters)**   | Szybkie liczniki sprzętowe                                | Działają asynchronicznie, omijając cykl skanowania procesora.<br> Niezbędne do zliczania sygnałów o wysokiej dynamice<br> (np. enkodery na wałach silników, np. 200 Hz).

## 2. Podstawowe i złożone typy danych w sterownikach Simatic

### 1. Podstawowe (elementarne) typy danych. <br> Mieszczą się w standardowych rejestrach.<br> Określają dokładny format zapisu zero-jedynkowego.

**Typ Danych**                              | **Rozmiar pamięci**                                               | **Charakterystyka i zasady użycia**
---                                         | ---                                                               | ---
**`BOOL`**                                  | 1 bit                                                             | Stan logiczny `TRUE` (1) lub `FALSE` (0).
**`BYTE`** <br> **`WORD`** <br> **`DWORD`** | 8 bitów (1 bajt) <br> 16 bitów (2 bajty) <br> 32 bity (4 bajty)   | Grupowanie bitów bez interpretacji matematycznej.<br> `WORD` (słowo) zajmuje 2 kolejne bajty (np. `%MW10`),<br> `DWORD` (podwójne słowo) zajmuje aż 4 bajty.
**`INT`** <br> **`DINT`**                   | 16 bitów <br> 32 bity                                             | Standardowe liczby całkowite ze znakiem (+/-).<br> (Występują też wersje bez znaku: `UINT` / `UDINT`).
**`REAL`**                                  | 32 bity                                                           | Liczba zmiennoprzecinkowa (ułamkowa).<br> Wymaga zawsze adresowania 32-bitowego (np. `%MD`).
**`CHAR`** <br> **`TIME`**                  | 8 bitów <br> Wartość w [ms]                                       | `CHAR` zajmuje pełny bajt dla 1 znaku ASCII.<br> `TIME` określa czas trwania (np. zapis `T#5s`).

### 2. Złożone (kompleksowe) typy danych

**Typ Złożony**             | **Główna cecha**                      | **Szczegóły i zastosowanie**
---                         | ---                                   | ---
**`STRING`**                | Łańcuch znaków ASCII                  | Domyślnie zajmuje **254 znaki + 2 bajty nagłówka**. Nagłówek przechowuje maksymalną i bieżącą długość ciągu.
**`ARRAY`** (Tablica)       | Zbiór elementów **tego samego typu**  | Umożliwia indeksowanie i masowe operacje na danych. Zapis np. `ARRAY[1..20] of INT` (20 pomiarów pod jedną nazwą).
**`STRUCT`** (Struktura)    | Zbiór elementów **różnych typów**     | Grupuje różne parametry w jeden logiczny obiekt. Np. "Silnik" zawiera `Start` (BOOL) oraz `Prąd` (REAL).
**`UDT`**                   | Typ zdefiniowany przez użytkownika    | Własny szablon z typów podstawowych lub złożonych. Pozwala powielać strukturę (np. dla 10 silników) bez konieczności ręcznego przepisywania parametrów.

### 3. Adresacja i zarządzanie pamięcią

**Zagadnienie**                         | **Zasada działania**                                                                          | **Zagrożenia i błędy**
---                                     | ---                                                                                           | ---
**Nakładanie się pamięci** (Overlap)    | Użycie typu `D` (Double) wymaga 4 bajtów. Adres `%MD80` zajmuje bajty: **80, 81, 82 i 83**.   | Deklaracja kolejnej zmiennej pod adresem np. `%MD83` nadpisze pamięć pierwszej zmiennej, powodując krytyczny błąd logiki programu.
**Konwersja typów** ("w dół")           | Zmiana formatu z większego na mniejszy, np. z typu `REAL` na typ `INT`.                       | Kompilator zezwala na operację, ale wiąże się to z **ucięciem miejsc po przecinku** i utratą precyzji.
**Brak operacji bezpośrednich**         | Dotyczy wyłącznie typów złożonych. (Znajdują się one w DB lub pamięci TEMP/STAT).             | Na całych tablicach lub strukturach nie można bezpośrednio wykonywać instrukcji matematycznych.

## 3. Programowanie strukturalne i typy bloków programowych

### 1. Bloki wykonawcze (OB, FC, FB)

**Typ Bloku**                   | **Główna cecha** | **Szczegóły i zasady działania**
---                             | ---                                                                      | ---
**`OB`** (Bloki organizacyjne)  | Interfejs między sprzętem,<br> systemem operacyjnym<br> a programem użytkownika. | **OB1 (Main):** Główna pętla skanowania,<br> działająca cyklicznie w nieskończoność<br> (jej czas definiuje "szybkość" sterownika).<br> To tutaj następuje wywoływanie (CALL)<br> innych bloków kodu. 
**Wyjątki:**                    | Bloki przerwań<br> np. blok First SCAN | Wykonywany wyłącznie jeden<br> raz przy starcie sterownika<br> (przejście ze stanu STOP do RUN),<br> służący do inicjalizacji zmiennych.
**`FC`** (Funkcje)              | Bloki kodu przeznaczone<br> do wykonywania konkretnych<br> algorytmów (np. skalowanie,<br> matematyka, powtarzalna prosta logika). | **Brak pamięci wewnętrznej:**<br> FC nie zapamiętuje stanów między cyklami programu.<br> Zmienne w sekcji `TEMP` są czyszczone po zakończeniu bloku.<br> Do przechowywania wyników musi używać zmiennych globalnych<br> (flagi `%M`, wyjścia `%Q`, lub dane z bloków `DB`).
**`FB`** (Bloki funkcyjne)      | Realizują programowanie<br> oparte na obiektowości.<br> Posiadają identyczne funkcje<br> algorytmiczne jak FC,<br> ale dysponują własną pamięcią trwałą. | Posiadają obszar zmiennych `Static`,<br> które nie ulegają skasowaniu po zakończeniu<br> cyklu skanowania sterownika. **Wielokrotne wywołanie:**<br> Raz napisany algorytm dla zaworu w bloku FB,<br> można wywołać w bloku OB1 X razy dla X fizycznych zaworów.<br> Konieczne jest tylko przypisanie<br> osobnego obszaru pamięci dla każdego z nich.

### 2. Bloki danych (DB) i konfiguracja pamięci

**Rodzaj / Opcja**                              | **Główna cecha**                                      | **Szczegóły i zastosowanie**
---                                             | ---                                                   | ---
**`DB`** (Bloki danych)                         | Służą wyłącznie do magazynowania wartości zmiennych.  | Nie zawierają logiki wykonawczej typu LAD/SCL.<br> Mogą przechowywać proste i złożone typy danych.
**Global DB**                                   | Zmienne globalne                                      | Dostępne jako wspólny magazyn dla całego projektu,<br> z którego może korzystać każdy inny blok.
**Instance DB**                                 | Pamięć instancyjna bloku FB                           | Generowane automatycznie podczas wywoływania bloków FB.<br> Tworzą dedykowane środowisko pamięci przypisane do konkretnej funkcji.
**Optymalizacja**<br> (Optimized block access)  | Zarządzanie sposobem dostępu CPU do pamięci           | Zaznaczona opcja przyspiesza dostęp CPU do pamięci.<br> Odznaczenie jej (stały offset) jest niezbędne<br> dla integracji ze starszymi zewnętrznymi panelami HMI,<br> które wymagają sztywnej adresacji.

## 4. Skalowanie wartości analogowych w PLC

### 1. Tor sygnałowy – od sprzętu do procesora

**Etap / Element**          | **Zasada działania**                                                                                  | **Szczegóły techniczne i diagnostyka**
---                         | ---                                                                                                   | ---
**Pomiar fizyczny**         | Czujnik (np. PT100) odbiera<br> wielkość fizyczną z obiektu.                                          | Przetwornik (Transmitter) konwertuje ją<br> na standard przemysłowy:<br> najczęściej pętlę prądową **4-20 mA** lub sygnał napięciowy **0-10 V**.
**Diagnostyka "Live Zero"** | Wartość fizycznego zera (np. 0 barów)<br> jest reprezentowana przez przepływ prądu 4 mA.              | Odczyt 0 mA jednoznacznie komunikuje sterownikowi<br> awarię przewodu lub czujnika (Underflow).<br> Dodatkowo pętla prądowa jest odporna na straty<br> wynikające z długości i rezystancji kabli.
**Konwersja ADC**           | Przetwornik analogowo-cyfrowy<br> w sterowniku transformuje<br> prąd/napięcie na typ całkowity `INT`. | Zależnie od rozdzielczości sterowników Siemens, standardowy,<br> w pełni prawidłowy sygnał daje zawsze<br> wynik liczbowy z zakresu **od 0 do 27648**.

### 2. Skalowanie programowe (Instrukcje matematyczne TIA Portal)

Obróbka surowej wartości z przetwornika (0–27648) na jednostki inżynierskie (np. bary, litry, stopnie).<br> Wymaga kaskadowego połączenia dwóch bloków systemowych:

**NORM_X (Normalizacja wartości)**                                                                          | **SCALE_X (Właściwe skalowanie)**
---                                                                                                         | ---
Sprowadza sygnał do wartości ułamkowej<br> (typ `REAL`).                                                    | Nakłada wartość procentową na faktyczną,<br> inżynierską skalę pomiarową czujnika.
Wejścia parametryzacji bloku<br> na stałe wpisane<br> `MIN = 0` oraz `MAX = 27648`.                         | Ułamek z bloku `NORM_X` (od 0.0 do 1.0)<br> trafia prosto na wejście<br> `VALUE` bloku `SCALE_X`.
Parametr `VALUE` odczytuje fizyczne<br> wejście sterownika<br> (np. `%IW10` w typie `INT`).                 | Programista deklaruje na wejściach<br> właściwości czujnika<br> (np. `MIN = 0.0`, `MAX = 100.0` dla zakresu temperatury 0-100 stopni).
Blok wylicza proporcję sygnału<br> i podaje na wyjście ułamek procentowy<br> w zakresie **od 0.0 do 1.0**.  | Na wyjściu `OUT` otrzymujemy przeskalowaną jednostkę inżynierską<br> (typ `REAL`, np. `45.5` °C),<br> którą używa się w logice komparatorów<br> lub wyświetla wprost na wizualizacji SCADA/HMI.