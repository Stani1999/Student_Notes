import hashlib

# Użycie SHA-256 do hashowania tekstu
text_to_hash = "SigmyZEnigmy"

hash_object = hashlib.sha256(text_to_hash.encode())  # Dane wejściowe muszą być typu bytes
hash_value = hash_object.hexdigest()  # Zwraca wartość hash jako ciąg znaków szesnastkowych

print(hash_value)


import os
import hashlib

def hash_password(password):
    sale = os.urandom(16)  
    key = hashlib.pbkdf2_hmac('sha256', password.encode(), sale, 100000)
    return sale + key

# Hashing hasła
password = "safePassword123"
password_hashed = hash_password(password)
print(password_hashed)


def own_hash(word):
    return hash(word)

haslo = "tajne123"
print(f"Hash 256: {haslo} : {own_hash(haslo)} ")

def simple_hash(password, table_size=10):
    return sum(otd(c) for c in password) % table_size

words = ["kod", "pies"]