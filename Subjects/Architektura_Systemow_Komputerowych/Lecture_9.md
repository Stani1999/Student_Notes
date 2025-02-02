# Architektura Systemów Komputerowych

## Wykład 9: Współczesna architektury procesorów i zestawy instrukcji. Procesory typu RISC.

### 1. **RISC (Reduced Instruction Set Computing)**
Architektura RISC charakteryzuje się:
| **Cecha**                                        | **Opis**                                                                                                                                         |
|--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| **Prosty zestaw instrukcji**                     | RISC zawiera niewiele podstawowych instrukcji, które są wykonywane bardzo szybko.                                                                |
| **Stała długość instrukcji**                     | Większość instrukcji ma stałą długość (np. 32 bity), co upraszcza dekodowanie.                                                                   |
| **Wykonywanie instrukcji w jednym cyklu zegara** | Proste instrukcje są wykonywane w jednym cyklu procesora.                                                                                        |
| **Load/Store Architecture** | Operacje arytmetyczne i logiczne wykonywane są na rejestrach, a dane są ładowane lub zapisywane do pamięci tylko za pomocą specjalnych instrukcji (np. `LDR`, `STR`). |
| **Duża liczba rejestrów**                        | RISC zazwyczaj ma więcej rejestrów niż CISC, co zmniejsza konieczność częstego dostępu do pamięci.                                               |

---

### 2. **Architektura ARM jako przykład RISC**
Architektura ARM jest jednym z najpopularniejszych przykładów RISC. Jej główne cechy to:
| **Cecha**                    | **Opis**                                                                                                                             |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| **Prosty zestaw instrukcji** | ARM zawiera podstawowe instrukcje, łatwe do zaimplementowania w sprzęcie.                                                            |
| **Stała długość instrukcji** | Większość instrukcji ARM ma 32 bity (w starszych wersjach) lub 16 bitów w trybie Thumb.                                              |
| **Load/Store Architecture**  | Operacje arytmetyczne i logiczne wykonywane są tylko na rejestrach, dostęp do pamięci przez instrukcje `LDR` (load) i `STR` (store). |
| **Duża liczba rejestrów**    | ARM ma 16 rejestrów ogólnego przeznaczenia (R0-R15), co zmniejsza zależność od pamięci.                                              |
| **Efektywność energetyczna** | ARM zaprojektowany z myślą o niskim zużyciu energii, idealny do urządzeń mobilnych.                                                  |

---

### 3. **Zestaw rozkazów ARM**
Zestaw rozkazów ARM jest prosty i zoptymalizowany. Obejmuje:
| **Instrukcje**                               | **Przykłady**                                                                 |
|----------------------------------------------|-------------------------------------------------------------------------------|
| **Instrukcje arytmetyczne i logiczne**       | `ADD`, `SUB`, `MUL`, `AND`, `ORR`, `EOR`                                      |
| **Instrukcje sterujące przepływem programu** | `B` (branch), `BL` (branch with link), `BX` (branch and exchange)             |
| **Instrukcje load/store**                    | `LDR` (load from memory), `STR` (store to memory)                             |
| **Instrukcje przesunięć i rotacji**          | `LSL` (logical shift left), `LSR` (logical shift right), `ROR` (rotate right) |
| **Instrukcje warunkowe**                     | `ADDEQ` (dodaj, jeśli flaga Z jest ustawiona)                                 |

**Legenda** wyjaśniająca kategorie i przykłady instrukcji ARM z tabeli:  

---

### **1. Instrukcje arytmetyczne i logiczne**  
- **Cel**: Wykonywanie podstawowych operacji matematycznych i logicznych na danych.  
- **Przykłady**:  
  - `ADD` (**A**dd): Dodawanie dwóch wartości.  
  - `SUB` (**Sub**tract): Odejmowanie.  
  - `MUL` (**Mul**tiply): Mnożenie.  
  - `AND`: Operacja logiczna **AND** (bitowe "i").  
  - `ORR` (**Or** **R**egister): Operacja logiczna **OR** (bitowe "lub").  
  - `EOR` (**Exclusive OR**): Operacja logiczna **XOR** (bitowe "albo").  

---

