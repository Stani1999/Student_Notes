# Architektura Systemów Komputerowych

## Wykład 5: Techniki zwiększania wydajności procesora. Część I: pamięć podręczna.

### **1. Różnica między pamięciami DRAM a SRAM**

| **Cecha**               | **DRAM (Dynamic RAM)**                                                                | **SRAM (Static RAM)**                                                                |
|-------------------------|---------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| **Zasada działania**    | Przechowuje dane w postaci ładunków w kondensatorach. Wymaga okresowego odświeżania.  | Przechowuje dane w przerzutnikach (flip-flopach). Nie wymaga odświeżania.            |
| **Szybkość**            | Wolniejsza (ze względu na konieczność odświeżania i wyższe opóźnienia dostępu).       | Szybsza (dostęp do danych jest niemal natychmiastowy).                               |
| **Zużycie energii**     | Niższe (ale wymaga energii do odświeżania).                                           | Wyższe (ze względu na stałe zasilanie przerzutników).                                |
| **Gęstość upakowania**  | Wysoka (więcej komórek pamięci na jednostkę powierzchni).                             | Niska (mniej komórek pamięci na jednostkę powierzchni).                              |
| **Koszt**               | Tańsza w produkcji.                                                                   | Droższa w produkcji.                                                                 |
| **Zastosowanie**        | Pamięć operacyjna (RAM) w komputerach.                                                | Pamięć podręczna (cache) w procesorach.                                              |

#### **Podsumowanie różnicy:**
- **DRAM** jest wolniejsza, ale tańsza i bardziej gęsta, dlatego jest używana jako główna pamięć operacyjna.
- **SRAM** jest szybsza, ale droższa i mniej gęsta, dlatego jest używana w pamięciach podręcznych (cache), gdzie liczy się szybkość dostępu.

---

### **2. Zasada działania pamięci podręcznej (cache memory)**

Pamięć podręczna (cache) to szybka pamięć, która przechowuje kopie często używanych danych lub instrukcji, aby przyspieszyć dostęp do nich. Oto jej zasada działania:

#### **Poziomy pamięci podręcznej:**
| **Poziom**        | **Opis**                                                                                                                            |
| ------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| **L1 (Level 1)**  | - Najszybsza i najmniejsza pamięć podręczna.<br>- Zintegrowana bezpośrednio z rdzeniem procesora.<br>- Podzielona na **cache instrukcji** (przechowuje instrukcje) i **cache danych** (przechowuje dane). |
| **L2 (Level 2)**  | - Większa i wolniejsza niż L1, ale nadal bardzo szybka. <br> - Znajduje się blisko rdzenia procesora.                               |
| **L3 (Level 3):** | - Największa i najwolniejsza pamięć podręczna. <br> - Współdzielona przez wszystkie rdzenie procesora w systemach wielordzeniowych. |

#### **Zasada działania:**
1. **Przechowywanie danych:**
   - Gdy procesor potrzebuje danych, najpierw sprawdza, czy znajdują się one w pamięci podręcznej.
   - Jeśli dane są w cache (tzw. **trafienie, hit**), procesor pobiera je stamtąd, co jest znacznie szybsze niż dostęp do pamięci RAM.
   - Jeśli danych nie ma w cache (tzw. **chybienie, miss**), procesor pobiera je z pamięci RAM i zapisuje kopię w cache na przyszłość.

2. **Polityki zastępowania:**
   - Gdy pamięć podręczna jest pełna, nowe dane zastępują stare. Stosowane są różne algorytmy, np.:
     - **LRU (Least Recently Used):** Zastępowane są dane, które były najdłużej nieużywane.
     - **FIFO (First In, First Out):** Zastępowane są dane, które najdłużej znajdują się w cache.

3. **Lokalność danych:**
   - Pamięć podręczna wykorzystuje **lokalność przestrzenną** (dane znajdujące się blisko siebie są często używane razem) i **lokalność czasową** (te same dane są często używane wielokrotnie w krótkim czasie).

#### **Zalety pamięci podręcznej:**
- **Zmniejszenie opóźnień:** Skraca czas dostępu do danych, co przyspiesza działanie procesora.
- **Zmniejszenie obciążenia magistrali:** Redukuje liczbę odwołań do wolniejszej pamięci RAM.
- **Zwiększenie wydajności:** Pozwala na szybsze wykonywanie programów.

---

### **Podsumowanie**

1. **Różnica między DRAM a SRAM:**
   - DRAM jest wolniejsza, tańsza i bardziej gęsta, używana jako pamięć operacyjna.
   - SRAM jest szybsza, droższa i mniej gęsta, używana jako pamięć podręczna.

2. **Zasada działania pamięci podręcznej:**
   - Cache przechowuje kopie często używanych danych, aby przyspieszyć dostęp do nich.
   - Działa na zasadzie lokalności danych i wykorzystuje hierarchię poziomów (L1, L2, L3).

---

# Bibliografia

## Wykład 5:
Materiał bazowy, https://fulmanski.pl/zajecia/comp_sys_arch/zajecia_20242025/lecture_05_performance_enhancing_techniques_part_01.pdf