# Podstawy Automatyki I Sterowania

## Pytania do kolokwium 

### 1. Omów pojęcia: obiekt regulacji, urządzenie wykonawcze, zakłócenie, element pomiarowy - w tym narysować symbole. 

![Układ Regulacji](pictures/Wiki_Układ_regulacji.png) <br> Żródło [Wikipedia.org - Układ regulacji (automatyka)](https://pl.wikipedia.org/wiki/Uk%C5%82ad_regulacji_%28automatyka%29)

**Pojęcie**               | **Opis**
:-------------------------| :--------------------------------------------------------------------------------------------------------
**Obiekt regulacji**      | Urządzenie lub proces, na który oddziałują sygnały nastawiające `u(t)`<br> i zakłócające `z(t)`, generując sygnały wyjściowe `y(t)`
**Urządzenie <br> wykonawcze** | Urządzenie wymuszające zmiany wielkości regulowanej, składające się z<br> elementu napędowego (np. siłownik) i wykonawczego (np. zawór regulacyjny)
**Zakłócenie**            | Niekorzystny sygnał zewnętrzny `z(t)`, to niepożądany czynnik, który powoduje <br> odchylenie wielkości regulowanej `y(t)` od wartości zadanej `w(t)`
**Element <br> pomiarowy**     | Wykonuje pomiar wielkości regulowanej `y(t)`, a następnie przekształcają na sygnał `v(t)` <br> (opisywanego także jako y<sub>m</sub>) zrozumiałego i gotowego do wprowadzenia do regulatora

### 2. Omów sposoby łączenia podstawowych bloków na schematach blokowych.

**Połączenie**          | **Opis danego połączonenia bloków** | **Transmisja wypadkowa**
------------------------|-------------------------------------|-----------------------------------
**Szeregowe<br>(kaskadowe)** | Sygnał wyjściowy z pierwszego bloku<br>  jest sygnałem wejściowym dla drugiego, i tak dalej <br> Informacja przepływa sekwencyjnie przez kolejne bloki | Iloczyn algebraiczny<br>$G_w = G_1 \cdot G_2 \cdot \dots \cdot G_n$
**Równoległe**          | Ten sam sygnał wejściowy jest podawany <br> jednocześnie na wszystkie bloki składowe, <br> a ich sygnały wyjściowe są sumowane <br> algebraicznie w węźle sumacyjnym | Suma algebraliczna <br> $G_w = G_1 + G_2 + \dots + G_n$
**Ze sprzężeniem <br> zwrotnym** | Sygnał wyjściowy obiektu jest zwracany (sprzęgany)<br> i odejmowany lub dodawany do sygnału wejściowego,<br> tworząc zamkniętą pętlę regulacji | $G_w = \frac{G_1}{1 \pm G_1 \cdot G_2}$ <br> dla sprzężenie zwrotnego `-` <br> dla sprzężenia dodatniego `+`

### 3. Omów na przykładzie różnice między regulacją ręczną i automatyczną 

 **Cecha <br> regulacji** | **Regulacja Ręczna <br> (Przykład: Zawór Grzejnikowy)** | **Regulacja Automatyczna <br> (Przykład: Termostat Grzejnikowy)** |
 :--- | :--- | :--- 
 **Pętla <br> sterowania** | Układ jest **otwarty**: <br> brak analizy sygnału wyjściowego <br> brak sprzężenia zwrotnego | Układ jest **zamknięty**: <br> proces odbywa się w obwodzie zamkniętym <br> układ sterowania ze **sprzężeniem zwrotnym** 
 **Przykład <br> urządzenia <br> wykonawczego** | Zawór grzejnikowy jest sterowany <br> **ręcznie** przez człowieka <br> (jako operatora) | Termostat grzejnikowy zawiera <br> **regulator** i **czujnik temperatury**, <br> który automatycznie steruje <br> temperaturą powietrza w pomieszczeniu 
 **Sterowanie** | **Ręcznie** przez człowieka,<br> który mierzy temperaturę <br> i porównuje ją z wartością zadaną (`w`),<br> a następnie ręcznie steruje <br> zaworem grzejnika | **Regulator** porównuje <br> wielkość regulowaną (`y`)<br> z wartością zadaną (`w`), <br> a następnie zmienia sygnał sterujący (`u`), <br> dążąc do warunku równości `y=w` 
 **Reakcja<br> na zakłócenia** | Wymaga **ponownego dostosowania** <br> zaworu przez człowieka <br> W przypadku zakłóceń (`z`) <br> układ nie będzie wykonywał zadania,<br >dopóki operator nie zareaguje | Działanie układu ma na celu <br> **eliminowanie wpływu zakłóceń** (`z`) <br> na wielkość regulowaną <br> Układu jest stosunkowo niewrażliwa <br> na zewnętrzne zakłócenia 
 **Dokładność** | Jest **niska**,<br> zależna od uwagi operatora; <br> może subiektywnie wpływać na proces | Ma na celu **minimalizację uchybu**<br> (to znaczy różnicy) <br> między wielkością regulowaną a zadaną, <br> zapewniając wymaganą jakość regulacji 

### 4. Omów metodę doświadczalną wyznaczania charakterystyk dynamicznych.

**Aspekt**  | **Opis** 
:---------- | :---------- 
**Kiedy <br> stosowana**  | W przypadku niedostatecznej wiedzy <br> o zjawiskach w obiekcie regulacji 
**Najczęstrza <br> metoda**    | **Charakterystyka Skokowa** 
**Stanowi** | Ocenę transmitancji obiektu na podstawie analizy <br> odpowiedzi obiektu na wymuszenie skokowe
**Umożliwia**    | Proste wyznaczenie <br>**współczynnika wzmocnienia, obiektu  statycznego** 
**Współczynnik** | $K = \frac{\Delta y}{\Delta u}$
 *gdzie* | $\Delta y$ - zmiana wartości ustalonej odpowiedzi skosowej obiektu <br> $\Delta u$ - zmiana wartości sygnału wejściowego

### 5. Scharakteryzuj i podaj przykład obiektu proporcjonalnego z opóźnieniem.

**Aspekt** | **Opis** |
:----- | :--- |
**Typ Obiektu** | Obiekt **statyczny (z samowyrównaniem)** <br> proporcjonalny z czystym opóźnieniem transportowym
**Odpowiedź <br> Dynamiczna** | Odpowiedź na wymuszenie skokowe jest **identyczna z wymuszeniem,<br> ale przesunięta w czasie** o wartość opóźnienia $T_t$ <br> brak inercji, tylko czyste opóźnienie
**Czas Opóźnienia $T_t$** | Określa czas, po którym sygnał wyjściowy zaczyna reagować <br> wynik fizycznego transportu (np. przepływu medium, przesuwu taśmy)
**Transmitancja Operatorowa** | $$G(s) = K \cdot e^{-T_t \cdot s}$$<br>gdzie:<br> $K$ – współczynnik wzmocnienia (dla czystego opóźnienia często $K = 1$),<br> $e^{-T_t s}$– człon opóźniający (transportowy)
**Przykład 1** | **Przewód z mieszającym zaworem regulacyjnym <br> oraz czujnikiem temperatury** – sygnał temperatury dociera do czujnika <br> z opóźnieniem wynikającym z czasu przepływu medium
**Przykład 2** | **Taśmowy podajnik węgla** <br> grubość warstwy paliwa w odległości $l$ od początku podajnika powtarza <br> grubość na początku, ale z opóźnieniem $T = \frac{l}{v}$

### 6. Scharakteryzuj i podaj przykład obiektu inercyjnego pierwszego rzędu.

**Aspekt** | **Opis** |
:----- | :--- 
**Typ Obiektu** | Obiekt **statyczny** (z samowyrównaniem)
**Odpowiedź <br> Dynamiczna** | Odpowiedź na wymuszenie skokowe dąży **asymptotycznie do nowej,<br>  skończonej wartości ustalonej** (bez opóźnienia transportowego)
**Stała Czasowa ($T$)** | Określa szybkość reakcji – jest to czas,<br> po którym wartość wyjściowa osiąga 63,2% wartości końcowej
**Transmitancja <br> Operatorowa** | $$G(s) = \frac{K}{T \cdot s + 1}$$<br>gdzie $K$ to współczynnik wzmocnienia, <br> $T$ to stała czasowa, <br> człon ${T \cdot s + 1}$ stanowi inercję
**Przykład** | **Podgrzewacz ciepłej wody** z trójdrogowym zaworem regulacyjnym

### 7. Omów sposoby doboru nastaw dynamicznych regulatora PID. 

**Aspekt** | **Opis**
:----- | :---
**Cel doboru nastaw** | Uzyskanie **wymaganej jakości regulacji** <br> minimalny uchyb statyczny,<br> akceptowalne przeregulowanie,<br> krótki czas regulacji <br> poprzez optymalny dobór trzech parametrów: <br>**`Kp`** wzmocnienia, <br>**`Ti`** czasu całkowania, <br>**`Td`** czasu różniczkowania
**1. Metoda<br> Zieglera‑Nicholsa<br> (1941)** | **Metoda eksperymentalna**,<br> wymaga przeprowadzenia testu na obiekcie:<br>1. Ustawienie regulatora na **działanie P** (`Ti`=max, `Td`=0).<br>2. Zwiększanie `Kp` aż pojawią się **niegasnące oscylacje**<br> na wyjściu (granica stabilności).<br>3. Zanotowaniu<br> **wzmocnienia krytycznego `Kpkr`**<br> i **okres drgań krytycznych `Tosc`**.<br>4. Obliczenie nastawy według wzorów:<br>   • **P:** `Kp = 0.5 * Kpkr`<br>   • **PI:** `Kp = 0.45 * Kpkr`, `Ti = 0.85 * Tosc`<br>   • **PID:** `Kp = 0.6 * Kpkr`, `Ti = 0.5 * Tosc`, `Td = 0.125 * Tosc` 
**2. Metoda<br> analityczna<br> (Chien, Hrones, Reswick)** | Wymaga **znanego modelu obiektu** (znane: `K0`, `T0`, `Tz`).<br>• Korzysta się z **gotowych tabel** (Dobóru dla nastaw tej metody),<br> które na podstawie parametrów obiektu podają optymalne nastawy dla:<br>  a) odpowiedzi na **zmianę wartości zadanej**<br> bez przeregulowania lub z 20% przeregulowaniem,<br>  b) odpowiedzi na **zakłócenie** (z jednym lub wieloma przeregulowaniami) 
**3. Samostrojenie<br> (auto‑tuning)<br> w regulatorach cyfrowych** | **Funkcja automatyczna** nowoczesnych regulatorów cyfrowych.<br>• Uruchamiana przy ustalonym stanie obiektu.<br>• Regulator **wymusza oscylacje**, analizuje je (ok. 5 cykli)<br> i **automatycznie oblicza optymalne nastawy** (`Kp`, `Ti`, `Td`).<br>• Czas strojenia: od **10 minut** (szybkie obiekty)<br> do **ponad 40 minut** (wolne obiekty)<br>• niezalecane dla obiektów krytycznych (np. rafinerii, reaktorów),<br> gdzie automatyczna zmiana nastaw w trybie auto‑tuningu<br> mogłaby spowodować niebezpieczne stany procesowe lub awarie
**Podsumowanie** | • **Ziegler‑Nichols** – uniwersalna, eksperymentalna,<br> do obiektów bez znanego modelu.<br>• **Metoda analityczna** – szybsza, wymaga modelu obiektu.<br>• **Samostrojenie** – najwygodniejsze,<br> dostępne w regulatorach cyfrowych,<br> ale wymaga czasu na test, i nie zawsze są bezpieczne

