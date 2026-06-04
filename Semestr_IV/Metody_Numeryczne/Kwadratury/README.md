# Całkowanie Numeryczne (Kwadratury) - Analiza i Wizualizacja

Projekt zrealizowany w architekturze WPF MVVM z zachowaniem zasady Single Responsibility Principle (SRP) oraz wzorca projektowego Strategy Pattern. Aplikacja służy do dynamicznego parsowania funkcji matematycznych wprowadzanych przez użytkownika oraz wyliczania całek oznaczonych na zadanym przedziale przy użyciu numerycznych metod przybliżonych (kwadratur).

## I. Architektura i realizacja zadań / Implementacja metod numerycznych

### I.1. **Definicja wspólnego interfejsu dla metod całkujących**

* `Interfaces/IQuadratureMethod.cs` - Kontrakt (interfejs) wymuszający na każdym algorytmie implementację głównej metody obliczeniowej (przedział od $a$ do $b$, liczba podziałów $n$, funkcja $f$).

### I.2. **Rozpoznawanie funkcji wpisanej przez użytkownika**

* `Services/Application/FunctionParserService.cs` - Serwis konwertujący wzór matematyczny z postaci tekstowej na wykonywalny w pamięci delegat `Func<double, double>`.
* Biblioteka `NCalc` - Umożliwia dynamiczne parsowanie i obliczanie wartości funkcji matematycznych wprowadzanych jako tekst.

### I.3. **Metoda prostokątów (Lewe, Środkowe, Prawe)**

* `Services/Algorithms/RectangleLeftMethod.cs` - Wariant lewy (wysokość z lewej krawędzi $x_i$).
* `Services/Algorithms/RectangleMidMethod.cs` - Wariant środkowy (oblicza środek kroku jako $x_{śr}$ oraz $y_{śr}$).
* `Services/Algorithms/RectangleRightMethod.cs` - Wariant prawy (wysokość z prawej krawędzi $x_{i+1}$).

### I.4. **Metoda trapezów (Aproksymacja liniowa)**

* `Services/Algorithms/TrapezoidalMethod.cs` - Algorytm obliczający pole ze średniej wielkości krawędzi wymnożonej przez szerokość kroku $h$.

### I.5. **Metoda parabol / Simpsona (Interpolacja Lagrange'a)**

* `Services/Algorithms/SimpsonMethod.cs` - Implementacja z wymuszeniem parzystej liczby przedziałów $n$ (nieparzyste są automatycznie inkrementowane) i rozdzieleniem wag (4 dla nieparzystych, 2 dla parzystych).

### I.6. **Przygotowanie uniwersalnych nagłówków i danych dla iteracji**

* `Models/QuadratureStepModel.cs` - Model przechowujący wyniki pojedynczych kroków iteracji (indeks $i$, parametry $x_i$, $y_i$, wartości środkowe oraz detale).

### I.7. **Generowanie wizualizacji pola pod wykresem**

* `Services/Application/QuadraturePlotService.cs` - Serwis budujący szkielet wykresu badanej funkcji $f(x)$.
* Biblioteka `OxyPlot.Wpf` - Umożliwia dynamiczne tworzenie wykresów w WPF.

### I.8. **Panel parametrów i wyników tabelarycznych**  Kontrolki UX odpowiedzialne za

* `UserControls/IntegrationParametersControl.xaml` - wprowadzanie danych.
* `UserControls/QuadratureStepsControl.xaml` - wyświetlanie tabeli kroków pośrednich.
* `UserControls/MethodResultsControl.xaml` - globalne porównywanie wyników wszystkich metod jednocześnie.

---

## II. Wiązanie całości (Architektura)

### II.1. **Widok Główny:** `Views/MainWindow.xaml`

* Okno główne jest rozwiązywane przez kontener Dependency Injection skonfigurowany w `App.xaml.cs`.
* Biblioteka `Microsoft.Extensions.DependencyInjection` - Umożliwia rejestrację i rozwiązywanie zależności między komponentami (np. serwisami, modelami, widokami).

### II.2. **Rdzeń uruchomieniowy i wstrzykiwanie zależności (DI)**

