# Analiza Fouriera (DFT/IDFT) - Odszumianie Danych

Projekt zrealizowany w architekturze WPF MVVM z zachowaniem zasady Single Responsibility Principle (SRP). Aplikacja służy do wczytywania zaszumionych sygnałów z plików Excel, analizy widma przy pomocy Dyskretnej Transformaty Fouriera (DFT), filtrowania szumów oraz rekonstrukcji sygnału przy użyciu Odwrotnej Transformaty Fouriera (IDFT).

## Architektura i realizacja zadań / Adaptacja rozwiązań Excelowych do WPF MVVM

1. **Wczytaj plik dft.xls** (kolumna A – nr próbki sygnału, kolumna B – sygnał zaszumiony)
* I. Plik (`Services/Infrastructure/ExcelImportService.cs`) - Import danych z Excela. Użytkownik podaje nr arkusza Excel oraz komórkę, od której są wypisane dane dla x(n) "sygnał zaszumiony". Dane trafiają do Modelu. Wykorzystuje: `[ExcelDataReader, ExcelDataReader.]`.

2. **Przygotowujemy opis kolumn dla transformaty Fouriera:**
* II. Plik (`UserControls/NoisySignalDataControl.xaml`) - Kontrolka (UserControl) prezentująca tabelę z kolumnami: `n` | `x(n) sygnał zaszumiony` | `DFT` | `|DFT|`.

3. **Menu DANE -> ANALIZA DANYCH –> ANALIZA FOURIERA:**
* III. Plik (`Services/Application/DftCalculationService.cs`) - Serwis, który oblicza DFT. Dodatkowo jedna z jego metod zwraca moduł, aby uzupełnić dane w Modelu.

4. **Wprowadzamy dane do analizy Fouriera zgodnie z rysunkiem -> Zatwierdzamy OK**
* IV. Plik (`Models/NoisySignalModel.cs`) - Model przechowujący wczytane dane (n | x(n) sygnał zaszumiony | DFT | |DFT|).

5. **W komórce E2 wprowadzamy formułę „=MODUŁ.LICZBY.ZESP(D2)” -> Kopiujemy formułę na całą kolumnę**
* Zrealizowane jako metoda wywoływana przez III. Plik (`DftCalculationService.cs` - przypisanie właściwości `DftMagnitude`).

6. **Generujemy wykres widma Amplitudowo – Częstotliwościowego.**
* V. Plik (`Models/PlotDataModel.cs`) - Model przechowujący dane do wykresów.
* VI. Plik (`Services/Application/PlotGeneratorService.cs`) - Serwis realizujący logikę generowania wykresu widma. Wykorzystuje: `[OxyPlot.Wpf]`.

7. **Przykładowy wykres:**
* VII. Plik (`UserControls/SpectrumPlotControl.xaml`) - Kontrolka wizualna odpowiedzialna za renderowanie utworzonych wykresów w oknie aplikacji.

8. **Przygotowujemy nagłówki kolumn dla sygnału pozbawionego szumu...**
* VIII. Plik (`UserControls/DenoisedSignalDataControl.xaml`) - Kontrolka prezentująca tabelę z kolumnami: `odszumione widmo` | `IDFT` | `y(n) sygnał odszumiony`.

9. **W widmie sygnału pozostawiamy tylko główny pik (wartości mniejsze zamieniamy na zero)**
* IX. Plik (`Services/Application/SpectrumThresholdService.cs`) - Serwis przeszukujący wyliczone moduły. Wybiera wartości powyżej wskazanego progu (domyślnie obliczanego dynamicznie), zmieniając te mniejsze na 0.

10. **Wyznaczamy Odwrotną DFT dla widma pozbawionego szumu...**
* X. Plik (`Services/Application/IdftCalculationService.cs`) - Serwis generujący odwrócone DFT (IDFT) na przefiltrowanych danych.

11. **W komórce I2 wprowadzamy formułę zamieniającą wartość obliczona przez IDFT z komórki H2 na liczbę**
* XI. Plik (`Services/Application/SignalReconstructionService.cs`) - Serwis wyciągający wartość rzeczywistą obliczeń do zmiennej y(n) reprezentującej sygnał odszumiony.

12. **Przykładowe wyniki wykonania obliczeń**
* XII. Plik (`Models/DenoisedSignalModel.cs`) - Model zawierający przefiltrowane piki, wyzerowane wartości oraz sygnał zrekonstruowany.

