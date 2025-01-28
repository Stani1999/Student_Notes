# Opcje i parametry poleceń w systemie Linux oraz ich zastosowania:

## 1. `alias`

| Komenda `alias`             | Zastosowanie                                                                             |
|-----------------------------|------------------------------------------------------------------------------------------|
| `alias`                     | Wyświetla listę wszystkich zdefiniowanych aliasów w bieżącej sesji.                      |
| `alias name='command'`      | Tworzy nowy alias o nazwie `name`, który uruchamia określone polecenie `command`.        |
| `alias name="command --opt"`| Tworzy alias z dodatkowymi opcjami w cudzysłowie (przydatne dla wielowyrazowych komend). |
| `unalias name`              | Usuwa alias o nazwie `name`.                                                             |
| `unalias -a`                | Usuwa wszystkie zdefiniowane aliasy w bieżącej sesji.                                    |

### Przykłady zastosowań `alias`:

| Alias                        | Działanie                                                                                   |
|------------------------------|---------------------------------------------------------------------------------------------|
| `alias ll='ls -lh'`          | Tworzy alias `ll`, który pokazuje listę plików z czytelnym formatem rozmiaru i szczegółami. |
| `alias la='ls -lha'`         | Tworzy alias `la` do wyświetlania wszystkich plików (w tym ukrytych) w szczegółowej liście. |
| `alias rm='rm -i'`           | Zmienia polecenie `rm` tak, aby zawsze pytało o potwierdzenie przed usunięciem pliku.       |
| `alias cp='cp -i'`           | Sprawia, że polecenie `cp` zawsze wymaga potwierdzenia przy nadpisywaniu plików.            |
| `alias mv='mv -i'`           | Sprawia, że polecenie `mv` wymaga potwierdzenia przy nadpisywaniu plików.                   |
| `alias grep='grep --color=auto'` | Dodaje kolory do wyników polecenia `grep` dla lepszej czytelności.                      |
| `alias cls='clear'`          | Tworzy alias `cls` jako alternatywę do polecenia `clear`.                                   |
| `alias ..='cd ..'`           | Tworzy alias `..` do szybkiego przejścia do katalogu nadrzędnego.                           |
| `alias update='sudo apt update && sudo apt upgrade'` | Tworzy alias do aktualizowania systemu (np. w Ubuntu).              |
| `alias gs='git status'`      | Skraca polecenie `git status` do `gs`.                                                      |

### Przykłady w praktyce:

1. **Tworzenie aliasu:**
   ```bash
   alias myls='ls -lh --color=auto'
   ```
   Teraz użycie `myls` wywoła polecenie `ls -lh --color=auto`.

2. **Usunięcie aliasu:**
   ```bash
   unalias myls
   ```
   Alias `myls` zostanie usunięty.

3. **Wyświetlenie wszystkich aliasów:**
   ```bash
   alias
   ```

4. **Trwałe zapisywanie aliasów:**
   Alias zdefiniowany w terminalu działa tylko w bieżącej sesji. Aby działał zawsze, należy go dodać do pliku konfiguracyjnego, np. `.bashrc` lub `.zshrc`:
   ```bash
   echo "alias ll='ls -lh'" >> ~/.bashrc
   source ~/.bashrc
   ```

### Przydatne aliasy do codziennej pracy:
- `alias h='history'` – Wyświetla historię poleceń.
- `alias free='free -m'` – Wyświetla użycie pamięci w MB.
- `alias ports='netstat -tulanp'` – Szybkie sprawdzanie otwartych portów.
- `alias please='sudo'` – Dla humorystycznego zamiennika `sudo`.

## 10. `du`

