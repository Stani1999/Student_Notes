# **Dokumentacja Systemu Zarządzania Użytkownikami**

## **Wprowadzenie**
System Zarządzania Użytkownikami to program napisany w Pythonie, który pozwala na:
- Wyświetlanie listy użytkowników.
- Dodawanie nowych użytkowników.
- Edycję danych użytkowników.
- Usuwanie istniejących użytkowników.
- Generowanie silnych haseł.

Program opiera się na plikach JSON do przechowywania danych o użytkownikach. Obsługuje podstawową walidację danych (np. imię, PESEL, NIP, REGON) przy użyciu zewnętrznych modułów.

---

## **Konfiguracja**
Aby skonfigurować system, zapoznaj się z [przewodnikiem instalacji i konfiguracji](../../Describe/installation_and_setup_pl.md).  
Znajdziesz tam szczegółowe instrukcje dotyczące instalacji Pythona oraz tworzenia środowiska wirtualnego.

1. **Środowisko:**
   - Upewnij się, że Python 3.x jest zainstalowany.
   - Dodaj zmienną środowiskową `Modules`, wskazującą na katalog, w którym znajdują się moduły walidacyjne.
      - Linux : 
         ```bash
         export PYTHONPATH=$PYTHONPATH:/ścieżka/do/Modules_py
      - Windows : 
         ```bash
         set PYTHONPATH=%PYTHONPATH%;C:\ścieżka\do\Modules_py 
   - Dodaj zmienną środowiskową `USER_DATA_PATH`, która określa ścieżkę do pliku `users.json`.

2. **Struktura katalogów:**
   - **`data/users.json`**: Plik JSON przechowujący dane o użytkownikach.

3. **Moduły zewnętrzne:**
   - `validate`: Moduł do walidacji danych (np. PESEL, NIP, REGON).
   - `with_JSON`: Moduł do wczytywania i zapisywania danych JSON.

---

## **Struktura Programu**

### **1. Zarządzanie danymi użytkowników**
#### **`USER_DATA`**
- Ścieżka do pliku `users.json`. Domyślnie wskazuje na `data/users.json`, ale można ją zmienić za pomocą zmiennej środowiskowej `USER_DATA_PATH`.

### **2. Operacje na plikach JSON**
#### **`wo.load_json(file_path)`**
- Wczytuje dane JSON z pliku.
- Jeśli plik nie istnieje, zwraca pustą strukturę danych.

#### **`wo.save_json(file_path, data)`**
- Zapisuje dane do pliku JSON w uporządkowanym formacie.

---

### **3. Funkcje Zarządzania Użytkownikami**

#### **`print_user(users, user_id, action)`**
- Wyświetla dane użytkownika po podaniu jego `user_id`.
- Jeśli w słowniku nie ma podanego `user_id`, wyświetla komunikat: "Nie znaleziono użytkownika o ID {user_id}"
- Posiada dwie informacje na swoim wyjściu
   1. typu bool, aby dowiedzić się czy użytkownik został znaleziony.
   2. typu str, zawiera ona informacje o użytkowniku, lub komunikat o braku id w słowniku.

#### **`print_users(users)`**
- Wyświetla listę użytkowników posortowaną według `user_id`.
- Jeśli lista użytkowników jest pusta, wyświetla komunikat: "Brak użytkowników."

#### **`is_user_id_available(users, user_id)`**
- Sprawdza, czy `user_id` jest dostępne.
- Zwraca wartość `True`, jeśli ID jest wolne.

#### **`add_user(user_data)`**
- Dodaje nowego użytkownika do pliku JSON.
- Sprawdza, czy `user_id` jest unikalne. W przeciwnym razie wyświetla błąd.

#### **`remove_user(user_id)`**
- Usuwa użytkownika na podstawie jego `user_id`.
- Jeśli użytkownik o podanym ID nie istnieje, wyświetla komunikat: "Nie znaleziono użytkownika o podanym ID."

#### **`edit_user(user_id, updated_data)`**
- Edytuje dane istniejącego użytkownika.
- Sprawdza, czy nowy `user_id` (jeśli podany) jest unikalny.

#### **`registration()`**
- Rejestruje nowego użytkownika, prosząc użytkownika o podanie danych:
  - **Imię i nazwisko:** Wymagane. Walidowane przez moduł `validates`.
  - **PESEL:** Opcjonalne. Walidowane przez moduł `validates`.
  - **NIP:** Opcjonalne. Walidowane przez moduł `validates`.
  - **REGON:** Opcjonalne. Walidowane przez moduł `validates`.
- Zwraca słownik z wprowadzonymi danymi.

---

### **4. Zarządzanie Hasłami**

#### **`generate_password(length=12)`**
- Generuje losowe, silne hasło o określonej długości (minimum 8 znaków).
- Hasło zawiera litery, cyfry i znaki specjalne.

---

## **Obsługa Programu**

### **Uruchamianie programu**
1. Zapisz kod do pliku, np. `user_management.py`.
2. Uruchom program:
    ```bash
    python user_management.py
    ```

### **Opcje w menu**
1. **Wyświetl listę użytkowników**  
   - Wyświetla wszystkich użytkowników z pliku `users.json`.

2. **Dodaj użytkownika**  
   - Prosi o podanie ID użytkownika oraz danych osobowych. Dodaje użytkownika do listy.

3. **Usuń użytkownika**  
   - Prosi o podanie ID użytkownika do usunięcia. Usuwa użytkownika z listy.

4. **Modyfikuj użytkownika**  
   - Prosi o podanie ID użytkownika, którego dane mają zostać zmodyfikowane. Aktualizuje dane w pliku JSON.

5. **Zapisz i wyjdź**  
   - Zapisuje zmiany i kończy działanie programu.

---

## **Struktura pliku JSON**
### **`users.json`**
```json
{
    "users": [
        {
            "user_id": "1",
            "name": "Jan Kowalski",
            "pesel": "90010112345",
            "nip": "1234563218",
            "regon": "876543210"
        }
    ]
}
```

---

## **Zalecenia**
1. Upewnij się, że moduły `validate` i `with_JSON` znajdują się w poprawnym katalogu.
2. Nie edytuj ręcznie pliku `users.json`, aby uniknąć uszkodzenia danych.
3. Regularnie wykonuj kopię zapasową pliku `users.json`.

---

## **Możliwe Rozszerzenia**
1. Dodanie walidacji w czasie rzeczywistym podczas wprowadzania danych (np. dynamiczne podpowiedzi).
2. Rozszerzenie programu o funkcję logowania użytkowników na podstawie haseł.
3. Integracja z bazą danych zamiast pliku JSON.
4. Dodanie graficznego interfejsu użytkownika (GUI).

---

## **Autorzy**
- [Stani1999](https://github.com/Stani1999)