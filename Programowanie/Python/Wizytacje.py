import os, csv, re

'''Headers declaration'''
FIELDNAMES_USER = ["user_id","name","phone"]
FIELDNAMES_VISI = ["visi_id", "data", "time", "user_id"]

'''File settings (path declaration + max reservations per day)'''
USER_DATA = "data/visi_data/user_data.txt"
VISI_DATA = "data/visi_data/visi_data.txt"
MAX_RESERVATIONS_PER_DAY = 8

#Validations section
def val_phone(phone: str) -> bool:
    """Validate phone number."""
    if len(phone) != 9 or not phone.isdigit():
        return False

    return True

def val_date(date_str: str) -> tuple[bool, str]:
    """Validate date in 'YYYY-MM-DD' format and provide feedback."""
    try:
        if re.match(r"^\d{4}-\d{2}-\d{2}$", date_str):
            year, month, day = map(int, date_str.split('-'))
            if 1 <= month <= 12 and 1 <= day <= 31:
                return True, "Poprawna data."
        return False, "Błąd: Data powinna być w formacie 'YYYY-MM-DD'."
    except ValueError:
        return False, "Błąd: Niepoprawna wartość daty."


def val_time(time_str: str) -> tuple[bool, str]:
    """Validate time in 'HH:MM' format and provide feedback."""
    try:
        time_parts = time_str.split(":")
        if len(time_parts) == 2:
            hour, minute = map(int, time_parts)
            if 0 <= hour <= 23 and 0 <= minute <= 59:
                return True, "Poprawna godzina."
        return False, "Błąd: Godzina powinna być w formacie 'HH:MM'."
    except ValueError:
        return False, "Błąd: Niepoprawna wartość godziny."


def val_name(name: str) -> tuple[bool, str]:
    """Validate user name."""
    if re.search(r'[0-9]', name):
        return False, "Imie nie może zawierać cyfry."
    if re.search(r'[!@#$%^&*(),?":{}|<>]', name):
        return False, "Imie nie może zawierać znaków specjalnych."
    if not re.search(r'[A-Z]', name):
        return False, "Imie musi zawierać wielkie litery."
    if not re.search(r'[a-z]', name):
        return False, "Imie musi zawierać małe litery."
    return True, f"Wprowadzasz dane dla {name}:"

def ensure_directory_exists(directory: str) -> None:
    """Create new directory if it doesn't exist yet."""
    try:
        os.makedirs(directory, exist_ok=True)
    except OSError as e:
        print(f"Error creating directory structure {directory}: {e}")

def load(file_path, fieldnames):
    """Load data from a CSV file."""
    data = {"data": []}
    if not os.path.exists(file_path):
        return data

    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file, fieldnames=fieldnames)
        next(reader, None)  # Skip header if necessary
        data["data"] = list(reader)
    return data

def save(data, file_path, fieldnames):
    """Save data to a file."""
    ensure_directory_exists(os.path.dirname(file_path))
    with open(file_path, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data["data"])

# Data Management
def print_user(users: dict, user_id: str) -> str:
    """Display a user, by user_id. and check if they are in dict"""
    for user in users.get("users", []):
        if user.get("user_id") == user_id: 
            return "Użtkownik zapisany na wizytę to : Imię i nazwisko: {user.get('name') or 'Nie podano'}, \nNr. Telefonu: {user.get('phone') or 'Nie podano'}"
        

    return "Nie znaleziono użytkownika o ID {user_id}"
def print_data(data):
    """Display a list of data, sorted by id."""
    print("\nLista danych:")
    if not data.get("data"):
        print("Brak rekordów.")
        return

    sorted_by_id = sorted(data["data"], key=lambda u: int(u.get("user_id", 0) or 0))

    for u in sorted_by_id:
        id = u.get("user_id") or "Nie podano"
        name = u.get("name") or "Nie podano"
        phone = u.get("phone") or "Nie podano"
        print(f"ID: {id}, Imię i nazwisko: {name}, Telefon: {phone}")

