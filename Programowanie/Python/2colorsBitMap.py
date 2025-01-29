## Zaimplementowane moduły 

import os # Import modułu os do funkcji czyszczenia zawartości w terminalu
import matplotlib.pyplot as plt
import numpy as np

## Zmienne

# Pobieranie nazwy programu (pliku)
program_name = os.path.basename(__file__) 

# Domyślne kolory (czarny i biały)
colors_set = [(0, 0, 0), (255, 255, 255)]  # Czarny i biały

# Deklaracja rozszerzeń plików w zależności od formatu
PBIN = ".b2" # Rozszerzenie pliku binarnego
P16X = ".b16" # Rozszerzenie pliku szesnastkowego


## Opis programu

program_description = f"""
Informacje dotyczące programu {program_name}. 
\nPrznaczenie programu:
Kodowanie i dekodowanie mapy bitowe w postaci binarnej lub szesnastkowej.
\nProgram obsługuje obrazy:
                          - o wymiarach od 1x1 piksel do 256x256 pikseli
                          - z maksymalnie 2 kolorami jednocześnie.
                          - kolory można dostosować lub używać domyślnych.
                          - domyślne kolory to: czerwony, zielony, niebieski i biały.
                          - dane pikseli można wprowadzać symbolicznie *"." za pierwszy a "x" za drugi kolor), binarnie lub szesnastkowo.
                          - na plikach o własnych formatach: {PBIN} (dla kodowania binarnego), {P16X} (dla kodowania szesnastkowego).
Alternatywa :
                          - Stworzono bardziej rozbudowany program (pozwalający kodować do 4 kolorłów jednocześnie),
                            aby z niego skorzystać użyj poniższego linku:
                            https://github.com/Stani1999/Student_Notes/blob/main/Programowanie/Python/4colorsBitMap.py
Sposób kodowania:
                          - I  bajt zawiera informację o szerokości obrazy
                          - II bajt zawiera informację o wysokości obrazy
                          - pozostałe bajty przeznaczone są na kodowanie ww. kolorów, kolejno jako 0, 1 - w systemie binarnym.
                          - bajty przekraczające zakres wyznaczany przez dwa pierwsze bajty są ignorowane
                          - w przepadku braku wystarczającej ilości bitów program dopisuje wartości "0".
                          - piksele są kolejkowane według zasad „kolejności leksykograficznej” - z lewej do prawej strony.
                          - Interpretacje kolorów zmienić w opcji 9. programu (wartości nie są przechowywane w pliku).
Sposób dokodowania :
                          - daizła analogicznie do zasad kodowania, jednak z jednym wyjątkiem
                            - program nie dopisuje "0" jeżeli ciąg jest zbyt krótki, potrafi jedynie ucinać zbyt długie ciągi danych. 
Instrukcja obsługi:
                          1. Zakoduj obraz (symbole '.' i 'x'):
                           - Wybierz opcję 1, aby zakodować obraz za pomocą symboli '.' (kropka) i 'x'.
                           - Podaj szerokość i wysokość obrazu.
                           - Wprowadź dane pikseli wiersz po wierszu, używając symboli '.' i 'x'.
                           - Program wygeneruje zakodowany obraz w postaci binarnej i szesnastkowej.

                          2. Zakoduj obraz (binarny):
                           - Wybierz opcję 2, aby zakodować obraz za pomocą ciągu binarnego.
                           - Podaj szerokość i wysokość obrazu.
                           - Wprowadź ciąg binarny reprezentujący piksele (0 dla pierwszego koloru, 1 dla drugiego).
                           - Program wygeneruje zakodowany obraz w postaci binarnej i szesnastkowej.

                          3. Zakoduj obraz (szesnastkowy):
                           - Wybierz opcję 3, aby zakodować obraz za pomocą ciągu szesnastkowego.
                           - Podaj szerokość i wysokość obrazu.
                           - Wprowadź ciąg szesnastkowy reprezentujący piksele.
                           - Program wygeneruje zakodowany obraz w postaci binarnej i szesnastkowej.

                          4. Odkoduj obraz (binarny):
                           - Wybierz opcję 4, aby odkodować obraz z postaci binarnej.
                           - Wprowadź zakodowany ciąg binarny.
                           - Program wyświetli szerokość, wysokość oraz dane pikseli obrazu.
                           - Możesz uruchomić wizualizację obrazu.

                          5. Odkoduj obraz (szesnastkowy):
                           - Wybierz opcję 5, aby odkodować obraz z postaci szesnastkowej.
                           - Wprowadź zakodowany ciąg szesnastkowy.
                           - Program wyświetli szerokość, wysokość oraz dane pikseli obrazu.
                           - Możesz uruchomić wizualizację obrazu.

                          6. Załaduj obraz z pliku:
                           - Wybierz opcję 6, aby załadować obraz z pliku.
                           - Podaj nazwę pliku (rozszerzenie {PBIN} dla formatu binarnego lub {P16X} dla szesnastkowego).
                           - Program odczyta plik i wyświetli dane obrazu.
                           - Możesz uruchomić wizualizację obrazu.

                          7. Zapisz obraz do pliku w formacie binarnym:
                           - Wybierz opcję 7, aby zapisać zakodowany obraz do pliku w formacie binarnym.
                           - Podaj nazwę pliku (rozszerzenie {PBIN} zostanie dodane automatycznie).
                           - Program zapisze obraz do pliku.

                          8. Zapisz obraz do pliku w formacie szesnastkowym:
                           - Wybierz opcję 8, aby zapisać zakodowany obraz do pliku w formacie szesnastkowym.
                           - Podaj nazwę pliku (rozszerzenie {P16X} zostanie dodane automatycznie).
                           - Program zapisze obraz do pliku.

                          9. Edytuj kolory do dekodowania obrazu:
                           - Wybierz opcję 9, aby zmienić kolory używane do wizualizacji obrazu.
                           - Domyślne kolory to czarny (0, 0, 0) i biały (255, 255, 255).
                           - Możesz wprowadzić nowe wartości RGB dla każdego koloru.

                          10. Informacje o programie:
                           - Wybierz opcję 10, aby wyświetlić tę instrukcję obsługi.

                          11. Wyjdź z programu:
                           - Wybierz opcję 11, aby zamknąć program.

                          Przykłady użycia:
                           - Aby zakodować obraz 3x3 piksele za pomocą symboli '.' i 'x':
                          1. Wybierz opcję 1.
                          2. Podaj szerokość: 3 i wysokość: 3.
                          3. Wprowadź dane pikseli:
                             Wiersz 1: .x.
                             Wiersz 2: x.x
                             Wiersz 3: .x.
                          4. Program wygeneruje zakodowany obraz.

                          - Aby odkodować obraz z pliku:
                          1. Wybierz opcję 6.
                          2. Podaj nazwę pliku, np. 'obraz{PBIN}'.
                          3. Program wyświetli dane obrazu i zapyta, czy chcesz uruchomić wizualizację.

                          Uwagi:
                           - Kolory są globalne i mogą być zmieniane w opcji 9.
                           - Pliki są zapisywane w formacie binarnym ({PBIN}) lub szesnastkowym ({P16X}).
                           - Wizualizacja obrazu jest opcjonalna i można ją uruchomić po odkodowaniu obrazu.

                        Autor: Stani1999
                        GitHub: https://github.com/Stani1999
                        Wersja: 0.1.1
                        Data: 2025.01.29
"""

