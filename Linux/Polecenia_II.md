# Polecenia linux cz. 2

## Polecenie `alias`-  skróty dla często używanych poleceń

**Alias** to nic innego jak skrót, który nadajemy dłuższemu poleceniu. Dzięki temu możemy przyspieszyć naszą pracę w terminalu, unikając ciągłego wpisywania tych samych, często powtarzających się komend.

### Jak tworzyć aliasy?

**Tworzenie tymczasowego aliasu:**

```bash
alias nowa_nazwa='stare_polecenie'
```

* **nowa_nazwa:** dowolna wybrana przez Ciebie nazwa aliasu.
* **stare_polecenie:** polecenie, które chcesz zastąpić skrótem.

**Przykład:**

```bash
alias ll='ls -la'
```

Teraz, zamiast wpisywać `ls -la` (aby wyświetlić szczegółowy listing plików), wystarczy wpisać `ll`.

**Tworzenie trwałego aliasu:**

Aby aliasy były dostępne po każdym uruchomieniu terminala, dodaj je do pliku `.bashrc`. Ten plik jest wykonywany przy każdym uruchomieniu powłoki Bash.

1. **Otwórz plik .bashrc w swoim ulubionym edytorze:**

   ```bash
   nano ~/.bashrc
   ```

2. **Dodaj swoje aliasy na końcu pliku:**

   ```
   alias ll='ls -la'
   alias rm='rm -i'  # Usuwanie plików z potwierdzeniem
   ```

3. **Zastosuj zmiany:**

   ```bash
   source ~/.bashrc
   ```

### Dlaczego warto używać aliasów?

* **Zwiększenie wydajności:** Oszczędzasz czas, unikając wpisywania długich poleceń.
* **Usprawnienie pracy:** Możesz tworzyć własne, spersonalizowane skróty, które ułatwią Ci pracę.
* **Poprawa czytelności:** Złożone polecenia można zastąpić prostymi aliasami, co ułatwia zrozumienie wykonywanych działań.

### Przykładowe aliasy:

* **Przełączanie się między katalogami:**
  ```bash
  alias ..='cd ..'
  ```
* **Czyszczenie ekranu:**
  ```bash
  alias clear='clear && printf "\e[3J"'
  ```
* **Szybki dostęp do często używanych katalogów:**
  ```bash
  alias projects='cd ~/projects'
  ```

### Uwagi:

* **Unikaj nadpisywania wbudowanych poleceń:** Nie nadawaj aliasów o takich samych nazwach jak istniejące polecenia, aby uniknąć nieoczekiwanych zachowań.
* **Uważaj na potencjalne konflikty:** Jeśli używasz wielu różnych narzędzi, upewnij się, że twoje aliasy nie kolidują z innymi definicjami.
* **Dokumentuj swoje aliasy:** Jeśli tworzysz wiele aliasów, warto je dobrze udokumentować, abyś Ty i inni użytkownicy mogli łatwo zrozumieć ich funkcjonalność.



## Polecenie `find` – Wyszukiwanie plików i katalogów

**`find`** to potężne narzędzie wiersza poleceń w Linuksie i innych systemach Unix-like, służące do **wyszukiwania plików i katalogów** w hierarchii systemu plików.

### Podstawowe użycie:

```bash
find ścieżka_startowa
```

To polecenie przeszuka katalog `ścieżka_startowa` i wszystkie jego podkatalogi, wyświetlając pełną ścieżkę do każdego znalezionego pliku i katalogu.

### Opcje:

* **`-name wzorzec`**: Wyszukiwanie plików o nazwie pasującej do wzorca.
  ```bash
  find . -name "*.txt"
  ```
  Znajdzie wszystkie pliki z rozszerzeniem `.txt` w bieżącym katalogu i jego podkatalogach.
* **`-type typ`**: Wyszukiwanie plików o określonym typie.
  ```bash
  find . -type d
  ```
  Znajdzie wszystkie katalogi w bieżącym katalogu i jego podkatalogach.
* **`-size +N`**: Wyszukiwanie plików większych niż N bloków.
  ```bash
  find . -size +100k
  ```
  Znajdzie pliki większe niż 100 kilobajtów.
* **`-mtime +N`**: Wyszukiwanie plików zmodyfikowanych N dni temu.
  ```bash
  find . -mtime +7
  ```
  Znajdzie pliki zmodyfikowane więcej niż 7 dni temu.
