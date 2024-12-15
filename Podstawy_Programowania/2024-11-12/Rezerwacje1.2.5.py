'''
### Zaimplementowanie biblioteki CSV, globalnego filename
'''
### Import bibliotelo
import csv

# Globalna zmienna `n`, która umożliwia zmianę ilości miejsc listy.
n = 10
### Globalne filename do łatwiejszego określania gdzie jest plik z tabelą.
filename="kino.csv"

### Ad. 9. 1/2 Funkcja sprawdzająca pojedyńcze liczby wprowadzane przez użytkownika.
def value_check(action, n): #action to informacja do użytkownika co zamieża zrobić z miejscem np. dla usuwania - "usunięcia"
    try:
        seat_number = int(input(f"Podaj numer miejsca do {action} (1-{n}): "))
    except ValueError:
        print("Numer miejsca musi być liczbą całkowitą.")
        return None

    if seat_number < 1 or seat_number > n:
        print(f"Nieprawidłowy numer miejsca. Wybierz numer od 1 do {n}.")
        return None

    return int(seat_number - 1) 

# Funkcja sprawdzająca liczby wymienione przez użytkownika. 
def which_seat(action):
    seat_input = input(f"Podaj numery miejsc, które chcesz {action} (oddzielone przecinkami np: 1,2,3): ")
    try:
        return [int(num.strip()) for num in seat_input.split(",")]
    except ValueError:
        print("Niepoprawny format danych. Upewnij się, że podałeś liczby oddzielone przecinkami.")
        return None

# Funkcja wyświetlająca aktualny stan rezerwacji
def print_seats(seats):
    print("Aktualne rezerwacje:")
    for i, seat in enumerate(seats, start=1):
            print(f"Miejsce {i}: {seat}")

# Funkcja dodająca rezerwację
def add_reservation(seats):
    n = len(seats) 
    
    index = value_check("dodać", n)   
    if index is None:
        return

    if seats[index] is None:
        name = str(input("Podaj swoje imię: "))
        seats[index] = name
        print(f"Rezerwacja miejsca numer {index +1} dla {name} została dokonana.")
    else:
        print(f"Miejsce numer {index +1} jest już zajęte przez {seats[index]}.")

# Funkcja usuwająca rezerwację
def remove_reservation(seats):
    n = len(seats) 
    
    index = value_check("usunąć", n)   
    if index is None:
        return

    if seats[index] is not None:
        try:
            option = int(input(f"Czy chcesz zmodyfikować rezerwację miejsca numer {index + 1} osoby {seats[index]}?\n1 - Tak, 2 - Nie: "))
            if option == 1:
                print(f"Rezerwacja miejsca numer {index + 1} dla {seats[index]} została usunięta.")
                seats[index] = None
            elif option == 2:
                print("Usuwanie rejestracji zostało anulowane.")
            else:
                print("Nieprawidłowy wybór. Wybierz 1 lub 2.")
        except ValueError:
            print("Nieprawidłowe dane wejściowe. Wybierz 1 lub 2.")
    else:
        print(f"Miejsce numer {index +1} jest już wolne.")

# Funkcja modyfikująca rezerwację
def mod_reservation(seats):
    n = len(seats) 
    
    index = value_check("modyfikacji", n)   
    if index is None:
        return

    if seats[index] is not None:
        try:
            option = int(input(f"Czy chcesz zmodyfikować rezerwację miejsca numer {index + 1} osoby {seats[index]}?\n1 - Tak, 2 - Nie: "))
            if option == 1:
                name = input("Podaj nowe imię: ")
                seats[index] = name
                print(f"Rezerwacja miejsca numer {index + 1} została zmodyfikowana. Nowa osoba: {name}.")
            elif option == 2:
                print("Modyfikacja została anulowana.")
            else:
                print("Nieprawidłowy wybór. Wybierz 1 lub 2.")
        except ValueError:
            print("Nieprawidłowe dane wejściowe. Wybierz 1 lub 2.")
    else:
        print(f"Miejsce numer {index + 1} jest wolne i nie można go modyfikować.")

# Funkcja sprawdza dostępnoćś miejsc i czy są już zajęte 
def check_availability(seats):
    """
    Sprawdza status wybranych miejsc (wolne lub zajęte) i określa, ile miejsc jest wolnych.
    """
    seat = which_seat("sprawdzić")
    if seat is None:
        return
    
    free_seat = 0  # Licznik wolnych miejsc
    
    print("Sprawdzanie miejsc:")
    for i in seat:
        if 1 <= i <= len(seats):  # Sprawdzamy, czy miejsce mieści się w zakresie
            if seats[i - 1] is None:
                print(f"Miejsce {i}: Wolne")
                free_seat += 1
            else:
                print(f"Miejsce {i}: Zajęte przez {seats[i - 1]}")
        else:
            print(f"Miejsce {i} nie istnieje. Podaj poprawny numer.")
    
    print(f"Łączna liczba wolnych miejsc w sprawdzonym zakresie: {free_seat}")