| Parametr `du`             | Zastosowanie                                                                                                                |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| `du`                | Wyświetla rozmiar katalogu i jego podkatalogów w domyślnych blokach (zwykle 1 KB).                                                |
| `-h`                | Wyświetla rozmiary w czytelnej formie (np. KB, MB, GB).                                                                           |
| `-k`                | Wyświetla rozmiary w kilobajtach (1 KB = 1024 bajtów).                                                                            |
| `-m`                | Wyświetla rozmiary w megabajtach.                                                                                                 |
| `-g`                | Wyświetla rozmiary w gigabajtach.                                                                                                 |
| `-c`                | Dodaje podsumowanie całkowitego rozmiaru na końcu.                                                                                |
| `-s`                | Wyświetla tylko całkowity rozmiar katalogu, bez szczegółów o podkatalogach.                                                       |
| `-a`                | Wyświetla rozmiary dla wszystkich plików, nie tylko katalogów.                                                                    |
| `-d N`              | Określa poziom głębokości, do którego `du` ma podawać rozmiary (np. `-d 1` – bieżący katalog i podkatalogi najwyższego poziomu).  |
| `--max-depth=N`     | To samo co `-d N`.                                                                                                                |
| `-L`                | Śledzi dowiązania symboliczne (domyślnie `du` ich nie podąża).                                                                    |
| `-x`                | Ogranicza analizę tylko do tego samego systemu plików (np. bez rozmiarów zamontowanych dysków).                                   |
| `--exclude=PATTERN` | Wyklucza pliki lub katalogi pasujące do wzorca (np. `--exclude=*.log`).                                                           |
| `--time`            | Wyświetla datę ostatniej modyfikacji każdego pliku lub katalogu.                                                                  |
| `--apparent-size`   | Wyświetla "pozorny" rozmiar pliku (ile danych zajmuje logicznie, a nie fizycznie na dysku).                                       |
| `--help`            | Wyświetla pomoc dotyczącą `du`.                                                                                                   |

### Przykłady zastosowań `du`:

| Komenda                      | Działanie                                                                                |
|------------------------------|------------------------------------------------------------------------------------------|
| `du -h`                      | Wyświetla rozmiary katalogów i plików w formacie czytelnym dla użytkownika (np. MB, GB). |
| `du -sh /var/log`            | Pokazuje całkowity rozmiar katalogu `/var/log` w formacie czytelnym.                     |
| `du -ah`                     | Wyświetla rozmiary wszystkich plików i katalogów w formacie czytelnym.                   |
| `du -d 1 -h`                 | Wyświetla rozmiary tylko dla katalogu bieżącego i jego bezpośrednich podkatalogów.       |
| `du -h --max-depth=2`        | Wyświetla rozmiary katalogów do głębokości 2 poziomów.                                   |
| `du -sh *`                   | Wyświetla podsumowanie rozmiaru dla każdego elementu w bieżącym katalogu.                |
| `du -ch`                     | Wyświetla rozmiary wszystkich elementów i podsumowuje całkowity rozmiar.                 |
| `du -h --exclude="*.log"`    | Wyświetla rozmiary katalogów i plików, pomijając pliki `.log`.                           |
| `du -sh /home/*`             | Pokazuje rozmiary katalogów użytkowników w `/home`.                                      |

### Przykłady w praktyce:

1. **Całkowity rozmiar katalogu w GB:**
   ```bash
   du -sh /var/log
   ```

2. **Rozmiary katalogów na pierwszym poziomie w formacie czytelnym:**
   ```bash
   du -h --max-depth=1
   ```

3. **Rozmiary plików i katalogów z wykluczeniem plików tymczasowych (`*.tmp`):**
   ```bash
   du -h --exclude="*.tmp"
   ```

4. **Pokazanie "pozornego" rozmiaru plików, ile danych logicznie zajmują:**
   ```bash
   du --apparent-size -h
   ```

5. **Podsumowanie rozmiaru wszystkich plików w katalogu:**
   ```bash
   du -sh *
   ```

6. **Znajdź największe katalogi w bieżącej lokalizacji:**
   ```bash
   du -h --max-depth=1 | sort -hr | head -10
   ```

### Przydatne wskazówki:
- `du -sh` jest jednym z najczęściej używanych, ponieważ daje szybki podgląd całkowitego rozmiaru katalogu.
- Kombinacja `du`, `sort` i `head` jest świetna do wyszukiwania dużych katalogów na dysku.

## 15. `find` 

