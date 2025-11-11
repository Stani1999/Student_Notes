# Architektura Systemów Komputerowych

## Wykład 7: Współczesna architektury procesorów i zestawy instrukcji. Część I.

### **1. Tryby adresowania**
Tryby adresowania określają, w jaki sposób procesor oblicza adres operandu (danych) dla instrukcji. Różne tryby adresowania są używane w zależności od potrzeb programisty i optymalizacji dostępu do danych.

**Wyszczegulniono je w poniższej tabeli:**

| Tryb adresowania | Opis | Przykład | Zasadność | Dodatkowe informacje |
|---|---|---|---|---|
| **Adresowanie bezpośrednie (Direct Addressing)** | Adres operandu jest podany bezpośrednio w instrukcji. | `MOV AX, [1234h]` - ładuje wartość z pamięci pod adresem 1234h do rejestru AX. | Proste i szybkie, ale ograniczone do stałych adresów, co zmniejsza elastyczność. | Używane do dostępu do zmiennych globalnych lub stałych. |
| **Adresowanie pośrednie (Indirect Addressing)** | Adres operandu jest przechowywany w rejestrze. | `MOV AX, [BX]` - ładuje wartość z pamięci pod adresem wskazywanym przez rejestr BX do rejestru AX. | Pozwala na dynamiczne obliczanie adresów, co zwiększa elastyczność programu. | Używane do przetwarzania tablic, list i innych struktur danych. |
| **Adresowanie rejestrowe (Register Addressing)** | Operand znajduje się bezpośrednio w rejestrze. | `MOV AX, BX` - kopiuje wartość z rejestru BX do rejestru AX. | Bardzo szybkie, ponieważ nie wymaga dostępu do pamięci. | Używane do operacji na danych, które są już w rejestrach. |
| **Adresowanie bezpośrednio-rejestrowe (Register Indirect with Offset)** | Adres operandu jest obliczany jako suma wartości rejestru i stałej wartości (offsetu). | `MOV AX, [BX+10h]` - ładuje wartość z pamięci pod adresem BX + 10h do rejestru AX. | Umożliwia dostęp do elementów tablicy lub struktur danych. | Używane do dostępu do pól struktur danych lub elementów tablicy o znanym przesunięciu. |
| **Adresowanie indeksowe (Indexed Addressing)** | Adres operandu jest obliczany jako suma wartości rejestru bazowego i rejestru indeksowego. | `MOV AX, [BX+SI]` - ładuje wartość z pamięci pod adresem BX + SI do rejestru AX. | Przydatne w iteracji po tablicach lub listach. | Używane do przetwarzania tablic, gdzie indeks jest przechowywany w rejestrze indeksowym. |
| **Adresowanie względne (Relative Addressing)** | Adres operandu jest obliczany jako suma wartości licznika programu (PC) i stałej wartości (offsetu). | Skoki warunkowe, np. `JMP 10h` - skok do adresu PC + 10h. | Używane głównie w instrukcjach skoków, umożliwia tworzenie przenośnego kodu. | Używane do implementacji pętli, instrukcji warunkowych i procedur. |
| **Adresowanie natychmiastowe (Immediate Addressing)** | Operand jest stałą wartością podaną bezpośrednio w instrukcji. | `MOV AX, 1234h` - ładuje wartość 1234h do rejestru AX. | Szybkie i proste, ale ograniczone do stałych wartości. | Używane do inicjalizacji zmiennych lub stałych. |
| **Adresowanie bazowe (Base Addressing)** | Adres operandu jest obliczany jako suma wartości rejestru bazowego i stałej wartości (offsetu). | `MOV AX, [BP+10h]` - ładuje wartość z pamięci pod adresem BP + 10h do rejestru AX. | Używane w operacjach na stosie lub strukturach danych. | Używane do dostępu do zmiennych lokalnych w procedurach. |
| **Adresowanie bazowo-indeksowe (Base-Indexed Addressing)** | Adres operandu jest obliczany jako suma wartości rejestru bazowego, rejestru indeksowego i stałej wartości (offsetu). | `MOV AX, [BX+SI+10h]` - ładuje wartość z pamięci pod adresem BX + SI + 10h do rejestru AX. | Umożliwia dostęp do złożonych struktur danych, takich jak tablice wielowymiarowe. | Używane do przetwarzania tablic wielowymiarowych lub list struktur. |
| **Adresowanie stosowe (Stack Addressing)** | Operandy są pobierane lub zapisywane na stosie. | `PUSH AX` - zapisuje wartość rejestru AX na stosie. | Używane w operacjach wywoływania funkcji i zarządzania zmiennymi lokalnymi. | Używane do przekazywania argumentów do funkcji i przechowywania zmiennych lokalnych. |

---

### **2. Zasadność obecności różnych trybów adresowania**