### 8. Scharakteryzuj regulatory dwustawne.

**Aspekt** | **Opis**
:--- | :---
**Zasada działania** | Sygnał wyjściowy ma **tylko 2 stany**: **włączony (1)** i **wyłączony (0)**
**Sterowanie** | Przełącza się, gdy uchyb przekroczy **strefę histerezy** wokół wartości zadanej
**Histereza** | Obszar "martwy" zapobiegający zbyt częstym przełączeniom. <br> Mniejsza = większa dokładność, większe zużycie. <br> Większa = mniejsza dokładność, dłuższa żywotność
**Jakość regulacji** | Wartość regulowana **oscyluje** między granicami histerezy. <br> Mierzy się: amplitudę, częstotliwość przełączeń, wartość średnią
**Zalety** | Proste, tanie, niezawodne, łatwe w montażu i obsłudze
**Wady** | Stałe oscylacje, ograniczona dokładność, zużycie mechaniczne przy częstym przełączaniu
**Zastosowania** | Termostaty, presostaty, higrostaty, regulatory poziomu, zabezpieczenia w HVAC
**Przykład** | **Termostat grzejnika** – włącza grzanie poniżej 19°C, wyłącza powyżej 21°C (histereza = 2°C)

### 9. Omów rezystancyjne czujniki pomiaru temperatury (p4) 
### 10. Omów czujniki pomiaru wilgotności(p4) 
### 11. Na czym polega zjawisko kawitacji w zaworach regulacyjnych?(p5) 
### 12. Omów podział i zastosowanie przepustnic regulacyjnych powietrza.(p5) 
 