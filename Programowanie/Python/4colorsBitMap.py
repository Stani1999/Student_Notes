## Zaimplementowane moduły 

import os # Import modułu os do funkcji czyszczenia zawartości w terminalu
import matplotlib.pyplot as plt
import numpy as np


## Zmienne

# Pobieranie nazwy programu (pliku)
program_name = os.path.basename(__file__) 

# Deklaracja domylśnych kolorów
colors_set = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 255)]

# Deklaracja rozszerzeń plików w zależności od formatu
PBIN = ".bm2" # Rozszerzenie pliku binarnego
P16X = ".bm16" # Rozszerzenie pliku szesnastkowego


## Opis programu

program_description = f"""
Informacje dotyczące programu {program_name}. 
\nPrznaczenie programu:
Kodowanie i dekodowanie mapy bitowe w postaci binarnej lub szesnastkowej.
\nProgram obsługuje obrazy:
                          - o wymiarach od 1x1 piksel do 256x256 pikseli
                          - z maksymalnie 4 kolorami jednocześnie.
                          - kolory można dostosować lub używać domyślnych.
                          - domyślne kolory to: czerwony, zielony, niebieski i biały.
                          - dane pikseli można wprowadzać symbolicznie (1-4), binarnie lub szesnastkowo.
                          - na plikach o własnych formatach: .bm2 (dla kodowania binarnego), .bm16 (dla kodowania szesnastkowego).
Sposób kodowania:
                          - I  bajt zawiera informację o szerokości obrazy
                          - II bajt zawiera informację o wysokości obrazy
                             - np. dla formatu 16-stkowego obraz 1x1 pikseli kodowany jest jako 0000 a 256x256 pikseli jako FFFF
                          - bajty od III  do V    kodują 1 kolor
                          - bajty od VI   do VIII kodują 2 kolor
                          - bajty od IX   do XI   kodują 3 kolor
                          - bajty od XII  do XIV  kodują 4 kolor
                             - wynika to z formatu RGB zajmującego 3 bajty na kolor
                          - pozostałe bajty przeznaczone są na kodowanie ww. kolorów, kolejno jako 00, 01, 10, 11 - w systemie binarnym.
                          - bajty przekraczające zakres wyznaczany przez dwa pierwsze bajty są ignorowane
                          - w przepadku braku wystarczającej ilości bitów program dopisuje wartości "0".
                          - piksele są kolejkowane według zasad „kolejności leksykograficznej” - z lewej do prawej strony.
Sposób dokodowania :
                          - daizła analogicznie do zasad kodowania, jednak z jednym wyjątkiem
                            - program nie dopisuje "0" jeżeli ciąg jest zbyt krótki, potrafi jedynie ucinać zbyt długie ciągi danych. 
Instrukcja obsługi:
                          1. Wybierz jedną z opcji z menu.
                          2. Postępuj zgodnie z instrukcjami wyświetlanymi na ekranie.
                          3. Wprowadź dane zgodnie z poleceniami.
                          4. Wyniki zostaną wyświetlone na ekranie lub zapisane do pliku.
"""


## Funkcje wizualne

import numpy as np
import matplotlib.pyplot as plt

