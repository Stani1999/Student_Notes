# Architektura Systemów Komputerowych

## Wykład 4: Procesor -- tryby pracy, współpraca z koprocesorem matematycznym, jednostka sterująca i jej mikrokod.

### **1. Tryby pracy procesora**

Procesor może działać w różnych trybach pracy, które określają poziom dostępu do zasobów systemowych i możliwości wykonywania instrukcji. Główne tryby pracy to:

| **Tryb pracy**          | **Opis**                                                                                                                                | **Uzasadnienie istnienia**                                                                                                    |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| **Tryb użytkownika (User Mode)** | Procesor działa z ograniczonym dostępem do zasobów systemowych. Aplikacje użytkownika nie mogą bezpośrednio zarządzać sprzętem ani pamięcią systemową. | Zapewnia bezpieczeństwo systemu, zapobiegając awariom spowodowanym błędami w aplikacjach użytkownika. |
| **Tryb jądra (Kernel Mode)**     | Procesor ma pełny dostęp do wszystkich zasobów systemowych, w tym do pamięci i urządzeń wejścia/wyjścia. Używany przez system operacyjny. | Umożliwia systemowi operacyjnemu zarządzanie sprzętem i wykonywanie operacji krytycznych dla działania systemu.    |
| **Tryb rzeczywisty (Real Mode)** | Tryb stosowany w starszych procesorach x86, w którym dostęp do pamięci jest ograniczony do 1 MB, a nie ma ochrony pamięci ani wielozadaniowości. | Zapewnia zgodność ze starszymi aplikacjami i systemami operacyjnymi.                                        |
| **Tryb chroniony (Protected Mode)** | Tryb, w którym procesor zapewnia ochronę pamięci, wielozadaniowość i inne zaawansowane funkcje. | Umożliwia nowoczesnym systemom operacyjnym efektywne zarządzanie zasobami i zapewnia bezpieczeństwo.                                                      |
| **Tryb wirtualny (Virtual Mode)** | Tryb, w którym procesor emuluje tryb rzeczywisty w środowisku trybu chronionego. | Umożliwia uruchamianie starszych aplikacji w nowoczesnych systemach operacyjnych.                                                                                          |

#### **Uzasadnienie istnienia trybów pracy:**
| **Cecha**          | **Opis**                                                                                                       |
|--------------------|----------------------------------------------------------------------------------------------------------------|
| **Bezpieczeństwo** | Tryb użytkownika ogranicza dostęp aplikacji do krytycznych zasobów systemowych, zapobiegając awariom i atakom. |
| **Wydajność**      | Tryb jądra umożliwia systemowi operacyjnemu efektywne zarządzanie zasobami.                                    |
| **Zgodność**       | Tryby rzeczywisty i wirtualny zapewniają zgodność ze starszymi aplikacjami i systemami operacyjnymi.           |

---

### **2. Współpraca procesora głównego z koprocesorem matematycznym (FPU)**

| Zadanie                   | Procesor główny                                 | Koprocesor matematyczny (FPU)                                                                                       |
|---------------------------|-------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| **Typ operacji**          | Liczby całkowite, zarządzanie instrukcjami      | Liczby zmiennoprzecinkowe                                                                                           |
| **Działanie** | Przekazuje instrukcje zmiennoprzecinkowe do FPU | Wykonuje operacje na liczbach zmiennoprzecinkowych (dodawanie, odejmowanie, mnożenie, dzielenie, funkcje trygonometryczne itp.) |
| **Wynik**                 | Odbiera wyniki z FPU                            | Zwraca wyniki do procesora głównego                                                                                 |
| **Współpraca**            | Współdzieli pamięć i rejestry z FPU             | Współpracuje z procesorem głównym w celu efektywnej wymiany danych                                                  |
| **Zalety**                | -                                               | Znacząco przyspiesza obliczenia zmiennoprzecinkowe, zwiększa precyzję i szybkość obliczeń                           |

## Podsumowanie

Koprocesor matematyczny (FPU) to wyspecjalizowany układ, który odciąża główny procesor w zadaniach związanych z operacjami na liczbach zmiennoprzecinkowych. Dzięki temu, komputer może wykonywać bardziej złożone obliczenia naukowe, inżynieryjne i graficzne. Współczesne procesory często mają zintegrowany FPU, co jeszcze bardziej zwiększa ich wydajność.