## Funkcje wizualne

def visualize_image(pixel_matrix: list[list[int]]) -> None:
    """
    Wizualizuje obraz na podstawie macierzy pikseli i globalnych kolorów.
    Obraz jest wyświetlany od lewego górnego rogu, a okno pojawia się w lewym górnym rogu ekranu.
    """
    global colors_set  # Użyj globalnych kolorów

    visual = input("\nCzy uruchomić wizualizację? (tak/nie), enter = tak: ").lower()
    if visual == "" or visual == "tak":
        height, width = len(pixel_matrix), len(pixel_matrix[0])
        image = np.zeros((height, width, 3), dtype=np.uint8)

        for i in range(height):
            for j in range(width):
                color_index = pixel_matrix[i][j]  # 0 lub 1
                if 0 <= color_index < len(colors_set):
                    image[i, j] = colors_set[color_index]

        # Utwórz figurę z określonym kolorem tła
        fig = plt.figure(facecolor='lightgray')  # Tło figury
        ax = fig.add_subplot(111, facecolor='lightgray')  # Tło osi

        # Wyświetl obraz z lewym górnym rogiem jako początek układu współrzędnych
        ax.imshow(image, origin='upper')  # origin='upper' — odwróć oś Y
        ax.axis('off')  # Wyłącz osie

        # Ustawienie okna w lewym górnym rogu ekranu
        try:
            manager = plt.get_current_fig_manager()
            manager.window.wm_geometry("+0+0")  # Pozycja (0,0) = lewy górny róg
        except AttributeError:
            pass  # Niektóre środowiska mogą nie obsługiwać tej funkcji

        plt.show()
    else:
        print("Wizualizacja została pominięta.")

