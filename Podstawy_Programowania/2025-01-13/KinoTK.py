import re, os, json
import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter.ttk import Treeview

# Ścieżka domyślna do katalogu danych
DATA_DIR = os.getenv("DATA_DIR", "data")
MOVIES_FILE = "movies.json"
CUSTOMER_FILE = "customers.json"

def ensure_directory_exists(directory: str) -> None:
    """Tworzy nowy katalog, jeżeli nie istnieje."""
    try:
        os.makedirs(directory, exist_ok=True)
    except OSError as e:
        print(f"Błąd podczas tworzenia struktury katalogowej {directory}: {e}")

class Movie:
    def __init__(self, title, duration, showtimes):
        self.title = title
        self.duration = duration
        self.showtimes = showtimes

    def add_showtime(self, time):
        if time not in self.showtimes:
            self.showtimes.append(time)
            print(f"Dodano godzinę seansu: {time} dla filmu {self.title}.")
        else:
            print(f"Godzina {time} już istnieje dla filmu {self.title}.")

    def remove_showtime(self, time):
        if time in self.showtimes:
            self.showtimes.remove(time)
            print(f"Usunięto godzinę seansu: {time} dla filmu {self.title}.")
        else:
            print(f"Godzina {time} nie istnieje dla filmu {self.title}.")

    def display_details(self):
        print(f"Film: {self.title}")
        print(f"Czas trwania: {self.duration} minut")
        print("Godziny seansów:")
        for time in self.showtimes:
            print(f"- {time}")

    def to_dict(self):
        return {
            "title": self.title,
            "duration": self.duration,
            "showtimes": self.showtimes
        }

    @staticmethod
    def from_dict(data):
        return Movie(data["title"], data["duration"], data["showtimes"])


class Customer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.reservations = []

    def add_reservation(self, movie, time):
        self.reservations.append({"movie": movie.title, "time": time})
        print(f"{self.first_name} {self.last_name} zarezerwował(a) film: {movie.title} na godzinę {time}.")

    def display_reservations(self):
        if not self.reservations:
            print(f"{self.first_name} {self.last_name} nie ma żadnych rezerwacji.")
        else:
            print(f"Rezerwacje dla {self.first_name} {self.last_name}:")
            for reservation in self.reservations:
                print(f"- Film: {reservation['movie']}, Godzina: {reservation['time']}")

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "reservations": self.reservations
        }

    @staticmethod
    def from_dict(data):
        customer = Customer(data["first_name"], data["last_name"])
        customer.reservations = data["reservations"]
        return customer


class VIPCustomer(Customer):
    def __init__(self, first_name, last_name, discount_rate=0.2):
        super().__init__(first_name, last_name)
        self.discount_rate = discount_rate

    def get_discounted_price(self, price):
        return price * (1 - self.discount_rate)

    def book_private_show(self, movie, time):
        self.reservations.append({"movie": movie.title, "time": time, "private": True})
        print(f"{self.first_name} {self.last_name} (VIP) zarezerwował(a) cały seans: {movie.title} na godzinę {time}.")

    def to_dict(self):
        data = super().to_dict()
        data["discount_rate"] = self.discount_rate
        return data

    @staticmethod
    def from_dict(data):
        vip_customer = VIPCustomer(data["first_name"], data["last_name"], data.get("discount_rate", 0.2))
        vip_customer.reservations = data["reservations"]
        return vip_customer


class Cinema:
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.movies = []
        self.customers = []
        ensure_directory_exists(self.data_dir)

    def add_movie(self, movie):
        self.movies.append(movie)
        print(f"Dodano film: {movie.title}.")

    def add_customer(self, customer):
        self.customers.append(customer)
        print(f"Dodano klienta: {customer.first_name} {customer.last_name}.")

    def display_movies(self):
        print("\nRepertuar kina:")
        if not self.movies:
            print("Brak filmów w repertuarze.")
        else:
            for movie in self.movies:
                movie.display_details()

    def display_all_reservations(self):
        print("\nSzczegóły wszystkich rezerwacji:")
        if not self.customers:
            print("Brak klientów.")
        else:
            for customer in self.customers:
                customer.display_reservations()

    def save_to_files(self):
        movies_file = os.path.join(self.data_dir, MOVIES_FILE)
        customers_file = os.path.join(self.data_dir, CUSTOMER_FILE)

        with open(movies_file, "w", encoding="utf-8") as file:
            json.dump([movie.to_dict() for movie in self.movies], file, indent=4)

        with open(customers_file, "w", encoding="utf-8") as file:
            json.dump([customer.to_dict() for customer in self.customers], file, indent=4)

    def load_from_files(self):
        movies_file = os.path.join(self.data_dir, MOVIES_FILE)
        customers_file = os.path.join(self.data_dir, CUSTOMER_FILE)

        try:
            with open(movies_file, "r", encoding="utf-8") as file:
                self.movies = [Movie.from_dict(data) for data in json.load(file)]
        except FileNotFoundError:
            print(f"Plik {movies_file} nie istnieje. Utworzono pustą listę filmów.")

        try:
            with open(customers_file, "r", encoding="utf-8") as file:
                self.customers = [Customer.from_dict(data) for data in json.load(file)]
        except FileNotFoundError:
            print(f"Plik {customers_file} nie istnieje. Utworzono pustą listę klientów.")


