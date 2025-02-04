# Architektura Systemów Komputerowych

## Wykład 3: Procesor -- podstawowe bloki funkcjonalne i działanie.

### **1. Bloki funkcjonalne procesora**

| **Blok funkcjonalny**                     | **Rola**                                                  |
|-------------------------------------------|-----------------------------------------------------------|
| **Jednostka arytmetyczno-logiczna (ALU)** | Wykonuje operacje arytmetyczne i logiczne.                |
| **Jednostka sterująca (CU)**              | Zarządza przepływem danych i steruje pracą procesora.     |
| **Rejestry**                              | Przechowują dane i adresy tymczasowo.                     |
| **Szyny danych, adresowa i sterująca**    | Umożliwiają komunikację wewnętrzną procesora.             |
| **Pamięć podręczna (Cache)**              | Przyspiesza dostęp do często używanych danych.            |
| **Jednostka zarządzania pamięcią (MMU)**  | Obsługuje pamięć wirtualną i tłumaczenie adresów.         |
| **Jednostka zmiennoprzecinkowa (FPU)**    | Obsługuje operacje na liczbach zmiennoprzecinkowych.      |
| **Potok instrukcji (Pipeline)**           | Pozwala na równoległe przetwarzanie instrukcji.           |
| **Jednostka przewidywania skoków**        | Minimalizuje opóźnienia wynikające ze skoków warunkowych. |

---

### **2. Podział i charakterystyka rejestrów**

Rejestry w procesorze można podzielić na kilka kategorii w zależności od ich funkcji i przeznaczenia:

| **Typ rejestru**                 | **Charakterystyka**                                                                                                          |
|----------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| **Rejestry ogólnego przeznaczenia (GPR)** | Przechowują dane i wyniki obliczeń, są uniwersalne i często wykorzystywane przez programistów (np. EAX, EBX w x86). |
| **Rejestry specjalne**           | Pełnią określone funkcje. Ich przykłady są wymienione poniżej.                                                               |
| **Licznik rozkazów (PC)**        | Adres następnej instrukcji do wykonania. <br> W architekurze Intel'owskiej odpowiada za to instruction pointer (IP)          |
| **Rejestr instrukcji (IR)**      | Przechowuje bieżącą instrukcję do dekodowania i wykonania.                                                                   |
| **Rejestr stanu (FLAGS)**        | Informacje o stanie procesora (np. zero, overflow, carry).                                                                   |
| **Rejestr wskaźnika stosu (SP)** | Adres wierzchołka stosu, istotny dla zarządzania wywołaniami funkcji.                                                        |
| **Rejestry zmiennoprzecinkowe**  | Przechowują liczby zmiennoprzecinkowe, kluczowe w obliczeniach naukowych i grafice.                                          |
| **Rejestry adresowe**            | Przechowują adresy pamięci używane do odwoływania się do danych w RAM.                                                       |
| **Rejestry segmentowe**          | W architekturach z segmentacją pamięci (np. x86) przechowują adresy segmentów.                                               |
| **Rejestry kontrolne**           | Zarządzają stanem i konfiguracją procesora (np. rejestry MMU).                                                               |
| **Rejestr bufora pamięci (MBR)** | Przechowuje dane odczytane z pamięci lub dane, które mają być zapisane do pamięci.                                           |
| **Rejestr adresu pamięci (MAR)** | Przechowuje adres komórki pamięci, do której nastąpi odwołanie podczas operacji odczytu lub zapisu.                          |
---

### **3. Zagadnienia projektowe dotyczące rejestrów** 

| **Kategoria**             | **Opis**                                                                                                                                             |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Ilość rejestrów**       | Większa liczba zwiększa wydajność, minimalizując dostęp do RAM. <br> Mniejsza liczba zmniejsza złożoność i koszty produkcji.                         |
| **Rodzaj rejestrów** | GPR powinny być liczne dla efektywnej pracy procesora. <br> Rejestry specjalne powinny wspierać kluczowe operacje. <br> Rejestry zmiennoprzecinkowe są niezbędne w aplikacjach wymagających precyzyjnych obliczeń. |
| **Rozmiar rejestrów**     | Większy rozmiar pozwala na szybsze przetwarzanie danych. <br> Mniejszy rozmiar zmniejsza złożoność, ale może obniżyć wydajność.                      |
| **Organizacja rejestrów** | Rejestry widoczne dla programisty powinny być intuicyjne w użyciu. <br> Rejestry wewnętrzne optymalizują działanie procesora.                        |
| **Optymalizacja dostępu** | Potokowanie instrukcji wymaga szybkiego dostępu do rejestrów. <br> Przewidywanie skoków minimalizuje opóźnienia związane z instrukcjami warunkowymi. |

---

### **4. Cykl pracy procesora**

Cykl pracy procesora, zwany również **cyklem rozkazowym**, składa się z kilku etapów, które są powtarzane w celu wykonania kolejnych instrukcji. Oto główne etapy cyklu pracy procesora:

| **Etap**                            | **Opis**                                                                                                                                                                   |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Pobranie instrukcji (Fetch)** | Procesor pobiera instrukcję z pamięci, korzystając z adresu wskazywanego przez **licznik rozkazów (PC)**. Następnie zwiększa wartość PC, aby wskazywał na następną instrukcję. |
| **Dekodowanie instrukcji (Decode)** | Jednostka sterująca (CU) dekoduje pobraną instrukcję, aby określić, jakie operacje należy wykonać i które rejestry lub pamięć będą zaangażowane.                           |
| **Wykonanie instrukcji (Execute)**  | Jednostka arytmetyczno-logiczna (ALU) wykonuje operację określoną przez instrukcję (np. dodawanie, odejmowanie, porównanie).                                               |
| **Zapis wyników (Writeback)**       | Wynik operacji jest zapisywany do odpowiedniego rejestru lub pamięci.                                                                                                      |
| **Aktualizacja stanu**              | Procesor aktualizuje swój stan, np. modyfikuje rejestr stanu (FLAGS) w zależności od wyniku operacji.                                                                      |