* **`-exec polecenie {} \;`**: Wykonuje polecenie na każdym znalezionym pliku.
  ```bash
  find . -name "*.txt" -exec grep "słowo" {} \;
  ```
  Szuka słowa "słowo" we wszystkich plikach `.txt` w bieżącym katalogu i jego podkatalogach.

### Przykładowe zastosowania:

* **Wyszukiwanie plików o określonym rozszerzeniu:**
  ```bash
  find . -name "*.pdf"
  ```
* **Wyszukiwanie plików zmodyfikowanych w ostatnim tygodniu:**
  ```bash
  find . -mtime -7
  ```
* **Usuwanie wszystkich plików o rozszerzeniu .tmp:**
  ```bash
  find . -name "*.tmp" -delete
  ```


## Polecenie `tar` – Tworzenie i zarządzanie archiwami

**`tar`** (od angielskiego *Tape ARchiver*) to potężne narzędzie wiersza poleceń w systemach Unix-like, służące do tworzenia, modyfikowania i wyodrębniania archiwów. Archiwa utworzone za pomocą `tar` to pliki zawierające wiele innych plików i katalogów, często skompresowane za pomocą dodatkowych narzędzi jak `gzip`, `bzip2` czy `xz`.

### Podstawowe użycie:

```bash
tar [opcje] [plik_archiwum] [pliki_do_archiwizacji]
```

### Najczęściej używane opcje:

* **`-c`:** Tworzy nowe archiwum.
* **`-x`:** Wyodrębnia pliki z archiwum.
* **`-t`:** Wyświetla zawartość archiwum.
* **`-r`:** Dodaje pliki do istniejącego archiwum.
* **`-u`:** Aktualizuje pliki w archiwum.
* **`-v`:** Wyświetla szczegółowe informacje o wykonywanych operacjach.
* **`-f`:** Określa nazwę pliku archiwum.

### Przykładowe zastosowania:

* **Tworzenie archiwum:**
  ```bash
  tar -czvf archiwum.tar.gz dokumenty
  ```
  Tworzy skompresowane archiwum `archiwum.tar.gz` zawierające zawartość katalogu `dokumenty`.
* **Wyodrębnianie archiwum:**
  ```bash
  tar -xvf archiwum.tar.gz
  ```
  Wyodrębnia wszystkie pliki z archiwum `archiwum.tar.gz` do bieżącego katalogu.
* **Wyświetlanie zawartości archiwum:**
  ```bash
  tar -tvf archiwum.tar.gz
  ```
  Wyświetla listę plików znajdujących się w archiwum `archiwum.tar.gz`.

### Kompresja archiwów:

`tar` sam w sobie nie kompresuje danych. Aby skompresować archiwum, należy połączyć go z narzędziami kompresji takimi jak:
* **`gzip`:** Tworzy pliki z rozszerzeniem `.gz`.
* **`bzip2`:** Tworzy pliki z rozszerzeniem `.bz2`.
* **`xz`:** Tworzy pliki z rozszerzeniem `.xz`.

**Przykład z kompresją:**
```bash
tar -czvf archiwum.tar.gz dokumenty
```
Tworzy archiwum `archiwum.tar.gz`, gdzie `.gz` oznacza, że archiwum zostało skompresowane algorytmem gzip.


## Rozpakownie pliku
```
Tar -xzvs [nazwa_pliku].tar.gz
```
## Polecenie `gzip` – Kompresja plików

**`gzip`** to popularne narzędzie wiersza poleceń w systemach Unix-like (w tym Linux), służące do **kompresji plików**. Algorytm gzip zapewnia bezstratną kompresję, co oznacza, że po dekompresji otrzymujemy dokładnie takie same dane, jakie mieliśmy na początku. Pliki skompresowane gzip mają zazwyczaj rozszerzenie `.gz`.

### Podstawowe użycie:

```bash
gzip plik.txt
```

To polecenie skompresuje plik `plik.txt`, zastępując go skompresowaną wersją `plik.txt.gz`.

### Opcje:

* **`-c`**: Kompresuje do standardowego wyjścia. Pozwala na przekierowanie wyjścia do innego pliku.
  ```bash
  gzip -c plik.txt > plik.txt.gz
  ```
