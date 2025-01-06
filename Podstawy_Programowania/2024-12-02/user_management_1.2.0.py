import sys, os, string
from secrets import choice

# Import modules
sys.path.append (os.getenv("Modules","Podstawy_Programowania"))
'''Append to python path to dir with modules'''
from Modules_py import validate as val
'''Import modul with validation nip, pesel ect.'''
from Modules_py import with_JSON as wJ
'''Import modul with JSON load and save'''

# Constants
USER_DATA = os.getenv("USER_DATA_PATH", "data/users.json")

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
    if not users.get("users"):
        print("Brak użytkowników.")
        return

    sorted_users = sorted(users["users"], key=lambda u: int(u.get("user_id", 0) or 0))

    for u in sorted_users:
        user_id = u.get("user_id") or "Nie podano"
        name = u.get("name") or "Nie podano"
        pesel = u.get("pesel") or "Nie podano"
        nip = u.get("nip") or "Nie podano"
        regon = u.get("regon") or "Nie podano"
        print(f"ID: {user_id}, Imię i nazwisko: {name}, PESEL: {pesel}, NIP: {nip}, REGON: {regon}")

def is_user_id_available(users: dict, user_id: str) -> bool:
    """Check if user_id is available."""
    return user_id not in {u.get("user_id") for u in users["users"]}

def add_user(user_data: dict) -> None:
    """Add a new user to the users.json file after checking user_id uniqueness."""
    users = wJ.load(USER_DATA)

    if not is_user_id_available(users, user_data["user_id"]):
        print(f"\nBłąd: ID '{user_data['user_id']}' już istnieje. Wybierz inne ID.")
        return

    users["users"].append(user_data)
    wJ.save(users, USER_DATA)
    print("\nUżytkownik został dodany.")

def remove_user(user_id: str) -> None:
    """Remove user by user_id."""
    users = wJ.load(USER_DATA)
    updated_users = [u for u in users["users"] if u.get("user_id") != user_id]
    if len(updated_users) == len(users["users"]):
        print("\nNie znaleziono użytkownika o podanym ID.")
    else:
        users["users"] = updated_users
        wJ.save(users, USER_DATA)
        print("\nUżytkownik został usunięty.")

def edit_user(user_id: str, updated_data: dict) -> None:
    """Edit existing user data."""
    users = wJ.load(USER_DATA)
    user = next((u for u in users["users"] if u.get("user_id") == user_id), None)

    if not user:
        print("\nNie znaleziono użytkownika o podanym ID.")
        return

    new_user_id = updated_data.get("user_id")
    if new_user_id and new_user_id != user_id and not is_user_id_available(users, new_user_id):
        print(f"\nBłąd: ID '{new_user_id}' już istnieje. Wybierz inne ID.")
        return

    user.update(updated_data)
    wJ.save(users, USER_DATA)
    print("\nDane użytkownika zostały zaktualizowane.")

def registration() -> dict:
    """Register a new user."""
    name = None
    while name is None or (name and not val.name(name)[0]):
        name = str(input("Nowe imię i nazwisko: "))
        '''Info from function'''
        print(val.name(name)[1])
            
    pesel = None
    while pesel is None or (pesel and not val.pesel(pesel)):
        pesel = input("Podaj PESEL (opcjonalne): ")
        if pesel and not val.pesel(pesel):
            print("Błędny PESEL. Spróbuj ponownie.")

    nip = None
    while nip is None or (nip and not val.nip(nip)):
        nip = input("Podaj NIP (opcjonalne): ")
        if nip and not val.nip(nip):
            print("Błędny NIP. Spróbuj ponownie.")

    regon = None
    while regon is None or (regon and not val.regon(regon)):
        regon = input("Podaj REGON (opcjonalne): ")
        if regon and not val.regon(regon):
            print("Błędny REGON. Spróbuj ponownie.")

    return {
        "name": name,
        "pesel": pesel,
        "nip": nip,
        "regon": regon
    }

def main() -> None:
    """Program main interface"""
    while True:
        users = wJ.load(USER_DATA)
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
                user_id = str(int(input(("Podaj ID użytkownika: "))))
                user_data = registration()
                user_data["user_id"] = user_id
                add_user(user_data)
            elif option == "3":
                user_id = str(int(input("Podaj ID użytkownika do usunięcia: ")))
                remove_user(user_id)
            elif option == "4":
                user_id = str(int(input("Podaj ID użytkownika do modyfikacji: ")))
                print("Podaj nowe dane użytkownika: ")
                updated_data = registration()
                updated_data = {k: v for k, v in updated_data.items() if v is not None}
                edit_user(user_id, updated_data)
            elif option == "5":
                wJ.save(users, USER_DATA)
                print(f"\nZapisano dane użytkowników do pliku {USER_DATA}. Do zobaczenia!")
                break
            else:
                print("Nieprawidłowy wybór. Wybierz liczbę z listy:")
        except ValueError:
            print(f"\nNieprawidłowe dane wejściowe. Wybierz liczbę z listy:")

# Uruchomienie programu
if __name__ == "__main__":
    main()