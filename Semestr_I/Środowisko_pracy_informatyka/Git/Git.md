# Praca w systemie Git 

- Dotyczy systemu operacyjnego Linux


## 1. Konfiguracja wstępne 

### 1. Zaleca się zmiane domylśnego edytora np na Nano.

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
    git init            #inicjalizacja
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

#### 1. Commit można utossamiać z "zrobienie zzrztu pamięci" naszego repozytorium 

- Dzięki temu będziemy mogli do niego wrócić w dowolnym czasie.

```zsh
git commit -m "Treść Commitu"
```
    
- Flaga `-m` (od message) powoduje to, że w obrzarze `" "` możemy bezpośrednio wpisać Tytuł naszego komita
    - Bez użycia `-m` otworzy się nasz edytor tekstu.

#### 2. Flaga `--allow-empty` pozwala nam na utworzenie commitu, bez zmian na repozytorium.  

```zsh
git commit --allow-empty -m "Twoja wiadomość commit"
```

#### 3. Flaga --amend (poprawka) pozwala na poprawę commit'a

```zsh
git commit --amend --no-edit
```

- Jej efektem jest tak naprawdę podmiana commit'u
    - Usunięcie commit'a oraz
    z  
    - Utworzenie nowego w jego miejsce.

- Pozwala ona zmienić 
    - Wiadomość tego commit'a 
    
    - Pliki wewnątrz tego commit'u
    
    - Do edycji bez zmiany wiadomości służy flaga `--no-edit`

### 4. Historia Commit'ów
    
#### 1. Jest powiązana ze struktóą plików tworzoych na podstawie
- odpowiednich, niemutowalnych #-szy.
- możliwe jest więc odtworzenie ich zawartości w dowolnym czsie.

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

#### 2. Za pomocą polecenia `git rebase` można edytować historię commit'ów

Jest to pomocne kiedy chcemy przebudować naszą gałąź roboczą przed dodaniem jej do `main`
- Załużmy, że na `main'e` pojawiły się ziany wprowadzone przez innych developerów.

- Celem przebudowy użyjemy komendy :

```zsh
git rebase main                     # podanie main to przebudowa gałęzi na której pracujemy do gałęci main
```

- Aktywny zostanie tryb rebase'owania.
    - W terminal pojawi się opis rebase-i

- W między czasie będziemy musieli rozwiązać konflikty z poszczegulnymi commit'ami
    - Po usunięciu bierzącego konfliktu należy:
        - `git add .` - aby dodać poprawki kodu oraz

        - `git rebase --continue` - aby przejść do następnego commit'a
    
    - Na koniec powinniśmu w terminalu otrzymaĆ komunikat: `Successfuly rebased and updated ...`.

- Nie jest to zalecane jeżeli na tej gałęzi nie pracujemy sami.

- Jej wynikiem jest utworzenie nowych commitów, gdzie najstarszy z nich zrówna się z najstarszym commitem gałęzi `main`


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

### 7. Cofanie zmian na repozytorium

```zsh
git reset
```

Tabela falg dla powyższego polecenia.

| **Flaga**            | **Co zmienia?**                        | **Index (Staging Area)** | **Working Directory (Tree)**  | **Opis**                                                                                                                               |
|----------------------|----------------------------------------|--------------------------|----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| **`--soft`**         | Resetuje tylko HEAD                    |  Zachowany               | Zachowany                                          | Przesuwa HEAD do wskazanego commita, ale zachowuje zmiany w obszarze staging i katalogu roboczym.                 |
| **`--mixed`** (domyślna) | Resetuje HEAD i index              |  Wyczyszczony            | Zachowany                                          | Przesuwa HEAD do wskazanego commita, usuwa zmiany z obszaru staging, ale zachowuje je w katalogu roboczym.        |
| **`--hard`**         | Resetuje HEAD, index i katalog roboczy | Wyczyszczony             | Wyczyszczony                                       | Przesuwa HEAD do wskazanego commita i usuwa wszystkie zmiany zarówno z obszaru staging, jak i katalogu roboczego. |
| **`--merge`**        | Resetuje HEAD i index, zachowując tylko niezapisane zmiany | Wyczyszczony| Zachowuje tylko niezapisane zmiany          | Służy do przygotowania do ponownego mergowania bez niszczenia zmian, które są w konflikcie lub niezatwierdzone.   |
| **`--keep`**         | Resetuje HEAD i index, przy brak zmian w plikach | Wyczyszczony   | Zachowany przy braku konfliktów | Zachowuje zmiany w katalogu roboczym, ale resetuje HEAD i staging, pod warunkiem, że zmiany nie spowodują konfliktów.                |

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