| Aspekt                  | Opis                                                                                                  |
|-------------------------|-------------------------------------------------------------------------------------------------------|
| **Elastyczność**        | Różne tryby adresowania pozwalają programistom efektywnie zarządzać pamięcią i danymi.                |
| **Optymalizacja**       | Niektóre tryby są szybsze (np. rejestrowe), podczas gdy inne są bardziej uniwersalne (np. pośrednie). |
| **Złożoność programów** | Umożliwiają implementację zaawansowanych struktur danych i algorytmów.                                |
| **Kompatybilność**      | Wsparcie dla różnych trybów adresowania pozwala na zachowanie zgodności z istniejącym kodem.          |
| **Uwaga**               | Nie wszystkie tryby adresowania są dostępne we wszystkich architekturach procesorów.                  |

---

### **3. Wpływ liczby adresów w instrukcjach na język maszynowy**

| Rodzaj instrukcji                | Format                     | Przykład            | Zalety | Wady |
|----------------------------------|----------------------------|---------------------|--------|------|
| **Instrukcje z trzema adresami** | `instrukcja adres1, adres2, adres3` | `ADD R1, R2, R3` – dodaje wartości z R2 i R3, wynik zapisuje w R1. | Bardzo elastyczne, pozwalają na wykonywanie złożonych operacji w jednej instrukcji. | Wymagają dłuższych instrukcji, zwiększają rozmiar kodu maszynowego i zużycie pamięci. |
| **Instrukcje z dwoma adresami** | `instrukcja adres1, adres2` | `ADD R1, R2` – dodaje wartość z R2 do R1, wynik zapisuje w R1. | Mniejsze rozmiary instrukcji, bardziej efektywne wykorzystanie pamięci. | Wymagają więcej instrukcji do wykonania złożonych operacji. |
| **Instrukcje z jednym adresem** | `instrukcja adres1` | `LOAD R1` – ładuje wartość z pamięci do rejestru R1. | Bardzo krótkie instrukcje, oszczędność pamięci. | Wymagają więcej instrukcji do wykonania prostych operacji, co może zwiększyć czas wykonania programu. |
| **Instrukcje bezadresowe (stosowe)** | `instrukcja` | `ADD` – dodaje dwie wartości ze szczytu stosu. | Bardzo krótkie instrukcje, prosta implementacja. | Ograniczona elastyczność, trudniejsze programowanie. |

### **4. Problemy i kompromisy związane z projektowaniem formatu instrukcji**

| Problem                | Opis                                                                             | Kompromis                                                                                                       |
|------------------------|----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| **Długość instrukcji** | Dłuższe instrukcje (np. z trzema adresami) zwiększają rozmiar kodu maszynowego.  | Skrócenie instrukcji zmniejsza rozmiar kodu, ale wymaga więcej instrukcji do wykonania tej samej operacji.      |
| **Liczba rejestrów**           | Większa liczba rejestrów wymaga więcej bitów do ich adresowania.         | Ograniczenie liczby rejestrów upraszcza instrukcje, ale może wymagać częstszego dostępu do pamięci.             |
| **Złożoność dekodowania instrukcji** | Złożone formaty instrukcji wymagają bardziej skomplikowanej jednostki dekodującej. | Uproszczenie formatu instrukcji ułatwia dekodowanie, ale może ograniczać funkcjonalność.        |
| **Wydajność wykonania**        | Instrukcje z wieloma adresami mogą wymagać większej liczby cykli do wykonania. | Optymalizacja pod kątem szybkiego wykonania prostych instrukcji kosztem elastyczności.                    |
| **Kompatybilność wsteczna**    | Nowe formaty instrukcji muszą być zgodne z istniejącym oprogramowaniem. | Zachowanie wsparcia dla starszych instrukcji zwiększa złożoność procesora.                                       |
| **Optymalizacja pod kątem pamięci podręcznej** | Krótsze instrukcje lepiej wykorzystują pamięć podręczną, ale mogą wymagać więcej instrukcji. | Wybór formatu instrukcji, który równoważy rozmiar kodu i liczbę instrukcji. |
| **Elastyczność programowania** | Proste formaty instrukcji (np. bezadresowe) mogą utrudniać programowanie. | Bardziej złożone instrukcje ułatwiają programowanie, ale zwiększają złożoność sprzętu.                         |

### **Podsumowanie**
- Liczba adresów w instrukcjach wpływa na elastyczność, rozmiar kodu maszynowego i wydajność wykonania.
- Projektowanie formatu instrukcji wymaga znalezienia równowagi między złożonością sprzętu, wydajnością a łatwością programowania.
- Każda architektura procesora musi uwzględniać te kompromisy, aby zapewnić optymalne działanie w różnych zastosowaniach.

---

# Bibliografia

## Wykład 7:
Materiał bazowy, https://fulmanski.pl/zajecia/comp_sys_arch/zajecia_20242025/lecture_07_modern_processor_architectures_and_instruction_sets_part_01_02.pdf