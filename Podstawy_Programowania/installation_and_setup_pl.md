# Instalacja Python
Aby uruchomić poniższy kod python musisz najpierw zainstalować python.
Możesz to zrobić w następujący sposób:

### Windows
1. Pobierz instalator z linku klikając jego ikonę poniżej.
   <div style="text-align: left;">
      <img src="python.png" alt="Python" />
   </div>
2. Uruchom instalator i upewnij się, że zaznaczyłeś opcję "Add Python to PATH".
3. Kliknij "Install Now".

### Linux (Debian/Bash)
Wykkonaj poniższe instrukcje w terminalu:


```bash
sudo apt update
sudo apt install python3
```

# Tworzenie środowiska wirtualnego
Zaleca się korzystanie ze środowisk wirtualnych, aby odizolować zależności projektu od globalnych pakietów Pythona.

## Tworzenie i aktywowanie środowiska wirtualnego

**Windows**
1. Utwórz środowisko wirtualne:
        ```bash
        python -m venv <nazwa_katalogu>
        ```
2. Aktywuj środowisko:
        ```bash
        <nazwa_katalogu>\Scripts\activate
        ```

**Linux/macOS**
1. Utwórz środowisko wirtualne:
        ```bash
        python3 -m venv <nazwa_katalogu>
        ```
2. Aktywuj środowisko:
        ```bash
        source <nazwa_katalogu>/bin/activate
        ```

3. Po aktywacji środowiska wirtualnego możesz instalować zależności, np. za pomocą `pip`, które będą izolowane w obrębie tego środowiska.