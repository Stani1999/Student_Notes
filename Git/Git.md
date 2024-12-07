# Praca w systemie Git

## 1. Konfiguracja wstępne 

### 1. Zaleca się zmiane domylśnego edytora Vim np na Nano.

- Vim może okazać się zbyt skomplikowanym edyterem do edytowania commitów.
- Zmiany możemy dokonać wpisując w terminalu następujące polecenie:

    ```zsh
    git config --global core.editor "nano"
    ```
- w miejsce nano możesz wstawić dowolny edytor tekstu.

### 2. Zaleca się zmianę domylśnego brancha z master na main.

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

 ## 2. Polecenia do pracy w Git.
 
 Polecenie pokazujące status naszej przesterzni w Git

 ```zsh
 git status
 ```

Otrzymujemy następujące informaceje zawierające:
 - Listę commitów,
 - Ilość plików nieśledzonych,
 - Dokonane zmiany.