def validate_time_format(time_str):
    """
    Sprawdza, czy podany czas jest w formacie HH:MM i poprawnym zakresie.
    """
    time_pattern = re.compile(r"^(?:[01]\d|2[0-3]):[0-5]\d$")
    return bool(time_pattern.match(time_str))


class CinemaApp:
    def __init__(self, cinema):
        self.cinema = cinema
        self.root = tk.Tk()
        self.root.title("SYSTEM REZERWACJI KINA POLIBUDDA")
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        # Repertuar filmowy
        self.movie_frame = tk.LabelFrame(self.root, text="Filmy", padx=10, pady=10)
        self.movie_frame.pack(fill="both", expand=True)

        self.movie_tree = Treeview(self.movie_frame, columns=("Title", "Duration", "Showtimes"), show="headings")
        self.movie_tree.heading("Title", text="Tytuł")
        self.movie_tree.heading("Duration", text="Czas trwania (min)")
        self.movie_tree.heading("Showtimes", text="Godziny seansów")
        self.movie_tree.pack(fill="both", expand=True)

        self.add_movie_button = tk.Button(self.movie_frame, text="Dodaj Film", command=self.add_movie)
        self.add_movie_button.pack(pady=5)

        self.remove_showtime_button = tk.Button(self.movie_frame, text="Usuń Godzinę Seansu", command=self.remove_showtime)
        self.remove_showtime_button.pack(pady=5)

        self.add_showtime_button = tk.Button(self.movie_frame, text="Dodaj Godzinę Seansu", command=self.add_showtime)
        self.add_showtime_button.pack(pady=5)


        # Klienci
        self.customer_frame = tk.LabelFrame(self.root, text="Klienci", padx=10, pady=10)
        self.customer_frame.pack(fill="both", expand=True)

        self.customer_tree = Treeview(self.customer_frame, columns=("FirstName", "LastName"), show="headings")
        self.customer_tree.heading("FirstName", text="Imię")
        self.customer_tree.heading("LastName", text="Nazwisko")
        self.customer_tree.pack(fill="both", expand=True)

        self.add_customer_button = tk.Button(self.customer_frame, text="Dodaj Klienta", command=self.add_customer)
        self.add_customer_button.pack(pady=5)

        self.remove_customer_button = tk.Button(self.customer_frame, text="Usuń Klienta", command=self.remove_customer)
        self.remove_customer_button.pack(pady=5)

        # Rezerwacje
        self.reservation_frame = tk.LabelFrame(self.root, text="Rezerwacje", padx=10, pady=10)
        self.reservation_frame.pack(fill="both", expand=True)

        self.reservation_tree = Treeview(
            self.reservation_frame, columns=("Customer", "Movie", "Time", "Private"), show="headings"
        )
        self.reservation_tree.heading("Customer", text="Klient")
        self.reservation_tree.heading("Movie", text="Film")
        self.reservation_tree.heading("Time", text="Godzina")
        self.reservation_tree.heading("Private", text="Prywatny seans")
        self.reservation_tree.pack(fill="both", expand=True)

        self.make_reservation_button = tk.Button(self.reservation_frame, text="Dodaj Rezerwację", command=self.make_reservation)
        self.make_reservation_button.pack(pady=5)

        self.cancel_reservation_button = tk.Button(self.reservation_frame, text="Anuluj Rezerwację", command=self.cancel_reservation)
        self.cancel_reservation_button.pack(pady=5)

        # Zapis danych
        self.save_button = tk.Button(self.root, text="Zapisz", command=self.save_data)
        self.save_button.pack(pady=5)

        # Aktualizacja danych
        self.update_movie_list()
        self.update_customer_list()
        self.update_reservation_list()

    def update_movie_list(self):
        """Aktualizuje listę filmów w GUI."""
        for row in self.movie_tree.get_children():
            self.movie_tree.delete(row)

        for movie in self.cinema.movies:
            self.movie_tree.insert("", "end", values=(movie.title, movie.duration, ", ".join(movie.showtimes)))

    def update_customer_list(self):
        """Aktualizuje listę klientów w GUI."""
        for row in self.customer_tree.get_children():
            self.customer_tree.delete(row)

        for customer in self.cinema.customers:
            self.customer_tree.insert("", "end", values=(customer.first_name, customer.last_name))

    def update_reservation_list(self):
        """Aktualizuje listę rezerwacji w GUI."""
        for row in self.reservation_tree.get_children():
            self.reservation_tree.delete(row)

        for customer in self.cinema.customers:
            for reservation in customer.reservations:
                self.reservation_tree.insert(
                    "", "end",
                    values=(
                        f"{customer.first_name} {customer.last_name}",
                        reservation["movie"],
                        reservation["time"],
                        "Tak" if reservation.get("private") else "Nie"
                    ),
                )

    def add_showtime(self):
        """Dodaje nową godzinę seansu dla wybranego filmu."""
        selected_item = self.movie_tree.selection()
        if not selected_item:
            messagebox.showerror("Błąd", "Nie wybrano żadnego filmu.")
            return

        # Pobierz dane zaznaczonego filmu
        movie_data = self.movie_tree.item(selected_item, "values")
        movie_title = movie_data[0]

        # Znajdź film
        movie = next((m for m in self.cinema.movies if m.title == movie_title), None)
        if not movie:
            messagebox.showerror("Błąd", "Nie znaleziono filmu.")
            return

        # Pobierz godzinę od użytkownika
        new_showtime = simpledialog.askstring("Dodaj Godzinę Seansu", f"Podaj nową godzinę seansu dla filmu '{movie_title}':")
        if not new_showtime:
            return

        # Sprawdź poprawność formatu godziny
        if not validate_time_format(new_showtime):
            messagebox.showerror("Błąd", "Godzina jest w nieprawidłowym formacie. Użyj formatu HH:MM.")
            return

        # Dodaj godzinę, jeśli nie istnieje
        if new_showtime in movie.showtimes:
            messagebox.showerror("Błąd", f"Godzina {new_showtime} już istnieje w repertuarze filmu {movie_title}.")
            return

        movie.showtimes.append(new_showtime)
        self.update_movie_list()
        messagebox.showinfo("Sukces", f"Dodano godzinę seansu: {new_showtime} dla filmu {movie_title}.")


    def remove_showtime(self):
        """Usuwa zaznaczoną godzinę seansu z filmu. Usuwa film, jeśli nie ma już żadnych godzin seansów."""
        selected_item = self.movie_tree.selection()
        if not selected_item:
            messagebox.showerror("Błąd", "Nie wybrano żadnego filmu.")
            return

        # Pobierz dane zaznaczonego filmu
        movie_data = self.movie_tree.item(selected_item, "values")
        movie_title = movie_data[0]

        # Znajdź film
        movie = next((m for m in self.cinema.movies if m.title == movie_title), None)
        if not movie:
            messagebox.showerror("Błąd", "Nie znaleziono filmu.")
            return

        # Pobierz godzinę od użytkownika
        time_to_remove = simpledialog.askstring(
            "Usuń Godzinę Seansu", f"Podaj godzinę seansu do usunięcia z filmu '{movie_title}':"
        )
        if not time_to_remove:
            return

        # Sprawdź, czy godzina istnieje w repertuarze
        if time_to_remove in movie.showtimes:
            movie.showtimes.remove(time_to_remove)
            self.update_movie_list()

            # Sprawdź, czy film nie ma już żadnych godzin seansów
            if not movie.showtimes:
                self.cinema.movies.remove(movie)
                messagebox.showinfo("Film Usunięty", f"Film '{movie_title}' został usunięty, ponieważ nie ma żadnych godzin seansów.")
                self.update_movie_list()
            else:
                messagebox.showinfo("Sukces", f"Usunięto godzinę seansu: {time_to_remove} dla filmu '{movie_title}'.")
        else:
            messagebox.showerror("Błąd", f"Godzina {time_to_remove} nie istnieje w repertuarze filmu '{movie_title}'.")


        # Pobierz dane zaznaczonego filmu
        movie_data = self.movie_tree.item(selected_item, "values")
        movie_title = movie_data[0]

        # Znajdź film
        movie = next((m for m in self.cinema.movies if m.title == movie_title), None)
        if not movie:
            messagebox.showerror("Błąd", "Nie znaleziono filmu.")
            return

        # Pobierz godzinę od użytkownika
        time_to_remove = simpledialog.askstring(
            "Usuń Godzinę Seansu", f"Podaj godzinę seansu do usunięcia z filmu '{movie_title}':"
        )
        if not time_to_remove:
            return

        if time_to_remove in movie.showtimes:
            movie.showtimes.remove(time_to_remove)
            self.update_movie_list()
            messagebox.showinfo("Sukces", f"Usunięto godzinę seansu: {time_to_remove} dla filmu {movie_title}.")
        else:
            messagebox.showerror("Błąd", f"Godzina {time_to_remove} nie istnieje w repertuarze filmu {movie_title}.")


    def add_movie(self):
        """Dodaje nowy film do repertuaru."""
        title = simpledialog.askstring("Dodaj Film", "Podaj tytuł filmu:")
        if not title:
            return
        duration = simpledialog.askinteger("Dodaj Film", "Podaj czas trwania filmu (min):")
        if not duration:
            return
        showtimes_str = simpledialog.askstring("Dodaj Film", "Podaj godziny seansów (oddzielone przecinkami):")
        if not showtimes_str:
            return

        showtimes = [time.strip() for time in showtimes_str.split(",") if validate_time_format(time.strip())]

        if not showtimes:
            messagebox.showerror("Błąd", "Nie podano żadnej poprawnej godziny seansu.")
            return

        movie = Movie(title, duration, showtimes)
        self.cinema.add_movie(movie)
        self.update_movie_list()

    def add_customer(self):
        """Dodaje nowego klienta."""
        first_name = simpledialog.askstring("Dodaj Klienta", "Podaj imię klienta:")
        if not first_name:
            return
        last_name = simpledialog.askstring("Dodaj Klienta", "Podaj nazwisko klienta:")
        if not last_name:
            return

        customer = Customer(first_name, last_name)
        self.cinema.add_customer(customer)
        self.update_customer_list()

    def remove_customer(self):
        """Usuwa zaznaczonego klienta."""
        selected_item = self.customer_tree.selection()
        if not selected_item:
            messagebox.showerror("Błąd", "Nie wybrano żadnego klienta.")
            return

        # Pobierz dane zaznaczonego klienta
        customer_data = self.customer_tree.item(selected_item, "values")
        customer_name = f"{customer_data[0]} {customer_data[1]}"

        # Znajdź i usuń klienta
        customer = next((c for c in self.cinema.customers if f"{c.first_name} {c.last_name}" == customer_name), None)
        if customer:
            self.cinema.customers.remove(customer)
            self.update_customer_list()
            self.update_reservation_list()  # Aktualizacja rezerwacji po usunięciu klienta
            messagebox.showinfo("Sukces", f"Usunięto klienta: {customer_name}.")
        else:
            messagebox.showerror("Błąd", "Nie znaleziono klienta do usunięcia.")


        # Lista klientów do wyboru
        customer_names = [f"{customer.first_name} {customer.last_name}" for customer in self.cinema.customers]
        selected_name = simpledialog.askstring(
            "Usuń Klienta",
            f"Wybierz klienta do usunięcia:\n\n{chr(10).join(customer_names)}",
            initialvalue=customer_names[0]
        )

        if not selected_name:
            return

        # Szukamy klienta na podstawie wyboru
        for customer in self.cinema.customers:
            if f"{customer.first_name} {customer.last_name}" == selected_name:
                self.cinema.customers.remove(customer)
                self.update_customer_list()
                messagebox.showinfo("Sukces", f"Klient {selected_name} został usunięty.")
                return

        # Jeśli nie znaleziono klienta
        messagebox.showerror("Błąd", f"Nie znaleziono klienta: {selected_name}.")

    def make_reservation(self):
        """Dodaje rezerwację dla wybranego klienta."""
        customer_name = simpledialog.askstring("Rezerwacja", "Podaj imię i nazwisko klienta (np. Jan Kowalski):")
        if not customer_name:
            return
        movie_title = simpledialog.askstring("Rezerwacja", "Podaj tytuł filmu:")
        if not movie_title:
            return
        showtime = simpledialog.askstring("Rezerwacja", "Podaj godzinę seansu:")
        if not showtime or not validate_time_format(showtime):
            messagebox.showerror("Błąd", "Godzina seansu jest w nieprawidłowym formacie. Użyj formatu HH:MM.")
            return

        customer = next((c for c in self.cinema.customers if f"{c.first_name} {c.last_name}" == customer_name), None)
        movie = next((m for m in self.cinema.movies if m.title == movie_title), None)

        if not customer:
            messagebox.showerror("Błąd", "Nie znaleziono klienta.")
            return

        if not movie:
            messagebox.showerror("Błąd", "Nie znaleziono filmu.")
            return

        customer.add_reservation(movie, showtime)
        self.update_reservation_list()

    def cancel_reservation(self):
        """Anuluje zaznaczoną rezerwację."""
        selected_item = self.reservation_tree.selection()
        if not selected_item:
            messagebox.showerror("Błąd", "Nie wybrano żadnej rezerwacji.")
            return

        # Pobierz dane zaznaczonej rezerwacji
        reservation_data = self.reservation_tree.item(selected_item, "values")
        customer_name = reservation_data[0]
        movie_title = reservation_data[1]
        showtime = reservation_data[2]

        # Znajdź klienta
        customer = next((c for c in self.cinema.customers if f"{c.first_name} {c.last_name}" == customer_name), None)
        if not customer:
            messagebox.showerror("Błąd", "Nie znaleziono klienta.")
            return

        # Znajdź i usuń rezerwację
        reservation = next(
            (r for r in customer.reservations if r["movie"] == movie_title and r["time"] == showtime), None
        )
        if reservation:
            customer.reservations.remove(reservation)
            self.update_reservation_list()
            messagebox.showinfo("Sukces", f"Usunięto rezerwację na film {movie_title} dla {customer_name}.")
        else:
            messagebox.showerror("Błąd", "Nie znaleziono rezerwacji do anulowania.")


        # Wybierz klienta
        customer_name = simpledialog.askstring("Anulowanie rezerwacji", "Podaj imię i nazwisko klienta (np. Jan Kowalski):")
        if not customer_name:
            return

        # Znajdź klienta
        customer = next((c for c in self.cinema.customers if f"{c.first_name} {c.last_name}" == customer_name), None)
        if not customer:
            messagebox.showerror("Błąd", "Nie znaleziono klienta.")
            return

        # Sprawdź, czy klient ma rezerwacje
        if not customer.reservations:
            messagebox.showinfo("Brak rezerwacji", f"Klient {customer_name} nie ma żadnych rezerwacji.")
            return

        # Wyświetl listę rezerwacji klienta do wyboru
        reservation_list = [f"{res['movie']} o {res['time']}" for res in customer.reservations]
        selected_reservation = simpledialog.askstring(
            "Anulowanie rezerwacji",
            f"Wybierz rezerwację do usunięcia:\n\n{chr(10).join(reservation_list)}",
            initialvalue=reservation_list[0]
        )

        if not selected_reservation:
            return

        # Znajdź i usuń rezerwację
        for reservation in customer.reservations:
            if f"{reservation['movie']} o {reservation['time']}" == selected_reservation:
                customer.reservations.remove(reservation)
                self.update_reservation_list()
                messagebox.showinfo("Sukces", f"Rezerwacja {selected_reservation} została anulowana.")
                return

        # Jeśli nie znaleziono pasującej rezerwacji
        messagebox.showerror("Błąd", f"Nie znaleziono rezerwacji: {selected_reservation}.")


    def save_data(self):
        """Zapisuje dane do plików."""
        self.cinema.save_to_files()
        messagebox.showinfo("Sukces", "Dane zapisano pomyślnie.")

    def on_close(self):
        """Akcja wykonywana podczas zamknięcia okna."""
        self.save_data()
        self.root.destroy()

    def run(self):
        self.root.mainloop()


# Program główny
if __name__ == "__main__":
    # Inicjalizacja kina
    cinema = Cinema(DATA_DIR)
    cinema.load_from_files()

    app = CinemaApp(cinema)
    app.run()