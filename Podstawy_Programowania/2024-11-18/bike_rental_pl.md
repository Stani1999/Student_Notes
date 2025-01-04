---

# **Dokumentacja Systemu Wypożyczalni Rowerów**
## **Wprowadzenie**
System Wypożyczalni Rowerów to program napisany w Pythonie, służący do zarządzania wypożyczaniem rowerów. Obsługuje takie funkcje jak:
- Wypożyczanie rowerów.
- Anulowanie wypożyczenia.
- Generowanie dziennych raportów wypożyczeń.
- Obliczanie kosztów wypożyczenia na podstawie czasu.

Program korzysta z plików JSON do przechowywania danych o wypożyczeniach i zapewnia, że katalogi i pliki są prawidłowo inicjowane. Zawiera także wstępne przygotowanie do wysyłania faktur e-mailowych.

---

## **Konfiguracja**
Aby skonfigurować system, zapoznaj się z [przewodnikiem instalacji i konfiguracji](../installation_and_setup_pl.md).  
Znajdziesz tam szczegółowe instrukcje dotyczące instalacji Pythona oraz tworzenia środowiska wirtualnego.

---

## **Struktura Programu**

### **1. Zarządzanie plikami i katalogami**
- **Katalog danych (`data`)**: Przechowuje pliki JSON programu.
  - `rentals.json`: Zawiera informacje o wypożyczeniach.
  - `daily_reports/`: Przechowuje dzienne raporty.

### **2. Operacje na plikach JSON**
#### **`load_json(file_path)`**
- Wczytuje dane z pliku JSON.
- Jeśli plik nie istnieje lub jest uszkodzony, zwraca pustą listę.

#### **`save_json(file_path, data)`**
- Zapisuje dane do pliku JSON w uporządkowanym formacie.

#### **`ensure_directory_exists(directory)`**
- Zapewnia istnienie wskazanego katalogu. Jeśli nie istnieje, tworzy go.

---

### **3. Funkcje Wypożyczalni**

#### **`rent_bike(customer_name, rental_duration)`**
- Rozpoczyna wypożyczenie dla klienta.
- Dodaje szczegóły wypożyczenia (imię, czas rozpoczęcia, czas trwania) do `rentals.json`.

#### **`cancel_rental(customer_name)`**
- Anuluje aktywne wypożyczenie dla podanego klienta, usuwając jego dane z `rentals.json`.

#### **`calculate_cost(rental_duration)`**
- Oblicza koszt wypożyczenia na podstawie czasu:
  - **Pierwsza godzina**: 10 zł.
  - **Dodatkowe godziny**: 5 zł/godz.

---

### **4. Funkcje Raportowania**

#### **`generate_daily_report()`**
- Generuje raport JSON z wypożyczeniami wykonanymi w bieżącym dniu.
- Zapisuje raport w katalogu `daily_reports/daily_report_<data>.json`.

#### **`send_rental_invoice_email(customer_email, rental_details)`**
- Wstępna funkcja do wysyłania faktur e-mailowych. 
- Wyświetla szczegóły faktury w konsoli.

---

## **Obsługa Programu**

### **Uruchamianie programu**
1. Zapisz kod do pliku, np. `bike_rental.py`.
2. Uruchom program:
    ```bash
    python bike_rental.py
    ```

### **Opcje w menu**
1. **Wypożycz rower**
    - Wprowadź imię klienta i czas wypożyczenia.
2. **Anuluj wypożyczenie**
    - Usuń wypożyczenie podając imię klienta.
3. **Generuj dzienny raport**
    - Wyświetla dzisiejsze wypożyczenia oraz ich koszty.
4. **Wyjdź**
    - Kończy działanie programu.

---

## **Struktura plików JSON**
### `rentals.json`
```json
[
    {
        "customer_name": "Jan Kowalski",
        "start_time": "2024-12-29T12:00:00",
        "rental_duration": 2
    },
]
```

### Przykładowy dzienny raport (`daily_report_<data>.json`)
```json
[
    {
        "customer_name": "Jan Kowalski",
        "start_time": "2024-12-29T12:00:00",
        "rental_duration": 2
    }
]
```

---

## **Zalecenia**
1. Korzystaj ze **środowiska wirtualnego** do zarządzania zależnościami.
2. Upewnij się, że katalogi (`data`, `daily_reports`) istnieją, uruchamiając program przynajmniej raz.
3. Nie edytuj ręcznie plików JSON, aby uniknąć ich uszkodzenia.
4. Podczas wprowadzania danych używaj poprawnych nazw klientów (unikaj znaków specjalnych).

---

## **Możliwe Rozszerzenia**
1. Integracja z serwerem e-mail do wysyłania faktur.
2. Dodanie interfejsu graficznego (GUI) dla lepszej obsługi użytkownika.
3. Implementacja zaawansowanego przetwarzania błędów dla nieprawidłowych danych wejściowych.

---

## **Autorzy**
- [Stani1999](https://github.com/Stani1999)

---