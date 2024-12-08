# Praca w systemie Git 

- Dotyczy systemu operacyjnego Linux

## 1. Konfiguracja wstępne 

### 1. Zaleca się zmiane domylśnego edytora Vim np na Nano.

- Vim może okazać się zbyt skomplikowanym edyterem do edytowania commitów.

- Zmiany możemy dokonać wpisując w terminalu następujące polecenie:

    ```zsh
    git config --global core.editor "nano"
    ```

- w miejsce nano możesz wstawić dowolny edytor tekstu.

### 2. Zaleca się zmianę domylśnego branch'a z master na main.

- Domylśna nazwa master nie jest już używana ze względu na "poprawność polityczną".

- Służy do tego komenda:

    ```zsh
    git config --global init.defaultBranch main
    ```

### 3. Tworzenie repozytorium

- Służy do tego polecenie:

    ```zsh
    git init
    ```

- Wynikiem polecenia jest utworzenie w naszym folderze następującej struktury plików w folderze .git:

    - FEATCH_HEAD - Pusty plik

    - HEAD - Zawiera branch na którym aktualnie pracujemy.

    - config - podstawowa konfiguracja

    - description - zawiera opis dot. naszego repo.

### 4. Utworzenie globalnego pliku .gitignore

- Dział on w tedy dla wszystkich projektów

- Przydatny aby ignorować pliki dot. środowiska wirtalnego python, czy pliku .DS_Store na systemie MAC_OS

- W celu utworzenia globalnego .gitignore należy:

    1. Stworzyć odpowiedni plik :

         ```zsh
        nano ~/.gitignore
        ```
        
        - W celu wypełnienia pliku możesz skożystać ze strony gitignore.io.
        
            - w polu wyszukiwania wprowadź venv i po kliknięciu "Create" skopiuj jego zawartość do ww. pliku.

    2. Skonfigurować go następującym poleceniem
    
        ```zsh
        git config --global core.excludesfile ~/.gitignore
        ```

 ## 2. Polecenia do pracy w Git
 
### 1. Polecenie pokazujące status naszej przesterzni w Git

```zsh
git status
```

Otrzymujemy następujące informaceje zawierające:
- Listę commitów,
    
- Ilość plików nieśledzonych,
    
- Dokonane zmiany.

### 2. Polecenie dodające pliki do stage's

```zsh
git add .
```

Efektem ww. komendy jest dodanie całej zawartści repozytorium do przestrzeni Stage (Index)
    
- Aby dodać wszystkie pliki ww. komendzie użyto znaku "."

- Jeżeli chcesz dodać konkretny plik to zamiast ww. znalu wpisz jego nazwę wraz z rozszerzeniem.

### 3. Commit'owanie zmian

Commit to swego rodzaju "zrobienie zzrztu ekranu" naszego repozytorium - do którego będziemy mogli wrócić w dowolnym czasie.

```zsh
git commit -m "Treść Commitu"
```
    
- Flaga `-m` (od message) powoduje to, że w obrzarze `" "` możemy bezpośrednio wpisać Tytuł naszego komita
    - Bez użycia `-m` otworzy się nasz edytor tekstu.

### 4. Historia Commit'ów
    
Jest powiązana ze struktóą plików tworzoych na podstawie odpowiednich, niemutowalnych #-szy, aby było możliwe przywrócenie ich zawartości w dowolnym czsie pracy na repozytorium. 

```zsh
git log
```

Otrzymujemy: 
    
```
commit <xxnnnnnnnnnnnnn> (HEAD -> <lokalna_gałąź>, [gałąź_zdalna])
Author: <Osoba_komitująca> <<Urządzenie z którego commit'owała>>
Date:   <Dziań.tyg. Miesiąc Dzień H:M:S Rok +0100>

[Tytuł Commitu]
```
- `xxnnnnnnnnnnnnn` # commitu prezentowany jako ciąg niepowtarzalnych znaków identyfikujący nasz commit
    
- W podkatalogu objects katalogu .git tworzy się folder `xx`, zawierający plik `nnnnnnnnnnnnn`
    
- Poza `xx` tworzą się jeszcze dwa inne katalogi powiązane z 
    - Drzewem katalogów 
        - Plik w nim mówi, którego pliku dotyczył commit.
    - Blob'em trzymającym zawartość naszego pliku.

### 5. Jeżeli w Stage są dwa pliki a chcemy skomitować tylko jeden z nich możemy unstage'ować drugi użyć następującej komendy:

```zsh
git restore --staged <plik_do_unstage'owania>
```

