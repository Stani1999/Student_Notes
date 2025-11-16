
# Relacyjne Bazy Danych - Notatki z Ćwiczeń (PostgreSQL)

## 06.10.2025 — Instalacja PSQL (Linux)

### Instalacja i konfiguracja

#### 1. Aktualizacja systemu

```bash
sudo apt update && sudo apt upgrade -y
```

#### 2. Instalacja PostgreSQL

* Polecenie instalacyjne (przykład dla wersji 18):

```bash
sudo apt install postgresql-18
```

#### 3. Sprawdzenie statusu usługi

```bash
sudo systemctl status postgresql
```

#### 4. Aktywacja nieaktywnej usługi

```bash
sudo systemctl start postgresql
```

#### 5. Uruchomienie interaktywnej konsoli PSQL jako użytkownik `postgres`

```bash
sudo -u postgres psql
```

---

## 13.10.2025 — Użytkownicy i konfiguracja dostępu

### Przełączanie użytkowników

**Przełączenie na użytkownika `postgres` (superadmin):**

```bash
sudo -i -u postgres
```

**Logowanie do konsoli PSQL jako superadmin:**

```bash
psql
```

### Konfiguracja dostępu (pg_hba.conf)

**Sprawdzenie lokalizacji pliku konfiguracyjnego w psql:**

```sql
SHOW hba_file;
```

**Otwieranie konfiguracji pg_hba (przykład dla wersji 16):**

```bash
sudo nano /etc/postgresql/16/main/pg_hba.conf
```

**Przeładowanie konfiguracji:**

```bash
sudo systemctl reload postgresql
```

#### Ważne informacje

* Zdalne logowanie jest domyślnie zablokowane.
* Katalog `conf.d` nadpisuje wcześniejsze ustawienia.
* Opcja `hostssl` umożliwia logowanie przez SSL.
* Zalecana alokacja RAM: **25%**, nie więcej niż **40%**.
* WAL (Write-Ahead Logging) zapisuje każdą zmianę w logach.

---

## 20.10.2025 — Bezpieczeństwo i dobre praktyki

### Aspekty bezpieczeństwa

* Ograniczaj dostęp tylko do konkretnych adresów IP.
* Zmieniaj domyślne porty i adresy.
* **Bastion Host** — maszyna pośrednia o stałym IP do łączenia się z bazą.
* Przechowuj konfiguracje w repozytorium Git.

---

## 27.10.2025 — Narzędzie `psql` i ustawienia połączenia

### Narzędzie `psql` (CLI)

**Zalety:**

* szybkie przeglądanie tabel,
* historia poleceń,
* możliwość wykonywania skryptów.

### Polecenia pomocnicze (psql)

| Komenda | Opis                   |
| ------- | ---------------------- |
| `\list` | Lista baz danych       |
| `\c`    | Połączenie z inną bazą |
| `\dn`   | Lista schematów        |
| `\df`   | Lista funkcji          |
| `\dn+`  | Szczegóły schematów    |
| `\?`    | Pomoc dla komend psql  |
| `\h`    | Pomoc dla poleceń SQL  |

### Łączenie z bazą i plik `.pgpass`

**Łączenie z lokalnym serwerem:**

```bash
psql -h 127.0.0.1 -p 5432
```

**Zmienne środowiskowe:**

```bash
export PGUSER=postgres
export PGDATABASE=postgres
```

**Plik `.pgpass`**

* przechowuje dane logowania,
* musi mieć uprawnienia:

```bash
chmod 600 ~/.pgpass
```

**Składnia pliku `.pgpass`:**

```sh
hostname:port:database:username:password
```

### Zmiana portu

**Sprawdzenie lokalizacji configu:**

```sql
SHOW config_file;
```

**Otwieranie konfiguracji config_file (przykład dla wersji 16):**

```bash
sudo nano /etc/postgresql/16/main/postgresql.conf
```

Zmień parametr `port` i zrestartuj usługę PostgreSQL.

```sh
sudo systemctl restart postgresql
```

---

## 03.11.2025 — Typy danych i tabele

### Tworzenie tabel

* Sprawdzać dokumentację typów danych.
* **Unikać używania `TEXT`**, gdyż może spowalniać bazę.

### Typy danych — wymiarowanie

**`char` vs `varchar`:**

* `char(n)` — stała liczba znaków, niewykorzystane miejsca wypełniane spacjami.
* `varchar(n)` — zmienna długość, efektywniejszy.

**`uuid`:**

* mniej przewidywalny niż ID numeryczne,
* składa się z kilku bloków,
* zawiera wartość czasu → lepsze sortowanie.

---

## Typy niestandardowe (Domain i Composite)

### 1. DOMAIN — rozszerzenia typów

**Przykład: wymuszenie wartości nieujemnej**

```sql
CREATE DOMAIN positive_integer AS INTEGER
    DEFAULT 0
    NOT NULL
    CHECK (VALUE >= 0);
```

**Przykład: walidacja kodu pocztowego**

```sql
CREATE DOMAIN us_postal_code AS TEXT
    CHECK (VALUE ~ '^\d{5}$' OR VALUE ~ '^\d{2}-\d{3}$');
```

---

### 2. Typy złożone (Composite Types)

**Tworzenie typu złożonego:**

```sql
CREATE TYPE address AS (
    street TEXT,
    city TEXT,
    postal_code VARCHAR(6)
);
```

**Użycie w tabeli:**

```sql
CREATE TABLE cluster (
    id SERIAL PRIMARY KEY,
    user_address address
);
```

**Wstawianie danych:**

```sql
INSERT INTO cluster (user_address)
VALUES (ROW('ul. Główna 1', 'Warszawa', '00-001'));
```

---