def print_visi(data):
    """Display a list of data, sorted by id."""
    print("\nLista danych:")
    if not data.get("data"):
        print("Brak rekordów.")
        return

    sorted_by_id = sorted(data["data"], key=lambda u: int(u.get("visi_id", 0) or 0))

    for u in sorted_by_id:
        id = u.get("visi_id") or "Nie podano"
        data = u.get("data") or "Nie podano"
        time = u.get("time") or "Nie podano"
        user_id = u.get("user_id") or "Nie podano"
        print(f"Rezerwacja o ID: {id} jest planowana na dzień {data} o godzinie {time}, dotyczy użytkownika z ID: {user_id}")

def is_id_available(data, id):
    """Check if id is available."""
    return id not in {u.get("user_id") for u in data["data"]}

def visi_is_id_available(data, id):
    """Check if id is available."""
    return id not in {u.get("visi_id") for u in data["data"]}

def add_data(record_data, file_path, fieldnames):
    """Add a new record to a specified CSV file after checking id uniqueness."""
    data = load(file_path, fieldnames)

    data["data"].append(record_data)
    save(data, file_path, fieldnames)
    print("\nRekord został dodany.")

def remove_data(id, file_path, fieldnames):
    """Remove record by id from a specified file."""
    data = load(file_path, fieldnames)
    updated_data = [u for u in data["data"] if u.get("user_id") != id]
    if len(updated_data) == len(data["data"]):
        print("\nNie znaleziono rekordu o podanym ID.")
    else:
        data["data"] = updated_data
        save(data, file_path, fieldnames)
        print("\nRekord został usunięty.")

def edit_data(id, updated_data, file_path, fieldnames):
    """Edit existing record data in a specified file."""
    data = load(file_path, fieldnames)
    record = next((u for u in data["data"] if u.get("user_id") == id), None)

    if not record:
        print("\nNie znaleziono rekordu o podanym ID.")
        return

    new_id = updated_data.get("user_id")
    if new_id and new_id != id and not is_id_available(data, new_id):
        print(f"\nBłąd: ID '{new_id}' już istnieje. Wybierz inne ID.")
        return

    record.update(updated_data)
    save(data, file_path, fieldnames)
    print("\nDane rekordu zostały zaktualizowane.")

def registration(user_id) -> dict:
    """Register a new user."""
    name = None
    while name is None or (name and not val_name(name)[0]):
        name = str(input("Podaj imię i nazwisko: "))
        '''Info from function'''
        if name == "":
            print(val_name(name)[1])
            name = None
        else:
            print(val_name(name)[1])
            
    phone = None
    while phone is None or (phone and not val_phone(phone)):
        phone = input("Podaj numer telefonu (opcjonalne): ")
        if phone and not val_phone(phone):
            print("Błędny numer telefonu. Spróbuj ponownie.")

    return {
        "user_id": user_id,
        "name": name,
        "phone": phone or ""
    }

def visit_reservation(visi_id, user_id, user_data, visi_data) -> dict:
    """Reservation visit."""
    if is_id_available(user_data, user_id) is False:
        date = None
        while date is None or (date and not val_date(date)[0]):
            date = input("Podaj datę (YYYY-MM-DD): ")
            if date == "":
                print(val_date(date)[1])
                date = None
            else:
                print(val_date(date)[1])

        # Sprawdzenie limitu rezerwacji na dzień
        if count_reservations_by_date(date, visi_data) >= MAX_RESERVATIONS_PER_DAY:
            print(f"\nLimit rezerwacji ({MAX_RESERVATIONS_PER_DAY}) na dzień {date} został osiągnięty.")
            return None

        time = None
        while time is None or (time and not val_time(time)[0]):
            time = input("Podaj godzinę (HH:MM): ")
            if time == "":
                print(val_time(time)[1])
                time = None
            else:
                print(val_time(time)[1])

        return {
            "visi_id": visi_id,
            "date": date, 
            "time": time,
            "user_id": user_id
        }
    else:
        print(f"Nie można dokonać rezerwacji, ponieważ użytkownik o ID {user_id} nie istnieje.")


def count_reservations_by_date(date: str, data: dict) -> int:
    """Count the number of reservations for a given date."""
    return sum(1 for record in data["data"] if record.get("date") == date)


