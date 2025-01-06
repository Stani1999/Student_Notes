'''JSON via with open Function Module to load and save data in file'''

import os, json

def ensure_directory_exists(directory: str) -> None:
    """Create new directory if it doesn't exist yet."""
    try:
        os.makedirs(directory, exist_ok=True)
    except OSError as e:
        print(f"Błąd podczas tworzenia struktury katalogowej {directory}: {e}")
        
def load_json(file_path: str) -> dict:
    """Load users data from JSON file."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Plik nieznaleziony {file_path}. Tworze pusty plik z na dane.")
    except json.JSONDecodeError as e:
        print(f"Błąd podczas dekodowania: {file_path}: {e}")
    return {"users": []}

def save_json(users: dict, file_path: str) -> None:
    """Save file with user data."""
    ensure_directory_exists(os.path.dirname(file_path))
    temp_file = file_path + ".tmp"
    with open(temp_file, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4)
    os.replace(temp_file, file_path)
