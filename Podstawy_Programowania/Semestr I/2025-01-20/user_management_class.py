import os, json, re, logging, datetime
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Treeview

# Path to default data directory
BASE_DIR = os.path.dirname(__file__)  # Start with current program directory,
DATA_DIR = os.path.join(BASE_DIR, "data") # Data directory name in the above mentioned directory,
USERS_FILE = os.path.join(DATA_DIR, "users_data.json") # User data file name in the above mentioned directory,
LOG_FILE = os.path.join(DATA_DIR, "operations.log") # Operations file name in the data directory.
LOG_CRITICAL = os.path.join(DATA_DIR, "critical.log") # Critical log file name in the data directory.

# Window resolution settings
WIDTH = 1280
HEIGHT = 720

# Logger configuration
logging.basicConfig(filename=LOG_CRITICAL, level=logging.CRITICAL)

# Add time to event
logger = logging.getLogger(__name__)
logger.info(f"The event occurred at: {datetime.datetime.now()}")

# Validations
def validate_email(email:str) -> tuple[bool, str]:
    """
    Validates the given email address using a regular expression.

    Args:
        email (str): The email address to be validated.

    Returns:
        tuple: A tuple containing a boolean indicating whether the email is valid,
               and an optional error message.
    """

    regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    if re.fullmatch(regex, email):
        return True, None  # If email is correct
    elif '@' not in email:
        return False, "Brak znaku '@' w adresie email"
    else:
        return False, "Nieprawidłowy format adresu email"

    
def ensure_directory_exists(directory: str) -> None:
    """Creates a new directory if it doesn't exist.

    This function ensures that the specified directory exists, creating it if necessary.
    """
    try:
        os.makedirs(directory, exist_ok=True)
    except OSError as e:
        print(f"Błąd podczas tworzenia struktury katalogowej {directory}: {e}")


class User:
    """Represents a user in the system."""
    def __init__(self, username: str, email: str, role: str) -> dict:
        """
        Initializes a new User object.

        Args:
            username (str): The username of the user.
            email (str): The email address of the user.
            role (str): The role of the user (e.g., "admin", "user").
        """
        self.username = username
        self.email = email
        self.role = role

    def to_dict(self) -> dict:
        """
        Returns a dictionary representation of the user.

        Returns:
            dict: A dictionary containing the user's username, email, and role.
        """
        return {"username": self.username, "email": self.email, "role": self.role}


class UserManager:
    """
    Manages user data and performs operations on it.

    This class handles operations such as loading, saving, adding, removing, 
    and displaying users. Additionally, it logs operations to a specified log file.
    """
    def __init__(self):
        """
        Initializes the UserDataManager.

        Creates the data directory if it doesn't exist and loads existing users from the file.
        """
        ensure_directory_exists(DATA_DIR)
        self.users = self.load_users()

    def load_users(self) -> list:
        """
        Loads users from the JSON file.

        Returns:
            list: A list of user dictionaries. If the file doesn't exist or is empty, 
                  returns an empty list.
        """
        if os.path.exists(USERS_FILE):
            with open(USERS_FILE, "r") as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return []
        return []

    def save_users(self):
        """
        Saves the current list of users to the JSON file.

        Dumps the `self.users` list (containing user dictionaries) to the file 
        specified by `USERS_FILE` in JSON format with indentation for better readability.
        """
        with open(USERS_FILE, "w") as file:
            json.dump(self.users, file, indent=4)

    def log_operation(self, operation: str, log_file: str = None):
        """
        Logs the specified operation to the log file.

        Appends the given `operation` string to the log file in append mode, ensuring that 
        each operation is written on a new line.
        """
        with open(LOG_FILE, "a") as file:
            file.write(operation + "\n")

    def add_user(self, user: User):
        """
        Adds a new user to the list of users.

        Args:
            user (User): The User object to be added.

        Raises:
            ValueError: If a user with the same username already exists.

        Appends the user's data (as a dictionary) to the `self.users` list, 
        saves the updated list to the file, and logs the operation.
        """
        if any(u["username"] == user.username for u in self.users):
            raise ValueError("Użytkownik o podanym username już istnieje.")
        self.users.append(user.to_dict())
        self.save_users()
        self.log_operation(f"Add user: {user.username}, at: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}")

    def remove_user(self, username: str):
        """
        Removes a user with the given username from the list of users.

        Args:
            username (str): The username of the user to be removed.

        Raises:
            ValueError: If no user with the given username is found.

        Removes the user's data from the `self.users` list, saves the updated list 
        to the file, and logs the operation.
        """
        initial_count = len(self.users)
        self.users = [u for u in self.users if u["username"] != username]
        if len(self.users) == initial_count:
            raise ValueError("Nie znaleziono użytkownika o podanym username.")
        self.save_users()
        self.log_operation(f"Deleted user: {username}, at: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}")

    def display_all_users(self) -> list:
        """
        Returns a list of all users to display.

        Returns:
            list: A list of dictionaries, where each dictionary represents a user.
        """
        return self.users