| Parametr `find`           | Zastosowanie                                                                        |
|---------------------------|-------------------------------------------------------------------------------------|
| `-a` (domyślnie)          | Logiczne "I" (np. `-name "*.txt" -a -size +10k`).                                   |
| `.`                       | Określa bieżący katalog jako punkt startowy do wyszukiwania.                        |
| `/path/to/dir`            | Wskazuje katalog, w którym ma rozpocząć się wyszukiwanie.                           |
| `-name "pattern"`         | Wyszukuje pliki i katalogi według nazwy (wzorzec z uwzględnieniem wielkości liter). |
| `-iname "pattern"`        | Wyszukuje pliki i katalogi według nazwy (ignorując wielkość liter).                 |
| `-type f`                 | Wyszukuje tylko pliki.                                                              |
| `-type d`                 | Wyszukuje tylko katalogi.                                                           |
| `-size +N`                | Wyszukuje pliki większe niż N (np. `-size +10M` – większe niż 10 MB).               |
| `-size -N`                | Wyszukuje pliki mniejsze niż N (np. `-size -5k` – mniejsze niż 5 KB).               |
| `-mtime +N`               | Wyszukuje pliki modyfikowane więcej niż N dni temu.                                 |
| `-mtime -N`               | Wyszukuje pliki modyfikowane mniej niż N dni temu.                                  |
| `-atime +N`               | Wyszukuje pliki otwierane więcej niż N dni temu.                                    |
| `-atime -N`               | Wyszukuje pliki otwierane mniej niż N dni temu.                                     |
| `-ctime +N`               | Wyszukuje pliki, których metadane zmieniano więcej niż N dni temu.                  |
| `-ctime -N`               | Wyszukuje pliki, których metadane zmieniano mniej niż N dni temu.                   |
| `-perm mode`              | Wyszukuje pliki o określonych uprawnieniach (np. `-perm 644`).                      |
| `-user username`          | Wyszukuje pliki należące do konkretnego użytkownika.                                |
| `-group groupname`        | Wyszukuje pliki należące do konkretnej grupy.                                       |
| `-exec command {} \;`     | Wykonuje podane polecenie na każdym znalezionym pliku (np. `-exec rm {} \;`).       |
| `-delete`                 | Usuwa znalezione pliki (należy zachować ostrożność!).                               |
| `-empty`                  | Wyszukuje puste pliki lub katalogi.                                                 |
| `-maxdepth N`             | Ogranicza głębokość przeszukiwania do N poziomów.                                   |
| `-mindepth N`             | Pomija katalogi na poziomach głębokości mniejszych niż N.                           |
| `-newer file`             | Wyszukuje pliki nowsze niż podany plik.                                             |
| `-not` lub `!`            | Neguje warunek (np. `-not -name "*.txt"` – wszystko poza plikami `.txt`).           |
| `-o`                      | Logiczne "LUB" (np. `-name "*.txt" -o -name "*.log"`).                              |

### Przykłady:
1. Znajdź wszystkie pliki `.txt` w bieżącym katalogu:
   ```bash
   find . -name "*.txt"
   ```
2. Znajdź pliki większe niż 100 MB w `/var/log`:
   ```bash
   find /var/log -type f -size +100M
   ```
3. Usuń puste katalogi w `/tmp`:
   ```bash
   find /tmp -type d -empty -delete
   ```
4. Wykonaj `ls -l` na wszystkich plikach `.log`:
   ```bash
   find . -name "*.log" -exec ls -l {} \;
   ``` 
## 17. `grep`

---

### **Tabela opcji `grep`**

| Parametr `grep`      | Zastosowanie                                                                                      |
|----------------------|---------------------------------------------------------------------------------------------------|
| `-i`                 | Ignoruje wielkość liter podczas wyszukiwania.                                                     |
| `-v`                 | Wyszukuje linie **niepasujące** do wzorca.                                                        |
| `-c`                 | Zlicza liczbę linii pasujących do wzorca.                                                         |
| `-l`                 | Wyświetla **tylko** nazwy plików, w których znaleziono dopasowania.                               |
| `-L`                 | Wyświetla **tylko** nazwy plików, które **nie** zawierają dopasowań.                              |
| `-n`                 | Wyświetla numer linii w pliku, w której znaleziono dopasowanie.                                   |
| `-o`                 | Wyświetla **tylko** dopasowane fragmenty tekstu zamiast całych linii.                             |
| `-r` lub `-R`        | Przeszukuje katalogi rekursywnie.                                                                 |
| `-w`                 | Dopasowuje całe słowa (nie części wyrazów).                                                       |
| `-x`                 | Dopasowuje tylko całe linie (nie części linii).                                                   |
| `-A N`               | Wyświetla **N** linii po dopasowaniu (after).                                                     |
| `-B N`               | Wyświetla **N** linii przed dopasowaniem (before).                                                |
| `-C N`               | Wyświetla **N** linii przed i po dopasowaniu (context).                                           |
| `--color=auto`       | Podświetla znalezione wzorce w wynikach.                                                          |
| `-E`                 | Umożliwia używanie wyrażeń regularnych (równoważne `egrep`).                                      |
| `-F`                 | Szuka dosłownego ciągu znaków (bez interpretacji znaków specjalnych).                             |
| `-P`                 | Umożliwia używanie pełnych wyrażeń regularnych Perl (Perl-Compatible Regular Expressions – PCRE). |

