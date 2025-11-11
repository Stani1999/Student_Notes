# Architektura Systemów Komputerowych

## Wykład 6: Techniki zwiększania wydajności procesora. Część II: przetwarzanie potokowe.

### 1. **Idea przetwarzania potokowego (instruction pipelining)**

| **Cecha** | **Opis** |
|---|---|
| **Definicja** | Technika polegająca na podziale procesu wykonywania instrukcji na kilka etapów (np. pobranie instrukcji, dekodowanie, wykonanie, zapis wyników). |
| **Działanie** | Instrukcje są przetwarzane "potokowo" - w tym samym czasie, różne instrukcje znajdują się na różnych etapach potoku.<br>Podczas gdy jedna instrukcja jest w fazie wykonywania, kolejna może być pobierana, a jeszcze kolejna dekodowana. |
| **Etapy potoku (przykład)** | - **Pobranie instrukcji (Instruction Fetch - IF):** Pobranie instrukcji z pamięci. <br> - **Dekodowanie instrukcji (Instruction Decode - ID):** Rozpoznanie rodzaju instrukcji i przygotowanie argumentów. <br> - **Wykonanie (Execute - EX):** Wykonanie operacji arytmetycznych lub logicznych. <br> - **Dostęp do pamięci (Memory Access - MEM):** Odczyt lub zapis danych z/do pamięci (opcjonalne). <br> - **Zapis wyników (Write Back - WB):** Zapisanie wyniku do rejestru. |
| **Korzyści** | - **Zwiększona przepustowość:** Wzrost liczby instrukcji wykonywanych w jednostce czasu. <br> - **Wyższa wydajność:** Skrócenie czasu potrzebnego na wykonanie wielu instrukcji. <br> - **Lepsze wykorzystanie zasobów procesora:** Równoległe wykorzystanie różnych jednostek funkcjonalnych. |
| **Przykład** | Wyobraźmy sobie linię produkcyjną, gdzie na różnych etapach powstaje samochód.<br>Podobnie w potoku procesora, instrukcje "przechodzą" przez kolejne etapy, będąc przetwarzane równolegle. |

**Dodatkowe informacje:**

*   Przetwarzanie potokowe jest kluczową techniką stosowaną w nowoczesnych procesorach w celu zwiększenia ich wydajności.
*   W praktyce, potoki mogą mieć różną liczbę etapów, a ich implementacja jest bardziej złożona, uwzględniając m.in. zależności między instrukcjami (tzw. hazardy).
*   Efektywność potoku zależy od wielu czynników, takich jak długość potoku, rodzaj wykonywanych instrukcji i optymalizacja oprogramowania.

---

### 2. **Różnica między procesorem skalarnym a superskalarnym**

| **Rodzaj procesora**        | **Opis**                                                                                                                                            |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| **Procesor skalarny**:      | Może wykonywać tylko jedną instrukcję w danym momencie (choć może być podzielona na etapy potokowe).                                                |
| **Procesor superskalarny**: | Może wykonywać wiele instrukcji jednocześnie, wykorzystując wiele jednostek wykonawczych (np. kilka jednostek arytmetycznych).<br>Procesor dynamicznie analizuje zależności między instrukcjami i planuje ich równoległe wykonanie. |

---

### 3. **Zjawisko pipeline hazard**
| **Zjawizko**            | **Opis**                                                                                                             |
|-------------------------|----------------------------------------------------------------------------------------------------------------------|
| **Pipeline hazard**     | To sytuacja, w której przetwarzanie potokowe zostaje wstrzymane z powodu konfliktu. Wyróżnia się trzy typy hazardów: |
| **Hazard strukturalny** | Brak zasobów (np. dwóch instrukcji próbujących jednocześnie użyć tej samej jednostki wykonawczej).                   |
| **Hazard danych**       | Instrukcja zależy od wyniku innej instrukcji, który nie jest jeszcze dostępny.                                       |
| **Hazard sterowania**   | Wynika ze zmiany kolejności wykonywania instrukcji (np. skoki warunkowe).                                            |

---

### 4. Wykonanie instrukcji poza kolejnością (out-of-order execution)

| **Cecha**        | **Opis**                                                                                                                                                                                |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Definicja**    | Technika, w której procesor dynamicznie zmienia kolejność wykonywania instrukcji,<br> aby zminimalizować przestoje spowodowane oczekiwaniem na dane (hazardy).                          |
| **Działanie**    | Procesor analizuje zależności między instrukcjami.<br>Instrukcje, które nie zależą od wyników wcześniejszych, mogą być wykonywane wcześniej, nawet jeśli w programie występują później. |
| **Warunki** | Zachowanie semantyki programu - wynik musi być identyczny, jak przy sekwencyjnym wykonaniu instrukcji.<br>Zmiana kolejności jest możliwa tylko wtedy, gdy nie wpływa na poprawność obliczeń. |
| **Korzyści**     | Zwiększenie wydajności poprzez lepsze wykorzystanie potoku procesora.<br> Unikanie przestojów i oczekiwania na dane.                                                                    |
| **Ograniczenia** | Zwiększona złożoność procesora.<br>Potrzeba śledzenia zależności między instrukcjami i zarządzania ich kolejnością.                                                                     |

