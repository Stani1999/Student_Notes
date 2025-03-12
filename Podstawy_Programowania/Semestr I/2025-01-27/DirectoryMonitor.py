import logging as log
import os

# Path to default data directory
BASE_DIR = os.path.dirname(__file__)  # Start with current program directory,
DATA_DIR = os.path.join(BASE_DIR, "data")  # Data directory name in the above-mentioned directory,
LOG_FILE = os.path.join(DATA_DIR, "directory.log")  # Critical log file name in the data directory.


def ensure_directory_exists(directory: str) -> None:
    """Creates a new directory if it doesn't exist.

    This function ensures that the specified directory exists, creating it if necessary.
    """
    try:
        os.makedirs(directory, exist_ok=True)
    except OSError as e:
        print(f"Error creating directory structure {directory}: {e}")


ensure_directory_exists(DATA_DIR)

log.basicConfig(filename=LOG_FILE, level=log.INFO, format='%(asctime)s - %(message)s')


class DirectoryMonitor:
    @staticmethod
    def find_file(filename: str) -> str:
        """
        Search for a file in the data directory.

        Args:
            filename (str): The name of the file to search for.

        Returns:
            str: Full path to the file if found, or a message indicating it's not found.
        """
        log.info(f"Searching for file: {filename}")
        for root, dirs, files in os.walk(DATA_DIR):
            if filename in files:
                file_path = os.path.join(root, filename)
                log.info(f"Znaloziono folder: {file_path}")
                return f"File found: {file_path}"
        log.info(f"File not found: {filename}")
        return f"Nie znaleziono folderu {filename}."


# Main function
def main():
    find = input("Enter the name of the file to search: ")
    monitor = DirectoryMonitor()
    result = monitor.find_file(find)
    print(result)


# Program entry point
if __name__ == "__main__":
    main()