* **`App.xaml`** – Główny plik konfiguracyjny XAML całej aplikacji. Zawiera globalne zasoby, w tym zmodyfikowany styl walidacji błędów (estetyczna czerwona ramka wokół niepoprawnych pól tekstowych bez niszczenia układu layoutu).
* **`App.xaml.cs`** – Kod startowy aplikacji. Zastępuje domyślne uruchamianie okna przez zaimplementowanie kontenera Dependency Injection (`ServiceCollection`). Rejestruje wszystkie widoki, modele, parsery funkcji, algorytmy oraz strategie graficzne, a następnie inicjuje `MainWindow`.

### II.3. **Orkiestrator Logiki (ViewModel):** `ViewModels/MainViewModel.cs`

* Wzorzec MVVM z automatycznym powiadamianiem o zmianach `CommunityToolkit.Mvvm`.
* `ViewModels/MainViewModel.Commands.cs` – Zawierający wyłącznie logikę przypisaną do akcji użytkownika. Obejmuje komendy wyzwalające obliczanie całki i podział iteracji na wszystkie algorytmy.
* `ViewModels/MainViewModel.Observers.cs` – Zawierający wyłącznie metody nasłuchujące (`PropertyChanged`). Aktywuje m.in. żółte ostrzeżenie na interfejsie informujące o automatycznym zaokrągleniu w górę precyzji $n$ dla Metody Simpsona.

### II.4. **Weryfikacja Danych:** `Validators/MainViewModelValidator.cs`

* Mechanizm sprawdzający poprawność wprowadzanych parametrów matematycznych (np. czy $n > 0$, czy $a < b$) z obsługą błędów UI `fluentvalidation.dependencyinjectionextensions`

---

## III. Dodatkowe kroki wykonane podczas realizacji projektu

W celu zapewnienia stabilności matematycznej oraz wysokich standardów (Clean Architecture), aplikacja wykorzystuje dodatkowe rozwiązania:

### III.1. **Bezpieczna obsługa danych i ostrzeżenia (UX/UI)**

* Zabezpieczenie wizualne – wyłączenie w kontrolce widoku osi opcji zoomowania i przesuwania (`IsZoomEnabled = false`), co chroni wizualizację przed przypadkowym przesuwaniem i skalowaniem.
* Ujednolicenie separatorów dziesiętnych – Zaimplementowano w kodzie, automatyczną zamianę przecinków na kropki (funkcja `Replace(',', '.')`) dla wpisywanych granic całkowania ($a$, $b$) oraz samego wzoru funkcji .

### III.2. **Wzorzec Strategii dla Wykresów (Strategy Pattern)**

* W celu eliminacji rozbudowanych instrukcji warunkowych (tzw. drabinek `if/else`) przy renderowaniu figur geometrycznych dla różnych kwadratur, wprowadzono interfejs `IPlottingStrategy`.
* Każda metoda otrzymała dedykowaną, wyizolowaną klasę rysującą umieszczoną w folderze `Services/PlottingStrategies/` (np. `RectangleLeftPlottingStrategy`, `SimpsonPlottingStrategy`, `TrapezoidalPlottingStrategy`).
* Główny serwis odpowiedzialny za wykresy w locie deleguje zadanie renderowania do odpowiedniej strategii na podstawie nazwy aktualnie wybranej metody, co w pełni realizuje zasadę Open-Closed Principle (OCP).

### III.3. **Implementacja Metody Gaussa-Legendre'a**

* Jako zwieńczenie prac algorytmicznych dodano metodę Gaussa (plik `Services/Algorithms/GaussLegendreMethod.cs`) wraz z odpowiadającą jej strategią rysowania wykresu (`GaussPlottingStrategy.cs`).
* Kwadratura Gaussa-Legendre’a jest pierwotnie zdefiniowana dla standardowego przedziału $[-1, 1]$:

$$\int_{-1}^{1} f(x)dx \approx \sum_{i=1}^{n} w_i f(t_i)$$

* Algorytm wykorzystuje gotowy wzór na transformację afiniczną, dynamicznie przeliczając standardowe węzły i wagi z przedziału [-1, 1] na dowolny docelowy przedział [a, b] wprowadzony przez użytkownika.:

$$x = \frac{a+b}{2} + \frac{b-a}{2}t$$

$$dx = \frac{b-a}{2}dt$$

* Ostateczny wzór użyty w algorytmie (obsługujący twardo zakodowane węzły i wagi wielomianów dla dokładności $n$ od 1 do 5) przyjmuje postać:

$$\int_{a}^{b} f(x)dx \approx \frac{b-a}{2} \sum_{i=1}^{n} w_i f\left(\frac{b-a}{2}t_i + \frac{a+b}{2}\right)$$