### 2. Przełączanie się po repozytorium w tym między branch'ami

#### 1. Istnieją do tego dwa sposoby zmiany gałęzi.

- Nowszy sposób :

    ```zsh
    git switch -c <nazwa_branch'a>
    ```
    
    - Flaga `-c` (create) tworzy nową gałąź i dopiero się na nią przełącz 

- Starszy sposób to:

    ```zsh
    git checkout -b <nazwa_branch'a>
    ``` 

    - W tym przypadku flaga `-b` (branch) służy do utworzenia nowej gałęzi przed przełączeniem

- Aby przełączać się na już utworzone gałęzie trzeba usunąć flagi '-c' lub '-b'

#### 2. W przypadku gałęzi poleceń  `git switch` oraz `git checkout`, można używać naprzemiennie
- Robią one dokładnie to samo tzn.
    - Przenoszą `HEAD` aby wskazywał on na aktywny branch,
        - Aktywny branch wskazuje na swój najmłodszy commit.

#### 3. Polecenie `git checkout` potrafi przełączać się między plikami (przenosi na nie wskaźnik HEAD)



#### 4. Aby przeżucić dane między gałęziami należy:
- W trakcie ich edytowania przełączyć się na docelowy branch.
- Ich zmiany mogą być przeniesione do obszaru Stage (Index)

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


## 3. Połączenie z repozytorium zdalnym (GitHub)

### 1. [Stwórz klucz uwiwrzytelniania](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

### 2. [Utwórz repozytorium na GitHub](https://github.com/new)

### 3. W opcji Quick setup wybierz SSH 
- Skopiuj polecenia zależnie od tego czy:
    - Zamierzasz je utworzyć, 
    - Masz istniejące repo. 


## 4. Pracac z GitHub (Repozytorium zdalnym)

### 1. Aby zaciągnąć repozytorium zdalne należy użyć polecenia:

```zsh
git clone <adress> <nazwa_folderu_z_repo>
```

W przypadku braku <nazwa_folderu_z_repo> 
- Zostanie utworzony folder o takiej samej nazwie co repozytorium.

### 2. Aby wypchnąć zmiany 

```zsh
git push
```

### 3. Aby pobrać zmiany ze zadlnego repozytorium

```zsh
git pull
```

### 4. Dodawanie branch'a (gałęzi) na repozytorium zdalne

```zsh
git push --set-upstream origin <nazwa_repozytorium>
```

### 5. Nasze nowe gałęzie mogą być automatycznie dodawane zdalnego repozytorium.

Służy do tego następujące polecenie:

```zsh
git config --global push.autoSetupRemote true
```


## 5. Praca na repozytorium zdalnym

### 1. `Pull Request`

Jest to sposób dołączania branch'y do innych branch'y

#### 1. Aby to zrobić należy

1. Na Otowrzyć repozytorium na stronie GitHub.

2. Przejść do zakładki `Pull request` 

- Porównanie zmian :
    - `base:` <branch_do_którego_dołączamy>
    - `corpare:` <branch_do_z'merge'owania>

3. Kroki 1. i 2 można poinąć: 
    - klikając w link wyświetlany w terminalu
        - Pojawi się on tem po użyciu komendy `git push` w nowej gałęzi.
        - Należy się jednak upewnić, że parametry `base` oraz `corpare` są prawidłowe.