* **`-v`**: Verbose: Wyświetla informacje o postępie kompresji.
* **`-k`**: Keep: Zachowuje oryginalny plik.
* **`-r`**: Recursive: Rekursywnie kompresuje wszystkie pliki w podanym katalogu.

### Przykład:

```bash
gzip -rv dokumenty
```

To polecenie rekursywnie skompresuje wszystkie pliki w katalogu `dokumenty` i podkatalogach.

### Dlaczego warto używać gzip?

* **Oszczędność miejsca:** Kompresja pozwala zmniejszyć rozmiar plików, co jest przydatne przy archiwizowaniu danych lub przesyłaniu ich przez sieć.
* **Szybkość transferu:** Mniejsze pliki szybciej się przesyłają.
* **Efektywne wykorzystanie przestrzeni dyskowej:** Kompresja pozwala zaoszczędzić miejsce na dysku.


## Polecenie `gunzip` – De kompresja plików gzip

**`gunzip`** to narzędzie wiersza poleceń w Linuksie i innych systemach Unix-like, służące do **dekompresji plików skompresowanych za pomocą algorytmu gzip**. Pliki skompresowane gzip mają zwykle rozszerzenie `.gz`.

### Podstawowe użycie:

```bash
gunzip plik.gz
```

To polecenie dekompresuje plik `plik.gz`. Po dekompresji powstanie plik o nazwie `plik`.

### Opcje:

* **`-f`**: Force: Nadpisuje istniejący plik bez pytania.
* **`-v`**: Verbose: Wyświetla informacje o postępie dekompresji.

### Przykład:

```bash
gunzip -v dokument.tar.gz
```

To polecenie dekompresuje plik `dokument.tar.gz` i wyświetla informacje o postępie dekompresji.

### Uwagi:

* **Bezpieczeństwo:** Upewnij się, że masz wystarczająco miejsca na dysku przed dekompresją dużego pliku.
* **Prawa dostępu:** Sprawdź, czy masz odpowiednie uprawnienia do dekompresji pliku.


## Polecenie `head` – Wyświetlanie początku pliku

**`head`** to narzędzie wiersza poleceń w Linuksie i innych systemach Unix-like, które służy do **wyświetlania początkowych linii pliku**. Jest przydatne do szybkiego przeglądania zawartości plików, zwłaszcza dużych.

### Podstawowe użycie:

```bash
head plik.txt
```

To polecenie wyświetli pierwsze 10 linii pliku `plik.txt`.

### Opcje:

* **`-n liczba`**: Wyświetla określoną liczbę linii.
  ```bash
  head -n 5 plik.txt
  ```
  Wyświetli pierwsze 5 linii.

### Przykładowe zastosowanie:

* **Szybki przegląd zawartości pliku:**
  ```bash
  head config.txt
  ```
* **Sprawdzenie nagłówka pliku:**
  ```bash
  head -n 1 dane.csv
  ```


## Polecenie `tail` – Wyświetlanie końca pliku

**`tail`** to przydatne narzędzie w Linuksie, które pozwala na wyświetlanie ostatnich linii pliku. Jest często używane do monitorowania logów systemowych czy śledzenia postępu procesów.

### Podstawowe użycie:

```bash
tail plik.txt
```

To polecenie wyświetli ostatnie 10 linii pliku `plik.txt`.

### Opcje:

* **`-n liczba`**: Wyświetla określoną liczbę linii.
  ```bash
  tail -n 5 plik.txt
  ```
  Wyświetli ostatnie 5 linii.
* **`-f`**: Monitoruje plik i wyświetla nowe linie w czasie rzeczywistym.
  ```bash
  tail -f log.txt
  ```
  Będzie ciągle aktualizować wyświetlane linie, gdy nowe będą dodawane do pliku.

### Przykładowe zastosowania:

* **Monitorowanie logów serwera:**
  ```bash
  tail -f /var/log/apache2/access.log
  ```
* **Przeglądanie ostatnich zmian w pliku konfiguracyjnym:**
  ```bash
  tail -n 20 config.txt
  ```
* **Śledzenie postępu procesu:**
  ```bash
  tail -f process.log
  ```


## Polecenie `less` – Bardziej elastyczne przeglądanie plików

**`less`** to rozszerzenie funkcjonalności polecenia `more`. Jest to bardziej zaawansowane narzędzie do przeglądania plików tekstowych, które oferuje wiele dodatkowych opcji i ułatwia nawigację po dużych plikach.