### 6. Jeżeli chcemy cofnąć zmiany w plikach modyfikowanych lokalnie

```zsh
git checkout .
```

- Ww. polecenie usuwa wszystkie zmmiany w working tree (nie zostały przekazane do Stage)
    
- Jeżeli zamiast `.` podamy nazwę konkretnego pliku to cofniemy zmiany tylko w nim.

### 7. Cofanie zmian do ostatniego komita (repozytorium)

```zsh
git reset --hard
```
    
- Usuwa wszystkie zmiany, które znajdowały się w przestrzeni Stage
    - Rwónież te bez odwołań w repozytorium.
    
- Usuwa **modyfikacje** na plikach, które są na repozytorium.
    - Nie zmienia plików lokalnych (w working tree), jeżeli: 
        -  Nie ma ich w repozytorium, 
            - Nie ma do czego się cofnąć.

## 2. Branch'e (gałęzie)

- Branch to wskaźnik do konkretnego commit'u
    - Za nim porusza się wskaźnik `HEAD`.

- Brnche przesuwa się wraz z commit'em 
    - Wskazuje na najmłodszy commit.

Podstawowe polecenie do operacji z branch'ami:

```zsh
git branch
```

- Wyświetli ona wszystkie utworzone gałęzie.

- `*` przed nazwą branch'a oznacza, że działamy na nim.

### 1. Dodawanie nowego branch'a

- Za poleceniem wpisz nazwę nowego branch'a:

```zsh
git branch <nazwa_branch'a>
```

- Utworzono branch <nazwa_branch'a>

- Pozostajemy na poprzednim branch'u (nie przełączyliśmy się)

### 2. Przełączanie się między branch'ami

#### 1. Istnieją do tego dwa sposoby:


- Nowszy sposób :

    ```zsh
    git switch <nazwa_branch'a>
    ```
    
- Starszy sposób to:

    ```zsh
    git checkout <nazwa_branch'a>
    ``` 

#### 2. Używając starszego sposobu, możemy jednocześnie tworzyć nowy branch z przełączenim się na niego. 

- Służy do tego flaga `-b`

    ```zsh
    git checkout -b <nazwa_branch'a>
    ```

#### 3. Poleceń  `git switch` oraz `git checkout`, można używać naprzemiennie.
- Robią one dokładnie to samo tzn.
    - Przenoszą `HEAD` aby wskazywał on na aktywny branch.
        - Aktywny branch wskazuje na swój najmłodszy commit. 

### 3. Połączenie gałęzi

#### 1. Aby połączyć ze sobą gałęzie należy:
1. Przełączyć się na starszą gałąź
2. Użyć polecenia:

    ```zsh
    git marge <branch_do_połączenia>
    ```

3. Połączenie bez konfliktu
- Zmiany wystąpiły tylko w jednej z gałęzi:
    - Fast Forward (Scalenie bez konfliktu)
    - Przesunięcie wskaźnika aktywnego branch'a,
        - Na najmłodszy commit'u branch'a <branch_do_połączenia>.

    4. Połączenie z wystąpieniem konfliktu
    - Plik był edytowany na więcej niż jednej gałęzi jednocześnie:
        - Przesunięcie wskaźnika aktywnego branch'a,
            - Na nowo utworzony commit tzw. "merge commit" 
            - który ma więcej niż jednego rodzica
                - wskazuje na commity z gałęzi, z których się wywodzi. 

### 4. Usuwanie branch'y

```zsh
git branch -d <branch_do_usunięcia>
```

## 3. Połączenie z repozytorium zdalnym (GitHub)\

1. [Stwórz klucz uwiwrzytelniania](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

2. [Utwórz repozytorium na GitHub](https://github.com/new)

3. W opcji Quick setup wybierz SSH 
    - Skopiuj polecenia zależnie od tego czy:
        - Zamierzasz je utworzyć, 
        - Masz istniejące repo. 

## 4. Pracac z GitHub (Repozytorium zdalnym)

1. Aby zaciągnąć repozytorium zdalne należy użyć polecenia:

```zsh
git clone <adress> <nazwa_folderu_z_repo>
```

W przypadku braku <nazwa_folderu_z_repo> 
- Zostanie utworzony folder o takiej samej nazwie co repozytorium.

2. Aby wypchnąć zmiany 

```zsh
git push
```

3. Aby pobrać zmiany ze zadlnego repozytorium

```zsh
git pull
```

## 5. Pull Request (PR) i przegląd kodu

### 1. Pull Request 