4. Tworzenie `New pull request`

- Wybieramy nasze branch'e `base` oraz `corpare`
    - Poniżej w `Showing` zostaną wyświetlone różniece między wybranymi branch'ami

- Następnie wybierz `Create pull request`
    - Wprowadź krótki tytuł 
    
    - W opisie podaj :
        - Co się zmieniło?
        
        - Jak przetestować te zmiany?
        
        - Informacje o branch'u
            - Czego brakuje?
            
            - Z jakim branch'em lub zadaniem jest on powiązany itp.
    
    - Po ww. czynnościach naciśnij
        - `Create pull request`

- Nasze zapytanie zostało utworzone.

### 2. Ocena zmian w kodzie.

1. Wewnątrz zakładki `Pull request` wewnątrz naszego repo na stronie Github.

- W prawym górnym rogu (pod `<>Code v`) mamy informacje ile lini kodu się zmieniło

- Po zapoznaniu się z treścią zapytania.
    - Należy przejść do `Flies Chenges` 
    
    - Wyświetlą się wtedy wszystkie zmiany między porównywanymi gałęziami.
    
    - Podczas przeglądania kodu możemy za pomocą znaków `+` przy numerach wierszy
        - Dodawać wskazówki, uwagi co do proponowanego kodu.
        
        - Dobrą praktyką jest sugierowanie rozwiązań a nie je nażucacanie.

- Po zapoznaniu się z kodem możemy użyj `Finish your review`
    - Dodać komentaż na temat kodu
    
    - Zaakceptować zmiany 
        - jeżeli jesteśmy pewni, że przed zmerge'owaniem wszystko zostanie poprawione.
    
    - Poprosić o zmiany (odrzucić pull request).

2. Po tym jak zmiany zostaną rozpatrzone pozytywnie 
    
    - Można na wykonać krok `Merge pull request`
    
    -  Znajduje się on na począdku pull request'a
        - Na dole strony.
        
3. Jeżeli wystąpią konflikty trzeba je rozwiązać
    - GitHub zablokuje możliwość użycia opcji `Merge pull request`
        - Po naprwieniu konfliktu kliknij `Mark as resoulved`
    
    - Z poziomu GitHub opcja `Resolve conflicts`
    
    - Z poziomu gałęzi lokalnych
    
        ```zsh
        git merge main
        ```

4. Po tym kroku należy zawsze pobrać zmiany na lokalne repozytorium.
    
    - W tym celu skożystaj z polecenia `git pull`. 


## 6. `stash` (schowek )

### 1. Działą na zasadzie stosu (LIFO) 

- Możemy dodawać do niego nieskończoną ilość zmian

- Zmiany te im są starsze tym wyższy mają index 
    - Najmłodsza zawesze ma index `0`

### 2. Aby przenieść dane do stash

```zsh
git stash
```
- Brak barametru oznacza przeniesienie do schowka 
    - plików z working directory (tree)
    - plików z stage (index)

#### 1. Parametr `list` informacje o tym jakie zmiany znajdują się w stash'u 

```zsh
git stash list
```

#### 2. Prametr służące do przywracania danych.

- `apply` - nie usuwa zmian ze stach'a

- `pop` - usuwa zmiany z przestrzeni stash

```zsh
git stash apply             # przywróć i zostaw zmiany

git stash pop               # przywróć i skasuj zmiany
```

W celu wyjęcie ze stasha starszych zmian należy po ww. komendach podać stash{n}
- n to numer index'u starszej zmiany.

```zsh
git stash apply stash{n}    # przywróć zmiany z pod n-tego index'su.
```

#### 3. Parametr `save` służy do zapisania danych w stachu z własną wiadomością.

```zsh
git stash save "Wiadomość"
``` 

#### 4. Parametr `drop` służy do usuwania zmian ze stash'a
- Tak jak poprzednio można usuwać zmiany o konkretnym n-tym index'ie.

```zsh
git stash drop stash{n}
```