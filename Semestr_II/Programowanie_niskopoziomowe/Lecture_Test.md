# Plik zawiera : Pytania do testu z programowania niskopoziomowego.


## Lista pytań

| LP. | Pytanie                                                                                                                                         | Prawda | Fałsz |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------ | ----- |
| 1.  | Program napisany w asemblerze NASM i skompilowany z użyciem opcji `-f elf64`, ale korzystający z 32-bitowych rejestrów takich jak `EAX`, `EBX`, będzie nadal działał według 32-bitowej konwencji wywołań funkcji – mimo że powstał plik binarny w formacie 64-bitowym. |        |       |
| 2.  | W składni GNU AS operand źródłowy znajduje się po prawej stronie instrukcji `mov`, a operand docelowy po lewej.                                 |        |       |
| 3.  | W NASM etykiety kończą się dwukropkiem, podobnie jak w języku C.                                                                                |        |       |
| 4.  | W składni AT\&T rejestry są poprzedzane znakiem `%`.                                                                                            |        |       |
| 5.  | W asemblerze `NASM` sekcja `.bss` służy do deklarowania danych nieinicjalizowanych, takich jak zmienne zaalokowane za pomocą `resb` lub `resd`. |        |       |
| 6.  | Sekcja `.text` zawiera dane programu, takie jak łańcuchy tekstowe i zmienne globalne.                                                           |        |       |
| 7.  | W programach asemblerowych kompilowanych samodzielnie przy użyciu `nasm` i `ld`, punkt wejścia może być funkcją `main`.                         |        |       |
| 8.  | Instrukcja `CMP` porównuje dwa operandy przez ich odjęcie, ale nie zapisuje wyniku.                                                             |        |       |
| 9.  | `INC eax` zwiększa zawartość rejestru `eax` o 2.                                                                                                |        |       |
| 10. | `XOR eax, eax` to efektywny sposób na wyzerowanie zawartości rejestru `eax`.                                                                    |        |       |
| 11. | Instrukcja `JMP` wykonuje bezwarunkowy skok do wskazanej etykiety.                                                                              |        |       |
| 12. | `JNE` wykona skok, gdy wynik porównania jest równy.                                                                                             |        |       |
| 13. | W asemblerze NASM instrukcja `SUB eax, ebx` odejmuje wartość rejestru `ebx` od `eax` i zapisuje wynik w `eax`.                                  |        |       |
| 14. | W asemblerze instrukcja `CALL` zapisuje adres powrotu na stosie, umożliwiając późniejszy powrót do miejsca wywołania funkcji.                   |        |       |
| 15. | Funkcja wywołana w asemblerze nie musi przywracać rejestrów po zakończeniu działania.                                                           |        |       |
| 16. | Rejestr `ebp` często wskazuje początek ramki stosu funkcji.                                                                                     |        |       |
| 17. | Instrukcja `CALL` automatycznie umieszcza adres powrotny na stosie.                                                                             |        |       |
| 18. | Funkcję w języku C można wywołać z poziomu asemblera, o ile przestrzega się konwencji ABI.                                                      |        |       |
| 19. | Funkcja w języku C musi zawsze coś zwracać, gdy jest wywoływana z asemblera.                                                                    |        |       |
| 20. | W systemach 64-bitowych parametry funkcji C są przekazywane głównie przez rejestry.                                                             |        |       |
| 21. | Jednostka zmiennoprzecinkowa (`FPU`) samodzielnie odczytuje dane z pamięci, obsługując adresowanie bez udziału głównego procesora (`CPU`).      |        |       |
| 22. | `SSE` i `AVX` pozwalają na równoległe przetwarzanie danych (`SIMD`).                                                                            |        |       |
| 23. | Instrukcje `MMX` i `SSE` korzystają z różnych zestawów rejestrów, więc mogą być używane równolegle bez problemu.                                |        |       |
| 24. | Każdy program w Arduino IDE musi zawierać funkcje `setup()` i `loop()`, nie występuje `main`.                                                   |        |       |
| 25. | W kodzie Arduino funkcja `digitalRead(pin)` odczytuje stan logiczny na wejściu cyfrowym pinu.                                                   |        |       |
| 26. | W kodzie Arduino funkcja `analogWrite()` służy do odczytu napięcia na pinie analogowym.                                                         |        |       |
| 27. | W kodzie Arduino funkcja `digitalWrite(pin, HIGH)` ustawia pin cyfrowy w stan wysoki.                                                           |        |       |
| 28. | Rejestr przesuwny może być wykorzystywany zarówno do multipleksacji, jak i do demultipleksacji — dane można wpisywać i odczytywać               |        |       |
| 29. | Stan przycisku można sprawdzić przez `digitalRead()` i porównać z `HIGH`.                                                                       |        |       |
| 30. | Jednostka zmiennoprzecinkowa posiada własne rejestry i nie korzysta z pamięci operacyjnej, ponieważ ta jest od rejestrów zbyt wolna.            |        |       |
| 31. | Bufor cykliczny nadpisuje stare dane, gdy dojdzie do przepełnienia.                                                                             |        |       |
| 32. | W języku C można uzyskać reprezentację binarną liczby bez używania instrukcji warunkowych, stosując przesuwanie bitów i operację `AND` z 1.     |        |       |
| 33. | W buforze cyklicznym `head` wskazuje na miejsce zapisu, a `tail` na miejsce odczytu.                                                            |        |       |
| 34. | Wyświetlacz LCD można obsłużyć przez `I2C` z użyciem odpowiednich bibliotek w Arduino.                                                          |        |       |
| 35. | Kod Arduino wymaga użycia biblioteki, aby uzyskać dostęp do pinów.                                                                              |        |       |
| 36. | Bufor cykliczny może przechowywać wartości temperatur do późniejszego wyświetlenia ich jako histogramu na LCD.                                  |        |       |