13. **Wykonujemy wykres danych z kolumny I2:I65 (porównanie)**
* XIII. Plik (`Views/MainWindow.xaml`) - Główny widok aplikacji, łączący wszystkie kontrolki (`NoisySignalDataControl`, `DenoisedSignalDataControl`, `SpectrumPlotControl`) i umożliwiający wygodne korzystanie z programu. Używa kontrolki pośredniej (`CombinedTablesControl.xaml`) do synchronizacji suwaków.

14. **Porównanie otrzymanych wykresów dla sygnału zaszumionego oraz dla sygnału odszumionego**
* XIV. Plik (`Services/Infrastructure/ComparisonPlotGenerator.cs`) - Serwis tworzący wykres porównawczy liniowy (sygnał x(n) wejściowy vs y(n) wyjściowy). Wykorzystuje: `[OxyPlot.Wpf]`.

---

## Wiązanie całości (Architektura)

* **Widok Główny:** `Views/MainWindow.xaml`
* Tworzony i zarządzany przez wbudowany kontener DI. Wykorzystuje: `[Microsoft.Extensions.DependencyInjection]`

* **Orkiestrator Logiki (ViewModel):** `ViewModels/MainViewModel.cs` (wraz z podziałem `partial` na `.Commands.cs` oraz `.Observers.cs`)
* Wzorzec MVVM z automatycznym powiadamianiem o zmianach. Wykorzystuje: `[CommunityToolkit.Mvvm]`

* **Weryfikacja Danych:** `Validators/MainViewModelValidator.cs`
* Mechanizm sprawdzający poprawność wprowadzanych parametrów z obsługą wizualnych błędów. Wykorzystuje: `[FluentValidation]`

---

## Dodatkowe pliki i komponenty systemowe

W trakcie rozwoju projektu, w celu utrzymania najwyższych standardów czystego kodu (Clean Architecture) i poprawy interfejsu użytkownika (UX), aplikacja została rozbudowana o następujące pliki:

### 15. Synchronizacja interfejsu (Połączone Tabele)

* **`UserControls/CombinedTablesControl.xaml`** (oraz jego Code-Behind `.xaml.cs`) – Pośrednia kontrolka wizualna, która spina tabelę sygnału zaszumionego (`NoisySignalDataControl`) i odszumionego (`DenoisedSignalDataControl`). Ukrywa podwójne paski przewijania (scroll) i za pomocą logiki w kodzie zrównuje ich marginesy oraz synchronizuje przewijanie, tworząc iluzję jednej, spójnej tabeli.

### 16. Dynamiczne obliczanie parametrów

* **`Services/Application/ThresholdCalculationService.cs`** – Wydzielony mikro-serwis odpowiedzialny wyłącznie za matematyczne wyliczenie domyślnego progu szumu (wartość `N/2`). Wywoływany automatycznie za każdym razem, gdy użytkownik zmieni źródło danych (plik, arkusz lub komórkę).

### 17. Rozszerzenia ViewModelu (Wzorzec Partial Class)

Aby zapobiec rozrostowi głównego pliku logiki (`MainViewModel.cs`) do tzw. "God Object", został on podzielony na 3 fizyczne pliki za pomocą słowa kluczowego `partial`:

* **`ViewModels/MainViewModel.Commands.cs`** – Plik zawierający wyłącznie logikę przypisaną do akcji użytkownika (przyciski, kliknięcia). Obejmuje komendy takie jak wczytywanie pliku czy główna orkiestracja analizy danych.
* **`ViewModels/MainViewModel.Observers.cs`** – Plik zawierający wyłącznie metody nasłuchujące (`On...Changed`). Automatycznie reaguje na zmiany wprowadzane przez użytkownika w polach tekstowych i zarządza wyświetlaniem zielonego monitu o konieczności ponownej analizy.

### 18. Rdzeń uruchomieniowy i wstrzykiwanie zależności (DI)

* **`App.xaml`** – Główny plik konfiguracyjny XAML całej aplikacji. Zawiera globalne zasoby, w tym zdefiniowany domyślny, niestandardowy styl walidacji błędów (czerwona ramka wokół pól, w których użytkownik wpisał nieprawidłowe dane).
* **`App.xaml.cs`** – Kod startowy aplikacji. Zastępuje domyślne uruchamianie okna przez zaimplementowanie kontenera Dependency Injection (`ServiceProvider`). Rejestruje wszystkie widoki, modele widoków (`ViewModels`) oraz walidatory z biblioteki `FluentValidation`, a następnie inicjuje i wyświetla `MainWindow`.