### **2. Instrukcje sterujące przepływem programu**  
- **Cel**: Zmiana kolejności wykonywania instrukcji (np. skoki, wywołania funkcji).  
- **Przykłady**:  
  - `B` (**B**ranch): Bezwarunkowy skok do innej części kodu.  
  - `BL` (**B**ranch with **L**ink): Skok z zapisaniem adresu powrotu (używane przy wywołaniach funkcji).  
  - `BX` (**B**ranch and e**X**change): Skok z możliwością zmiany trybu procesora (np. ARM ↔ Thumb).  

---

### **3. Instrukcje load/store**  
- **Cel**: Przenoszenie danych między pamięcią a rejestrami procesora.  
- **Przykłady**:  
  - `LDR` (**L**oa**d** **R**egister): Załaduj wartość z pamięci do rejestru.  
  - `STR` (**S**to**r**e **R**egister): Zapisz wartość z rejestru do pamięci.  
  - **Uwaga**: Mogą współpracować z różnymi trybami adresowania (np. `LDR R0, [R1]` – ładuj z adresu w R1).  

---

### **4. Instrukcje przesunięć i rotacji**  
- **Cel**: Manipulacja bitami w rejestrach (przesuwanie, rotacja).  
- **Przykłady**:  
  - `LSL` (**L**ogical **S**hift **L**eft): Przesunięcie bitowe w lewo (np. `LSL R0, R1, #2` – przesuń R1 o 2 bity w lewo, wynik do R0).  
  - `LSR` (**L**ogical **S**hift **R**ight): Przesunięcie bitowe w prawo.  
  - `ROR` (**R**otate **R**ight): Rotacja bitowa w prawo (ostatni bit trafia na początek).  

---

### **5. Instrukcje warunkowe**  
- **Cel**: Wykonanie operacji tylko wtedy, gdy spełniony jest określony warunek (np. stan flag procesora).  
- **Przykłady**:  
  - `ADDEQ` (**Add** **Eq**ual): Wykonaj dodawanie tylko jeśli flaga **Z** (Zero) jest ustawiona (wynik poprzedniej operacji był zerem).  
  - Inne warunki: `NE` (not equal), `GT` (greater than), `LT` (less than) itd. (np. `SUBLT` – odejmij, jeśli mniejsze).  

---

### **Kluczowe pojęcia**:  
- **Rejestry**: Lokalne pamięci procesora (np. `R0`, `R1`), przechowujące dane lub adresy.  
- **Flagi**: Bity w rejestrze stanu (**C**arry, **Z**ero, **N**egative, **V** Overflow) sterujące instrukcjami warunkowymi.  
- **Adresowanie**: Sposób określania lokalizacji danych w pamięci (np. `[R1]` – wartość spod adresu w R1).

---

### 4. **Zalety i wady RISC/ARM**
| **Zalety**                           | **Wady**                                                               |
|--------------------------------------|------------------------------------------------------------------------|
| **Prosta implementacja sprzętowa**   | Większa liczba instrukcji potrzebnych do wykonania złożonych operacji. |
| **Wysoka wydajność**                 | Wymaga bardziej złożonego kompilatora do generowania efektywnego kodu. |
| **Niskie zużycie energii**           |                                                                        |
| **Łatwość optymalizacji wydajności** |                                                                        |

---

### 5. **Porównanie RISC (ARM) z CISC (x86)**
| **Porównanie RISC (ARM) z CISC (x86)** | **RISC (ARM)**                | **CISC (x86)**               |
|----------------------------------------|-------------------------------|------------------------------|
| **Złożoność instrukcji**               | Proste instrukcje             | Złożone instrukcje           |
| **Długość instrukcji**                 | Stała długość                 | Zmienna długość              |
| **Zużycie energii**                    | Niskie                        | Wyższe                       |
| **Zastosowania**                       | Urządzenia mobilne i embedded | Komputery osobiste i serwery |

---

| **Podsumowanie**                                                  | **RISC (ARM)** |
|-------------------------------------------------------------------|----------------|
| **Zorientowanie na prostotę, wydajność i niskie zużycie energii** | Dzięki stałej długości instrukcji, architekturze load/store i dużej liczbie rejestrów, ARM jest idealny dla urządzeń wymagających wysokiej wydajności przy minimalnym zużyciu energii. |

---

# Bibliografia

## Wykład 9:
Materiał bazowy, https://fulmanski.pl/zajecia/comp_sys_arch/zajecia_20242025/lecture_09_modern_processor_architectures_and_instruction_sets_risc_arm.pdf