#### **Przykłady zastosowań:**
- Grafika 3D, symulacje naukowe, obliczenia inżynierskie, sztuczna inteligencja.

---

### **3. Mikroinstrukcje i ich udział w sterowaniu jednostką sterującą**

Mikroinstrukcje to niskopoziomowe instrukcje, które sterują działaniem jednostki sterującej (CU) procesora. Są one częścią **mikrokodu**, który definiuje sposób wykonywania instrukcji maszynowych.

#### **Czym są mikroinstrukcje?**
- Mikroinstrukcje to podstawowe kroki, które jednostka sterująca wykonuje, aby zrealizować instrukcję maszynową.
- Każda instrukcja maszynowa jest tłumaczona na sekwencję mikroinstrukcji.

#### **Rola mikroinstrukcji w sterowaniu jednostką sterującą:**
| Funkcja                    | Opis                                                                                                                                                                                                                                                               |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Dekodowanie instrukcji** | Jednostka sterująca (CU) analizuje instrukcję maszynową i za pomocą mikroinstrukcji określa, jakie operacje należy wykonać, aby ją zrealizować. <br> Mikroinstrukcje "tłumaczą" instrukcję maszynową na sekwencję prostszych działań, zrozumiałych dla procesora.  |
| **Generowanie sygnałów sterujących** | Mikroinstrukcje generują sygnały sterujące, które koordynują pracę poszczególnych bloków funkcjonalnych procesora (ALU, rejestry, pamięć). <br> Sygnały te aktywują odpowiednie obwody i umożliwiają przepływ danych między komponentami.                     |
| **Realizacja operacji**    | Mikroinstrukcje definiują kolejność i sposób wykonania operacji, takich jak: <br> pobieranie danych z pamięci, przesyłanie ich do jednostki arytmetyczno-logicznej (ALU), <br> wykonywanie obliczeń, a następnie zapisywanie wyników z powrotem do pamięci lub rejestrów.     |

#### **Przykład działania mikroinstrukcji:**
- Dla instrukcji dodawania (np. `ADD R1, R2`), mikroinstrukcje mogą wyglądać następująco:

| Krok | Mikroinstrukcja               | Opis |
|---|----------------------------------|------------------------------------------------------------------------------------------------|
| 1 | Pobierz wartość z rejestru R1    | Wartość z rejestru R1 jest pobierana i umieszczana w wewnętrznym rejestrze procesora.          |
| 2 | Pobierz wartość z rejestru R2    | Wartość z rejestru R2 jest pobierana i umieszczana w innym wewnętrznym rejestrze procesora.    |
| 3 | Przekaż wartości do ALU          | Wartości z wewnętrznych rejestrów są przekazywane do jednostki arytmetyczno-logicznej (ALU).   |
| 4 | Wykonaj operację dodawania w ALU | ALU wykonuje operację dodawania na otrzymanych wartościach.                                    |
| 5 | Zapisz wynik do rejestru R1      | Wynik dodawania jest zapisywany z powrotem do rejestru R1, zastępując jego poprzednią wartość. |

#### **Zalety mikroinstrukcji:**
- **Elastyczność:** Mikrokod można łatwo modyfikować, co umożliwia dostosowanie procesora do nowych instrukcji lub optymalizacji.
- **Uproszczenie projektowania:** Mikroinstrukcje pozwalają na uproszczenie projektowania jednostki sterującej, ponieważ złożone instrukcje są realizowane przez sekwencje prostych kroków.

---

### **Podsumowanie**

- **Tryby pracy procesora** (użytkownika, jądra, rzeczywisty, chroniony, wirtualny) zapewniają bezpieczeństwo, wydajność i zgodność systemu.
- **Koprocesor matematyczny FPU** współpracuje z głównym procesorem, przyspieszając obliczenia zmiennoprzecinkowe i zwiększając precyzję.
- **Mikroinstrukcje** są kluczowe dla działania jednostki sterującej, definiując kroki niezbędne do wykonania instrukcji maszynowych.

---

# Bibliografia

## Wykład 4:
Materiał bazowy, https://fulmanski.pl/zajecia/comp_sys_arch/zajecia_20242025/lecture_04_control_unit_and_microcode.pdf