class UserManagementApp():
    """Represents the User Management application.

    This class manages the graphical user interface (GUI) for the user management system, 
    allowing users to add, remove, and view user data in a Treeview widget.
    """

    def __init__(self, root):
        """
        Initializes the UserManagementApp.

        Args:
            root (tkinter.Tk): The root window of the application.

        Sets up the UserManager, initializes the root window, 
        and creates the GUI widgets for the application.
        """
        self.manager = UserManager()
        self.root = root
        self.root.title("System zarządzania użytkownikami")

        # Center the window on the screen
        self.center_window(WIDTH, HEIGHT)
        
        # Build the GUI widgets for the application
        self.create_widgets()

    def center_window(self, width:int, height:int):
        """Centers the application window on the screen."""
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def create_widgets(self):
        """Creates the GUI widgets for the application."""
        self.tree = Treeview(self.root, columns=("Username", "Email", "Role"), show="headings")
        self.tree.heading("Username", text="Nazwa użytkownika")
        self.tree.heading("Email", text="Adres E-mail")
        self.tree.heading("Role", text="Rola")
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.refresh_tree()

        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(fill=tk.X)

        add_button = tk.Button(button_frame, text="Dodaj użytkownika", command=self.add_user)
        add_button.pack(side=tk.LEFT, padx=5, pady=5)

        remove_button = tk.Button(button_frame, text="Usuń użytkownika", command=self.remove_user)
        remove_button.pack(side=tk.LEFT, padx=5, pady=5)

    def refresh_tree(self):
        """
        Refreshes the treeview widget with the latest user data.

        Clears the existing treeview and populates it with 
        the current list of users from the UserManager.
        """
        for row in self.tree.get_children():
            self.tree.delete(row)
        for user in self.manager.display_all_users():
            self.tree.insert("", tk.END, values=(user["username"], user["email"], user["role"]))

    def add_user(self):
        """
        Displays a dialog box to add a new user.
        """

        def get_user_data():
            """
            Retrieves user data from input fields and adds a new user.

            This function gets the username, email, and role from the 
            input fields. It validates the input, creates a User object, 
            adds the user to the manager, refreshes the treeview, 
            and displays success or error messages.

            Raises:
                ValueError: If any of the required fields are empty.
                ValueError: If a user with the same username already exists.
                ValueError: If the email address is invalid. 
            """
            username = entry_username.get()
            email = entry_email.get()
            role = entry_role.get()
            
            is_valid, error_message = validate_email(email)

            if not is_valid:
                messagebox.showerror("Błąd", f"Wystąpił następujący błąd: {error_message}")
                return

            if not username or not email or not role:
                messagebox.showerror("Błąd", "Wszystkie pola są wymagane.")
                return

            try:
                user = User(username, email, role)
                self.manager.add_user(user)
                self.refresh_tree()
                messagebox.showinfo("Operacja powiodła się", "Użytkownik dodany pomyślnie.")
                dialog.destroy()  # Close dialog windows
            except ValueError as e:
                messagebox.showerror("Błąd", str(e))

        # Creating a dialog box
        dialog = tk.Toplevel(self.root)
        dialog.title("Dodaj użytkownika")

        # Labels and input fields
        label_username = tk.Label(dialog, text="Nazwa użytkownika:")
        entry_username = tk.Entry(dialog)
        label_email = tk.Label(dialog, text="Adres email:")
        entry_email = tk.Entry(dialog)
        label_role = tk.Label(dialog, text="Rola:")
        entry_role = tk.Entry(dialog)

        # Buttons
        button_ok = tk.Button(dialog, text="OK", command=get_user_data)
        button_cancel = tk.Button(dialog, text="Anuluj", command=dialog.destroy)

        # Placing items in a dialog using grid()
        label_username.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        entry_username.grid(row=0, column=1, padx=10, pady=5)
        label_email.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        entry_email.grid(row=1, column=1, padx=10, pady=5)
        label_role.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        entry_role.grid(row=2, column=1, padx=10, pady=5)
        button_ok.grid(row=3, column=0, padx=10, pady=10, sticky=tk.E)
        button_cancel.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

        dialog.transient(self.root)  # Dialog box on top of main
        dialog.grab_set()  # Blocks interaction with the main window as long as the dialog is open
        dialog.mainloop()

    def remove_user(self):
        """
        Removes the selected user from the list.

        Handles the removal of a user from the list, including:
        - Checking if a user is selected.
        - Getting the username of the selected user.
        - Calling the UserManager to remove the user.
        - Refreshing the treeview to reflect the changes.
        - Displaying appropriate success or error messages.
        """
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Błąd", "Nie zaznaczono użytkownika")
            return

        username = self.tree.item(selected_item, "values")[0]
        try:
            self.manager.remove_user(username)
            self.refresh_tree()
            messagebox.showinfo("Operacja powiodła się", "Użytkownik został usunięty")
        except ValueError as e:
            messagebox.showerror("Błąd", str(e))


if __name__ == "__main__":
    """Start a program"""
    root = tk.Tk()
    app = UserManagementApp(root)
    root.mainloop()