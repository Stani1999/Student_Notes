# Podstawy Automatyki I Sterowania

## Pytania do kolokwium 

### 1. Omów pojęcia: obiekt regulacji, urządzenie wykonawcze, zakłócenie, element pomiarowy - w tym narysować symbole. 

![Układ Regulacji](pictures/Wiki_Układ_regulacji.png) <br> Żródło [Wikipedia.org - Układ regulacji (automatyka)](https://pl.wikipedia.org/wiki/Uk%C5%82ad_regulacji_%28automatyka%29)

**Pojęcie**               | **Opis**
:-------------------------| :--------------------------------------------------------------------------------------------------------
**Obiekt regulacji**      | Urządzenie lub proces, na który oddziałują sygnały <br> nastawiające `u(t)` i zakłócające `z(t)`,<br> generując sygnały wyjściowe `y(t)`
**Urządzenie <br> wykonawcze** | Urządzenie wymuszające zmiany wielkości regulowanej,<br> składające się z elementu napędowego (np. siłownik)<br> i wykonawczego (np. zawór regulacyjny)
**Zakłócenie**            | Niekorzystny sygnał zewnętrzny `z(t)`,<br> to niepożądany czynnik, który powoduje <br> odchylenie wielkości regulowanej `y(t)`<br> od wartości zadanej `w(t)`
**Element <br> pomiarowy**     | Wykonuje pomiar wielkości regulowanej `y(t)`,<br> a następnie przekształca ją na sygnał `v(t)`<br> (opisywanego także jako y<sub>m</sub>) zrozumiałego <br> i gotowego do wprowadzenia do regulatora

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
 **Sterowanie** | **Ręcznie** przez człowieka,<br> który mierzy temperaturę <br> i porównuje ją z wartością zadaną (`w`),<br> a następnie ręcznie steruje <br> zaworem grzejnika | **Regulator** porównuje <br> wielkość regulowaną (`y`) z wartością zadaną (`w`), <br> a następnie zmienia sygnał sterujący (`u`), <br> dążąc do warunku równości `y=w` 
 **Reakcja na zakłócenia** | Wymaga **ponownego dostosowania** <br> zaworu przez człowieka <br> W przypadku zakłóceń (`z`) <br> układ nie będzie wykonywał zadania,<br >dopóki operator nie zareaguje | Działanie układu ma na celu <br> **eliminowanie wpływu zakłóceń** (`z`) <br> na wielkość regulowaną <br> Układu jest stosunkowo niewrażliwa <br> na zewnętrzne zakłócenia 
 **Dokładność** | Jest **niska**,<br> zależna od uwagi i zmęczenia operatora; <br> człowiek może subiektywnie wpływać na proces | Ma na celu **minimalizację uchybu**<br> (to znaczy różnicy) <br> między wielkością regulowaną a zadaną, <br> zapewniając wymaganą jakość regulacji 

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

Aspekt | Opis |
:--- | :--- |
**Typ Obiektu** | Obiekt **statyczny (z samowyrównaniem)** <br> proporcjonalny z czystym opóźnieniem transportowym
**Odpowiedź <br> Dynamiczna** | Odpowiedź na wymuszenie skokowe jest **identyczna z wymuszeniem,<br> ale przesunięta w czasie** o wartość opóźnienia $T_t$ <br> brak inercji, tylko czyste opóźnienie
**Czas Opóźnienia $T_t$** | Określa czas, po którym sygnał wyjściowy zaczyna reagować <br> wynik fizycznego transportu (np. przepływu medium, przesuwu taśmy)
**Transmitancja Operatorowa** | $$G(s) = K \cdot e^{-T_t \cdot s}$$<br>gdzie:<br> $K$ – współczynnik wzmocnienia (dla czystego opóźnienia często $K = 1$),<br> $e^{-T_t s}$– człon opóźniający (transportowy)
**Przykład 1** | **Przewód z mieszającym zaworem regulacyjnym <br> oraz czujnikiem temperatury** – sygnał temperatury dociera do czujnika <br> z opóźnieniem wynikającym z czasu przepływu medium
**Przykład 2** | **Taśmowy podajnik węgla** <br> grubość warstwy paliwa w odległości $l$ od początku podajnika powtarza <br> grubość na początku, ale z opóźnieniem $T = \frac{l}{v}$

### 6. Scharakteryzuj i podaj przykład obiektu inercyjnego pierwszego rzędu.

Aspekt | Opis 
:--- | :--- 
**Typ Obiektu** | Obiekt **statyczny** (z samowyrównaniem)
**Odpowiedź <br> Dynamiczna** | Odpowiedź na wymuszenie skokowe dąży **asymptotycznie do nowej,<br>  skończonej wartości ustalonej** (bez opóźnienia transportowego)
**Stała Czasowa ($T$)** | Określa szybkość reakcji – jest to czas,<br> po którym wartość wyjściowa osiąga <br> 63,2% wartości końcowej
**Transmitancja <br> Operatorowa** | $$G(s) = \frac{K}{T \cdot s + 1}$$<br>gdzie $K$ to współczynnik wzmocnienia, <br> $T$ to stała czasowa, <br> człon ${T \cdot s + 1}$ stanowi inercję
**Przykład** | **Podgrzewacz ciepłej wody** z trójdrogowym zaworem regulacyjnym

### 7. Scharakteryzuj regulatory dwustawne.

Aspekt | Opis
:--- | :---


### 8. Omów rezystancyjne czujniki pomiaru temperatury (p4) 
### 9. Omów czujniki pomiaru wilgotności(p4) 
### 10. Na czym polega zjawisko kawitacji w zaworach regulacyjnych?(p5) 
### 11. Omów podział i zastosowanie przepustnic regulacyjnych powietrza.(p5) 
### 12. Omów sposoby doboru nastaw dynamicznych regulatora PID. 