# Funkcja dodająca rezerwację wielu miejsc naraz.
def add_multiple_reservations(seats):
    seat = which_seat("zarezerwować")
    if seat is None:
        return
    
    name = input("Podaj imię osoby rezerwującej: ")
    
    print("Rezerwacja miejsc:")
    for i in seat:
        if 1 <= i <= len(seats):  # Sprawdzamy, czy miejsce mieści się w zakresie
            if seats[i - 1] is None:  # Indeksy w liście zaczynają się od 0
                seats[i - 1] = name
                print(f"Miejsce {i} zostało zarezerwowane dla {name}.")
            else:
                print(f"Miejsce {i} jest już zajęte przez {seats[i - 1]}.")
        else:
            print(f"Miejsce {i} nie istnieje. Podaj poprawny numer.")

# Usuwanie wielu rezerwacji dla konkretnej osoby
def cancel_all_reservations(seats):
    name = input("Podaj imię osoby, której rezerwacje chcesz usunąć: ")
    
    removed = 0  # Licznik usuniętych rezerwacji
    
    for i in range(len(seats)):
        if seats[i] == name:  # Sprawdzamy, czy miejsce jest zarezerwowane przez podaną osobę
            seats[i] = None
            removed += 1
    
    if removed > 0:
        print(f"Usunięto {removed} rezerwacji dla {name}.")
    else:
        print(f"Nie znaleziono żadnych rezerwacji dla {name}.")

# Funkcja ładująca rezerwacje z pliku

def load_seats_from_file():
    global n, filename
    seats = [None] * n  # Tworzymy listę o długości n z pustymi miejscami
    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # Pomijamy nagłówek (jeśli jest)
            for row in reader:
                seat_number = int(row[0])  # Numer miejsca
                seat = row[1] if row[1] != "Brak" else None
                if 1 <= seat_number <= n:
                    seats[seat_number - 1] = seat
        print(f"Rezerwacje wczytane z pliku {filename}.")
    except FileNotFoundError:
        print(f"Plik {filename} nie istnieje. Tworzona jest nowa lista.")
    except Exception as e:
        print(f"Wystąpił błąd podczas odczytu pliku: {e}")
    return seats

# Funkcja zapisująca rezerwacje do pliku
def save_seats_to_file(seats):
    global n, filename
    with open(filename, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        # Nagłówek
        writer.writerow(["Miejsce", "Rezerwacja"])
        # Dane miejsc od 1 do n
        for i in range(1, n + 1):
            seat = seats[i - 1] if i - 1 < len(seats) else None
            writer.writerow([i, seat if seat is not None else "Brak"])

# Funkcja główna
def main():
    print("Witaj w programie służącym do zapisu rezerwacji miejsc w kinie.")
    seats = load_seats_from_file() #Fragment kodu zmieniony aby program pobrał dane z plik.

    while True:
        save_seats_to_file(seats) # Fragment kodu dodany celem zapisu listy do pliku.
        try:
            option = int(input(
                "\nAby kontynuować wybierz jedną z poniższych opcji:\n"
                "1. Wyświetl rezerwacje\n"
                "2. Dodaj rezerwację\n"
                "3. Usuń rezerwację\n"
                "4. Modyfikuj rezerwację\n"
                "5. Zapisz i wyjdź\n"
                "6. Wyświetl dostępność miejsc\n"
                "7. Dodaj rezerwacje na kilka miejsc\n"
                "8. Usuń wszystkie rezerwacje dla...\n"
                "Wybór: "
            ))
            if option == 1:
                print_seats(seats)
            elif option == 2:
                add_reservation(seats)
            elif option == 3:
                remove_reservation(seats)
            elif option == 4:
                mod_reservation(seats)
            elif option == 5:
                print("\nProgram zakończył działanie. Do zobaczenia!")
                print(f"\nRezerwacje zapisane do pliku {filename}.")
                break
            elif option == 6:
                check_availability(seats)
            elif option == 7:
                add_multiple_reservations(seats)
            elif option == 8:
                cancel_all_reservations(seats)             
            else:
                print("Nieprawidłowy wybór. Wybierz liczbę z listy")
        except ValueError:
            print("Nieprawidłowe dane wejściowe. Wybierz liczbę z listy.")

# Uruchomienie programu
if __name__ == "__main__":
    main()