def visualize_image(pixel_matrix: list[list[int]], colors: list[tuple[int, int, int]]) -> None:
    """
    Wizualizuje obraz na podstawie macierzy pikseli i przypisanych kolorów.

    Args:
        pixel_matrix (List[List[int]]): Dwuwymiarowa lista pikseli.
            Każdy element to indeks (od 1 do n) wskazujący na kolor w liście `colors`.
        colors (List[Tuple[int, int, int]]): Lista kolorów w formacie RGB.
            Każdy kolor to krotka z trzema wartościami (R, G, B), gdzie:
            - R (int): czerwony (0-255),
            - G (int): zielony (0-255),
            - B (int): niebieski (0-255).
    """
    visual = input("\nCzy uruchomić wizualizację? (tak/nie), enter = tak: ").lower()
    if visual == "" or visual == "tak":
        height, width = len(pixel_matrix), len(pixel_matrix[0])
        image = np.zeros((height, width, 3), dtype=np.uint8)

        for i in range(height):
            for j in range(width):
                color_index = pixel_matrix[i][j] - 1  # Indeksowanie od 0
                if 0 <= color_index < len(colors):
                    image[i, j] = colors[color_index]

        # Tworzenie figury z ciemnym tłem
        fig = plt.figure(facecolor='lightgray')  # Ciemne tło okna
        ax = fig.add_subplot(111, facecolor='lightgray')  # Ciemne tło osi

        # Wyświetlanie obrazu
        ax.imshow(image, origin='upper')  # origin='upper' — odwrócenie osi Y
        ax.axis('off')  # Ukrycie osi

        # Ustawienie okna w lewym górnym rogu ekranu
        try:
            manager = plt.get_current_fig_manager()
            manager.window.wm_geometry("+0+0")  # Pozycja (0,0) = lewy górny róg
        except AttributeError:
            pass  # Obsługa środowisk, które nie wspierają wm_geometry()

        plt.show()
    else:
        print("Wizualizacja została pominięta.")

def print_menu():
    """Wyświetla meny programu"""

    print("\nAby kontynuować, wybierz jedną z poniższych opcji:")
    print("\n1. Zakoduj obraz (symbole 1-4)")
    print("2. Zakoduj obraz (binarny)")
    print("3. Zakoduj obraz (szesnastkowy)")
    print("4. Odkoduj obraz (binarny)")
    print("5. Odkoduj obraz (szesnastkowy)")
    print("6. Załaduj obraz z pliku")
    print("7. Zapisz obraz do pliku w formacie binarnym")
    print("8. Zapisz obraz do pliku w formacie szesnastkowym")
    print("9. Informacje o programie")
    print("10. Wyjdź z programu")


def clear_screen() :
    """Funkcja do czyszczenia ekranu"""
    
    os.system('cls' if os.name == 'nt' else 'clear') # Czyszczenie ekranu w zależności od systemu

clear_screen() # Czyszczenie terminala przed uruchomieniem menu programu


def image_settings() -> tuple:
    """Pobiera ustawienia obrazu od użytkownika.

    Returns:
        Krotka (szerokość, wysokość, kolory).

    Raises:
        ValueError: Jeśli podane dane są nieprawidłowe.
    """
    print("\nWypełnij następujące pola:\n")
    width = int(input("Podaj szerokość obrazu (1-256): "))
    if not 1 <= width <= 256: # Walidacja szerokości
        raise ValueError("Szerokość obrazu musi być liczbą całkowitą z zakresu 1-256.")

    height = int(input("Podaj wysokość obrazu (1-256): "))
    if not 1 <= height <= 256: # Walidacja wysokości
        raise ValueError("Wysokość obrazu musi być liczbą całkowitą z zakresu 1-256.")

    print("Czy chcesz użyć domyślnych kolorów? (tak/nie), enter = tak")
    use_default_colors = input().lower() # Wybór palety kolorów, konwertowanie str na małe litery

    if use_default_colors in ("nie", "n"): # Sprawdzanie wyboru użytkownika
        colors = [] # tworzenie pustej listy, na informacje o kolorach
        for label in ["1", "2", "3", "4"]: # Iteracja po etykietach
            while True: # pętla dopóki użytkownik nie poda poprawnych wartości.
                color_input = input(f"Jaki kolor przypisać do oznaczenia '{label}' (Format R,G,B, np. 255,0,255): ").strip()
                try:  # obsługa błędu
                    r, g, b = map(int, color_input.split(",")) # pobieranie ciągów dot. kolorów
                    if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255: # walidacja zakresu 0-255 dla kolorów
                        colors.append((r, g, b)) # dodanie koloru do wcześniej utworzonej listy
                        break # zatrzymanie 
                    else: 
                        print("Wartości R, G i B muszą być liczbami całkowitymi z zakresu 0-255.")
                except ValueError: # oczekiwanie błędu wartości
                    print("Nieprawidłowy format koloru. Podaj wartości w formacie R,G,B.")
    else:
        colors = colors_set # przypisanie domylśnych kolorów

    return width, height, colors # zwracanie danych


