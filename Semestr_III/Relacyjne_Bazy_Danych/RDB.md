
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

## 13.11.2025:

### Struktura początkowa i Domeny

Utworzenie podstawowych tabel (`users`, `forms`) oraz domeny (`form_title`) z kluczami głównymi i obcymi.

```sql
-- Tabela użytkowników, users
CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

```sql
-- Definicja domeny dla tytułu formularza (PSQL nie obsługuje NOT EXISTS dla domen)
CREATE DOMAIN form_title AS VARCHAR(255) NOT NULL;
```

```sql
-- Tabela formularzy, forms
CREATE TABLE IF NOT EXISTS forms (
    form_id SERIAL PRIMARY KEY,
    title form_title UNIQUE, -- Użycie utworzonej domeny
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    owner_id INTEGER NOT NULL,
    CONSTRAINT fk_owner
    FOREIGN KEY(owner_id) 
    REFERENCES users(user_id)
    ON DELETE CASCADE
);
```

---

### Zadanie 1: Tabela Pytania (`questions`)

Utworzenie tabeli `questions` przechowującej pytania do formularzy.

**Wskazówka:** Staramy się tworzyć nazwy kluczy, aby identyfikowały się z nazwą tabeli (np. `fk_form`).

```sql
-- Tabela questions:
CREATE TABLE IF NOT EXISTS questions (
    question_id smallserial PRIMARY KEY,
    form_id INTEGER NOT NULL,
    question_text TEXT NOT NULL,
    question_type VARCHAR(50) NOT NULL, /* np text, rating, wybór itp. */
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_form
        FOREIGN KEY(form_id)
            REFERENCES forms(form_id)
    ON DELETE CASCADE
);
```

---

### Wprowadzanie Danych

Przykładowe dane do tabel `users`, `forms` i `questions`.

```sql
-- Dodwanie userów
INSERT INTO users (email, password_hash) VALUES
('Gołt@Pessi.wowo', 'hash30'),
('Gołt@Ronaldo.siu', 'hash7'),
('TRUE_GOAT@Ronal.dinho', 'hash10');
```

```sql
-- Dodwanie formularzy
INSERT INTO forms (title, owner_id) VALUES
('Ankieta satysfakcji klienta', 1),
('Formularz rejestracyjny', 2);
```

```sql
-- Dodwanie pytań
INSERT INTO questions (form_id, question_text, question_type) VALUES
(1, 'Jak oceniasz obsługę?', 'rating'),
(1, 'Co możemy poprawić?', 'text'),
(2, 'Podaj swoje imię i nazwisko', 'text');
```

---

### Zadanie 2: Modyfikacja Tabeli `forms`

#### A. Dodanie kolumny `status`

Dodanie kolumny `status` do tabeli `forms` z domyślną wartością `'draft'`.

```sql
-- A do tabeli forms dodajemy kolumnę status domyślnie jako 'draft'
ALTER TABLE forms ADD COLUMN status VARCHAR (20) DEFAULT 'draft';
```

#### Dodanie nowego formularza (z domyślnym statusem)

```sql
-- Dodajemy nowy formularz bez podawania statusu
INSERT INTO forms (title, owner_id) VALUES
('Quiz', 1);
```

#### Dodanie i aktualizacja `response_count`

Dodanie kolumny `response_count` i zaktualizowanie jej wartości w istniejących formularzach.

**Uwaga:** W PostgreSQL wartości **NULL** nie są zliczane do funkcji agregującej `COUNT`.

```sql
-- Dodanie kolumny do forms response_count
ALTER TABLE forms ADD COLUMN response_count INTEGER DEFAULT 0;
```

```sql
-- Dodanie przykładowych danych do formularzy
UPDATE forms SET response_count = 150 WHERE form_id = 1;
UPDATE forms SET response_count = 75 WHERE form_id = 2;
UPDATE forms SET response_count = 50 WHERE form_id = 3;
```

---

### Funkcje Agregujące i Grupowanie

#### Obliczenia globalne (SUM, AVG, MAX, MIN)

```sql
-- Suma wartości wszystkich odpowiedzi
SELECT SUM(response_count) AS total_responses FROM forms;
```

```sql
-- Dla średniej i max min
SELECT AVG(response_count) AS average_responses,
       MAX(response_count) AS max_responses,
       MIN(response_count) AS min_responses
FROM forms;
```

#### Grupowanie (`GROUP BY`)

Policzenie, ilu formularzy jest właścicielem każdy z użytkowników.

```sql
-- Aby policzyć ile formularzy ma każdy z użytkowników 
SELECT owner_id, count(*) AS number_of_forms
FROM forms
GROUP BY owner_id  
ORDER BY number_of_forms DESC;
```

---
