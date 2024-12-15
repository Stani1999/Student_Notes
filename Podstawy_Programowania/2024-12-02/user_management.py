import os, json , string, re
from secrets import choice

# Constants
USER_DATA = os.getenv("USER_DATA_PATH", "data/users.json")

# Helper Functions
def ensure_directory_exists(directory: str) -> None:
    """Create new directory if it doesn't exist yet."""
    try:
        os.makedirs(directory, exist_ok=True)
    except OSError as e:
        print(f"Błąd podczas tworzenia struktury katalogowej {directory}: {e}")

# File Operations
def load_users() -> dict:
    """Load users data from JSON file."""
    try:
        with open(USER_DATA, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Plik nieznaleziony {USER_DATA}. Tworze pusty plik z na dane.")
    except json.JSONDecodeError as e:
        print(f"Błąd podczas dekodowania: {USER_DATA}: {e}")
    return {"users": []}

def save_users(users: dict) -> None:
    """Save file with user data."""
    ensure_directory_exists(os.path.dirname(USER_DATA))
    temp_file = USER_DATA + ".tmp"
    with open(temp_file, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4)
    os.replace(temp_file, USER_DATA)

# Validation Functions
def validate_pesel(pesel: str) -> bool:
    """Validate PESEL number."""
    if len(pesel) != 11 or not pesel.isdigit():
        return False

    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    control_sum = sum(int(pesel[i]) * weights[i] for i in range(10))
    control_digit = (10 - (control_sum % 10)) % 10
    return control_digit == int(pesel[10])

def validate_nip(nip: str) -> bool:
    """Validate NIP number."""
    if len(nip) != 10 or not nip.isdigit():
        return False

    weights = [6, 5, 7, 2, 3, 4, 5, 6, 7]
    control_sum = sum(int(nip[i]) * weights[i] for i in range(9))
    control_digit = control_sum % 11
    return control_digit == int(nip[9]) if control_digit < 10 else False

def validate_regon(regon: str) -> bool:
    """Validate REGON number."""
    if len(regon) not in [9, 14] or not regon.isdigit():
        return False

    weights = [8, 9, 2, 3, 4, 5, 6, 7] if len(regon) == 9 else [2, 4, 8, 5, 0, 9, 7, 3, 6, 1, 2, 4, 8]
    control_sum = sum(int(regon[i]) * weights[i] for i in range(len(weights)))
    control_digit = control_sum % 11
    return control_digit == int(regon[len(weights)])

def validate_password(password):
    """Validate password strength."""
    if len(password) < 8:
        return False, "Hasło jest za krótkie."
    if not re.search(r'[a-z]', password):
        return False, "Hasło musi zawierać małe litery."
    if not re.search(r'[A-Z]', password):
        return False, "Hasło musi zawierać wielkie litery."
    if not re.search(r'[0-9]', password):
        return False, "Hasło musi zawierać cyfry."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Hasło musi zawierać znaki specjalne."
    return True, "Hasło jest silne."

# Password Management
def generate_password(length=12):
    """Generate strong password."""
    if length < 8:
        raise ValueError("Hasło musi mieć przynajmniej 8 znaków.")
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(choice(characters) for _ in range(length))

# User Management
def print_users(users: dict) -> None:
    """Display a list of users, sorted by user_id."""
    print("\nLista użytkowników:")
    if not users["users"]:
        print("Brak użytkowników.")
        return

    sorted_users = sorted(users["users"], key=lambda u: int(u.get("user_id", 0) or 0))

    for u in sorted_users:
        user_id = u.get("user_id", "Nie podano")
        name = u.get("name", "Nie podano")
        pesel = u.get("pesel", "Nie podano")
        nip = u.get("nip", "Nie podano")
        regon = u.get("regon", "Nie podano")
        print(f"ID: {user_id}, Imię i nazwisko: {name}, PESEL: {pesel}, NIP: {nip}, REGON: {regon}")

def is_user_id_available(users: dict, user_id: str) -> bool:
    """Check if user_id is available."""
    return user_id not in {u.get("user_id") for u in users["users"]}

def add_user(user_data: dict) -> None:
    """Add a new user to the users.json file after checking user_id uniqueness."""
    users = load_users()

    if not is_user_id_available(users, user_data["user_id"]):
        print(f"\nBłąd: ID '{user_data['user_id']}' już istnieje. Wybierz inne ID.")
        return

    users["users"].append(user_data)
    save_users(users)
    print("\nUżytkownik został dodany.")

def remove_user(user_id: str) -> None:
    """Remove user by user_id."""
    users = load_users()
    updated_users = [u for u in users["users"] if u.get("user_id") != user_id]
    if len(updated_users) == len(users["users"]):
        print("\nNie znaleziono użytkownika o podanym ID.")
    else:
        users["users"] = updated_users
        save_users(users)
        print("\nUżytkownik został usunięty.")

def edit_user(user_id: str, updated_data: dict) -> None:
    """Edit existing user data."""
    users = load_users()
    user = next((u for u in users["users"] if u.get("user_id") == user_id), None)

    if not user:
        print("\nNie znaleziono użytkownika o podanym ID.")
        return

    new_user_id = updated_data.get("user_id")
    if new_user_id and new_user_id != user_id and not is_user_id_available(users, new_user_id):
        print(f"\nBłąd: ID '{new_user_id}' już istnieje. Wybierz inne ID.")
        return

    user.update(updated_data)
    save_users(users)
    print("\nDane użytkownika zostały zaktualizowane.")

def registration() -> dict:
    """Register a new user."""
    name = ""
    while not name:
        name = input("Nowe imię i nazwisko: ")
        if name != None:
            print("To pole musi zostać wypełnione.")

    pesel = None
    while pesel is None or (pesel and not validate_pesel(pesel)):
        pesel = input("Podaj PESEL (opcjonalne): ")
        if pesel and not validate_pesel(pesel):
            print("Błędny PESEL. Spróbuj ponownie.")

    nip = None
    while nip is None or (nip and not validate_nip(nip)):
        nip = input("Podaj NIP (opcjonalne): ")
        if nip and not validate_nip(nip):
            print("Błędny NIP. Spróbuj ponownie.")

    regon = None
    while regon is None or (regon and not validate_regon(regon)):
        regon = input("Podaj REGON (opcjonalne): ")
        if regon and not validate_regon(regon):
            print("Błędny REGON. Spróbuj ponownie.")

    return {
        "name": name,
        "pesel": pesel,
        "nip": nip,
        "regon": regon
    }

def main() -> None:
    """Program main interface"""
    users = load_users()
    while True:
        try:
            print("\nAby kontynuować wybierz jedną z poniższych opcji:")
            print("1. Wyświetl listę użytkowników")
            print("2. Dodaj użytkownika")
            print("3. Usuń użytkownika")
            print("4. Modyfikuj użytkownika")
            print("5. Zapisz i wyjdź")
            option = input("Wybór: ")

            if option == "1":
                print_users(users)
            elif option == "2":
                user_id_int = int(input(("Podaj ID użytkownika: ")))
                user_id = str(user_id_int)
                user_data = registration()
                user_data["user_id"] = user_id
                add_user(user_data)
                users = load_users()
            elif option == "3":
                user_id = str(input("Podaj ID użytkownika do usunięcia: "))
                remove_user(user_id)
                users = load_users()
            elif option == "4":
                user_id = str(input("Podaj ID użytkownika do modyfikacji: "))
                print("Podaj nowe dane użytkownika: ")
                updated_data = registration()
                updated_data = {k: v for k, v in updated_data.items() if v is not None}
                edit_user(user_id, updated_data)
                users = load_users()
            elif option == "5":
                save_users(users)
                print(f"\nZapisano dane użytkowników do pliku {USER_DATA}. Do zobaczenia!")
                break
            else:
                print("Nieprawidłowy wybór. Wybierz liczbę z listy.")
        except ValueError:
            print(f"\nNieprawidłowe dane wejściowe. Wybierz liczbę z listy.")

# Uruchomienie programu
if __name__ == "__main__":
    main()