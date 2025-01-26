import os, json
import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter.ttk import Treeview

# Path to default data directory
BASE_DIR = os.path.dirname(__file__)  # Current program directory
DATA_DIR = os.path.join(BASE_DIR, "data")
USERS_FILE = os.path.join(DATA_DIR, "users_data.json")

def ensure_directory_exists(directory: str) -> None:
    """Create new directory if dosn't existed"""
    try:
        os.makedirs(directory, exist_ok=True)
    except OSError as e:
        print(f"Błąd podczas tworzenia struktury katalogowej {directory}: {e}")


class User:
    """Class represents a user in the system."""
    def __init__(self, username: str, email: str, role: str):
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

    def to_dict(self):
        """
        Returns a dictionary representation of the user.

        Returns:
            dict: A dictionary containing the user's username, email, and role.
        """
        return {"username": self.username, "email": self.email, "role": self.role}


class UserManager:
    def __init__(self):
        """
        Initializes the UserDataManager.

        Creates the data directory if it doesn't exist and loads existing users from the file.
        """
        ensure_directory_exists(DATA_DIR)
        self.users = self.load_users()

    def load_users(self):
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

    def log_operation(self, operation: str):
        """
        Logs the specified operation to the log file.

        Appends the given `operation` string to the log file.
        """
        log_file = os.path.join(DATA_DIR, "operations.log")
        with open(log_file, "a") as file:
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
        self.log_operation(f"Dodano użytkownika: {user.username}")

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
        self.log_operation(f"Usunięto użytkownika: {username}")

    def display_all_users(self):
        return self.users


class UserManagementApp:
    def __init__(self, root):
        self.manager = UserManager()
        self.root = root
        self.root.title("User Management")
        self.create_widgets()

    def create_widgets(self):
        self.tree = Treeview(self.root, columns=("Username", "Email", "Role"), show="headings")
        self.tree.heading("Username", text="Username")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Role", text="Role")
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.refresh_tree()

        button_frame = tk.Frame(self.root)
        button_frame.pack(fill=tk.X)

        add_button = tk.Button(button_frame, text="Add User", command=self.add_user)
        add_button.pack(side=tk.LEFT, padx=5, pady=5)

        remove_button = tk.Button(button_frame, text="Remove User", command=self.remove_user)
        remove_button.pack(side=tk.LEFT, padx=5, pady=5)

    def refresh_tree(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for user in self.manager.display_all_users():
            self.tree.insert("", tk.END, values=(user["username"], user["email"], user["role"]))

    def add_user(self):
        username = simpledialog.askstring("Add User", "Enter username:")
        email = simpledialog.askstring("Add User", "Enter email:")
        role = simpledialog.askstring("Add User", "Enter role:")

        if not username or not email or not role:
            messagebox.showerror("Error", "All fields are required.")
            return

        try:
            user = User(username, email, role)
            self.manager.add_user(user)
            self.refresh_tree()
            messagebox.showinfo("Success", "User added successfully.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def remove_user(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "No user selected.")
            return

        username = self.tree.item(selected_item, "values")[0]
        try:
            self.manager.remove_user(username)
            self.refresh_tree()
            messagebox.showinfo("Success", "User removed successfully.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = UserManagementApp(root)
    root.mainloop()