### Podstawowe użycie:

```bash
less plik.txt
```

Podobnie jak w przypadku `more`, to polecenie wyświetli zawartość pliku `plik.txt` strona po stronie.

### Kluczowe różnice między `less` a `more`:

* **Nawigacja:** `less` pozwala na swobodne przewijanie zarówno w górę, jak i w dół, podczas gdy `more` umożliwia jedynie przechodzenie do następnej strony.
* **Wyszukiwanie:** `less` oferuje zaawansowane funkcje wyszukiwania, takie jak wyszukiwanie według wzorca, wyszukiwanie z wyróżnieniem oraz wyszukiwanie wstecz.
* **Edycja:** W niektórych wersjach `less` można nawet edytować zawartość pliku bezpośrednio w trakcie przeglądania.
* **Wyjście:** `less` pozwala na bardziej elastyczne wychodzenie z trybu przeglądania, oferując dodatkowe opcje.

### Przydatne klawisze w `less`:

* **Spacja**: Wyświetla kolejną stronę.
* **b**: Cofnięcie o jedną stronę.
* **g**: Przejdź na początek pliku.
* **G**: Przejdź na koniec pliku.
* **/szukana_fraza**: Wyszukaj do przodu.
* **?szukana_fraza**: Wyszukaj do tyłu.
* **n**: Powtórz ostatnie wyszukiwanie.
* **N**: Powtórz ostatnie wyszukiwanie w przeciwną stronę.
* **q**: Zakończ przeglądanie.
* **h**: Wyświetl podpowiedź z dostępnymi poleceniami.

### Przykładowe zastosowania:

* **Szybkie przewijanie dużego pliku:**
  ```bash
  less -N plik.txt
  ```
  Wyświetla numery linii, ułatwiając nawigację.
* **Wyszukiwanie konkretnego wzorca:**
  ```bash
  less plik.txt
  /błąd
  ```
  Szuka słowa "błąd" w pliku.
* **Edycja pliku (jeśli jest to możliwe):**
  ```bash
  less -e plik.txt
  ```
  Otwiera plik w trybie edycji (zazwyczaj za pomocą edytora `vi`).



## Polecenie `ln` – Tworzenie dowiązań

**`ln`** (link) to polecenie w Linuksie i innych systemach Unix-like, służące do **tworzenia dowiązań** między plikami. Dowiązania pozwalają na utworzenie dodatkowego "wejścia" do istniejącego pliku, bez kopiowania jego zawartości.

### Rodzaje dowiązań:

* **Dowiązania twarde:**
  * Są to bezpośrednie odwołania do inodu (numeru i-węzła) pliku.
  * Dowiązanie twarde i oryginalny plik dzielą te same dane na dysku.
  * Dowiązanie twarde musi znajdować się na tym samym systemie plików co oryginalny plik.
  * Usunięcie oryginalnego pliku powoduje, że dowiązania twarde stają się nieprawidłowe.
* **Dowiązania symboliczne (skróty):**
  * Są to pliki, które zawierają ścieżkę do oryginalnego pliku.
  * Mogą wskazywać na pliki w różnych systemach plików.
  * Usunięcie oryginalnego pliku powoduje, że dowiązanie symboliczne staje się nieprawidłowe.

### Podstawowe użycie:

```bash
ln [opcje] plik_źródłowy plik_docelowy
```

* **`plik_źródłowy`:** Plik, do którego tworzymy dowiązanie.
* **`plik_docelowy`:** Nazwa nowego dowiązania.

### Opcje:
* **`-s`:** Tworzy dowiązanie symboliczne.

### Przykład:

```bash
ln -s dokument.txt skrot_do_dokumentu
```

To polecenie utworzy dowiązanie symboliczne o nazwie `skrot_do_dokumentu`, które będzie wskazywać na plik `dokument.txt`.

### Zastosowania:

* **Tworzenie skrótów:** Ułatwia dostęp do często używanych plików.
* **Zarządzanie bibliotekami:** Wiele programów używa dowiązań do współdzielonych bibliotek.
* **Tworzenie kopii zapasowych:** Dowiązania twarde mogą być używane do tworzenia szybkiej kopii zapasowej ważnych plików.


## Polecenie `more` – Przeglądanie plików strona po stronie

