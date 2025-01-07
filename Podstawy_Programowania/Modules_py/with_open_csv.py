'''CSV via with open Function Module to load and save data in file'''

import csv, os

def ensure_directory_exists(directory: str) -> None:
    """Create new directory if it doesn't exist yet."""
    try:
        os.makedirs(directory, exist_ok=True)
    except OSError as e:
        print(f"Błąd podczas tworzenia struktury katalogowej {directory}: {e}")

def load_csv_list(file_path: str) -> list:
    """Load data from a CSV file."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        print(f"Plik nie znaleziony {file_path}. Tworzę pusty plik CSV.")
        ensure_directory_exists(os.path.dirname(file_path))
        save_csv([], file_path)  # Tworzy pusty plik
        return []
    except csv.Error as e:
        print(f"Błąd podczas odczytu pliku CSV {file_path}: {e}")
        return []

def save_csv_list(data: list, file_path: str, fieldnames: list = None) -> None:
    """Save data to a CSV file."""
    if not data:
        print("Dane są puste, zapisano pusty plik.")
        fieldnames = fieldnames or []
    else:
        fieldnames = fieldnames or data[0].keys()

    ensure_directory_exists(os.path.dirname(file_path))
    temp_file = file_path + ".tmp"
    try:
        with open(temp_file, "w", encoding="utf-8", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        os.replace(temp_file, file_path)
    except OSError as e:
        print(f"Błąd podczas zapisu pliku CSV {file_path}: {e}")


def load_csv_dict(file_path, fieldnames):
    """Load users from a CSV file."""
    users = {"users": []}
    if not os.path.exists(file_path):
        return users

    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file, fieldnames=fieldnames)
        next(reader, None)  # Pomijaj nagłówek tylko, jeśli jest potrzebne
        users["users"] = list(reader)
    return users

def save_csv_dict(data, file_path, fieldnames):
    """Save users to a CSV file."""
    with open(file_path, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data["users"])

'''
# Przykładowe użycie modułu
if __name__ == "__main__":
    # Ścieżka do pliku CSV
    file_path = "example_data/users.csv"

    # Załaduj dane
    users = load_csv(file_path)
    print("Wczytane dane:", users)

    # Dodaj nowego użytkownika i zapisz
    users.append({"id": "1", "name": "John Doe", "email": "john.doe@example.com"})
    save_csv(users, file_path)
    print(f"Dane zapisane do pliku {file_path}.")
'''
