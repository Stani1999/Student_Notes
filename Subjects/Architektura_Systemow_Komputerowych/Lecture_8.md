# Architektura Systemów Komputerowych

## Wykład 8: Współczesna architektury procesorów i zestawy instrukcji. Procesory typu CISC na przykładzie rodziny x86 oraz x64

### 1. **CISC (Complex Instruction Set Computing)**

Architektura CISC charakteryzuje się:
| **Cecha**                                         | **Opis**                                                                                                                             |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| **Bogatym zestawem instrukcji**                   | Zawiera wiele złożonych instrukcji, które mogą wykonywać skomplikowane operacje w jednym rozkazie.                                   |
| **Różnorodnymi trybami adresowania**              | Umożliwia dostęp do danych na wiele sposobów, np. bezpośrednio, pośrednio, przez rejestry itp.                                       |
| **Zmienną długością instrukcji**                  | Instrukcje mogą mieć różną liczbę bajtów, co zapewnia elastyczność, ale komplikuje dekodowanie.                                      |
| **Instrukcje działające bezpośrednio na pamięci** | W CISC wiele instrukcji może operować bezpośrednio na danych w pamięci, zamiast wymagać ich wcześniejszego załadowania do rejestrów. |

---

### 2. **Architektura x86 jako przykład CISC**

Architektura x86 jest klasycznym przykładem CISC. Jej główne cechy to:
| **Cecha**                           | **Opis**                                                                                                                   |  
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------|  
| **Rozbudowany zestaw instrukcji**   | Zawiera setki instrukcji, w tym do operacji na łańcuchach znaków, arytmetyki zmiennoprzecinkowej czy zarządzania pamięcią. |  
| **Różne tryby adresowania**         | Obsługuje tryby adresowania takie jak bezpośrednie, pośrednie, rejestrowe, indeksowane i inne.                             |
| **Zmienna długość instrukcji**      | Instrukcje mogą mieć od 1 do 15 bajtów, co zapewnia elastyczność, ale wymaga skomplikowanego dekodera.                     |
| **Instrukcje operujące na pamięci** | Wiele instrukcji może działać bezpośrednio na danych w pamięci, np. `ADD [adres], wartość`.                                |

---

### 3. **Zestaw rozkazów x86**

Zestaw rozkazów x86 jest bardzo rozbudowany i obejmuje:
| **Instrukcje**                    | **Przykłady** |  
|-----------------------------------|---------------|  
| **Arytmetyczne i logiczne**       | `ADD`, `SUB`  |  
| **Sterujące przepływem programu** | `JMP`, `CALL` |  
| **Operujące na pamięci**          | `MOV`, `PUSH` |  
| **Wejścia/wyjścia**               | `IN`, `OUT`   |  
| **Specjalne**                     | `INT`, `HLT`  |  

**Legenda:**  
- `ADD` – dodawanie wartości  
- `SUB` – odejmowanie wartości  
- `JMP` – skok do innej części kodu  
- `CALL` – wywołanie procedury  
- `MOV` – przenoszenie danych  
- `PUSH` – zapis na stos  
- `IN` – odczyt danych z portu wejściowego  
- `OUT` – zapis danych do portu wyjściowego  
- `INT` – wywołanie przerwania  
- `HLT` – zatrzymanie procesora

---

### 4. **Zalety i wady CISC/x86**
| **Zalety** | **Wady** |  
|------------|----------|  
| - Bogaty zestaw instrukcji ułatwia programowanie na wysokim poziomie. <br> - Złożone instrukcje mogą zmniejszyć liczbę rozkazów potrzebnych do wykonania zadania. <br> - Elastyczność w zarządzaniu pamięcią i danymi. | - Skomplikowana implementacja sprzętowa (dekodowanie instrukcji, zarządzanie pamięcią). <br> - Większe zużycie energii i generowanie ciepła. <br> - Trudność w optymalizacji pod kątem wydajności. |

---

### 5. **Podsumowanie**
Architektura CISC, reprezentowana przez x86, jest zorientowana na bogaty zestaw instrukcji i elastyczność programowania. Mimo że jest bardziej złożona niż architektury RISC, pozostaje dominująca w komputerach osobistych i serwerach ze względu na kompatybilność wsteczną i szerokie wsparcie oprogramowania.

---

# Bibliografia

## Wykład 8:
Materiał bazowy, https://fulmanski.pl/zajecia/comp_sys_arch/zajecia_20242025/lecture_08_modern_processor_architectures_and_instruction_sets_cisc_x86.pdf