def print_menu():
    """Wyświetla menu programu."""
    print("\nAby kontynuować, wybierz jedną z poniższych opcji:")
    print("\n1. Zakoduj obraz (symbole `.` `x`)")
    print("2. Zakoduj obraz (binarny)")
    print("3. Zakoduj obraz (szesnastkowy)")
    print("4. Odkoduj obraz (binarny)")
    print("5. Odkoduj obraz (szesnastkowy)")
    print("6. Załaduj obraz z pliku")
    print("7. Zapisz obraz do pliku w formacie binarnym")
    print("8. Zapisz obraz do pliku w formacie szesnastkowym")
    print("9. Edytuj kolory do dekodowania obrazu")
    print("10. Informacje o programie")
    print("11. Wyjdź z programu")

def clear_screen() :
    """Funkcja do czyszczenia ekranu"""
    
    os.system('cls' if os.name == 'nt' else 'clear') # Czyszczenie ekranu w zależności od systemu

clear_screen() # Czyszczenie terminala przed uruchomieniem menu programu


def image_settings() -> tuple[int, int]:
    """
    Pobiera ustawienia obrazu od użytkownika (szerokość i wysokość).

    Returns:
        Krotka (szerokość, wysokość).

    Raises:
        ValueError: Jeśli podane dane są nieprawidłowe.
    """
    print("\nWypełnij następujące pola:\n")
    
    # Pobierz szerokość obrazu
    width = int(input("Podaj szerokość obrazu (1-256): "))
    if not 1 <= width <= 256:  # Walidacja szerokości
        raise ValueError("Szerokość obrazu musi być liczbą całkowitą z zakresu 1-256.")

    # Pobierz wysokość obrazu
    height = int(input("Podaj wysokość obrazu (1-256): "))
    if not 1 <= height <= 256:  # Walidacja wysokości
        raise ValueError("Wysokość obrazu musi być liczbą całkowitą z zakresu 1-256.")

    return width, height  # Zwróć tylko szerokość i wysokość

## Funkcje kodujące dekodując