**Dodatkowe informacje:**

*   Wykonanie poza kolejnością jest powszechnie stosowane w nowoczesnych procesorach.
*   Technika ta współdziała z innymi mechanizmami, takimi jak potokowanie i przewidywanie rozgałęzień<br> (branch predictor, np. **układ przewidywania skoków**), aby jeszcze bardziej zwiększyć wydajność.
*   Procesor musi być w stanie cofnąć zmiany, jeśli okaże się, że instrukcja wykonana poza kolejnością była jednak zależna od wcześniejszych.

---

### 5. Właściwości układu przewidywaia skoków, implementowanego w nowoczesnych procesorach.

| **Cecha**                      | **Opis**                                                                                                   |
|--------------------------------|------------------------------------------------------------------------------------------------------------|
| **Definicja**                  | Odpowiada za przewidywanie, czy wystąpi skok, minimalizując straty wynikające z błędnych przewidywań.      |
| **Rodzaje skoków**             | Skoki mogą być bezwarunkowe (adres skoku znany) lub warunkowe (adres znany, ale warunek oceniany później). |
| **Metody przewidywania**       | 1. **Przewidywanie statyczne** – najprostsza metoda, zakładająca, że skok: <br> - zawsze zajdzie (60% skuteczności), <br> - skok wsteczny zajdzie, a w przód nie (65% skuteczności). <br> 2. **Przewidywanie dynamiczne** – bazuje na historii skoków zapisanej w tablicach. |
| **Tablica historii skoków**    | Zawiera informacje o poprzednich skokach: <br> - 1-bitowa historia (czy skok zaszedł ostatnio), <br> - 2-bitowa historia (bardziej szczegółowa historia skoków), <br> - liczba wpisów: 128-1024, <br> - dodatkowe informacje: bity statusu, adres instrukcji wywołującej skok, adres skoku. |
| **Problem skoków warunkowych** | Warunek skoku obliczany jest dopiero na etapie wykonania rozkazu, co wymusza spekulacyjne wykonywanie instrukcji po skoku. <br> Błędne przewidywanie skoku prowadzi do opróżnienia potoku i kasowania niepotrzebnie wykonanych instrukcji, co powoduje opóźnienia. |
| **Skuteczność nowoczesnych układów** | Przekracza 98%, dzięki zaawansowanym technikom przewidywania. |

### 6. **Przemianowanie rejestrów (register renaming)**

| **Cecha**           | **Opis**                                                                                                                   |
|---------------------|----------------------------------------------------------------------------------------------------------------------------|
| **Definicja**       | Technika ta polega na dynamicznym przypisywaniu fizycznych rejestrów do rejestrów logicznych (widocznych dla programisty). |
| **Korzyści**        | Pozwala to uniknąć hazardów danych, gdy wiele instrukcji próbuje użyć tego samego rejestru logicznego.                     |
| **Sposób dziłania** | Procesor przypisuje tymczasowe rejestry fizyczne, co umożliwia równoległe wykonywanie instrukcji bez konfliktów.           |

---

### 7. **Simultaneous multithreading (SMT)**

| **Cecha**     | **Opis**                                                                                                                                            |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| **Definicja** | SMT to technika, w której jeden procesor fizyczny symuluje wiele wątków poprzez równoczesne wykonywanie instrukcji z różnych wątków na tych samych jednostkach wykonawczych. | 
| **Przykład**  | Technologia Hyper-Threading firmy Intel, która pozwala na równoczesne przetwarzanie wielu wątków na jednym rdzeniu.                                 |

---

### 8. **Przetwarzanie typu SIMD (single instruction, multiple data)**

| **Cecha**        | **Opis**                                                                                                                                            |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| **Definicja**    | SIMD to technika, w której jedna instrukcja jest wykonywana na wielu danych jednocześnie.                                                           | 
| **Specyfikacja** | Procesor posiada specjalne rejestry i jednostki wykonawcze, które mogą przetwarzać wektory danych (np. 4 liczby zmiennoprzecinkowe) w jednym cyklu. |
| **Przykłady rozszerzeń SIMD** | SSE, AVX (x86) czy NEON (ARM).                                                                                                         |
| **Zastosowanie** | Aplikacje wymagających przetwarzania dużych zbiorów danych, takich jak grafika, multimedia czy obliczenia naukowe.                                  |

---

# Bibliografia

## Wykład 6:
Materiał bazowy, https://fulmanski.pl/zajecia/comp_sys_arch/zajecia_20242025/lecture_06_performance_enhancing_techniques_part_02.pdf
<br> Układ przewidywania skoków, https://esezam.okno.pw.edu.pl/mod/book/view.php?id=51&chapterid=1083