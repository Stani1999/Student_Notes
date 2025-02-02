# Architektura Systemów Komputerowych

## Wykład 1: Ewolucja urządzeń automatyzujących proces liczenia.

| **Okres**       | **Urządzenie / Wynalazek**                | **Opis**                                                                                                                                                 |
|-----------------|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| **XIX wiek**    | **Maszyna Analityczna** (Charles Babbage) | Pierwszy projekt ogólnego, programowalnego urządzenia obliczeniowego. Mechaniczna konstrukcja, programowanie za pomocą kart perforowanych.               |
| **1889**        | **Maszyna Holleritha**                    | Używana do przetwarzania danych spisowych w USA. Wykorzystywała karty perforowane do przechowywania i przetwarzania danych.                              |
| **1937**        | **Model teoretyczny maszyny Turinga**     | Alan Turing zaproponował abstrakcyjny model maszyny obliczeniowej, który stał się podstawą teorii obliczeń.                                              |
| **1941**        | **Z3 (Konrad Zuse)**                      | Pierwszy programowalny komputer cyfrowy, zbudowany przez Konrada Zuse. Działał na podstawie instrukcji zapisanych na taśmie perforowanej.                |
| **1945**        | **ENIAC** (Electronic Numerical Integrator and Computer) | Pierwszy programowalny komputer elektroniczny. Zajmował 167 m², używał 17 000 lamp próżniowych.                                           |
| **1947**        | **Tranzystor** (wynaleziony przez Bardeena, Brattaina i Shockleya) | Zastąpił lampy próżniowe – mniejszy, szybszy, bardziej energooszczędny i niezawodny.                                            |
| **1958**        | **Układ scalony** (Jack Kilby, Texas Instruments) | Miniaturyzacja komponentów elektronicznych na jednym chipie krzemowym.                                                                           |
| **1965**        | **Prawo Moore'a**                         | Obserwacja, że liczba tranzystorów w układach scalonych podwaja się co 18-24 miesięcy, prowadząc do wykładniczego wzrostu mocy obliczeniowej.            |
| **1971**        | **Intel 4004** (pierwszy mikroprocesor)   | Pierwszy komercyjny mikroprocesor (4-bitowy), zapoczątkował rozwój nowoczesnych komputerów.                                                              |
| **1981**        | **IBM PC (IBM 5150)**                     | Pierwszy komputer osobisty (PC) firmy IBM, który stał się standardem dla rynku komputerów osobistych. Wykorzystywał procesor Intel 8088 i system MS-DOS. |
| **1982**        | **Intel 80286**                           | Znacznie zwiększył wydajność komputerów PC oraz umożliwił pracę w **trybie chronionym**, co pozwalało na wielozadaniowość i lepsze zarządzanie pamięcią. |
| **1985** | **Intel 80386** | Pierwszy 32-bitowy procesor, który wprowadził **zaawansowane zarządzanie pamięcią** i **wielozadaniowość**,kładąc fundamenty pod nowoczesne systemy operacyjne, jak Windows. Był podstawą komputerów osobistych pod koniec lat 80. i na początku 90. |
| **2007**        | **iPhone** (Apple)                        | Pierwszy iPhone zrewolucjonizował rynek telefonów komórkowych, wprowadzając nowoczesne smartfony z ekranem dotykowym i dostępem do Internetu.            |
| **2023**        | **Procesor A17 Bionic** (Apple)           | Najnowszy procesor firmy Apple, wykorzystywany w iPhone'ach 15. Zbudowany w technologii 3 nm, oferuje ogromną moc obliczeniową i energooszczędność.      |
| **XXI wiek**    | **Komputery kwantowe**                    | Obecnie rozwijana technologia, która wykorzystuje zjawiska mechaniki kwantowej do przetwarzania danych. Obiecują ogromny wzrost mocy obliczeniowej.      |

---

### **Wyjaśnienie prawa Moore'a:**
Prawo Moore'a to obserwacja sformułowana przez Gordona Moore'a w 1965 roku, która stwierdza, że **liczba tranzystorów w układach scalonych podwaja się mniej więcej co 18-24 miesięcy**. To prawo przez dziesięciolecia napędzało postęp technologiczny, umożliwiając miniaturyzację, zwiększenie wydajności i obniżenie kosztów produkcji układów scalonych. Obecnie obserwuje się spowolnienie tempa wzrostu zgodnego z prawem Moore'a ze względu na fizyczne ograniczenia technologii krzemowej.

Prawo Moore'a było przez wiele lat motorem postępu w branży półprzewodników, umożliwiając rozwój coraz wydajniejszych i tańszych urządzeń elektronicznych. Jednak w ostatnich latach tempo tego postępu zaczyna zwalniać, co wynika z coraz większych trudności technologicznych i kosztów związanych z dalszym miniaturyzacją tranzystorów.

---

## Wykład 2: Podstawowe informacje o architekturach procesorów i pamięci.

### 1. Architektura von Neumanna i Harwardzka