## Funkcje kodujące dekodując

def encode_image(mode: int) -> tuple:
    """
    Koduje obraz w postaci binarnej lub szesnastkowej, z literacją kolorów od 1 do 4.

    Args:
        mode: Tryb danych wejściowych (1 - symboliczny, 2 - binarny, 16 - szesnastkowy).

    Returns:
        Krotka (zakodowane bity, zakodowany ciąg szesnastkowy).

    Raises:
        ValueError: Jeśli podane dane są nieprawidłowe.
    """
    # Pobierz ustawienia obrazu, jeśli nie zostały podane

    width, height, colors = image_settings() # Pobierz ustawienia obrazu

    # Weryfikacja rozmiaru obrazu
    if width < 1 or width > 256 or height < 1 or height > 256: # Sprawdzenie, czy szerokość i wysokość są w zakresie 1-256
        raise ValueError("Szerokość i wysokość obrazu muszą być w zakresie 1-256.") # komunikat o błędzie
    
    # Tryb 1: Symboliczny
    if mode == 1: # Warunek uruchomienia trybu symbolicznego
        print(f"Wprowadź dane wierszami dla obrazu {width}x{height}.")
        print(f"Każdy wiersz musi zawierać dokładnie {width} wartości (1-4).")

        pixel_data = []  # Lista do przechowywania danych pikseli
        for row in range(height): # Pętla do wprowadzania danych zależnie od wysokości
            while True: # Pętla sprawdzająca czy użytkownik wprowadzi poprawne dane dla konkretnego wiersza.
                line = input(f"Wprowadź dane dla wiersza {row + 1}: ")
                if len(line) != width:  # Sprawdzanie długości wiersza czy jest równy szerokości
                    print(f"Błąd: Wiersz musi zawierać dokładnie {width} wartości. Spróbuj ponownie.")
                    continue # Wprowadź dane ponownie
                if not all(c in '1234' for c in line):  # Sprawdzanie poprawności symboli
                    print("Błąd: Dozwolone wartości to tylko liczby 1, 2, 3, 4. Spróbuj ponownie.")
                    continue # Wprowadź dane ponownie
                pixel_data.extend(int(x) for x in line)  # Dodanie danych do listy pikseli
                break  # Wiersz wprowadzony poprawnie, przejdź do następnego

        # Konwersja danych na ciąg binarny
        pixel_data = ''.join(f"{x - 1:02b}" for x in pixel_data)  # 1 → "00", 2 → "01", itd. 

    # Tryb 2: Binarny
    elif mode == 2: # Warunek uruchomienia trybu binarnego
        encoded_data = input(f"Podaj kod binarny {width*height}-bitowy dla obrazu (binarnie): ")
        max_bits = width * height * 2  # Liczba bitów potrzebna na dane pikseli
        pixel_data = encoded_data.strip() # Usunięcie białych znaków z początku i końca
        if not all(c in '01' for c in pixel_data): # Sprawdzenie, czy ciąg binarny zawiera tylko '0' i '1'
            raise ValueError("Ciąg binarny może zawierać wyłącznie znaki '0' i '1'.")
        pixel_data = adjust_bit_string(pixel_data, max_bits) # Dopasowanie długości ciągu binarnego

    elif mode == 16:  # Warunek uruchomienia trybu szesnastkowego
        encoded_data = input(f"Podaj kod binarny {(width * height * 2 + 3) // 4}-bitowy dla obrazu obrazu (szesnastkowo): ")
        max_hex_length = (width * height * 2 + 3) // 4  # Maksymalna długość ciągu szesnastkowego
        pixel_data = encoded_data.strip()  # Usunięcie białych znaków z początku i końca
        
        # Sprawdzenie, czy długość ciągu szesnastkowego jest poprawna
        if len(pixel_data) > max_hex_length: # Gdy długość ciągu jest większa niż maksymalna
            raise ValueError(f"Podano zbyt długi ciąg szesnastkowy. Maksymalna dozwolona długość: {max_hex_length} znaków.") # Komunikat o błędzie

        try: # Próba konwersji ciągu szesnastkowego na binarny
            int(pixel_data, 16)  # Walidacja danych szesnastkowych
            pixel_data = bin(int(pixel_data, 16))[2:]  # Konwersja na binarny
            pixel_data = adjust_bit_string(pixel_data, width * height * 2)  # Dopasowanie długości ciągu binarnego
        except ValueError:  # W przypadku nieprawidłowego ciągu szesnastkowego
            raise ValueError("Podano niepoprawny ciąg szesnastkowy.")  # Komunikat o błędzie


    # Kodowanie szerokości, wysokości i kolorów
    encoded_bits = f"{width - 1:08b}{height - 1:08b}" # Szerokość i wysokość
    for color in colors: # Dla każdego koloru w liście
        r, g, b = color # Rozpakowanie koloru
        encoded_bits += f"{r:08b}{g:08b}{b:08b}" # Dodanie kolorów do zakodowanych danych

    # Dodanie danych pikseli do zakodowanych danych
    encoded_bits += pixel_data

    # Dopasowanie długości ciągu binarnego do wielokrotności 8
    encoded_bits = adjust_bit_string(encoded_bits, (len(encoded_bits) + 7) // 8 * 8) 

    # Konwersja ciągu binarnego na szesnastkowy
    encoded_hex = hex(int(encoded_bits, 2))[2:].upper()

    # Dodanie brakujących zer wiodących do pełnych bajtów
    while len(encoded_hex) < len(encoded_bits) // 4: # Dopóki długość ciągu szesnastkowego jest mniejsza niż długość ciągu binarnego
        encoded_hex = "0" + encoded_hex # Dodanie zera wiodącego

    return encoded_bits, encoded_hex # Zwróć zakodowane bity i ciąg szesnastkowy


def decode_image(encoded_data: str, mode: int) -> tuple:
    """
    Dekoduje obraz z postaci binarnej lub szesnastkowej, z literacją kolorów od 1 do 4.

    Args:
        encoded_data: Zakodowany obraz w postaci binarnej lub szesnastkowej.
        mode: Tryb danych wejściowych (2 - binarny, 16 - szesnastkowy).

    Returns:
        Krotka (szerokość, wysokość, kolory, dane pikseli w układzie dwuwymiarowym)

    Raises:
        ValueError: Jeśli zakodowane dane są nieprawidłowe.
    """
    if mode == 16: # Jeśli tryb szesnastkowy
        encoded_bits = bin(int(encoded_data, 16))[2:].zfill(len(encoded_data) * 4) # Konwersja ciągu szesnastkowego na binarny
    elif mode == 2: # Jeśli tryb binarny
        encoded_bits = encoded_data # Przypisanie zakodowanych danych
    else: # Jeśli tryb nie jest ani 2 ani 16
        raise ValueError("Nieobsługiwany tryb. Użyj 2 dla binarnego lub 16 dla szesnastkowego.") # Komunikat o błędzie

    if len(encoded_bits) < 64: # Sprawdzenie, czy zakodowane dane są zbyt krótkie
        raise ValueError("Zakodowane dane są zbyt krótkie, aby zawierać wymagane informacje.") # Komunikat o błędzie

    # Dekodowanie szerokości i wysokości
    width = int(encoded_bits[:8], 2) + 1 # Szerokość
    height = int(encoded_bits[8:16], 2) + 1 # Wysokość

    # Dekodowanie kolorów (4 kolory, każdy 3 × 8 = 24 bity)
    colors = [] # Lista na kolory
    for i in range(16, 112, 24): # Zakres wynika z kodowania: 16 bitów na wymiary + 24 bity na kolory = 112 początek ciągu bitów
        r = int(encoded_bits[i:i + 8], 2) 
        g = int(encoded_bits[i + 8:i + 16], 2) 
        b = int(encoded_bits[i + 16:i + 24], 2)    
        colors.append((r, g, b)) # Dodanie koloru do listy

    # Dekodowanie danych pikseli (2 bity na piksel)
    pixel_data = [] # Lista na dane pikseli
    pixel_start = 112 # Kodowanie <=> Wymiary: 16 + Kolory: 96 = Początek ciągu bitów: 112
    for i in range(pixel_start, pixel_start + (width * height * 2), 2):
        pixel_value = int(encoded_bits[i:i + 2], 2) + 1  # Przesunięcie od 1 do 4
        pixel_data.append(pixel_value)

    # Przekształcenie danych pikseli do macierzy dwuwymiarowej
    pixel_matrix = [pixel_data[i * width:(i + 1) * width] for i in range(height)]

    # Sprawdzenie długości zakodowanych danych
    calculated_bit_length = 112 + width * height * 2 # Obliczenie długości zakodowanych danych 
    if len(encoded_bits) < calculated_bit_length: # Sprawdzenie, czy długość zakodowanych danych jest zbyt krótka
        raise ValueError("Długość zakodowanych danych jest zbyt krótka.") # Komunikat o błędzie

    return width, height, colors, pixel_matrix # Zwróć szerokość, wysokość, kolory i dane pikseli


def adjust_bit_string(bit_string: str, required_length: int) -> str:
    """
    Dopasowuje długość ciągu bitów do wymaganej wartości.

    Funkcja modyfikuje podany ciąg bitów tak, aby miał dokładnie `required_length` bitów.
    Jeśli ciąg jest za krótki, dopełnia go zerami od prawej strony zerami.
    Jeśli ciąg jest za długi, obcina nadmiarowe bity od prawej strony.

    Args:
        bit_string: Ciąg bitów składający się wyłącznie z znaków '0' i '1'.
        required_length: Całkowita liczba bitów, jaką powinien mieć wynikowy ciąg.

    Returns:
        Ciąg bitów o długości `required_length`, będący dopasowaną wersją wejściowego ciągu.
    """

    if len(bit_string) < required_length: # Dopisanie zer do ciągu, jeśli jest za krótki
        bit_string = bit_string.ljust(required_length, '0') # Dopisanie zer

    elif len(bit_string) > required_length: # Obcięcie ciągu, jeśli jest za długi
        bit_string = bit_string[:required_length]  # Obcięcie ciągu
    return bit_string # Zwrócenie ciągu

## Funkcje operacji na plikach

def write_file(file_name: str, data: str):
    """Zapisuje dane do pliku."""
    try: # Obsługa błędów
        with open(file_name, "w") as file: # Otwarcie pliku do zapisu
            file.write(data) # Zapisanie danych do pliku
    except IOError as e: # Wyjątek dla błędu zapisu
        print(f"Błąd podczas zapisywania pliku: {e}") # Komunikat o błędzie


def read_file(file_name: str) -> str:
    """Odczytuje dane z pliku."""
    try: # Obsługa błędów
        with open(file_name, "r") as file:  # Otwarcie pliku do odczytu
            return file.read() # Odczytanie danych z pliku
    except IOError as e: # Wyjątek dla błędu odczytu
        print(f"Błąd podczas odczytu pliku: {e}") # Komunikat o błędzie
        return "" # Zwrócenie pustego ciągu

def detect_file_format(file_name: str) -> int:
    """
    Wykrywa format pliku na podstawie rozszerzenia.
    Zwraca 2 dla formatu binarnego (.bm2) i 16 dla formatu szesnastkowego (.bm16).
    """
    if file_name.endswith(".bm2"): # Jeśli plik kończy się na .bm2
        return 2 # Zwróć 2 celem odczytu danych binarnych (mode 2)
    elif file_name.endswith(P16X):
        return 16 # Zwróć 16 celem odczytu danych szesnastkowych (mode 16)
    else: # Jeśli plik nie jest ani .bm2 ani .bm16
        raise ValueError("Nieobsługiwany format pliku. Użyj .bm2 lub .bm16.") # Komunikat o błędzie


## Menu główne programu

if __name__ == "__main__":

    encoded_bits, encoded_hex = "", ""  # Zainicjalizowanie zmiennych przechowujących dane
    show_menu = 0  # Licznik powtórzeń wprowadzony w celu ukrycia menu po pierwszym uruchomieniu
    print(f"Witaj w programie {program_name}, aby uzyskać dodatkowe informacje skorzystaj z opcji nr 9.")

    while True:
        if show_menu == 1:  # Wyświetlenie komunikatu przed powrotem do menu
            print(f"\nPozostajesz w programie {program_name}.")
            menu = input("\nAby powrócić do menu, naciśnij dowolny klawisz.")
            if menu != None: # Jeśli użytkownik naciśnie dowolny klawisz
                show_menu = 2 # Przesuń licznik powtórzeń celem wyświetlenia menu z komunikatem powrotu
                continue # Kontynuuj program

        if show_menu == 0:  # Wyświetlenie menu przy pierwszym uruchomieniu lub po powrocie z menu
            print_menu() # Wyświetlenie menu
        
        if show_menu == 2:  # Wyświetlenie menu po powrocie z menu
            clear_screen()
            print(f"Witaj ponownie w menu programu {program_name}")
            print_menu() # Wyświetlenie menu

        show_menu = 1  # Zwiększenie licznika powtórzeń w celu wyświetlenia komunikatu

        try: # Obsługa błędów
            choice = int(input("\nWybór: ")) # Wybór opcji
            clear_screen()

            if choice == 1:
                print ("Wybrano opcję 1. Zakoduj obraz (symbole 1-4)")
                encoded_bits, encoded_hex = encode_image(1) # Zakoduj obraz w trybie symboli
                print(f"\nZakodowany obraz (binarnie): {encoded_bits}")
                print(f"Zakodowany obraz (szesnastkowo): {encoded_hex}")

            elif choice == 2:
                print ("Wybrano opcję 2. Zakoduj obraz (binarny)")
                encoded_bits, encoded_hex = encode_image(2) # Zakoduj obraz w trybie binarnym
                print(f"\nZakodowany obraz (binarnie): {encoded_bits}")
                print(f"Zakodowany obraz (szesnastkowo): {encoded_hex}")

            elif choice == 3:
                print ("Wybrano opcję 3. Zakoduj obraz (szesnastkowy)")
                encoded_bits, encoded_hex = encode_image(16) # Zakoduj obraz w trybie 16-stkowym
                print(f"\nZakodowany obraz (binarnie): {encoded_bits}")
                print(f"Zakodowany obraz (szesnastkowo): {encoded_hex}")

            elif choice == 4:
                print ("Wybrano opcję 4. Odkoduj obraz (binarny)")
                encoded_data = input("Podaj zakodowany obraz (binarnie): ")
                width, height, colors, pixel_matrix = decode_image(encoded_data, 2)
                print(f"\nSzerokość: {width}, Wysokość: {height}")
                print("Kolory:")
                for i, color in enumerate(colors, 1):
                    print(f"Kolor {i}: R={color[0]}, G={color[1]}, B={color[2]}")
                print("Dane pikseli:")
                for row in pixel_matrix:
                    print(row)
                visualize_image(pixel_matrix, colors)

            elif choice == 5:
                print ("Wybrano opcję 5. Odkoduj obraz (szesnastkowy)")
                encoded_data = input("Podaj zakodowany obraz (szesnastkowo): ")
                width, height, colors, pixel_matrix = decode_image(encoded_data, 16)
                print(f"\nSzerokość: {width}, Wysokość: {height}")
                print("Kolory:")
                for i, color in enumerate(colors, 1):
                    print(f"Kolor {i}: R={color[0]}, G={color[1]}, B={color[2]}")
                print("Dane pikseli:")
                for row in pixel_matrix:
                    print(row) 
                visualize_image(pixel_matrix, colors)

            elif choice == 6:
                print ("Wybrano opcję 6. Załaduj obraz z pliku")
                print("\nWypełnij następujące pola:\n")
                file_name = input("Podaj nazwę pliku: ")
                try:
                    file_format = detect_file_format(file_name) # Wykryj format pliku
                    data = read_file(file_name) # Odczytaj dane z pliku
                    if data:
                        if file_format == 2: # Jeśli format binarny
                            print("\nOdczytano plik w formacie binarnym.")
                            width, height, colors, pixel_matrix = decode_image(data, 2) # Dekodowanie obrazu binarnego
                        elif file_format == 16: # Jeśli format szesnastkowy
                            print("\nOdczytano plik w formacie szesnastkowym.")
                            width, height, colors, pixel_matrix = decode_image(data, 16) # Dekodowanie obrazu szesnastkowego
                        print(f"\nSzerokość: {width}, Wysokość: {height}")
                        print("Kolory:")
                        for i, color in enumerate(colors, 1): # Wyświetlenie kolorów
                            print(f"Kolor {i}: R={color[0]}, G={color[1]}, B={color[2]}")
                        print("Dane pikseli:")
                        for row in pixel_matrix: # Wyświetlenie danych pikseli
                            print(row)
                        visualize_image(pixel_matrix, colors)
                except ValueError as e: # Wyjątek dla nieprawidłowego formatu pliku
                    print(f"Błąd formatu pliku: {e}")   

            # Zapisywanie obrazu do pliku w formacie binarnym
            elif choice == 7: 
                print ("Wybrano opcję 7. Zapisz obraz do pliku w formacie binarnym")
                print("\nWypełnij następujące pola:\n")
                file_name = input(f"Podaj nazwę pliku (z rozszerzeniem {PBIN}): ")
                if not file_name.endswith(PBIN): # Dodanie rozszerzenia, jeśli nie zostało podane
                    file_name += PBIN
                if encoded_bits: # Jeśli są dane do zapisania
                    write_file(file_name, encoded_bits)
                    print(f"\nObraz zapisano do pliku {file_name} w formacie binarnym.")
                else: # Jeśli nie ma danych do zapisania
                    print("\nBrak danych do zapisania. Najpierw zakoduj obraz.")

            # Zapisywanie obrazu do pliku w formacie szesnastkowym
            elif choice == 8:
                print ("Wybrano opcję 8. Zapisz obraz do pliku w formacie szesnastkowym")
                print("\nWypełnij następujące pola:\n")
                file_name = input(f"Podaj nazwę pliku (z rozszerzeniem {P16X}): ")
                if not file_name.endswith(P16X): # Dodanie rozszerzenia, jeśli nie zostało podane
                    file_name += P16X  
                if encoded_hex: # Jeśli są dane do zapisania
                    write_file(file_name, encoded_hex) # Zapisz dane do pliku
                    print(f"\nObraz zapisano do pliku {file_name} w formacie szesnastkowym.")
                else: # Jeśli nie ma danych do zapisania
                    print("Brak danych do zapisania. Najpierw zakoduj obraz.")

            # Wyjście z programu
            elif choice == 9:
                print ("Wybrano opcję 9. Informacje o programie")
                print(program_description)

            # Wyświetlenie pomocy
            elif choice == 10:
                print ("Wybrano opcję 10. Wyjdź z programu")
                print("\nDziękuję za skorzystanie z programu!")
                break # Zakończ program

            else: # W przypadku nieprawidłowego wyboru
                print("Nieprawidłowy wybór. Spróbuj ponownie.")

        except ValueError as e: # Wyjątek dla nieprawidłowych danych
            print(f"\nNieprawidłowe dane wejściowe: {e}")
        except KeyboardInterrupt: # Wyjątek dla przerwania klawiszem
            print("\nPrzerwano przez użytkownika.")
            break
        except EOFError: # Wyjątek dla końca pliku
            print("\nNie można odczytać danych. Spróbuj ponownie.")
        except Exception as e: # Wyjątek dla nieoczekiwanego błędu
            print(f"\nWystąpił nieoczekiwany błąd: {e}")
            break