---

### **Przykłady zastosowań `grep`**

| Komenda | Działanie |
|-----------------------------------------------------------|-----------------------------------------------------------------------------|
| `grep "error" logfile.log`                                | Wyszukuje linie zawierające słowo "error" w pliku `logfile.log`.            |
| `grep -i "error" logfile.log`                             | Wyszukuje "error", ignorując wielkość liter (np. "Error", "ERROR").         |
| `grep -v "info" logfile.log`                              | Wyświetla linie, które **nie** zawierają "info".                            |
| `grep -c "warning" logfile.log`                           | Zlicza liczbę linii zawierających "warning".                                |
| `grep -l "TODO" *.txt`                                    | Wyświetla nazwy plików `.txt`, w których znaleziono "TODO".                 |
| `grep -n "failed" logfile.log`                            | Wyświetla linie zawierające "failed" z numerami linii.                      |
| `grep -o "[0-9]\{3\}-[0-9]\{3\}-[0-9]\{4\}" contacts.txt` | Wyszukuje i wyświetla tylko numery telefonów w formacie `XXX-XXX-XXXX`.     |
| `grep -r "function" /home/user/projects`                  | Rekursywnie przeszukuje katalog `/home/user/projects` pod kątem "function". |
| `grep -w "root" /etc/passwd`                              | Szuka całego słowa "root" (np. **nie** dopasuje "rooted").                  |
| `grep -x "Hello World" file.txt`                          | Szuka dokładnej linii "Hello World" w pliku.                                |
| `grep -A 3 "ERROR" logfile.log`                           | Wyświetla 3 linie **po** znalezieniu "ERROR".                               |
| `grep -B 2 "FAIL" logfile.log`                            | Wyświetla 2 linie **przed** znalezieniem "FAIL".                            |
| `grep -C 2 "CRITICAL" logfile.log`                        | Wyświetla 2 linie przed i po znalezieniu "CRITICAL".                        |
| `grep --color=auto "error" logfile.log`                   | Podświetla pasujące słowa "error" w wynikach.                               |
| `grep -E "error|fail|critical" logfile.log`               | Szuka wielu słów jednocześnie (`egrep` odpowiednik).                        |
| `grep -F "C:\Program Files" config.txt`                   | Szuka dosłownego ciągu znaków (bez interpretacji `\`).                      |

---

### **Zaawansowane przykłady**

#### **1. Znalezienie wszystkich plików zawierających dany tekst w katalogu:**
```bash
grep -rl "search_term" /path/to/directory
```
🔹 `-r` – przeszukiwanie rekursywne  
🔹 `-l` – wypisanie tylko nazw plików  

---

#### **2. Szukanie wszystkich adresów IP w pliku:**
```bash
grep -Eo "[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+" logfile.log
```
🔹 `-E` – używa rozszerzonych wyrażeń regularnych  
🔹 `-o` – wyświetla tylko dopasowane adresy  

---

#### **3. Znalezienie największych plików i katalogów na serwerze i odfiltrowanie niepotrzebnych wyników:**
```bash
du -ah /var/log | grep -v "0$"
```
🔹 `du -ah` – pokazuje rozmiary plików  
🔹 `grep -v "0$"` – odfiltrowuje linie kończące się na "0"  

---

#### **4. Wyszukanie otwartych portów w `netstat` i podświetlenie wyniku:**
```bash
netstat -tuln | grep --color "LISTEN"
```
🔹 `LISTEN` – pokazuje aktywne porty nasłuchujące  

---

#### **5. Monitorowanie logów w czasie rzeczywistym z podświetleniem błędów:**
```bash
tail -f /var/log/syslog | grep --color -E "error|fail|critical"
```
🔹 `tail -f` – śledzi plik logów na żywo  
🔹 `grep --color -E "error|fail|critical"` – podświetla wybrane słowa  

---

## 23. `ls`

| Parametr `ls` | Zastosowanie                                                                                                       |
|---------------|--------------------------------------------------------------------------------------------------------------------|
| `-a`          | Wyświetla wszystkie pliki, w tym ukryte (zaczynające się od `.`, np. `.bashrc`).                                   |
| `-A`          | Wyświetla wszystkie pliki, oprócz `.` (bieżącego katalogu) i `..` (katalogu nadrzędnego).                          |
| `-l`          | Wyświetla szczegółowe informacje o plikach i katalogach w formacie listy (permissions, właściciel, rozmiar, data). |
| `-h`          | Wyświetla rozmiary plików w czytelnej formie (np. KB, MB, GB) w połączeniu z `-l`.                                 |
| `-R`          | Rekurencyjnie wyświetla zawartość katalogów i podkatalogów.                                                        |
| `-t`          | Sortuje pliki według daty modyfikacji (najnowsze jako pierwsze).                                                   |
| `-S`          | Sortuje pliki według rozmiaru (największe jako pierwsze).                                                          |
| `-r`          | Odwraca kolejność sortowania (np. z rosnącej na malejącą).                                                         |
| `-d`          | Wyświetla informacje o katalogu jako pliku, zamiast jego zawartości.                                               |
| `-i`          | Wyświetla numery inode dla plików.                                                                                 |
| `-1`          | Wyświetla każdy plik w osobnym wierszu.                                                                            |
| `-m`          | Wyświetla pliki oddzielone przecinkami.                                                                            |
| `-n`          | Wyświetla UID i GID zamiast nazw użytkownika i grupy (w formacie `-l`).                                            |
| `-p`          | Dodaje `/` po nazwach katalogów w wyniku.                                                                          |
| `-F`          | Dodaje symbol określający typ pliku (np. `/` dla katalogów, `*` dla plików wykonywalnych).                         |
| `--color`     | Wyświetla pliki z kolorami określającymi typy (np. katalogi na niebiesko).                                         |
| `--full-time` | Wyświetla pełną datę i czas modyfikacji pliku (w połączeniu z `-l`).                                               |
| `--sort=TYPE` | Sortuje pliki według określonego kryterium (np. `size`, `time`, `name`).                                           |
| `-q`          | Wyświetla znaki niedrukowalne jako znak `?`.                                                                       |
| `-v`          | Sortuje pliki według wersji (np. plik2, plik10 zamiast plik10, plik2).                                             |
| `-k`          | Wyświetla rozmiary w kilobajtach (domyślnie w blokach 1024 bajty).                                                 |

### Przykłady użycia `ls`:
1. Wyświetl wszystkie pliki w katalogu, w tym ukryte:
   ```bash
   ls -a
   ```
2. Wyświetl szczegóły plików w czytelnym formacie z rozmiarem (KB, MB, GB):
   ```bash
   ls -lh
   ```
3. Wyświetl pliki posortowane według daty modyfikacji:
   ```bash
   ls -lt
   ```
4. Wyświetl katalogi rekurencyjnie (z zawartością podkatalogów):
   ```bash
   ls -R
   ```
5. Wyświetl szczegóły plików z UID i GID zamiast nazw użytkowników:
   ```bash
   ls -ln
   ```
6. Wyświetl pliki z kolorami i symbolami określającymi typ pliku:
   ```bash
   ls -F --color
   ```

## 28. `netstat`

| Parametr `netstat` | Zastosowanie                                                                                   |
|--------------------|------------------------------------------------------------------------------------------------|
| `-a`               | Wyświetla wszystkie aktywne połączenia oraz gniazda nasłuchujące.                              |
| `-t`               | Wyświetla tylko połączenia TCP.                                                                |
| `-u`               | Wyświetla tylko połączenia UDP.                                                                |
| `-l`               | Wyświetla tylko gniazda w stanie nasłuchiwania.                                                |
| `-p`               | Wyświetla identyfikator procesu (PID) oraz nazwę programu dla każdego połączenia.              |
| `-n`               | Wyświetla adresy i porty w postaci numerycznej (bez rozwiązywania DNS).                        |
| `-r`               | Wyświetla tablicę routingu (podobnie do `route`).                                              |
| `-e`               | Wyświetla dodatkowe informacje o połączeniach, takie jak liczba wysłanych/odebranych pakietów. |
| `-s`               | Wyświetla statystyki dla protokołów (TCP, UDP, ICMP itp.).                                     |
| `-c`               | Odświeża dane w czasie rzeczywistym (odświeżanie co sekundę).                                  |
| `--tcp`            | Wyświetla statystyki dotyczące TCP.                                                            |
| `--udp`            | Wyświetla statystyki dotyczące UDP.                                                            |
| `--ip`             | Wyświetla statystyki dotyczące IP.                                                             |
| `--listening`      | To samo co `-l` – pokazuje tylko gniazda nasłuchujące.                                         |
| `-o`               | Wyświetla informacje o timerach połączeń TCP.                                                  |
| `-w`               | Wyświetla informacje o gniazdach Raw (surowych).                                               |
| `-g`               | Wyświetla członkostwo w grupach multicast.                                                     |
| `--help`           | Wyświetla pomoc dotyczącą użycia `netstat`.                                                    |

---

### Przykłady zastosowań `netstat`:

| Komenda                      | Działanie                                                                |
|------------------------------|--------------------------------------------------------------------------|
| `netstat -a`                 | Wyświetla wszystkie aktywne połączenia i porty nasłuchujące.             |
| `netstat -at`                | Wyświetla wszystkie połączenia TCP.                                      |
| `netstat -au`                | Wyświetla wszystkie połączenia UDP.                                      |
| `netstat -l`                 | Wyświetla wszystkie porty w stanie nasłuchiwania.                        |
| `netstat -p`                 | Wyświetla aktywne połączenia wraz z nazwami procesów i PID-ami.          |
| `netstat -n`                 | Wyświetla połączenia w postaci numerycznej (bez nazw hostów).            |
| `netstat -r`                 | Wyświetla tablicę routingu sieciowego.                                   |
| `netstat -s`                 | Wyświetla szczegółowe statystyki protokołów sieciowych.                  |
| `netstat -tuln`              | Wyświetla porty nasłuchujące TCP i UDP w postaci numerycznej.            |
| `netstat -e`                 | Wyświetla szczegółowe statystyki o połączeniach (np. liczba bajtów).     |
| `netstat -c`                 | Odświeża informacje o połączeniach w czasie rzeczywistym.                |

---

### Przykłady w praktyce:

1. **Wyświetlenie wszystkich aktywnych połączeń:**
   ```bash
   netstat -a
   ```

2. **Wyświetlenie wszystkich połączeń TCP w postaci numerycznej:**
   ```bash
   netstat -atn
   ```

3. **Wyświetlenie wszystkich nasłuchujących portów (TCP i UDP):**
   ```bash
   netstat -tuln
   ```

4. **Wyświetlenie połączeń z PID procesów:**
   ```bash
   netstat -p
   ```

5. **Wyświetlenie tablicy routingu:**
   ```bash
   netstat -r
   ```

6. **Statystyki protokołów sieciowych:**
   ```bash
   netstat -s
   ```

7. **Wyświetlenie gniazd nasłuchujących tylko na porcie UDP:**
   ```bash
   netstat -ul
   ```

---

### Przydatna uwaga:
`netstat` jest częścią pakietu **net-tools**, który w wielu współczesnych dystrybucjach Linuksa został zastąpiony przez narzędzia takie jak `ss` (socket statistics). Na przykład:

- Zamiast `netstat -tuln` można użyć:
  ```bash
  ss -tuln
  ```

  Oto tabela przedstawiająca różne zastosowania polecenia `useradd` w systemie Linux oraz jego najczęściej używane opcje:

---

### **Tabela opcji `useradd`**

| **Parametr `useradd`** | **Zastosowanie**                                                                                 |
|------------------------|--------------------------------------------------------------------------------------------------|
| `-m`                   | Tworzy katalog domowy użytkownika w `/home/nazwa_uzytkownika`.                                   |
| `-M`                   | Tworzy konto użytkownika bez tworzenia katalogu domowego (przydatne np. dla kont systemowych).   |
| `-d /ścieżka`          | Ustawia niestandardowy katalog domowy (np. `/opt/users/użytkownik`).                             |
| `-c "Opis"`            | Dodaje komentarz/pełną nazwę użytkownika (np. `-c "Jan Kowalski"`).                              |
| `-g grupa`             | Określa grupę podstawową użytkownika (np. `-g developers`).                                      |
| `-G grupa1,grupa2`     | Dodaje użytkownika do dodatkowych grup (np. `-G sudo,docker`).                                   |
| `-s /ścieżka`          | Ustawia domyślną powłokę użytkownika (np. `-s /bin/bash`).                                       |
| `-u UID`               | Określa niestandardowy numer UID użytkownika.                                                    |
| `-e YYYY-MM-DD`        | Ustawia datę wygaśnięcia konta (np. `-e 2025-12-31`).                                            |
| `-f dni`               | Ustawia liczbę dni po wygaśnięciu hasła, po której konto zostanie zablokowane (np. `-f 30`).     |
| `-p hasło`             | Ustawia zaszyfrowane hasło użytkownika (zazwyczaj lepiej użyć `passwd` po utworzeniu konta).     |
| `-r`                   | Tworzy konto systemowe (bez katalogu domowego, często dla usług).                                |
| `-k`                   | Kopiuje domyślne pliki konfiguracyjne do katalogu domowego użytkownika.                          |
| `--help`               | Wyświetla pomoc dotyczącą `useradd`.                                                             |
| `-L`                   | Zablokowuje konto użytkownika, czyniąc je niedostępnym do logowania.                             |

---

### **Przykłady zastosowań `useradd`**

| Komenda                               | Działanie                                                            |
|---------------------------------------|----------------------------------------------------------------------|
| `useradd nowyuser`                    | Tworzy użytkownika `nowyuser` bez katalogu domowego.                 |
| `useradd -m jan`                      | Tworzy użytkownika `jan` z katalogiem domowym `/home/jan`.           |
| `useradd -m -s /bin/bash -G sudo jan` | Tworzy użytkownika `jan` z powłoką Bash i dodaje go do grupy `sudo`. |
| `useradd -m -c "Jan Kowalski" jan`    | Tworzy użytkownika `jan` z pełnym opisem "Jan Kowalski".             |
| `useradd -m -d /opt/users/jan jan`    | Tworzy użytkownika `jan` z katalogiem domowym `/opt/users/jan`.      |
| `useradd -u 1500 jan`                 | Tworzy użytkownika `jan` z numerem UID `1500`.                       |
| `useradd -e 2025-12-31 jan`           | Tworzy użytkownika `jan` z kontem wygasającym 31 grudnia 2025 r.     |
| `useradd -G developers,docker jan`    | Dodaje użytkownika `jan` do grup `developers` i `docker`.            |
| `useradd -r systemuser`               | Tworzy konto systemowe `systemuser` bez katalogu domowego.           |

---

### **Ustawianie hasła dla nowego użytkownika**
Po utworzeniu konta użytkownika należy ustawić hasło:
```bash
passwd jan
```
System poprosi o podanie i potwierdzenie hasła.

---

### **Sprawdzenie dodanego użytkownika**
Po dodaniu użytkownika można sprawdzić jego dane:
```bash
id jan
```
Wyświetli UID, GID i grupy użytkownika.

Sprawdzenie katalogu domowego:
```bash
ls -ld /home/jan
```

Sprawdzenie konfiguracji użytkownika w `/etc/passwd`:
```bash
grep jan /etc/passwd
```

---

### **Usuwanie użytkownika**
Aby usunąć użytkownika (bez katalogu domowego):
```bash
userdel jan
```
Aby usunąć użytkownika i jego katalog domowy:
```bash
userdel -r jan
```

---