import os, json

# Constants
USER_DATA = os.getenv("USER_DATA_PATH", "data/phonebook.json")

def ensure_directory_exists(directory: str) -> None:
    """Tworzy nowy katalog, jeżeli nie istnieje."""
    try:
        os.makedirs(directory, exist_ok=True)
    except OSError as e:
        print(f"Błąd podczas tworzenia struktury katalogowej {directory}: {e}")

def read_phonebook(file_path: str) -> dict:
    """Czytanie danych książki telefonicznej z pliku."""
    ensure_directory_exists(os.path.dirname(file_path))
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Plik nie znaleziony {file_path}. Tworzenie pustej książki telefonicznej.")
        data = {"phonebook": []}
        save_phonebook(data, file_path)
        return data
    except json.JSONDecodeError as e:
        print(f"Błąd podczas dekodowania JSON z pliku {file_path}: {e}")
        return {"phonebook": []}

def save_phonebook(data: dict, file_path: str) -> None:
    """Zapisanie danych książki telefonicznej do pliku."""
    ensure_directory_exists(os.path.dirname(file_path))
    temp_file = file_path + ".tmp"
    with open(temp_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    os.replace(temp_file, file_path)

def numer_available(data: dict, number: str) -> bool:
    """Sprawdzanie dostępności numeru."""
    return number not in {u.get("numer") for u in data["phonebook"]}

def add_entry(phonebook: dict, numer: str) -> None:
    """Dodanie wpisu do książki telefonicznej."""
    if not validate_phone_number(numer):
        return
    if not numer_available(phonebook, numer):
        print(f"Błąd: Numer '{numer}' już istieje. Wybierz inny numer.")
        return
    name = input("Podaj imię i nazwisko użytkownika: ").strip()
    entry = {"numer": numer, "name": name}
    phonebook["phonebook"].append(entry)
    save_phonebook(phonebook, USER_DATA)
    print("Użytkownik został dodany.")


def display_phonebook(phonebook: dict) -> None:
    """Wyświetlenie zawartości książki telefonicznej."""
    print("\nLista użytkowników:")
    if not phonebook["phonebook"]:
        print("\nKsiążka telefoniczna jest pusta")
        print("")
        return

    sorted_by_numer = sorted(phonebook["phonebook"], key=lambda u: int(u.get("numer", 0) or 0))
    for u in sorted_by_numer:
        numer = u.get("numer", "Nie podano")
        name = u.get("name", "Nie podano")
        print(f"Numer: {numer}, Imię i nazwisko: {name}")

def remove_entry(numer: str) -> None:
    """Usuwanie użytkownika z książki telefonicznej."""
    if not validate_phone_number(numer):
        return
    data = read_phonebook(USER_DATA)
    updated = [u for u in data["phonebook"] if u.get("numer") != numer]
    if len(updated) == len(data["phonebook"]):
        print("Nie znaleziono użytkownika o podanym numerze.")
    else:
        data["phonebook"] = updated
        save_phonebook(data, USER_DATA)
        print("Użytkownik został usunięty.")


def modify_entry(numer: str, updated_data: dict) -> None:
    """Modyfikacja istniejącego wpisu, pozwalając na zmianę nazwy i numeru telefonu."""
    data = read_phonebook(USER_DATA)
    user = next((u for u in data["phonebook"] if u.get("numer") == numer), None)

    if not user:
        print("\nNie znaleziono użytkownika o podanym numerze telefonu.")
        return

    new_numer = updated_data.get("numer")
    if new_numer:
        if not validate_phone_number(new_numer):
            return
        if new_numer != numer and not numer_available(data, new_numer):
            print(f"\nBłąd: Numer '{new_numer}' już istnieje. Wybierz inny numer.")
            return

    user.update(updated_data)
    save_phonebook(data, USER_DATA)
    print("\nDane użytkownika zostały zaktualizowane.")

def validate_phone_number(numer: str) -> bool:
    """
    Walidacja numeru telefonu warunki działania:
    - Musi zawierać tylko cyfry.
    - Musi mieć długość 9 znaków (przykład: Polska).
    - Opcjonalnie: nie może zaczynać się od zera.
    """
    if not numer.isdigit():
        print("Numer telefonu może zawierać tylko cyfry.")
        return False
    if len(numer) != 9:
        print("Numer telefonu musi mieć dokładnie 9 cyfr.")
        return False
    if numer[0] == '0':
        print("Numer telefonu nie może zaczynać się od cyfry 0.")
        return False
    return True

def main() -> None:
    """Program główny."""
    while True:
        phonebook = read_phonebook(USER_DATA)
        print("\nAby kontynuować wybierz jedną z poniższych opcji:")
        print("1. Wyświetl książkę telefoniczną")
        print("2. Dodaj nowy numer")
        print("3. Usuń numer")
        print("4. Modyfikuj numer")
        print("5. Zapisz i wyjdź")
        option = input("Wybór: ")

        if option == "1":
            display_phonebook(phonebook)
        elif option == "2":
            phone_numer = input("Podaj numer telefonu użytkownika: ")
            add_entry(phonebook, phone_numer)
        elif option == "3":
            display_phonebook(phonebook)            
            numer = input("Podaj numer telefonu użytkownika do usunięcia: ")
            remove_entry(numer)
        elif option == "4":
            display_phonebook(phonebook)
            numer = input("Podaj numer telefonu użytkownika do modyfikacji: ")
            phonebook = read_phonebook(USER_DATA)
            user = next((u for u in phonebook["phonebook"] if u.get("numer") == numer), None)
            if not user:
                print("\nNie znaleziono użytkownika o podanym numerze.")
            else:
                print("\nPodaj nowe dane użytkownika (pozostaw puste, aby zachować istniejące dane):")
                new_name = input(f"Nowe imię i nazwisko ({user['name']}): ").strip()
                new_numer = input(f"Nowy numer ({user['numer']}): ").strip()

                updated_data = {}
                if new_name:
                    updated_data["name"] = new_name
                if new_numer:
                    updated_data["numer"] = new_numer

                modify_entry(numer, updated_data)

        elif option == "5":
            save_phonebook(phonebook, USER_DATA)
            print(f"Zapisano dane do pliku {USER_DATA}. Do zobaczenia!")
            break
        else:
            print("Nieprawidłowy wybór. Wybierz liczbę z listy.")

if __name__ == "__main__":
    main()