def main():
    """Program main interface"""
    while True:
        visi = load(VISI_DATA, FIELDNAMES_VISI)
        data = load(USER_DATA, FIELDNAMES_USER)
        try:
            print("\nAby kontynuować wybierz jedną z poniższych opcji:")
            print("1. Wyświetl listę użytkowników")
            print("2. Dodaj użytkownika")
            print("3. Usuń użytkownika")
            print("4. Modyfikuj użytkownika")
            print("5. Wyświetl listę rezerwacji")
            print("6. Dodaj rezerwacje")
            print("7. Usuń rezerwacje")
            print("8. Modyfikuj rezerwacje")
            print("9. Zapisz i wyjdź")
            option = input("Wybór: ")

            if option == "1":
                print_data(data)
            elif option == "2":
                user_id = str(int(input("Podaj ID nowego użytkownika: ")))
                if is_id_available(data, user_id) is False:
                    print(f"{user_id}, jest już zajęte,\nUżyj opcji 1. Wyświetl listę użytkowników i użyj innego ")
                else: 
                    user_data = registration(user_id)
                    add_data(user_data, USER_DATA, FIELDNAMES_USER)
                    print_user(data, user_id)[1]
            elif option == "3":
                user_id = str(int(input("Podaj ID użytkownika do usunięcia: ")))
                if is_id_available(data, user_id) is False:
                    remove_data(user_id, USER_DATA, FIELDNAMES_USER)
                else:
                    print(f"Brak użytkownika z ID : {user_id}.")
            elif option == "4":
                user_id = str(int(input("Podaj ID użytkownika do modyfikacji: ")))
                if is_id_available(data, user_id) is False:
                    print_user(data, user_id)[1]
                    print("Podaj nowe dane użytkownika: ")
                    updated_data = registration(user_id)
                    updated_data = {k: v for k, v in updated_data.items() if v}
                    edit_data(user_id, updated_data, USER_DATA, FIELDNAMES_USER)
                else:
                    print(f"Nie ma użytkownika o ID : {user_id},\nUżyj opcji 2. Dodaj użytkownika")
            elif option == "5":
                print_visi(visi)            
            elif option == "6":
                visi_id = str(int(input("Podaj ID nowej rezerwacji: ")))
                user_id = str(int(input("Podaj ID użytkownika do rezerwacji: ")))
                print_user(data, user_id)[1]
                if not visi_is_id_available(visi, visi_id):  # Sprawdzanie ID rezerwacji
                    print(f"\nID rezerwacji {visi_id} jest już zajęte.")
                    continue

                if is_id_available(data, user_id):  # Sprawdzanie ID użytkownika
                    print(f"\nNie można dokonać rezerwacji, ponieważ użytkownik o ID {user_id} nie istnieje.")
                    continue
                visi_data = visit_reservation(visi_id, user_id, data)
                if visi_data:
                    add_data(visi_data, VISI_DATA, FIELDNAMES_VISI)
                else:
                    print("Nie udało się dodać rezerwacji. Spróbuj ponownie.")
            elif option == "7":
                visi_id = str(int(input("Podaj ID rezerwacji do usunięcia: ")))
                if visi_is_id_available(visi, visi_id) is False:
                    remove_data(visi_id, VISI_DATA, FIELDNAMES_VISI)
                else:
                    print(f"Brak rezerwacji z ID : {visi_id}.")            
            elif option == "8":
                visi_id = str(int(input("Podaj ID rezerwacji do modyfikacji: ")))
                if visi_is_id_available(visi, visi_id) is False:
                    print("Podaj nowe dane rezerwacji: ")
                    user_id = str(int(input("Podaj ID użytkownika do rezerwacji")))
                    print_user(data, user_id)
                    updated_data = visit_reservation(visi_id, user_id, data)
                    updated_data = {k: v for k, v in updated_data.items() if v}
                    edit_data(visi_id, updated_data, VISI_DATA, FIELDNAMES_VISI)
                else:
                    print(f"Nie ma wizyty o ID : {visi_id},\nUżyj opcji 5. Dodaj rezerwacje")
            elif option == "9":
                print(f"\nDane użytkowników zapisano w pliku {USER_DATA}. Do zobaczenia!")
                break
            else:
                print("Nieprawidłowy wybór. Wybierz liczbę z listy:")
        except ValueError:
            print("\nNieprawidłowe dane wejściowe. Wybierz liczbę z listy:")

# Run the program
if __name__ == "__main__":
    main()