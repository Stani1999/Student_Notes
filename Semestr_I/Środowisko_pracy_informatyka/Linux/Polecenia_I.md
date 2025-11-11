# Polecenia linux cz. I

## 1. Polecenie `cat` – Proste, ale potężne narzędzie do wyświetlania plików

**`cat`** (skrót od "concatenate", czyli "łączyć") to jedno z podstawowych poleceń w Linuksie i innych systemach Unix-like. Służy przede wszystkim do **wyświetlania zawartości plików** na standardowym wyjściu (zwykle ekranie), ale ma również inne zastosowania.

### Podstawowe użycie

* **Wyświetlanie zawartości jednego pliku:**
   ```bash
   cat plik.txt
   ```
   To spowoduje wyświetlenie całego tekstu z pliku `plik.txt` na ekranie.

* **Łączenie wielu plików:**
   ```bash
   cat plik1.txt plik2.txt plik3.txt
   ```
   Zawartość wszystkich trzech plików zostanie wyświetlona kolejno.

### Inne zastosowania

* **Tworzenie nowego pliku:**
   ```bash
   cat > nowy_plik.txt
   ```
   To spowoduje utworzenie nowego pliku `nowy_plik.txt` i przejście w tryb edycji. Wszystko co wpiszesz, zostanie zapisane do tego pliku. Aby zakończyć edycję, naciśnij **Ctrl+D**.

* **Łączenie zawartości plików i zapis do nowego pliku:**
   ```bash
   cat plik1.txt plik2.txt > wynik.txt
   ```
   Zawartość plików `plik1.txt` i `plik2.txt` zostanie połączona i zapisana do nowego pliku `wynik.txt`.

* **Przekazywanie danych do innych programów:**
   ```bash
   cat plik.txt | grep "szukana_fraza"
   ```
   Zawartość pliku `plik.txt` zostanie przekazana jako wejście dla polecenia `grep`, które wyszuka w niej określoną frazę.

### Przydatne opcje

* **`-n`:** Numeruje linie.
  ```bash
  cat -n plik.txt
  ```
* **`-s`:** Zmienia wiele pustych linii na jedną.
  ```bash
  cat -s plik.txt
  ```
* **`-b`:** Numeruje wszystkie niepuste linie.


## 2. Polecenia `tail` i `tac` – Praktyczne narzędzia do pracy z plikami tekstowymi

Polecenia **`tail`** i **`tac`** są przydatne w codziennej pracy z plikami tekstowymi w systemach Linux. Służą do wyświetlania końcowych fragmentów plików (`tail`) oraz odwracania ich zawartości (`tac`). Można je stosować zarówno do analizy logów, jak i do bardziej zaawansowanych operacji na danych.

### Podstawowe użycie `tail`

* **Wyświetlanie ostatnich 10 linii pliku:**
   ```bash
   tail -n 10 plik.txt
   ```

   To polecenie pokazuje ostatnie 10 linii z pliku `plik.txt`. Opcja `-n` pozwala określić liczbę linii, które mają być wyświetlone.

* **Ciągłe monitorowanie zmian w pliku (np. logach):**
   ```bash
   tail -f log.txt
   ```

   Dzięki opcji `-f`, `tail` wyświetla w czasie rzeczywistym nowe linie dodawane do pliku.

### Podstawowe użycie `tac`

* **Wyświetlanie zawartości pliku w odwrotnej kolejności:**
   ```bash
   tac plik.txt
   ```

   Komenda ta odwraca kolejność linii w pliku `plik.txt`, zaczynając od ostatniej.

Oczywiście! Oto tabela z opisem przydatnych opcji:  

| Opcja    | Opis                                                            | Przykład                             |
|----------|-----------------------------------------------------------------|--------------------------------------|
| **`-i`** | Pyta przed nadpisaniem istniejącego pliku.                      | `tail -n 10 plik.txt > wynik.txt -i` |
| **`-p`** | Zachowuje uprawnienia, daty modyfikacji i inne atrybuty plików. | `tac plik.txt > wynik.txt -p`        |
| **`-f`** | Nadpisuje istniejące pliki bez pytania.                         | `tail -n 20 plik.txt > wynik.txt -f` |
| **`-v`** | Wyświetla szczegółowe informacje o przetwarzaniu plików.        | `tac plik.txt > wynik.txt -v`        |

Tabela pozwala na szybkie odnalezienie opcji i ich zastosowania wraz z odpowiednimi przykładami. 

### Przykłady bardziej zaawansowanego użycia