| **Cecha**               | **Architektura von Neumanna**                                           | **Architektura Harwardzka**                                   |
|-------------------------|-------------------------------------------------------------------------|---------------------------------------------------------------|
| **Struktura pamięci**   | Wspólna pamięć dla danych i instrukcji                                  | Oddzielna pamięć dla danych i instrukcji                      |
| **Magistrala**          | Wspólna magistrala dla danych i instrukcji (wąskie gardło von Neumanna) | Oddzielne magistrale dla danych i instrukcji                  |
| **Przetwarzanie**       | Instrukcje i dane przetwarzane sekwencyjnie                             | Możliwe jednoczesne pobieranie instrukcji i danych            |
| **Wydajność**           | Niższa, ograniczona przez współdzieloną magistralę                      | Wyższa, dzięki równoczesnemu dostępowi do pamięci             |
| **Zastosowanie**        | Komputery ogólnego przeznaczenia (PC, laptopy, serwery)                 | Systemy wbudowane, procesory sygnałowe (DSP), mikrokontrolery |
| **Elastyczność**        | Łatwiejsza implementacja i programowanie                                | Bardziej złożona budowa i trudniejsza implementacja           |

---

### 2. Pamięć wirtualna i stronicowanie pamięci

Pamięć wirtualna i stronicowanie to kluczowe mechanizmy zarządzania pamięcią, które umożliwiają efektywne i bezpieczne korzystanie z zasobów pamięci komputera. Dzięki nim możliwe jest uruchamianie dużych programów, wielozadaniowość oraz ochrona pamięci przed nieautoryzowanym dostępem.


| **Koncepcja**            | **Definicja**                                                                                                                                 | **Działanie**                                                                                                                                                                              | **Zalety**                                                                                                                |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| **Pamięć wirtualna**     | Mechanizm zarządzania pamięcią, który daje procesom wrażenie posiadania dużej, ciągłej przestrzeni adresowej, niezależnie od fizycznej dostępności pamięci RAM. | System operacyjny mapuje adresy wirtualne na fizyczne, umożliwiając uruchamianie programów większych niż dostępna pamięć fizyczna oraz izolację procesów.                | Umożliwia uruchamianie dużych programów, efektywne wykorzystanie pamięci RAM, izolację procesów i ochronę pamięci.        |
| **Stronicowanie pamięci**| Technika zarządzania pamięcią polegająca na podziale przestrzeni adresowej na równe bloki zwane stronami. | Pamięć wirtualna i fizyczna są dzielone na strony o stałym rozmiarze. Gdy proces potrzebuje dostępu do strony, która nie znajduje się w pamięci RAM, następuje przerwanie stronicowania, a system operacyjny ładuje odpowiednią stronę z pamięci masowej do RAM. | Eliminuje problem fragmentacji zewnętrznej i umożliwia efektywne wykorzystanie pamięci. |

---

### Dodatkowe informacje

- **Fragmentacja zewnętrzna**: Występuje, gdy wolna pamięć jest rozproszona w małych częściach, które są zbyt małe, aby pomieścić większe procesy, mimo że całkowita dostępna pamięć jest wystarczająca. Stronicowanie pomaga uniknąć tego problemu, ponieważ strony pamięci są alokowane dynamicznie i mogą być rozproszone w różnych miejscach pamięci fizycznej.
- **Przerwanie stronicowania (page fault)**: Sytuacja, w której proces próbuje uzyskać dostęp do strony, która nie znajduje się aktualnie w pamięci RAM. W takim przypadku system operacyjny musi załadować brakującą stronę z pamięci masowej (np. dysku twardego) do pamięci RAM, co powoduje pewne opóźnienie.
- **Algorytmy zastępowania stron**: System operacyjny stosuje różne algorytmy (np. FIFO, LRU), aby zdecydować, która strona powinna zostać usunięta z pamięci RAM, gdy potrzebne jest miejsce dla nowej strony.


 
### **Sposoby adresacji pamięci**

| **Tryb adresowania**          | **Opis**                                                                                            |
|-------------------------------|-----------------------------------------------------------------------------------------------------|
| **Bezpośrednie** (Direct)     | Adresowanie, w którym procesor bezpośrednio odnosi się do fizycznego adresu pamięci.                |
| **Pośrednie** (Indirect)      | Adresowanie, w którym procesor wskazuje adres wirtualny, a system operacyjny mapuje go na fizyczny. |
| **Indeksowane** (Indexed)     | Procesor używa dwóch adresów (np. bazowego i indeksowego), aby obliczyć adres pamięci wirtualnej.   |

### **Korzyści z pamięci wirtualnej i stronicowania**:
- **Elastyczność** – programy mogą być większe niż dostępna fizyczna pamięć RAM (pages and swaps).
- **Ochrona pamięci** – każde proces działa w swojej wirtualnej przestrzeni adresowej, izolując je od siebie (proces "myśli", że tylko one jest używamy).
- **Efektywne zarządzanie pamięcią** – tylko te strony, które są aktualnie potrzebne, są załadowane do pamięci, brak duplikatów.

---

# Bibliografia

## Wykład 1:
1. Materiał bazowy, https://fulmanski.pl/zajecia/comp_sys_arch/zajecia_20242025/lecture_01_evolution_of_automated_computing_devices.pdf
2. Prawo Moore'a, https://www.intel.com/content/www/us/en/newsroom/resources/moores-law.html?utm_source
## Wykład 2:
1. Materiał bazowy, https://fulmanski.pl/zajecia/comp_sys_arch/zajecia_20242025/lecture_02_processor_and_memory_architectures.pdf