#### **Potokowanie instrukcji (Pipeline):**
W nowoczesnych procesorach etapy cyklu rozkazowego są wykonywane równolegle dla różnych instrukcji, co znacznie zwiększa wydajność. Na przykład, podczas gdy jedna instrukcja jest dekodowana, następna może być pobierana.

**Pipeline bubble** to sytuacja, w której jeden lub więcej etapów potoku jest "pusty" (nie wykonuje żadnej użytecznej pracy). Powstaje, gdy procesor napotyka problem, który uniemożliwia płynne przechodzenie instrukcji przez potok. W efekcie w potoku pojawia się "przerwa" (bąbel), która zmniejsza wydajność procesora.

---

### **5. Zbiór instrukcji procesora**

Zbiór instrukcji procesora (ang. **Instruction Set Architecture, ISA**) to zestaw wszystkich instrukcji, które procesor może wykonać. Można go podzielić na dwie główne kategorie: **RISC** i **CISC**.

| **Kryterium lub Cecha**   | **RISC (Reduced Instruction Set Computer)**                                              | **CISC (Complex Instruction Set Computer)**                                      |
|---------------------------|------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| **Charakterystyka**       | Mały, prosty zestaw instrukcji, każda instrukcja wykonuje jedną operację, stała długość. | Duży, złożony zestaw instrukcji, mogą wykonywać wiele operacji, zmienna długość. |
| **Założenia projektowe**  | Prostota i szybkość                                                                      | Złożone operacje, zmniejszające liczbę instrukcji                                |
| **Zalety**                | Wysoka wydajność, łatwe potokowanie, mniejsze zużycie energii.                           | Mniejsza liczba instrukcji dla złożonych zadań, łatwiejsze programowanie.        |
| **Liczba instrukcji**     | Mała, prosta                                                                             | Duża, złożona                                                                    |
| **Długość instrukcji**    | Stała                                                                                    | Zmienna                                                                          |
| **Cykli na instrukcję**   | Zwykle jeden                                                                             | Często wiele                                                                     |
| **Wydajność**             | Wysoka dzięki prostocie i potokowaniu                                                    | Niższa ze względu na złożoność                                                   |
| **Zużycie energii**       | Niskie                                                                                   | Wyższe                                                                           |
| **Przykłady architektur** | ARM, MIPS, RISC-V                                                                        | x86 (Intel, AMD)                                                                 |

---

### **6. Przerwania**

Przerwania to mechanizm, który pozwala procesorowi na natychmiastową reakcję na zdarzenia zewnętrzne lub wewnętrzne. Są kluczowe dla efektywnego zarządzania zasobami systemu.

| **Rodzaj przerwania**     | **Opis**                                                                                                                                           |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| **Przerwania sprzętowe**  | Generowane przez urządzenia zewnętrzne (np. klawiatura, mysz, dysk twardy). <br> Umożliwiają reakcję procesora na zdarzenia w czasie rzeczywistym. |
| **Przerwania programowe** | Generowane przez programy (np. wywołanie funkcji systemowej). <br> Używane do komunikacji z systemem operacyjnym.                                  |
| **Przerwania wyjątków**   | Generowane przez procesor w odpowiedzi na błędy (np. dzielenie przez zero, brak strony w pamięci). <br> Umożliwiają obsługę błędów.                |

| **Rola przerwań:**       | **Opis**                                                                                                                             |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| **Reakcja na zdarzenia** | Przerwania pozwalają procesorowi na natychmiastową reakcję na ważne zdarzenia, bez konieczności ciągłego sprawdzania stanu urządzeń. |
| **Wielozadaniowość**     | Umożliwiają systemowi operacyjnemu przełączanie się między zadaniami, co jest kluczowe dla wielozadaniowości.                        |
| **Obsługa błędów**       | Pozwalają na wykrywanie i obsługę błędów w czasie rzeczywistym, co zwiększa stabilność systemu.                                      |

| **Mechanizm obsługi przerwań:**                     | **Opis**                                                                                                  |
|-----------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| **1. Zgłoszenie przerwania**                        | Urządzenie lub program zgłasza przerwanie do procesora.                                                   |
| **2. Zapis stanu**                                  | Procesor zapisuje stan bieżącego zadania (np. wartości rejestrów) na stosie.                              |
| **3. Przejście do procedury obsługi przerwania**    | Procesor przechodzi do specjalnej procedury obsługi przerwania (ISR, Interrupt Service Routine).          |
| **4. Wykonanie procedury**                          | Procedura obsługi przerwania wykonuje odpowiednie działania (np. odczyt danych z klawiatury).             |
| **5. Przywrócenie stanu**                           | Po zakończeniu obsługi przerwania procesor przywraca stan zapisany na stosie i wznawia przerwane zadanie. |

---

### **Podsumowanie**

- **Cykl pracy procesora** składa się z etapów: pobranie, dekodowanie, wykonanie i zapis wyników.
- **Zbiór instrukcji procesora** może być typu **RISC** (prosty, wydajny) lub **CISC** (złożony, uniwersalny).
- **Przerwania** to mechanizm umożliwiający procesorowi reakcję na zdarzenia w czasie rzeczywistym, co jest kluczowe dla wielozadaniowości i stabilności systemu.

---

# Bibliografia

## Wykład 3:
Materiał bazowy, https://fulmanski.pl/zajecia/comp_sys_arch/zajecia_20242025/lecture_03_processor_structure_and_function.pdf