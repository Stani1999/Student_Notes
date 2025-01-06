''' Validation Functions Module '''

import re


def pesel(pesel: str) -> bool:
    """Validate PESEL number."""
    if len(pesel) != 11 or not pesel.isdigit():
        return False

    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    control_sum = sum(int(pesel[i]) * weights[i] for i in range(10))
    control_digit = (10 - (control_sum % 10)) % 10
    return control_digit == int(pesel[10])

def nip(nip: str) -> bool:
    """Validate NIP number."""
    if len(nip) != 10 or not nip.isdigit():
        return False

    weights = [6, 5, 7, 2, 3, 4, 5, 6, 7]
    control_sum = sum(int(nip[i]) * weights[i] for i in range(9))
    control_digit = control_sum % 11
    return control_digit == int(nip[9]) if control_digit < 10 else False

def regon(regon: str) -> bool:
    """Validate REGON number."""
    if len(regon) not in [9, 14] or not regon.isdigit():
        return False

    weights = [8, 9, 2, 3, 4, 5, 6, 7] if len(regon) == 9 else [2, 4, 8, 5, 0, 9, 7, 3, 6, 1, 2, 4, 8]
    control_sum = sum(int(regon[i]) * weights[i] for i in range(len(weights)))
    control_digit = control_sum % 11
    return control_digit == int(regon[len(weights)])

def password(password: str) -> tuple[bool, str]:
    """Validate password strength."""
    if len(password) < 8:
        return False, "Hasło jest za krótkie."
    if not re.search(r'[a-z]', password):
        return False, "Hasło musi zawierać małe litery."
    if not re.search(r'[A-Z]', password):
        return False, "Hasło musi zawierać wielkie litery."
    if not re.search(r'[0-9]', password):
        return False, "Hasło musi zawierać cyfry."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Hasło musi zawierać znaki specjalne."
    return True, "Hasło jest silne."

def name(name: str) -> tuple[bool, str]:
    """Validate user name."""
    if re.search(r'[0-9]', name):
        return False, "Imie nie może zawierać cyfry."
    if re.search(r'[!@#$%^&*(),?":{}|<>]', name):
        return False, "Imie nie może zawierać znaków specjalnych."
    if not re.search(r'[A-Z]', name):
        return False, "Imie musi zawierać wielkie litery."
    if not re.search(r'[a-z]', name):
        return False, "Imie musi zawierać małe litery."
    return True, f"Wprowadzasz dane dla {name}:"