def encode_image(mode: int) -> tuple:
    """
    Koduje obraz w postaci binarnej lub szesnastkowej, używając symboli '.' i 'x'.

    Args:
        mode: Tryb danych wejściowych (1 - symboliczny, 2 - binarny, 16 - szesnastkowy).

    Returns:
        Krotka (zakodowane bity, zakodowany ciąg szesnastkowy).

    Raises:
        ValueError: Jeśli podane dane są nieprawidłowe.
    """
    width, height = image_settings()  # Pobierz tylko szerokość i wysokość

    # Tryb 1: Symboliczny ('.' i 'x')
    if mode == 1:
        print(f"Wprowadź dane wierszami dla obrazu {width}x{height}.")
        print(f"Każdy wiersz musi zawierać dokładnie {width} symboli ('.' lub 'x').")

        pixel_data = []  # Lista do przechowywania danych pikseli
        for row in range(height):
            while True:
                line = input(f"Wprowadź dane dla wiersza {row + 1}: ")
                if len(line) != width:
                    print(f"Błąd: Wiersz musi zawierać dokładnie {width} symboli. Spróbuj ponownie.")
                    continue
                if not all(c in '.x' for c in line):
                    print("Błąd: Dozwolone symbole to tylko '.' i 'x'. Spróbuj ponownie.")
                    continue
                pixel_data.extend(0 if c == '.' else 1 for c in line)  # '.' → 0, 'x' → 1
                break

        # Konwersja danych na ciąg binarny
        pixel_data = ''.join(f"{x:01b}" for x in pixel_data)  # 0 → "0", 1 → "1"

    # Tryb 2: Binarny
    elif mode == 2:
        encoded_data = input(f"Podaj kod binarny {width * height}-bitowy dla obrazu (binarnie): ")
        max_bits = width * height  # Liczba bitów potrzebna na dane pikseli
        pixel_data = encoded_data.strip()
        if not all(c in '01' for c in pixel_data):
            raise ValueError("Ciąg binarny może zawierać wyłącznie znaki '0' i '1'.")
        pixel_data = adjust_bit_string(pixel_data, max_bits)

    # Tryb 16: Szesnastkowy
    elif mode == 16:
        encoded_data = input(f"Podaj kod szesnastkowy dla obrazu: ")
        max_hex_length = (width * height + 3) // 4  # Maksymalna długość ciągu szesnastkowego
        pixel_data = encoded_data.strip()

        if len(pixel_data) > max_hex_length:
            raise ValueError(f"Podano zbyt długi ciąg szesnastkowy. Maksymalna dozwolona długość: {max_hex_length} znaków.")

        try:
            int(pixel_data, 16)  # Walidacja danych szesnastkowych
            pixel_data = bin(int(pixel_data, 16))[2:]  # Konwersja na binarny
            pixel_data = adjust_bit_string(pixel_data, width * height)  # Dopasowanie długości ciągu binarnego
        except ValueError:
            raise ValueError("Podano niepoprawny ciąg szesnastkowy.")

    # Kodowanie szerokości i wysokości
    encoded_bits = f"{width - 1:08b}{height - 1:08b}"  # Szerokość i wysokość

    # Dodanie danych pikseli do zakodowanych danych
    encoded_bits += pixel_data

    # Dopasowanie długości ciągu binarnego do wielokrotności 8
    encoded_bits = adjust_bit_string(encoded_bits, (len(encoded_bits) + 7) // 8 * 8)

    # Konwersja ciągu binarnego na szesnastkowy
    encoded_hex = hex(int(encoded_bits, 2))[2:].upper()

    # Dodanie brakujących zer wiodących do pełnych bajtów
    while len(encoded_hex) < len(encoded_bits) // 4:
        encoded_hex = "0" + encoded_hex

    return encoded_bits, encoded_hex

def decode_image(encoded_data: str, mode: int) -> tuple:
    """
    Dekoduje obraz z postaci binarnej lub szesnastkowej, używając globalnych kolorów.

    Args:
        encoded_data: Zakodowany obraz w postaci binarnej lub szesnastkowej.
        mode: Tryb danych wejściowych (2 - binarny, 16 - szesnastkowy).

    Returns:
        Krotka (szerokość, wysokość, dane pikseli w układzie dwuwymiarowym)

    Raises:
        ValueError: Jeśli zakodowane dane są nieprawidłowe.
    """
    global colors_set  # Użyj globalnych kolorów

    if mode == 16:
        encoded_bits = bin(int(encoded_data, 16))[2:].zfill(len(encoded_data) * 4)
    elif mode == 2:
        encoded_bits = encoded_data
    else:
        raise ValueError("Nieobsługiwany tryb. Użyj 2 dla binarnego lub 16 dla szesnastkowego.")

    if len(encoded_bits) < 16:  # 16 bitów na wymiary
        raise ValueError("Zakodowane dane są zbyt krótkie, aby zawierać wymagane informacje.")

    # Dekodowanie szerokości i wysokości
    width = int(encoded_bits[:8], 2) + 1
    height = int(encoded_bits[8:16], 2) + 1

    # Dekodowanie danych pikseli (1 bit na piksel)
    pixel_data = []
    pixel_start = 16  # 16 bitów na wymiary
    for i in range(pixel_start, pixel_start + (width * height)):
        pixel_value = int(encoded_bits[i], 2)  # 0 lub 1
        pixel_data.append(pixel_value)

    # Przekształcenie danych pikseli do macierzy dwuwymiarowej
    pixel_matrix = [pixel_data[i * width:(i + 1) * width] for i in range(height)]

    # Sprawdzenie długości zakodowanych danych
    calculated_bit_length = 16 + width * height  # 16 bitów na wymiary + (width * height) bitów na piksele
    if len(encoded_bits) < calculated_bit_length:
        raise ValueError("Długość zakodowanych danych jest zbyt krótka.")

    return width, height, pixel_matrix

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
    Zwraca 2 dla formatu binarnego (PBIN) i 16 dla formatu szesnastkowego (P16X).
    """
    if file_name.endswith(PBIN): # Jeśli plik kończy się na PBIN
        return 2 # Zwróć 2 celem odczytu danych binarnych (mode 2)
    elif file_name.endswith(P16X):
        return 16 # Zwróć 16 celem odczytu danych szesnastkowych (mode 16)
    else: # Jeśli plik nie jest ani PBIN ani P16X
        raise ValueError("Nieobsługiwany format pliku. Użyj PBIN lub P16X") # Komunikat o błędzie

def edit_colors() -> list[tuple[int, int, int]]:
    """
    Pozwala użytkownikowi edytować kolory używane do dekodowania obrazu.

    Returns:
        Lista kolorów w formacie RGB.
    """
    global colors_set  # Użyj globalnej zmiennej colors_set
    print("\nEdycja kolorów do dekodowania obrazu.")
    print(f"Aktualne kolory: 1. {colors_set[0]} (czarny), 2. {colors_set[1]} (biały)")

    new_colors = []  # Lista na nowe kolory
    for i in range(2):  # Tylko 2 kolory
        while True:
            color_input = input(f"Podaj nowy kolor {i + 1} (Format R,G,B, np. 255,0,0): ").strip()
            try:
                r, g, b = map(int, color_input.split(","))  # Rozdzielenie wartości RGB
                if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:  # Walidacja zakresu
                    new_colors.append((r, g, b))  # Dodanie koloru do listy
                    break
                else:
                    print("Wartości R, G i B muszą być liczbami całkowitymi z zakresu 0-255.")
            except ValueError:
                print("Nieprawidłowy format koloru. Podaj wartości w formacie R,G,B.")

    colors_set = new_colors  # Zastąp globalne kolory nowymi
    print(f"Zaktualizowane kolory: 1. {colors_set[0]}, 2. {colors_set[1]}")
    return colors_set

# Menu główne programu

if __name__ == "__main__":
    encoded_bits, encoded_hex = "", ""  # Zainicjalizowanie zmiennych przechowujących dane
    show_menu = 0  # Licznik powtórzeń wprowadzony w celu ukrycia menu po pierwszym uruchomieniu
    print(f"Witaj w programie {program_name}, aby uzyskać dodatkowe informacje skorzystaj z opcji nr 9.")

    while True:
        if show_menu == 1:  # Wyświetlenie komunikatu przed powrotem do menu
            print(f"\nPozostajesz w programie {program_name}.")
            menu = input("\nAby powrócić do menu, naciśnij dowolny klawisz.")
            if menu != None:
                show_menu = 2
                continue

        if show_menu == 0:  # Wyświetlenie menu przy pierwszym uruchomieniu lub po powrocie z menu
            print_menu()

        if show_menu == 2:  # Wyświetlenie menu po powrocie z menu
            clear_screen()
            print(f"Witaj ponownie w menu programu {program_name}")
            print_menu()

        show_menu = 1  # Zwiększenie licznika powtórzeń w celu wyświetlenia komunikatu

        try:
            choice = int(input("\nWybór: "))  # Wybór opcji
            clear_screen()

            if choice == 1:
                print("Wybrano opcję 1. Zakoduj obraz (symbole '.' i 'x')")
                encoded_bits, encoded_hex = encode_image(1)  # Przekaż szerokość i wysokość
                print(f"\nZakodowany obraz (binarnie): {encoded_bits}")
                print(f"Zakodowany obraz (szesnastkowo): {encoded_hex}")

            elif choice == 2:
                print("Wybrano opcję 2. Zakoduj obraz (binarny)")
                encoded_bits, encoded_hex = encode_image(2)
                print(f"\nZakodowany obraz (binarnie): {encoded_bits}")
                print(f"Zakodowany obraz (szesnastkowo): {encoded_hex}")

            elif choice == 3:
                print("Wybrano opcję 3. Zakoduj obraz (szesnastkowy)")
                encoded_bits, encoded_hex = encode_image(16)
                print(f"\nZakodowany obraz (binarnie): {encoded_bits}")
                print(f"Zakodowany obraz (szesnastkowo): {encoded_hex}")

            elif choice == 4:
                print("Wybrano opcję 4. Odkoduj obraz (binarny)")
                encoded_data = input("Podaj zakodowany obraz (binarnie): ")
                width, height, pixel_matrix = decode_image(encoded_data, 2)
                print(f"\nSzerokość: {width}, Wysokość: {height}")
                print("Dane pikseli:")
                for row in pixel_matrix:
                    print(row)
                visualize_image(pixel_matrix)  # Użyj globalnych kolorów

            elif choice == 5:
                print("Wybrano opcję 5. Odkoduj obraz (szesnastkowy)")
                encoded_data = input("Podaj zakodowany obraz (szesnastkowo): ")
                width, height, pixel_matrix = decode_image(encoded_data, 16)
                print(f"\nSzerokość: {width}, Wysokość: {height}")
                print("Dane pikseli:")
                for row in pixel_matrix:
                    print(row)
                visualize_image(pixel_matrix)  # Użyj globalnych kolorów

            elif choice == 6:
                print("Wybrano opcję 6. Załaduj obraz z pliku")
                print("\nWypełnij następujące pola:\n")
                file_name = input("Podaj nazwę pliku: ")
                try:
                    file_format = detect_file_format(file_name)
                    data = read_file(file_name)
                    if data:
                        if file_format == 2:
                            print("\nOdczytano plik w formacie binarnym.")
                            width, height, pixel_matrix = decode_image(data, 2)
                        elif file_format == 16:
                            print("\nOdczytano plik w formacie szesnastkowym.")
                            width, height, pixel_matrix = decode_image(data, 16)
                        print(f"\nSzerokość: {width}, Wysokość: {height}")
                        print("Dane pikseli:")
                        for row in pixel_matrix:
                            print(row)
                        visualize_image(pixel_matrix)  # Użyj globalnych kolorów
                except ValueError as e:
                    print(f"Błąd formatu pliku: {e}")

            elif choice == 7:
                print("Wybrano opcję 7. Zapisz obraz do pliku w formacie binarnym")
                print("\nWypełnij następujące pola:\n")
                file_name = input(f"Podaj nazwę pliku (z rozszerzeniem {PBIN}): ")
                if not file_name.endswith(PBIN):
                    file_name += PBIN
                if encoded_bits:
                    write_file(file_name, encoded_bits)
                    print(f"\nObraz zapisano do pliku {file_name} w formacie binarnym.")
                else:
                    print("\nBrak danych do zapisania. Najpierw zakoduj obraz.")

            elif choice == 8:
                print("Wybrano opcję 8. Zapisz obraz do pliku w formacie szesnastkowym")
                print("\nWypełnij następujące pola:\n")
                file_name = input(f"Podaj nazwę pliku (z rozszerzeniem {P16X}): ")
                if not file_name.endswith(P16X):
                    file_name += P16X
                if encoded_hex:
                    write_file(file_name, encoded_hex)
                    print(f"\nObraz zapisano do pliku {file_name} w formacie szesnastkowym.")
                else:
                    print("Brak danych do zapisania. Najpierw zakoduj obraz.")

            elif choice == 9:
                print("Wybrano opcję 9. Edytuj kolory do dekodowania obrazu")
                edit_colors()  # Wywołanie funkcji edycji kolorów

            elif choice == 10:
                print("Wybrano opcję 10. Informacje o programie")
                print(program_description)

            elif choice == 11:
                print("Wybrano opcję 11. Wyjdź z programu")
                print("Kliknij tutaj: https://example.com")
                print("\nDziękuję za skorzystanie z programu!")
                break

            else:
                print("Nieprawidłowy wybór. Spróbuj ponownie.")

        except ValueError as e:
            print(f"\nNieprawidłowe dane wejściowe: {e}")
        except KeyboardInterrupt:
            print("\nPrzerwano przez użytkownika.")
            break
        except EOFError:
            print("\nNie można odczytać danych. Spróbuj ponownie.")
        except Exception as e:
            print(f"\nWystąpił nieoczekiwany błąd: {e}")
            break