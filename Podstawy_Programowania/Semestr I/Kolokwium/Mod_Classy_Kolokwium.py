import os
import json


DATA_PATH: str = os.getcwd()
USER_DATA = f"{DATA_PATH}data/phonebook.json"
print (DATA_PATH)

class Phonebook:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self._load_phonebook()

    def _ensure_directory_exists(self, directory: str) -> None:
        """Tworzy nowy katalog, jeżeli nie istnieje."""
        try:
            os.makedirs(directory, exist_ok=True)
        except OSError as e:
            print(f"Błąd podczas tworzenia struktury katalogowej {directory}: {e}")

    def _load_phonebook(self) -> dict:
        """Czytanie danych książki telefonicznej z pliku."""
        self._ensure_directory_exists(os.path.dirname(self.file_path))
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Plik nie znaleziony {self.file_path}. Tworzenie pustej książki telefonicznej.")
            return {"phonebook": []}
        except json.JSONDecodeError as e:
            print(f"Błąd podczas dekodowania JSON z pliku {self.file_path}: {e}")
            return {"phonebook": []}

    def save(self) -> None:
        """Zapisanie danych książki telefonicznej do pliku."""
        self._ensure_directory_exists(os.path.dirname(self.file_path))
        temp_file = self.file_path + ".tmp"
        with open(temp_file, "w", encoding="utf-8") as file:
            json.dump(self.data, file, indent=4)
        os.replace(temp_file, self.file_path)

    def is_number_available(self, number: str) -> bool:
        """Sprawdzanie dostępności numeru."""
        return number not in {u.get("numer") for u in self.data["phonebook"]}

    def add_entry(self, number: str, name: str) -> None:
        """Dodanie wpisu do książki telefonicznej."""
        if not PhonebookValidator.validate_phone_number(number):
            return
        if not self.is_number_available(number):
            print(f"Błąd: Numer '{number}' już istnieje. Wybierz inny numer.")
            return
        self.data["phonebook"].append({"numer": number, "name": name})
        self.save()
        print("Użytkownik został dodany.")

    def display(self) -> None:
        """Wyświetlenie zawartości książki telefonicznej."""
        print("\nLista użytkowników:")
        if not self.data["phonebook"]:
            print("\nKsiążka telefoniczna jest pusta")
            return

        sorted_by_number = sorted(self.data["phonebook"], key=lambda u: int(u.get("numer", 0) or 0))
        for user in sorted_by_number:
            number = user.get("numer", "Nie podano")
            name = user.get("name", "Nie podano")
            print(f"Numer: {number}, Imię i nazwisko: {name}")

    def remove_entry(self, number: str) -> None:
        """Usuwanie użytkownika z książki telefonicznej."""
        if not PhonebookValidator.validate_phone_number(number):
            return
        updated = [u for u in self.data["phonebook"] if u.get("numer") != number]
        if len(updated) == len(self.data["phonebook"]):
            print("Nie znaleziono użytkownika o podanym numerze.")
        else:
            self.data["phonebook"] = updated
            self.save()
            print("Użytkownik został usunięty.")

    def modify_entry(self, old_phone_number: str, new_name: str, new_phone_number: str) -> None:
        """Modyfikacja istniejącego wpisu."""
        user = next((u for u in self.data["phonebook"] if u.get("numer") == old_phone_number), None)

        if not user:
            print("\nNie znaleziono użytkownika o podanym numerze telefonu.")
            return

        if new_phone_number:
            if not PhonebookValidator.validate_phone_number(new_phone_number):
                return
            if new_phone_number != old_phone_number and not self.is_number_available(new_phone_number):
                print(f"\nBłąd: Numer '{new_phone_number}' już istnieje. Wybierz inny numer.")
                return

        if new_name:
            user["name"] = new_name
        if new_phone_number:
            user["numer"] = new_phone_number

        self.save()
        print("\nDane użytkownika zostały zaktualizowane.")


class PhonebookValidator:
    @staticmethod
    def validate_phone_number(number: str) -> bool:
        """
        Walidacja numeru telefonu:
        - Musi zawierać tylko cyfry.
        - Musi mieć długość 9 znaków.
        - Nie może zaczynać się od zera.
        """
        if not number.isdigit():
            print("Numer telefonu może zawierać tylko cyfry.")
            return False
        if len(number) != 9:
            print("Numer telefonu musi mieć dokładnie 9 cyfr.")
            return False
        if number[0] == '0':
            print("Numer telefonu nie może zaczynać się od cyfry 0.")
            return False
        return True

menu = """
\nAby kontynuować wybierz jedną z poniższych opcji:
\n1. Wyświetl książkę telefoniczną
2. Dodaj nowy numer
3. Usuń numer
4. Modyfikuj numer
5. Zapisz i wyjdź
"""

def main():
    phonebook = Phonebook(USER_DATA)

    while True:
        print(menu)
        option = input("Wybór: ")

        if option == "1":
            phonebook.display()
        elif option == "2":
            number = input("Podaj numer telefonu użytkownika: ").strip()
            name = input("Podaj imię i nazwisko użytkownika: ").strip()
            phonebook.add_entry(number, name)
        elif option == "3":
            phonebook.display()
            number = input("Podaj numer telefonu użytkownika do usunięcia: ").strip()
            phonebook.remove_entry(number)
        elif option == "4":
            phonebook.display()
            old_number = input("Podaj numer telefonu użytkownika do modyfikacji: ").strip()
            new_name = input("Podaj nowe imię i nazwisko (pozostaw puste, aby zachować istniejące): ").strip()
            new_number = input("Podaj nowy numer (pozostaw puste, aby zachować istniejący): ").strip()
            phonebook.modify_entry(old_number, new_name, new_number)
        elif option == "5":
            phonebook.save()
            print(f"Zapisano dane do pliku {USER_DATA}. Do zobaczenia!")
            break
        else:
            print("Nieprawidłowy wybór. Wybierz liczbę z listy.")


if __name__ == "__main__":
    main()