---

## Klucz odpowiedzi + uzasadnienia

| LP. | **Odpowiedź** | Uzasadnienie                                                                                                                                     |
| --- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1.  | **Prawda**    | Program korzysta z 32-bitowych rejestrów i nie używa nowej konwencji (np. `RDI`, `RSI`, `RAX`).                                                  |
| 2.  | **Fałsz**     | W GNU AS (AT\&T) operand źródłowy jest po lewej, a docelowy po prawej – odwrotnie niż w NASM.                                                    |
| 3.  | **Fałsz**     | W NASM etykiety kończą się dwukropkiem, ale to nie ma związku z językiem C (gdzie funkcje nie mają `:`).                                         |
| 4.  | **Prawda**    | W składni AT\&T rejestry mają prefiks `%`, np. `%eax`, `%ebx`.                                                                                   |
| 5.  | **Prawda**    | `.bss` to sekcja nieinicjalizowanych danych, np. zmiennych zadeklarowanych dyrektywami `resb`, `resd` itd., co jest standardem w `NASM`.         |
| 6.  | **Fałsz**     | `.text` zawiera kod programu (instrukcje), dane są w `.data` lub `.bss`.                                                                         |
| 7.  | **Fałsz**     | `ld` oczekuje punktu wejścia `_start`, nie `main`.                                                                                               |
| 8.  | **Prawda**    | `CMP` ustawia flagi na podstawie różnicy, ale nie zapisuje wyniku.                                                                               |
| 9.  | **Fałsz**     | `INC` zawsze zwiększa operand o 1.                                                                                                               |
| 10. | **Prawda**    | `XOR` (tzw. zeroing idiom) nie wymaga ładowania wartości z pamięci lub dekodowania natychmiastowej liczby jak w przy użyciu `mov`                |
| 11. | **Prawda**    | `JMP` wykonuje bezwarunkowy skok do wskazanej etykiety.                                                                                          |
| 12. | **Fałsz**     | `JNE` skacze, gdy **wynik nie jest równy**, czyli ZF = 0.                                                                                        |
| 13. | **Prawda**    | `SUB eax, ebx` wykonuje `eax := eax - ebx`.                                                                                                      |
| 14. | **Prawda**    | `CALL` w asemblerze automatycznie zapisuje na stosie adres instrukcji po `CALL`, aby można było do niej wrócić za pomocą `RET`.                  |
| 15. | **Fałsz**     | Dobrą praktyką jest przywracanie stanu rejestrów używanych przez funkcję.                                                                        |
| 16. | **Prawda**    | `ebp` służy często jako wskaźnik ramki funkcji w standardowej konwencji wywołań.                                                                 |
| 17. | **Prawda**    | `CALL` zapisuje adres powrotu na stos, wykonuje skok i oczekuje `RET`.                                                                           |
| 18. | **Prawda**    | Jeśli przestrzegamy konwencji wywołań (np. SysV AMD64), funkcje C mogą być używane w ASM.                                                        |
| 19. | **Fałsz**     | Funkcja może być typu `void`, nie musi nic zwracać.                                                                                              |
| 20. | **Prawda**    | W konwencji SysV AMD64 pierwsze argumenty funkcji są przekazywane przez rejestry.                                                                |
| 21. | **Fałsz**     | `FPU` wykonuje operacje na danych zmiennoprzecinkowych, ale dostęp do pamięci (adresowanie, ładowanie danych) realizuje główny procesor (`CPU`). |
| 22. | **Prawda**    | `SSE` i `AVX` to zestawy instrukcji SIMD (`Single Instruction Multiple Data`).                                                                   |
| 23. | **Fałsz**     | `MMX` i `SSE` współdzielą rejestry, więc ich jednoczesne użycie wymaga ostrożności.                                                              |
| 24. | **Prawda**    | Każdy szkic (sketch) w Arduino zawiera funkcje `setup()` i `loop()`.                                                                             |
| 25. | **Prawda**    | `digitalRead()` służy do odczytu stanu cyfrowego pinu – `HIGH` lub `LOW`.                                                                        |
| 26. | **Fałsz**     | `analogWrite()` generuje sygnał PWM (wyjście), nie odczytuje napięcia.                                                                           |
| 27. | **Prawda**    | `digitalWrite(pin, HIGH)` ustawia stan wysoki na pinie cyfrowym.                                                                                 |
| 28. | **Fałsz**     | Rejestr przesuwny umożliwia przesyłanie danych z wejścia szeregowego do wyjść równoległych, ale **nie działa jak demultiplekser**                |
| 29. | **Prawda**    | Przycisk podłączony do cyfrowego pinu można obsłużyć przez `digitalRead()` i porównanie.                                                         |
| 30. | **Prawda**    | `FPU` faktycznie posiada własne rejestry, ale może również korzystać z pamięci RAM (np. ładować z niej dane), mimo że jest ona wolniejsza.       |
| 31. | **Prawda**    | Bufor cykliczny nadpisuje najstarsze dane przy przepełnieniu.                                                                                    |
| 32. | **Prawda**    | W języku C można użyć operatora przesunięcia bitowego (`>>`) i bitowego `AND` (`& 1`), by wydobyć kolejne bity bez konieczności stosowania `if`. |
| 33. | **Prawda**    | `head` wskazuje miejsce zapisu, `tail` miejsce odczytu.                                                                                          |
| 34. | **Prawda**    | Wyświetlacze LCD często współpracują z Arduino przez magistralę `I2C`.                                                                           |
| 35. | **Fałsz**     | Bezpośredni dostęp do wejścia/wyjścia na mikrokontrolerze nie jest ograniczony.                                                                  |
| 36. | **Prawda**    | Bufor cykliczny może przechowywać dane temperatur do późniejszego użycia, np. na LCD.                                                            |