**Polecenie `more`** to jedno z podstawowych narzędzi w wierszu poleceń, które pozwala na przeglądanie zawartości plików tekstowych strona po stronie. Jest szczególnie przydatne, gdy mamy do czynienia z dużymi plikami, które nie mieszczą się w całości na ekranie.

### Podstawowe użycie:

```bash
more plik.txt
```

To spowoduje wyświetlenie zawartości pliku `plik.txt`, po jednej stronie na raz. Aby przejść do następnej strony, naciskamy spację.

### Opcje:

* **`-n`**: Określa liczbę linii wyświetlanych na jednej stronie.
  ```bash
  more -n 20 plik.txt
  ```
  Wyświetli po 20 linii na stronę.
* **`+n`**: Zaczyna wyświetlanie od n-tej linii.
  ```bash
  more +100 plik.txt
  ```
  Zaczyna wyświetlanie od 100. linii.
* **`-s`**: Zmienia ciągi pustych linii na pojedynczą pustą linię.

### Inne przydatne klawisze:

* **Spacja**: Wyświetla kolejną stronę.
* **Enter**: Wyświetla kolejną linię.
* **b**: Cofnięcie o jedną stronę.
* **h**: Wyświetla podpowiedź z dostępnymi poleceniami.
* **q**: Zakończenie przeglądania.

### Przykładowe zastosowania:

* **Przeglądanie długich logów:**
  ```bash
  more /var/log/apache2/access.log
  ```
* **Szybkie przeglądanie zawartości pliku:**
  ```bash
  more config.txt
  ```
* **Szukanie konkretnego fragmentu:**
  ```bash
  more +100 plik.txt | grep "słowo"
  ```
  Zaczyna wyświetlanie od 100. linii i szuka w nich słowa "słowo".

### Porównanie z `less`

Podobnym do `more` narzędziem jest `less`. `less` oferuje więcej opcji, takich jak wyszukiwanie wstecz, przewijanie do góry i do dołu, oraz możliwość edycji zawartości. Jest bardziej zaawansowany, ale również nieco bardziej skomplikowany w obsłudze.


## Pipe (`|`) w wierszu poleceń: Łączenie poleceń

**Pipe (`|`)** to potężne narzędzie w wierszu poleceń, które pozwala na połączenie wyjścia jednego polecenia z wejściem drugiego. Dzięki temu możesz tworzyć złożone operacje na danych, przekazując wynik jednego polecenia jako dane wejściowe dla kolejnego.

### Podstawowe zastosowanie:

```bash
polecenie1 | polecenie2
```

To działa w następujący sposób:

1. **polecenie1** wykonuje swoje zadanie i generuje wynik.
2. **Wynik polecenia1** jest przekazywany bezpośrednio jako wejście do **polecenie2**.
3. **polecenie2** przetwarza otrzymane dane i generuje swój własny wynik.

### Przykład:

Załóżmy, że chcesz znaleźć wszystkie linie w pliku `plik.txt`, które zawierają słowo "błąd" i policzyć ich liczbę. Możesz to zrobić za pomocą następującej komendy:

```bash
grep "błąd" plik.txt | wc -l
```

Co się dzieje:

1. **`grep "błąd" plik.txt`** szuka w pliku `plik.txt` wszystkich linii zawierających słowo "błąd".
2. **`| wc -l`** przekazuje wynik `grep` (czyli znalezione linie) do `wc -l`, które zlicza liczbę linii.

### Bardziej złożone przykłady:

Możesz łączyć wiele poleceń, tworząc bardziej złożone operacje. Na przykład:

```bash
ps aux | grep "python" | grep -v grep | wc -l
```

Ta komenda:
1. Wyświetla listę wszystkich procesów (`ps aux`).
2. Filtruje wyniki, pokazując tylko procesy związane z Pythonem (`grep "python"`).
3. Usuwa z wyników sam proces `grep` (`grep -v grep`).
4. Liczy pozostałe procesy Pythona (`wc -l`).


## Komenda `grep`

**`grep`** to potężne narzędzie wiersza poleceń, które umożliwia wyszukiwanie wzorców tekstowych w plikach. Jest niezwykle przydatne do przeglądania dużych zbiorów danych, logów czy kodów źródłowych.

### Podstawowe użycie:

```bash
grep "wzorzec" plik
```

* **`wzorzec`:** Tekst, który chcesz znaleźć.
* **`plik`:** Plik, w którym chcesz szukać wzorca.

### Opcje:

