import logging as log
import os

# Path to default data directory
BASE_DIR = os.path.dirname(__file__)  # Start with current program directory,
DATA_DIR = os.path.join(BASE_DIR, "data") # Data directory name in the above mentioned directory,
LOG_FILE = os.path.join(DATA_DIR, "text.log") # Critical log file name in the data directory.

def ensure_directory_exists(directory: str) -> None:
    """Creates a new directory if it doesn't exist.

    This function ensures that the specified directory exists, creating it if necessary.
    """
    try:
        os.makedirs(directory, exist_ok=True)
    except OSError as e:
        print(f"Błąd podczas tworzenia struktury katalogowej {directory}: {e}")

ensure_directory_exists(DATA_DIR)

log.basicConfig(filename=LOG_FILE, level=log.INFO, format='%(asctime)s -%(message)s')


def word_count(text):
    words = text.split()
    return len(words)

def unique_words(text):
    unique_words = []
    words = text.split()

    for word in words:
        if word not in unique_words:
            unique_words.append(word)

    return unique_words

# Funkcja główna
def main():

    tekst = input ("Wprowadź tekst tutaj: ")

    liczba_slow = word_count(tekst)
    print(f"Liczba słów to {liczba_slow}")

    unikalne_slowa = unique_words(tekst)
    print(f"Unikalne słowa: {unikalne_slowa}")


# Program główny
if __name__ == "__main__":
    main()