* **Łączenie zawartości wielu plików i zapis do nowego pliku z datą modyfikacji każdego pliku:**
   ```bash
   for file in *.txt; do 
       echo "$(date -r "$file") $file:" >> połączone.txt
       cat "$file" >> połączone.txt
   done
   ```

   W tym przypadku skrypt w pętli `for` przechodzi przez wszystkie pliki z rozszerzeniem `.txt` w bieżącym katalogu, dodaje do każdego datę modyfikacji oraz nazwę pliku, a następnie ich zawartość zapisuje do pliku `połączone.txt`.

### Przydatne wskazówki

* Komenda `tail` z opcją `-f` jest szczególnie użyteczna podczas analizy logów systemowych w czasie rzeczywistym.
* `tac` świetnie nadaje się do analizy danych w plikach, gdzie ostatnie wpisy są najważniejsze.

Dzięki połączeniu poleceń takich jak `tail`, `tac` i pętli `for`, praca z plikami tekstowymi staje się znacznie bardziej efektywna i elastyczna.
```

## 3. Polecenie `cp` w Linuksie: Kopiowanie plików i katalogów

**`cp`** to jedno z podstawowych poleceń w systemie Linux, służące do **kopiowania plików i katalogów**. Dzięki niemu możemy tworzyć duplikaty plików, przenosić je do innych lokalizacji lub tworzyć kopie zapasowe danych.

### Podstawowe użycie:

```bash
cp źródło cel
```

* **źródło:** Plik lub katalog, który chcesz skopiować.
* **cel:** Nowa lokalizacja i/lub nazwa dla kopii.

**Przykład:**

```bash
cp dokument.txt dokument_kopia.txt
```
To polecenie utworzy kopię pliku `dokument.txt` o nazwie `dokument_kopia.txt` w tym samym katalogu.

### Kopiowanie do innego katalogu:

```bash
cp dokument.txt /home/user/dokumenty/
```
Plik `dokument.txt` zostanie skopiowany do katalogu `/home/user/dokumenty/`.

### Kopiowanie katalogów (rekurencyjne):

```bash
cp -r katalog_źródłowy katalog_docelowy
```
Opcja `-r` (lub `-R`) oznacza kopiowanie rekurencyjne, czyli kopiowanie całego katalogu wraz ze wszystkimi podkatalogami i plikami.

### Oto tabela z przydatnymi opcjami:  

| Opcja     | Opis                                                              | Przykład                              |
|-----------|-------------------------------------------------------------------|---------------------------------------|
| **`-i`**  | Pyta przed nadpisaniem istniejącego pliku.                        | `cp -i źródło.txt cel.txt`            |
| **`-p`**  | Zachowuje uprawnienia, daty modyfikacji i inne atrybuty plików.   | `cp -p źródło.txt cel.txt`            |
| **`-f`**  | Nadpisuje istniejące pliki bez pytania.                           | `cp -f źródło.txt cel.txt`            |
| **`-v`**  | Wyświetla szczegółowe informacje o kopiowaniu.                    | `cp -v źródło.txt cel.txt`            |
| **`-rp`** | Kopiuje rekurencyjnie katalog, zachowując uprawnienia             | `cp -rp źródło/ cel/`                 |

### Ważne uwagi:

* **Nadpisywanie plików:** Jeśli plik o takiej samej nazwie już istnieje w katalogu docelowym, zostanie on domyślnie nadpisany. Aby tego uniknąć, użyj opcji `-i`.
* **Prawa dostępu:** Upewnij się, że masz odpowiednie uprawnienia do odczytu i zapisu zarówno dla pliku źródłowego, jak i docelowego.
* **Łącza symboliczne:** Sposób kopiowania łączy symbolicznych zależy od użytych opcji. Opcja `-P` pozwala na zachowanie łączy symbolicznych.


## Polecenie `ls`: Wyświetlanie zawartości katalogu

**`ls`** (list) to podstawowe polecenie w Linuksie i innych systemach Unix-like, służące do **wyświetlania zawartości katalogów**.

### Podstawowe użycie:

```bash
ls
```

To polecenie wyświetli listę plików i katalogów znajdujących się w bieżącym katalogu.

| Opcja    | Opis                                                                                  | Przykład |
|----------|---------------------------------------------------------------------------------------|---------------------------|
| **`-l`** | Wyświetla szczegółowy informacji o uprawnieniach, właścicielu, grupie, rozmiarze, dacie modyfikacji i nazwie pliku. | `ls -l` |
| **`-a`** | Wyświetla wszystkie pliki, w tym ukryte (zaczynające się od kropki).                  | `ls -a`  |
| **`-h`** | Wyświetla rozmiar plików w czytelnym formacie (np. 10K, 2M).                          | `ls -lh` |
| **`-t`** | Sortuje pliki według daty modyfikacji.                                                | `ls -lt` |
| **`-r`** | Sortuje pliki w odwrotnej kolejności.                                                 | `ls -lr` |

### Kombinacje opcji:

Możesz łączyć różne opcje, aby uzyskać bardziej szczegółowe informacje:

```bash
ls -lah
```
To polecenie wyświetli szczegółowy listing wszystkich plików, w tym ukrytych, z rozmiarami w czytelnym formacie.


## Polecenie `man` w Linuksie: Twój osobisty przewodnik po systemach Unix-like

**`man`** to skrót od angielskiego słowa "manual", czyli "instrukcja obsługi". To jedno z najważniejszych narzędzi w Linuksie i innych systemach Unix-like, które służy do **wyświetlania dokumentacji** dotyczącej praktycznie każdego aspektu systemu.

**Jak działa `man`?**

Kiedy wpiszesz w terminalu:

```bash
man ls
```

zostanie wyświetlona szczegółowa dokumentacja dotycząca polecenia `ls`. Dowiesz się o wszystkich dostępnych opcjach, przykładach użycia i innych szczegółach związanych z tym poleceniem.

**Strony manuala są podzielone na sekcje:**

* **1:** Polecenia ogólnego przeznaczenia
* **2:** Wywołania systemowe
* **3:** Biblioteki
* **4:** Specjalne pliki (np. /dev)
* **5:** Formaty plików
* **6:** Gry
* **7:** Konwencje, makra
* **8:** Polecenia administracyjne

**Przykładowe użycie:**

```bash
man man
```
Wyświetli dokumentację dotyczącą samego polecenia `man`.

```bash
man 2 open
```
Wyświetli dokumentację dotyczącą wywołania systemowego `open` (sekcja 2).

**Przydatne opcje:**

* **`-k`:** Wyszukiwanie po słowach kluczowych (np. `man -k grep`).
* **`-s`:** Określenie sekcji (np. `man -s 3 printf`).
* **`-f`:** Szybkie wyszukiwanie (np. `man -f ls`).

**Nawigacja w manualu:**

* **Strona w górę:** Spacja
* **Strona w dół:** Spacja
* **Przejdź do początku strony:** `b`
* **Przejdź do końca strony:** `e`
* **Wyszukiwanie:** `/` (podświetla znalezione słowa)
* **Wyjście:** `q`

**Dlaczego `man` jest tak ważny?**

* **Dokumentacja:** Jest to najbardziej kompletne źródło informacji o systemie.
* **Aktualność:** Dokumentacja jest zwykle aktualizowana wraz z nowymi wersjami systemu.
* **Standaryzacja:** Format stron manuala jest stosowany w wielu systemach Unix-like, co ułatwia korzystanie z różnych dystrybucji Linuksa.


## Polecenie `mkdir` – Tworzenie katalogów

**`mkdir`** (make directory) to podstawowe polecenie w Linuksie i innych systemach Unix-like, służące do **tworzenia nowych katalogów**.

### Podstawowe użycie:

```bash
mkdir nazwa_katalogu
```

To polecenie utworzy nowy katalog o nazwie `nazwa_katalogu` w bieżącym katalogu.

### Tworzenie wielu katalogów:

```bash
mkdir katalog1 katalog2 katalog3
```

To polecenie utworzy trzy nowe katalogi: `katalog1`, `katalog2` i `katalog3` w bieżącym katalogu.

### Tworzenie katalogów w podkatalogach:

```bash
mkdir -p katalog1/podkatalog1/podkatalog2
```

Opcja `-p` (lub `--parents`) pozwala na rekurencyjne tworzenie katalogów, nawet jeśli niektóre z nich nie istnieją. W tym przypadku, zostanie utworzony katalog `katalog1`, a następnie w nim `podkatalog1`, a w nim `podkatalog2`.


## Polecenie `pwd` – Wyświetlanie bieżącego katalogu

**`pwd`** (print working directory) to proste, ale bardzo przydatne polecenie w Linuksie i innych systemach Unix-like. Służy ono do **wyświetlenia pełnej ścieżki bieżącego katalogu**.

### Podstawowe użycie:

```bash
pwd
```

To polecenie wyświetli pełną ścieżkę do katalogu, w którym aktualnie się znajdujesz.

### Przykład:

Jeśli jesteś w katalogu `/home/user/Documents`, po wpisaniu `pwd` w terminalu zostanie wyświetlona ścieżka `/home/user/Documents`.


## Polecenie `rm` – Usuwanie plików i katalogów

**`rm`** (remove) to potężne, ale niebezpieczne polecenie w Linuksie i innych systemach Unix-like. Służy do **usuwania plików i katalogów**.

### Podstawowe użycie:

```bash
rm plik.txt
```

To polecenie usunie plik `plik.txt`.

### Usuwanie wielu plików:

```bash
rm plik1.txt plik2.txt plik3.txt
```

To polecenie usunie wszystkie wymienione pliki.

### Usuwanie katalogów:

```bash
rmdir katalog
```

To polecenie usunie pusty katalog `katalog`.

### Opcja `-r` (rekurencyjne usuwanie):

```bash
rm -r katalog
```

Ta opcja pozwala na rekurencyjne usuwanie katalogu wraz ze wszystkimi jego zawartościami. **Używaj tej opcji z ostrożnością, ponieważ usunięte pliki nie mogą być odzyskane.**

### Opcja `-i` (interaktywne usuwanie):

```bash
rm -i plik.txt
```

Ta opcja powoduje, że `rm` zapyta o potwierdzenie przed usunięciem każdego pliku.

### Ważne uwagi:

* **Uważaj na opcję `-r`:** Może przypadkowo usunąć ważne dane.
* **Korzystaj z `-i` dla bezpieczeństwa:** Zawsze warto potwierdzić usunięcie plików.
* **Używaj kosza na śmieci:** W niektórych środowiskach graficznych istnieje kosz na śmieci, który pozwala na odzyskanie usuniętych plików.


## Polecenie `rmdir` – Usuwanie pustych katalogów

**`rmdir`** (remove directory) to polecenie w Linuksie i innych systemach Unix-like, służące do **usuwania pustych katalogów**.

### Podstawowe użycie:

```bash
rmdir nazwa_katalogu
```

To polecenie usunie pusty katalog o nazwie `nazwa_katalogu`.

### Przykład:

```bash
rmdir temp
```

Jeśli katalog `temp` jest pusty, to zostanie usunięty.

### Ważne uwagi:

* **Katalog musi być pusty:** `rmdir` może usunąć tylko puste katalogi.
* **Używaj z ostrożnością:** Przed usunięciem katalogu upewnij się, że jest on rzeczywiście pusty i że nie potrzebujesz jego zawartości.


## Polecenie `shell` – Uruchamianie nowej powłoki

**`shell`** to polecenie, które służy do **uruchomienia nowej powłoki**. W większości przypadków, domyślną powłoką jest Bash, więc użycie `shell` jest równoważne z wpisaniem `bash`.

### Podstawowe użycie:

```bash
shell
```

To polecenie otworzy nową instancję powłoki Bash.

### Dlaczego używać `shell`?

* **Nowe środowisko:** Otwiera nowe, czyste środowisko, niezależne od bieżącej sesji.
* **Testowanie zmian:** Możesz testować nowe konfiguracje lub skrypty bez wpływu na bieżącą sesję.
* **Izolacja procesów:** Procesy uruchomione w nowej powłoce są niezależne od procesów w bieżącej sesji.


## Polecenie `touch` – Tworzenie pustych plików

**`touch`** to proste, ale bardzo przydatne polecenie w Linuksie i innych systemach Unix-like. Służy ono do **tworzenia pustych plików** lub **aktualizowania znacznika czasu** istniejących plików.

### Podstawowe użycie:

```bash
touch nazwa_pliku
```

To polecenie utworzy nowy, pusty plik o nazwie `nazwa_pliku`. Jeśli plik o tej nazwie już istnieje, zostanie zaktualizowany jego znacznik czasu modyfikacji.

### Przykład:

```bash
touch raport.txt
```

To polecenie utworzy pusty plik tekstowy o nazwie `raport.txt`.

### Dodatkowe zastosowania:

* **Aktualizacja znacznika czasu:** Jeśli chcesz, aby system traktował plik tak, jakby został ostatnio zmodyfikowany, użyj `touch`.
* **Tworzenie wielu plików:** Możesz podać wiele nazw plików, np. `touch plik1.txt plik2.txt plik3.txt`.
* **Tworzenie struktury katalogów:** Chociaż `touch` służy głównie do tworzenia plików, można go wykorzystać do tworzenia struktury katalogów. Jeśli podasz ścieżkę do pliku, który nie istnieje, a po drodze brakuje niektórych katalogów, zostaną one automatycznie utworzone.

**Przykład tworzenia struktury katalogów:**

```bash
touch projekt/dokumenty/raport.txt
```

To polecenie utworzy katalog `projekt`, w nim katalog `dokumenty`, a następnie w nim plik `raport.txt`.