* **`-i`**: Ignoruje wielkość liter.
* **`-v`**: Wyświetla linie, które **nie** pasują do wzorca.
* **`-c`**: Liczy linie, które pasują do wzorca.
* **`-n`**: Numeruje linie.
* **`-r`**: Szuka rekurencyjnie w podkatalogach.
* **`-w`**: Dopasowuje całe słowa.
* **`-e`**: Umożliwia podanie wielu wzorców.
* **`-f plik`**: Pobiera wzorce z pliku.

### Przykłady:

* **Wyszukiwanie słowa "error" w pliku log.txt, ignorując wielkość liter:**
  ```bash
  grep -i "error" log.txt
  ```
* **Wyświetlenie linii, które nie zawierają słowa "success" w pliku results.txt:**
  ```bash
  grep -v "success" results.txt
  ```
* **Zliczenie wystąpień słowa "function" w wszystkich plikach .c w bieżącym katalogu i podkatalogach:**
  ```bash
  grep -rc "function" *.c
  ```
* **Wyszukiwanie wielu wzorców (error lub warning) w pliku:**
  ```bash
  grep -e "error" -e "warning" log.txt
  ```
* **Wyszukiwanie wzorca w wielu plikach, podając je w pliku patterns.txt:**
  ```bash
  grep -f patterns.txt *
  ```

### Wyrażenia regularne:

`grep` obsługuje wyrażenia regularne, co pozwala na bardziej zaawansowane wyszukiwania. Na przykład:

* **`.`:** Dowolny pojedynczy znak.
* **`*`:** Zero lub więcej wystąpień poprzedzającego znaku.
* **`^`:** Początek linii.
* **`$`:** Koniec linii.
* **`[abc]`:** Dowolny znak z podanego zestawu.
* **`[^abc]`:** Dowolny znak poza podanym zestawem.


## Komenda `tail`

**`tail`** to narzędzie wiersza poleceń, które służy do wyświetlania ostatnich linii pliku tekstowego. Jest szczególnie przydatne do monitorowania logów, gdzie często interesuje nas najnowsza aktywność.

### Podstawowe użycie:

```bash
tail plik.txt
```

To wyświetli ostatnie 10 linii pliku `plik.txt`.

### Opcje:

* **`-n liczba`**: Wyświetla określoną liczbę linii.
  ```bash
  tail -n 5 plik.txt
  ```
  Wyświetli ostatnie 5 linii.
* **`-f`**: Monitoruje plik i wyświetla nowe linie w czasie rzeczywistym.
  ```bash
  tail -f log.txt
  ```
  Będzie ciągle aktualizować wyświetlane linie, gdy nowe będą dodawane do pliku.

### Przykładowe zastosowania:

* **Monitorowanie logów serwera:**
  ```bash
  tail -f /var/log/apache2/access.log
  ```
* **Przeglądanie ostatnich zmian w pliku konfiguracyjnym:**
  ```bash
  tail -n 20 config.txt
  ```
* **Śledzenie postępu procesu:**
  ```bash
  tail -f process.log
  ```


# Narzędzie do archiwizacji `tar` (często łączone z zip'em) 
Podstawowe parametry:
- `-c` Create - tworzy nowy archiwum.
- `-x` Extract - wyodrębnia pliki z archiwum.
- `-t` Table of contents - wyświetla listę plików znajdujących się w archiwum bez ich wyodrębniania.
- `-f` File - określa nazwę pliku archiwum.
Parametry kompresji:
- `-z` Gzip - kompresuje archiwum za pomocą algorytmu gzip.
- `-j` Bzip2 - kompresuje archiwum za pomocą algorytmu bzip2.
- `-J` XZ - kompresuje archiwum za pomocą algorytmu xz.
Parametry dodatkowe:
- `-v` Verbose - wyświetla szczegółowe informacje podczas wykonywania operacji.

    - Przy roapakowaniu zamiast `c` wstawiamy `x`

# Klucz do liczenia lini, znaków, baitów, słów `wc`
Komenda 'wc' (word count) to podstawowe narzędzie wiersza poleceń służące do liczenia linii, słów, znaków i bajtów w plikach tekstowych.
- `-l` line Liczy linie.
- `-w` word Liczy słowa.
- `-c` characters(bytes) Liczy bajty.
- `-m` mark Liczy znaki (włącznie z niedrukowalnymi).