# Relacyjne Bazy Danych - Notatki z Ćwiczeń (PostgreSQL)

\* - oznacza dodane do notatek po zajęciach

## 2025.10.06 — Instalacja PSQL (Linux)

### Instalacja i konfiguracja

#### 1. Aktualizacja systemu

```bash
sudo apt update && sudo apt upgrade -y
```

#### 2. Instalacja PostgreSQL dla systemów opartych na Debianie/Ubuntu

- Polecenie instalacyjne (przykład dla wersji 18):

```bash
sudo apt install postgresql-18
```

#### 3. Sprawdzenie statusu usługi

- Usługa powinna być aktywna (active):

```bash
sudo systemctl status postgresql
```

#### 4. Aktywacja nieaktywnej usługi
 
- Jeżeli usługa jest nieaktywna, uruchom ją poleceniem:

```bash
sudo systemctl start postgresql
```

#### 5. Uruchomienie interaktywnej konsoli PSQL jako użytkownik `postgres`

- Domyślny superadmin PostgreSQL to użytkownik `postgres`, więc aby zalogować się do konsoli PSQL, użyj polecenia:

```bash
sudo -u postgres psql
```

#### \*6. Aby sprawdzić kto jest aktualnie podpięty do bazy

```sql
SELECT * FROM pg_stat_activity;
```

#### \*7. Sprawdzenie wersji PostgreSQL

```sql
SELECT version();
```

#### \*8. Wyjście z konsoli PSQL

- Aby wyjść z konsoli PSQL, wpisz:

```sql
\q
```

---

## 2025.10.12 — Użytkownicy i konfiguracja dostępu

### 1. Przełączanie użytkowników

**1.1 Przełączenie na użytkownika `postgres` (superadmin):**

- Uruchamia interaktywną powłokę jako użytkownik systemowy `postgres`, który posiada pełne uprawnienia administracyjne do serwera PostgreSQL.

- Wymaga podania hasła użytkownika wywołującego polecenie sudo (z Linux), a nie hasła użytkownika postgres

```bash
sudo -i -u postgres
```

- Aby wrócić do poprzedniego użytkownika (z Linux), użyj polecenia:

```bash
exit
```

**1.2 Logowanie do konsoli PSQL jako superadmin:**

- Po przełączeniu na użytkownika `postgres`, uruchom konsolę PSQL poleceniem:

```bash
psql
```

- Alternatywnie, można bezpośrednio uruchomić PSQL jako użytkownik `postgres` bez przełączania się na niego:

```bash
sudo -u postgres psql
```

### 2. Konfiguracja dostępu (pg_hba.conf)

- Definiuje adresy IP i metody autoryzacji dla połączeń z bazą danych PostgreSQL

#### 2.1 Sprawdzenie lokalizacji pliku konfiguracyjnego w psql:

```sql
SHOW hba_file;
```

- W ww. plikie `pg_hba.conf` definiowane są zasady uwierzytelniania i kontroli dostępu do bazy danych PostgreSQL.

#### 2.2 Otwieranie konfiguracji pg_hba (przykład dla wersji 16):

```bash
sudo nano /etc/postgresql/16/main/pg_hba.conf
```

#### 2.3 Przeładowanie konfiguracji:

- Stosowane w przypadku zmian w pliku `pg_hba.conf` bez konieczności restartu całej usługi:

```bash
sudo systemctl reload postgresql
```

#### 2.4 Przeładowanie konfiguracji:

* Zdalne logowanie jest domyślnie zablokowane
* Katalog `conf.d` nadpisuje wcześniejsze ustawienia
* Opcja `hostssl` umożliwia logowanie przez SSL
* Zalecana alokacja RAM: **25%**, nie więcej niż **40%**
* WAL (Write-Ahead Logging) zapisuje każdą zmianę w logach

### \*3. Zarządzanie użytkownikami w PostgreSQL

Komenda DDL (Data Manipulation Language)                            | Opis działania
--------------------------------------------------------------------|----------------------------------------------
`CREATE USER nazwa_uzytkownika WITH PASSWORD 'haslo';`              | Tworzy nowego użytkownika z określonym hasłem
`ALTER USER nazwa_uzytkownika WITH PASSWORD 'nowe_haslo';`          | Zmienia hasło istniejącego użytkownika
`ALTER USER nazwa_uzytkownika WITH NOLOGIN;`                        | Blokuje możliwość logowania się użytkownika
`DROP USER nazwa_uzytkownika;`                                      | Usuwa użytkownika z bazy danych

Komenda DCL (Data Control Language) — Kontrola dostępu              | Opis działania
--------------------------------------------------------------------|----------------------------------------------
`GRANT ALL PRIVILEGES ON DATABASE nazwa_bazy TO nazwa_uzytkownika;` | Przyznaje wszystkie uprawnienia do danej bazy
`REVOKE ALL ON DATABASE nazwa_bazy FROM nazwa_uzytkownika;`         | Odbiera uprawnienia użytkownikowi do bazy

### \*4. Zarządzanie bazami danych

#### \*4.1 Podstawowe polecenia do zarządzania bazami danych

Komenda DDL (Data Manipulation Language)                | Opis działania
--------------------------------------------------------|--------------------------------------------------
`CREATE TABLE nazwa (kolumna typ |  ...);`              | Tworzy nową tabelę z określonymi kolumnami
`ALTER TABLE nazwa RENAME TO nowa_nazwa;`               | Zmienia nazwę istniejącej tabeli
`ALTER TABLE nazwa ADD COLUMN kolumna typ;`             | Dodaje nową kolumnę do istniejącej tabeli
`ALTER TABLE nazwa DROP COLUMN kolumna;`                | Usuwa kolumnę z tabeli
`ALTER TABLE nazwa ALTER COLUMN kolumna TYPE nowy_typ;` | Zmienia typ danych istniejącej kolumny
`DROP TABLE nazwa;`                                     | Całkowicie usuwa tabelę i wszystkie jej dane z bazy
`TRUNCATE TABLE nazwa;`                                 | Usuwa wszystkie rekordy z tabeli |  ale zostawia jej strukturę

#### \*4.2 Sprawdzenie rozmiaru bazy danych

```sql
SELECT pg_size_pretty(pg_database_size('nazwa_bazy_danych'));
```

#### \*4.3 Optymalizacja bazy danych

```sql
VACUUM;  -- Czyści „martwe” dane po DELETE/UPDATE, odzyskuje miejsce
ANALYZE; -- Aktualizuje statystyki dla optymalizatora zapytań
```

#### \*4.4 Tworzenie kopii zapasowej bazy danych

```bash
pg_dump -U nazwa_uzytkownika -F c -b -v -f "nazwa_bazy.backup" nazwa_bazy
```

---

## 2025.10.20 — Bezpieczeństwo i dobre praktyki

### Aspekty bezpieczeństwa

* IP Whitelisting: Ograniczaj dostęp tylko do konkretnych adresów IP w pliku `pg_hba.conf`
* Zmieniaj domyślne porty (domyślnie `5432`) i adresy nasłuchiwania
* **Bastion Host**: Wykorzystuj maszynę pośrednią o stałym IP (skoczka) do łączenia się z bazą wewnątrz sieci prywatne
* Przechowuj konfiguracje (pliki .conf) w repozytorium Git, aby śledzić zmiany

---

## 2025.10.27 — Narzędzie `psql` i ustawienia połączenia

### 1. Narzędzie `psql` (CLI)

- Jest to narzędzie, dzięki któremu komunikujemy się z bazą danych.
Pozwala na:  

* szybkie przeglądanie tabel,
* historia poleceń,
* możliwość wykonywania skryptów.

### 2. Polecenia pomocnicze (psql)

Komenda|Pełny zamiennik lub rozwinięcie znaczenia|Opis działania
-----|---------------------------------------|-----------------
`\l`   | `\list`                             | Lista baz danych
`\c`   | `\connect`                          | Połączenie z inną bazą danych
`\h`   | `\help`                             | Pomoc dla poleceń SQL
`\dn`  | `Display Namespaces`                | Lista schematów
`\df`  | `Data Function / Display Functions` | Lista funkcji 
`\dn+` | `Display Namespaces Plus`           | Szczegóły schematów (ACL - Access Control List (uprawnienia), właściciel)
`\?`   | `Internal Help`                     | Pomoc dla komend psql
`\d`   | `Describe`                          | Struktura tabeli/widoku
`\d nazwa_tabeli` | `Describe nazwa_tabeli`  | Struktura konkretnej tabeli/widoku
`\dx`  | `Display Extensions`                | Lista rozszerzeń
`\dt`  | `Display Tables`                    | Pokazuje tylko listę tabel
`\dv`  | `Display Views`                     | *Pokazuje tylko listę widoków
`\di`  | `Display Indexes`                   | *Pokazuje tylko listę indeksów
`\dp`  | `Display Privileges`                | *Pokazuje uprawnienia do tabel/widoków
`\dt+` | `Display Tables Plus`               | *Szczegóły tabel (rozmiar,  właściciel,  ACL)
`\i`   | `Include`                           | *Wykonuje skrypt SQL z pliku zewnętrznego
`\q`   | `Quit`                              | *Wyjście z psql
 
- Brak `\` oznacza że nie jest to polecenie lecz nazwa, z której wywodzi się polecenie

- Niektóre z wymienionych poleceń `psql` (np. `\h`) posiadają system nawigacji, działający podobnie jak w linuksowym `less`:

  * `Space` — przewija o jedną stronę w dół,
  * `b` — przewija o jedną stronę w górę,
  * `Enter` — przewija o jedną linię w dół.
  * Aby wyjść z `psql` wystarczy nacisnąć klawisz `q`

 - Można doinstalować rozszerzenia bazodanowe, pozwalające utworzyć np. bazy geodezyjne czy wektorowe itp. (widodne w `\dx`)

### 3. Łączenie z bazą i plik `.pgpass`

**3.1 Łączenie z lokalnym serwerem:**

```bash
psql -h 127.0.0.1 -p 5432
```

- 127.0.0.1 to twój lokalny adres IP (loopback)
- `5432` to domyślny port PostgreSQL, jeżeli został zmieniony, podaj odpowiedni numer portu

**3.2 Zmienne środowiskowe:**

- Ustawienie zmiennych środowiskowych pozwala na pominięcie podawania ich w poleceniu `psql`.

    * Dla nazwy użytkownika:
        ```bash
        export PGUSER=postgres 
        ```
    * Dla nazwy bazy danych:
        ```bash
        export PGDATABASE=postgres
        ```

**Plik `.pgpass`** z którego `psql` automatycznie pobiera:

* dane logowania według składni:
    ```bash
    hostname:port:database:username:password
    ```
* musi mieć uprawnienian tylko dla użytkownika:

    ```bash
    chmod 600 ~/.pgpass
    ```
* Istanieją gotowe szablony do generowania pliku `.pgpass`, zawierające konkretne uprawnienia

### 4. Zmiana portu (postgresql.conf)

**4.1 Sprawdzenie lokalizacji configu:**

```sql
SHOW config_file;
```

**4.2 Otwieranie konfiguracji config_file (gdzie xx to wersja PostgreSQL):**

```bash
sudo nano /etc/postgresql/xx/main/postgresql.conf
```

Zmień parametr `port` i zrestartuj usługę PostgreSQL
Poza tym można zmienić adresy IP, na których nasłuchuje PostgreSQL (parametr `listen_addresses`)

```sh
sudo systemctl restart postgresql
```

---

## 2025.11.03 — Typy danych i tabele

### 1. Typy danych w PostgreSQL

#### 1.1 Typy numeryczne (Numeric Types) 

Typ danych         | Alias         | Rozmiar  | Opis
-------------------|---------------|----------|--------------------------------------------
`smallint`         | `int2`        | 2 bajty  | Liczby całkowite (-32768 do +32767)
`integer`          | `int`, `int4` | 4 bajty  | Standardowy wybór dla liczb całkowitych
`bigint`           | `int8`        | 8 bajtów | Duże liczby całkowite
`decimal`          | `numeric`     | zmienny  | Dokładne liczby (np. do finansów)
`real`             | `float4`      | 4 bajty  | Liczba zmiennoprzecinkowa (niska precyzja)
`double precision` | `float8`      | 8 bajtów | Liczba zmiennoprzecinkowa (wysoka precyzja)
`smallserial`      | `serial2`     | 2 bajty  | Autonumeracja 1-32767
`serial`           | `serial4`     | 4 bajty  | Autonumeracja 1-2 mld
`bigserial`        | `serial8`     | 8 bajtów | Autonumeracja dla ogromnych tabel
`money`            | –             | 8 bajtów | Kwoty walutowe

#### 1.2 Typy znakowe (Character Types)

Typ danych             | Alias      | Długość   | Opis                                                                             
-----------------------|------------|-----------|--------------------------------------------
`character(n)`         | `char(n)`    | stała     | Zawsze zajmuje n znaków (dopełnia spacjami)
`character varying(n)` | `varchar(n)` | zmienna   | Tekst o ograniczonej długości do n
`text`                 | –          | zmienna   | Nieograniczony tekst

#### 1.3 Typy Data/Czas (Date/Time Types)

Typ danych  | Rozmiar   | Opis                                                                             
------------|-----------|-----------------------------------------------------
`date`        | 4 bajty   | "Tylko data (rok |  miesiąc |  dzień)."
`time`        | 8 bajtów  | Godzina bez daty.
`timestamptz` | 8 bajtów  | Data i godzina z uwzględnieniem strefy czasowej
`timestamp`   | 8 bajtów  | Data i godzina bez strefy czasowej
`interval`    | 16 bajtów | Przedział czasowy (np. 1 day 2 hours)

Jednostki i przedziały dla typu `interval`:
- `YEAR`
- `MONTH`
- `DAY`
- `HOUR`
- `MINUTE`
- `SECOND`
- `YEAR TO MONTH`
- `DAY TO HOUR`
- `DAY TO MINUTE`
- `DAY TO SECOND`
- `HOUR TO MINUTE`
- `HOUR TO SECOND`
- `MINUTE TO SECOND`

#### 1.4 Typy geometryczne (Geometric Types)

Nazwa   | Opis               | Format (przykład)   | Rozmiar
--------|--------------------|---------------------|-----------
point   | Punkt              | "(x, y)"            | 16 bajtów
line    | Linia nieskończona | "{A, B, C}"         | 32 bajty
lseg    | Odcinek            | "((x1,y1),(x2,y2))" | 32 bajty
box     | Prostokąt          | "((x1,y1),(x2,y2))" | 32 bajty
polygon | Wielokąt           | "((x1,y1), ...)"    | zmienny
circle  | Koło               | "<(x,y), r>"        | 24 bajty

#### 1.5 Typy sieciowe (Network Types)

Nazwa    | Opis                      | Przykład
---------|---------------------------|---------------------
inet     | Adres hosta IPv4/IPv6     | 192.168.1.1
cidr     | Adres sieci IPv4/IPv6     | 192.168.1.0/24
macaddr  | Adres MAC                 | 08:00:2b:01:02:03
macaddr8 | Adres MAC (format EUI-64) | 08-00-2b-ff-fe-01-02-03

#### 1.6 Inne typy dabnnych

Nazwa    | Opis                             | Uwagi
---------|----------------------------------|------------------------------
boolean  | Prawda / Fałsz (true/false)      | Zajmuje 1 bajt
uuid     | Unikalny identyfikator (128-bit) | Lepszy niż tekstowy odpowiednik
json     | Tekstowy format JSON             | Sprawdza tylko poprawność składni
jsonb    | Binarny format JSON              | Indeksowalny i nowszy i szybszy w obróbce od `json`
bytea    | Dane binarne (obrazy,  pliki)    | Przechowywane "as is"
pg_lsn   | Log Sequence Number              | Fizyczny adres w logach WAL
tsvector | Dokument do wyszukiwania         | Używany przy Full Text Search

* **Unikać używania `TEXT`**, gdyż może spowalniać bazę.

**`uuid`:**

* mniej przewidywalny niż ID numeryczne,
* składa się z kilku bloków,
* zawiera wartość czasu → lepsze sortowanie.

---

#### 1.7 Typy niestandardowe (Domain i Composite)

Cecha                    | DOMAIN (Domena)                                                                  | COMPOSITE TYPE (Typ złożony)
-------------------------|----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------
**Definicja**            | Rozszerzenie istniejącego już typu (np. INTEGER, TEXT) o dodatkowe ograniczenia  | Tworzenie zupełnie nowej struktury składającej się z wielu różnych pól (jak obiekt)
**Główny Cel**           | Walidacja danych (wymuszanie formatu, zakresu lub braku NULL)                   | Grupowanie danych (logiczne połączenie powiązanych informacji w jedną kolumnę)
**Przykładowa Składnia** | `CREATE DOMAIN nazwa AS typ_bazowy CHECK (warunek);` przykład warunku (val >= 0) | `CREATE TYPE nazwa AS (pole1 typ1,  pole2 typ2)`
**Przykład użycia**      | Weryfikacja kodu pocztowego, upewnienie się, że cena > 0                         | Przechowywanie adresu (ulica, miasto, kod) jako jednego elementu
**Wstawianie danych**    | Jak zwykły typ: `INSERT INTO ... VALUES ('00-001');`                             | Wymaga konstruktora ROW: `VALUES (ROW('Główna',  'W-wa',  '00-001'));`

---

## 2025.11.13:

### 1. Struktura początkowa i Domeny

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

#### Z 1.1 Utworzenie tabeli `questions` przechowującej pytania do formularzy.

 - **Wskazówka:** Staramy się tworzyć nazwy kluczy, aby identyfikowały się z nazwą tabeli (np. `fk_form`).

```sql
-- Tabela questions:
CREATE TABLE IF NOT EXISTS questions (
    question_id smallserial PRIMARY KEY,
    form_id INTEGER NOT NULL,
    question_text TEXT NOT NULL,
    question_type VARCHAR(50) NOT NULL, /* np text, rating, wybór itp. */
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_form -- CONSTRAINT stosuje się, kiedy chcemy nadać nazwę ograniczeniu (np. kluczowi obcemu)
        FOREIGN KEY(form_id)
            REFERENCES forms(form_id)
    ON DELETE CASCADE

    -- CASCADE Automatycznie usuwa powiązane rekordy w tabeli potomnej,
    -- gdy usunięty zostanie rekord w tabeli nadrzędnej
    
);
```

---

#### 1.2 Wprowadzanie Danych

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

#### 2.1 Dodanie kolumny `status`

#### 2.1.1 Dodanie kolumny `status` do tabeli `forms` z domyślną wartością `'draft'`.

```sql
-- Do tabeli forms dodajemy kolumnę status domyślnie jako 'draft'
ALTER TABLE forms ADD COLUMN status VARCHAR (20) DEFAULT 'draft';
```

#### 2.1.2 Dodanie nowego formularza (z domyślnym statusem)

```sql
-- Dodajemy nowy formularz bez podawania statusu
INSERT INTO forms (title, owner_id) VALUES
('Quiz', 1);
```

#### 2.1.3 Dodanie i aktualizacja `response_count`

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

### 3. Funkcje Agregujące i Grupowanie

#### 3.1 Obliczenia globalne (SUM, AVG, MAX, MIN)

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

#### 3.2 Grupowanie (`GROUP BY`)

Policzenie, ilu formularzy jest właścicielem każdy z użytkowników.

```sql
-- Aby policzyć ile formularzy ma każdy z użytkowników 
SELECT owner_id, count(*) AS number_of_forms
FROM forms
GROUP BY owner_id  
ORDER BY number_of_forms DESC;
```

## 2025-11-17

### 1. Kontynuacja zadań SQL

```sql
-- Wyświetlenie wszystkich formularzy i liczby formularzy na użytkownika
Select * From forms;
Select owner_id as user_id,
COUNT(*) AS total
FROM forms
GROUP BY user_id
ORDER BY total DESC;
```

```sql
-- Użytkownicy z więcej niż jednym formularzem
SELECT owner_id, count(1) as forms_count
FROM forms
GROUP BY owner_id
HAVING count(1) > 2;
```

```sql
-- Wyświetlanie formulaża z większą liczba odpowiedzi niż 2
SELECT form_id, COUNT(1) AS ile_pytan
FROM questions
GROUP BY form_id
HAVING COUNT(1) > 1;
```

```sql
--- użytkownicy którzy mają łącznie ponad 100 odpowiedzi
SELECT owner_id, count(1) as ile_forms, sum(response_count) as ile_odp
FROM forms
GROUP BY owner_id
HAVING sum(response_count) > 100;
```

```sql
-- Parametr WHERE 
SELECT owner_id, count (1) as ile_forms, AVG(response_count) as ile_odp
FROM forms WHERE status = 'draft'
GROUP BY owner_id HAVING SUM(response_count) > 100;
```

```sql
-- Wyświetlić albo obublikowane lub w draft z minimum 50 odpowiedzi
-- user =2 opublikowane lub więcej lub równe 50 odpowiedzi 
SELECT form_id, title, owner_id, status, response_count 
FROM forms WHERE owner_id = 2
AND (status='published' OR response_count >= 50);
```

Aby zabezpieczyć się przed SQL injection należy przekształcać dodać znak `'`.

```sql
-- Zabezpieczenie przed SQL injection
SELECT title FROM forms WHERE title = 'Quiz' ilike `o%`;
-- ilike - nie rozróżnia wielkości liter
```

```sql
-- Użycie like 
Select email FROM users WHERE email LIKE 'adam._@example.com'; 
-- _ zastępuje dokładnie jeden znak
```

```sql 
-- Dodanie użytkownika z email adam*
INSERT INTO users (email, password_hash) VALUES 
('adam2@example.com', 'hash123'),
('adam10@example.com', 'hash456');
```

### 2. Wyrażenia Regularne (Regex) w PostgreSQL

#### 2.1. W regex . oznacza dowolny znak w ilości jeden, * oznacza zero lub więcej wystąpień poprzedzającego znaku.

#### 2.2. Aby je wyłączyć w regex używamy `\` przed znakiem.

```sql
SELECT email FROM users WHERE email ~ 'adam\.';
-- \. oznacza dosłowną kropkę
```

#### 2.3. Nie uwzględnianie wielkości liter w regex

```sql
SELECT email FROM users WHERE email ~* 'ADAM\.';
-- ~* oznacza ignorowanie wielkości liter
```

#### 2.4. Przykład walidacji e-mail za pomocą regex

```sql
--- Weryfikacja e-mail z pomocą regex
SELECT email FROM users WHERE email ~ '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$';
-- %+ oznacza alias adresu e-mail (+), nie działają one wszędzie np. do konta w rozwiązaniach chmurowych
-- ^ - początek ciągu
-- $ - koniec ciągu
-- - oznacza zakres znaków lub liczb lub myślnik w nazwie domeny
-- trzeba zaremować kropkę w domenie \. by była interpretowana dosłownie jako kropka 
```

### 3. Tematy związane z JOIN'ami

Warzne jest to że za pomocą JOIN'ów jesteśmy w stanie połączyć ze sobą dane z różnych tabel na podstawie relacji między nimi.

```sql
-- Przykład użycia JOIN
SELECT f.title, u.email
FROM forms as f
INNER JOIN users as u
ON f.owner_id = u.user_id;
```

Teraz wyciągamy wszystkich użytkowników wraz z liczbą formularzy które posiadają, ci co nie mają mają mieć 0.

```sql
-- Użytkownicy z liczbą formularzy
SELECT u.user_id, u.email, COUNT(f.form_id) AS number_of_forms
FROM users AS u
LEFT JOIN forms AS f -- left join by uwzględnia wszystkich użytkowników
ON u.user_id = f.owner_id
GROUP BY u.user_id, u.email;
```

Aby pokazać wszystkich użytkowników i wszystkie formularze możemy użyć FULL OUTER JOIN.

```sql
-- FULL OUTER JOIN
SELECT u.user_id, u.email, f.form_id, f.title
FROM users AS u
FULL OUTER JOIN forms AS f
ON u.user_id = f.owner_id;
```

### 4. Polecenia UPDATE

#### 4.1. Dodajemy kolumnę owner_email do tabeli forms, UPDATE wstawia do niej odpowiednie wartości z tabeli users.

A. Dodanie kolumny `owner_email` do tabeli `forms`.

```sql
-- Dodanie kolumny owner_email do tabeli forms
ALTER TABLE forms ADD COLUMN owner_email VARCHAR(255);
```

B. Aby dodać adres e-mail właściciela do tabeli forms używamy UPDATE z JOIN. <br>
Jeżeli chodzi o update to używamy najpierw from potem set i where.

```sql
-- Aktualizacja kolumny owner_email w tabeli forms
UPDATE forms f -- alisa może być jako AS f
SET owner_email = u.email
FROM users AS u
WHERE f.owner_id = u.user_id;
```

C. Usuwanie wartości z formularza

```sql
-- Usuwanie pytań powiązanych z formularzem o form_id = 2
DELETE FROM questions q 
USING forms f
WHERE q.form_id = f.form_id AND f.form_id = 2;
```

Jak wyciągnąć dane z autoinkermentacji za pomocą RETURNING?

```sql
-- Wstawianie nowego użytkownika i zwrócenie user_id
INSERT INTO users (email, password_hash)
VALUES ('Sigma@kosos.pl', 'hash999')
RETURNING user_id;
-- można również dodać informację o utworzonym czasie
-- RETURNING user_id, created_at;
```

W bazach danych nie ma POP można usuwać z usunięciem wartości, możemy przy returning wyświetlić informacje o usuniętej wartości.

```sql
-- Usuwanie użytkownika i zwrócenie usuniętego emaila
DELETE FROM users
WHERE email = 'Sigma@kosos.pl'
RETURNING user_id, created_at;
```

## 2025-11-24

```sql
-- Wyświetlenie wszystkich użytkowników
SELECT * FROM users;

-- Dodanie kolumny manager_id do tabeli users
ALTER TABLE users ADD COLUMN manager_id INTEGER REFERENCES users(user_id);

-- Aktualizacja kolumny manager_id dla użytkowników
UPDATE users SET manager_id = 1 WHERE user_id IN (2, 3);

-- Wyświetlanie wszystkich formularzy i i ch właścicieli (email, title)
--Rigth JOIN
SELECT f.title, u.email
FROM forms AS f
RIGHT JOIN users AS u
ON f.owner_id = u.user_id;

-- to samo ale chce wszystkie dane z tabeli users i forms
SELECT u.user_id, u.email, f.form_id, f.title
FROM users u
FULL OUTER JOIN forms f
ON u.user_id = f.owner_id;

-- CROSS JOIN
-- Połączenie tabeli users, questions -- email i question_type
SELECT u.email, q.question_type
FROM questions q
CROSS JOIN users u;

-- Z DISTINCT (właszna wersja mało wydajna)
SELECT DISTINCT u.email, q.question_type
FROM questions q
CROSS JOIN users u;

-- Z DiSTINCT ON (wersja wykładowcy - bardziej wydajnq)
SELECT u.email, q.question_type
FROM users u
CROSS JOIN (SELECT DISTINCT question_type FROM questions) AS q;

-- email pracownika (), email przełożonego, jeżeli nie ma przełożonego to NULL
SELECT e.email AS employee_email, m.email AS manager_email
FROM users e
LEFT JOIN users m
ON e.manager_id = m.user_id;

-- Znajdż użytkowników, którzy nie stworzyli żadnego formularza z pytaniem typu 'rating'
SELECT u.user_id, u.email 
FROM users u 
WHERE NOT EXISTS (
    SELECT 1 
    FROM forms f 
    JOIN questions q ON f.form_id = q.form_id 
    WHERE f.owner_id = u.user_id 
    AND q.question_type = 'rating'
);

-- Dodanie użytkownika jeżeli nie istnieje a jeżeli istnieje to zaktualizuj hasło
INSERT INTO users (email, password_hash, created_at)
VALUES ('adam2@example.com', 'newhash1234', CURRENT_TIMESTAMP)
ON CONFLICT (email) DO UPDATE
SET password_hash = EXCLUDED.password_hash,
created_at = CURRENT_TIMESTAMP;

-- Transakcje i punkty przywracania (savepoints)

BEGIN;  -- Rozpoczęcie transakcji

-- 1. Zmiana adresu email
UPDATE users SET email='jan.kowalski.update@example.com' WHERE user_id=1;

-- 2. Utworzenie punktu przywracania (savepoint)
SAVEPOINT before_delete;

-- 3. Usunięcie formularza
DELETE FROM forms WHERE form_id = 1;

-- 4. Sprawdzenie, czy formularz został usunięty (powinno zwrócić 0 wierszy)
SELECT * FROM forms WHERE form_id=1;

-- 5. Cofnięcie zmian TYLKO do momentu zapisu "before_delete" (cofamy usunięcie)
ROLLBACK TO SAVEPOINT before_delete;

-- 6. Sprawdzenie, czy formularz wrócił (powinien znów być widoczny)
SELECT * FROM forms WHERE form_id=1;

-- 7. Sprawdzenie, czy email nadal jest zmieniony (zmiana sprzed savepointa powinna zostać)
SELECT email FROM users WHERE user_id = 1;

COMMIT;  -- Zatwierdzenie transakcji
```

### Zadanie z Transakcjami i Savepointami

```sql

-- Dodanie anna nowak (jeżeli brak w bazie)
INSERT INTO users (email, password_hash) VALUES
('anna.nowak@example.com', 'initial_password_hash');

-- Dodanie multiple-choice pytań (jeżeli brak w bazie)
INSERT INTO questions (form_id, question_text, question_type) VALUES
(1, 'Jakie są Twoje ulubione kolory?', 'multiple-choice'),
(1, 'Które z poniższych zwierząt lubisz najbardziej?', 'multiple-choice');

-- a. Rozpocznij transakcję
BEGIN;

-- b. Zaktualizuj password_hash dla użytkownika anna.nowak
UPDATE users
SET password_hash = 'bardzo_nowe_haslo'
WHERE email = 'anna.nowak@example.com';

-- c. Utwórz punkt przywracania (SAVEPOINT) o nazwie password_changed
SAVEPOINT password_changed;

-- d. Usuń wszystkie pytania typu 'multiple-choice'
DELETE FROM questions
WHERE question_type = 'multiple-choice';

-- e. Sprawdź, czy pytania zniknęły 
SELECT * FROM questions WHERE question_type = 'multiple-choice';

-- f. Wróć do SAVEPOINT password_changed.
ROLLBACK TO SAVEPOINT password_changed;

-- g. Sprawdź czy pytania wróciły.
SELECT * FROM questions WHERE question_type = 'multiple-choice';

-- 2. Czy hasło nadal jest zaktualizowane?
SELECT email, password_hash FROM users WHERE email = 'anna.nowak@example.com';

-- h. Zatwierdź transakcję
COMMIT;

```

### \*Przypomienie transakcji i savepointów

Komenda TCL (Transaction Control Language) — Transakcje | Opis działania
--------------------------------------------------------|------------------------------------------
`BEGIN;`                                                  | Rozpoczyna transakcję
`COMMIT;`                                                 | Zapisuje wszystkie zmiany na stałe
`ROLLBACK;`                                               | Wycofuje wszystkie zmiany (jeśli coś poszło nie tak)
`SAVEPOINT nazwa;`                                        | Tworzy punkt kontrolny wewnątrz transakcji
`ROLLBACK TO SAVEPOINT nazwa;`                            | Cofnięcie do określonego punktu kontrolnego

Błąd z transakcjami      | Opis błędu
-------------------------|------------------------------------------------
`deadlock`               | Gdy dwie transakcje wzajemnie na siebie czekają
`serialization_failure`  | Gdy transakcje próbują zmienić te same dane jednocześnie

## 2025-12-01

```sql
-- Oknna

-- Użycie CTE do wyświetlenia formularzy z liczbą pytań
WITH user_forms_ranked AS(
    SELECT owner_id, create_at, LAG(create_at, 1) OVER (PARTITION BY owner_id ORDER BY created_at) AS previous_form_date
    FROM forms f)
SELECT uf.owner_id, uf.created_at, uf.previous_form_date,
uf.create_at::date - uf.previous_form_date::date AS days_since_previous
FROM user_forms_ranked uf;

-- lista formularzy z ilością pytań Questions do danego formularza 
WITH form_question_counts AS (
    SELECT form_id, COUNT(*) AS question_count
    FROM questions
    GROUP BY form_id
)
SELECT f.form_id, f.title, f.owner_id, f.created_at, fqc.question_count
FROM forms f
LEFT JOIN form_question_counts fqc ON f.form_id = fqc.form_id;

```

```sql
-- SELECT 
-- question_text,
-- created_at,
-- count(*) OVER (PARTITION BY form_id ORDER BY created_at) as total_questions_in_forms,
-- ROW_NUMBER() OVER (PARTITION BY form_id ORDER BY created_at) as running_question_count
-- FROM questions;
-- WHERE form_id IN (SELECT form_id FROM forms WHERE title = 'Ankieta satysfakcji klienta' LIMIT 1);__

SELECT 
    question_text,
    created_at,
    COUNT(*) OVER (PARTITION BY form_id) AS total_questions_in_form,
    ROW_NUMBER() OVER (PARTITION BY form_id ORDER BY created_at) AS running_question_count
FROM 
    questions
WHERE 
    form_id = (
        SELECT form_id 
        FROM forms 
        WHERE title = 'Ankieta satysfakcji klienta'
        LIMIT 1 -- Zwraca tylko jeden pasujący wiersz
    );
```

```sql
-- Dla każdego z formularzy, pokaż ile formularzy łączeni ma dany właściciel
SELECT
    f.title,
    COUNT(*) OVER (PARTITION BY f.owner_id) AS ile
FROM
    forms f;
```

```sql
-- 2 opcja With
WITH ile AS (
    SELECT COUNT(1) AS ile, owner_id 
    FROM forms
    GROUP BY owner_id)
SELECT f.title, i.ile
FROM forms f, ile i
WHERE f.owner_id = i.owner_id;
```

1. Podzapytania CTE -- Common Table Expressions (WITH)

- Dobrze znać użycie operatorów logicznych AND, OR, NOT oraz IN, EXISTS.
- Oraz Joinów (INNER, LEFT, RIGHT, FULL, CROSS).

``` sql
-- Znaleść wszystkie formularze, które należą do urzytkowników z domeny 'example.com'

SELECT title,owner_id
From forms
WHERE owner_id IN (
    SELECT user_id
    FROM users
    WHERE email LIKE '%@example.com'
);
```

``` sql
-- Znaleść wszystkie emaile użytkowników, którzy posiadają przynajmniej jeden formularz
SELECT email
FROM users u
WHERE EXISTS (
    SELECT 1
    FROM forms f
    WHERE f.owner_id = u.user_id
);
```

``` sql
-- Znajdź formularze z liczbą pytań powyżej średniej
SELECT AVG(num_questions) FROM (SELECT COUNT(1) AS num_questions
    FROM questions
    GROUP BY form_id);
```

``` sql
-- Policzyć jeszcze ilość questions 
SELECT f.title,
q_counts.num_questions
FROM forms f
JOIN (
    SELECT form_id, COUNT(1) AS num_questions
    FROM questions
    GROUP BY form_id) AS q_counts
    ON f.form_id = q_counts.form_id
    -- część do pokazywania powyżej średniej
WHERE q_counts.num_questions >= (SELECT AVG(num_questions) FROM (SELECT COUNT(1) AS num_questions
    FROM questions
    GROUP BY form_id));
```

```sql
-- Użycie Rekurencji 
WITH RECURSIVE employee_hierarchy AS (
    -- Warunek początkowy:
    SELECT user_id, email, manager_id, 1 AS level
    FROM users
    WHERE manager_id = 1
    UNION ALL
    -- krok rekurencyjny:
    SELECT u.user_id, u.email, u.manager_id, eh.level + 1
    FROM users u
    INNER JOIN employee_hierarchy AS eh ON u.manager_id = eh.user_id
)
SELECT * FROM employee_hierarchy;

```

### 2025-12-15

Funkcje rozpoczna i kończy się znakiem $$
Za nim wpisujemy jaki język np dla psql jetst to plpgsql
Funkcje może przyjmować różne języki np sql, plpgsql, plpythonu itp.
OR REPLACE pozwala nadpisać istniejącą funkcję - i nie trzeba jej usuwać przed ponownym tworzeniem
\*STRICT nie zważając na NULL - jeżeli któryś z parametrów jest NULL to funkcja nie zostanie wywołana i zwróci NULL

```sql

CREATE FUNCTION OR REPLACE FUNCTION nazwa() RETURNS INT AS $$ -- dolar z przyczyn praktycznych
-- wyżej warto nienadpisywać istniejącej funkcji (w nazwa)
-- ciało funkcji
DECLARE -- zawsze jest przed daną funkcją
-- tu deklarujemy zmienne
    licznik INT := 0; -- operator przypisania := -- jest to zaszłość z Pascala
    -- jeżeli nie zdefiniujemy wartości to domyślnie jest NULL
BEGIN -- Rozpoczęcie transakcji
-- tu piszemy kod logiki
    RETURN licznik; -- zwrócenie wartości -- ważne aby kończyć to średnikiem
END;
$$ LANGUAGE plpgsql; -- porodbnie jek wyżej nie zapomnieć średnika
```

Uruchomienie funkcji:

```sql
SELECT nazwa(); -- select pozwala nam na wyeksportowanie pojedyńczej wartości
```

Usuwanie funkcji:

```sql
DROP FUNCTION nazwa();
```

-- Możeym zwracać różne typy od VOID (nic nie zwraca) po typy złożone (całe tabele).

Ciało funkcji jest ciągiem stringowym i możemy je zasztukować aby nikt nie podejrzał nam kodu.

#### Funkcje wbudowane w PostgreSQL

##### Funkcje stringowe

```sql
-- length - długość stringa
SELECT length('Progres'); 
-- concat - łączenie stringów
SELECT concat('Progres', 'SQL');
-- aby wstawuć separator używamy concat_ws
SELECT concat_ws('-', 'Progres', 'SQL', '2025');
-- upper - zamiana na wielkie litery
SELECT upper('progres sql');
-- lower - zamiana na małe litery
SELECT lower('Progres SQL');
-- substring - wyciąganie podłańcucha
SELECT substring('2025-12-15' FROM 1 FOR 4); -- od 1 znaku przez 4 znaki (rok)
-- replace - zamiana podłańcucha
SELECT replace('Progres SQL', 'SQL', 'Database');
-- position - pozycja podłańcucha
SELECT position('dobry' IN 'Jesteś dobry w bazach danych'); -- zwraca pozycję pierwszego znaku
-- trim - usuwanie białych znaków z początku i końca
SELECT trim('   Progres SQL   ');
-- split_part - dzielenie stringa na części
SELECT split_part('zaufany@email.com', '@', 2); -- zwraca drugą część po znaku '@'
```

##### Funkcje matematyczne

```sql
SELECT abs(-10); -- wartość bezwzględna
SELECT avg(10, 20, 30); -- średnia
SELECT round(3.14159, 2); -- zaokrąglenie do 2 miejsc po przecinku
SELECT ceil(4.2); -- zaokrąglenie w górę
SELECT floor(4.8); -- zaokrąglenie w dół
SELECT random(); -- losowa wartość z zakresu 0.0 do 1.0
SELECT power(2, 3); -- potęgowanie (2 do potęgi 3)
SELECT sqrt(16); -- pierwiastek kwadratowy
SELECT sign(-67); -- zwraca -1, 0 lub 1 w zależności od znaku liczby

CREATE OR REPLACE FUNCTION random_int()
RETURNS INT AS $$
BEGIN
    RETURN FLOOR(RANDOM() * 100+1)::INT; -- losowa liczba całkow
END;
$$ LANGUAGE plpgsql;
```

##### Funkcje daty i czasu

```sql
-- bierząca data
SELECT CURRENT_DATE;
-- bieżąca data i czas z dokładnością do mikrosekund
SELECT now() 
-- 
SELECT age()
-- wyciąganie danych z daty
SELECT date_part('month', now()); -- wyciąganie miesiąca z bieżącej daty
--  date_trunc - zaokrąglanie daty do określonej jednostki
SELECT date_trunc('month', now()); -- zaokrąglenie do początku miesiącd
-- make_date - tworzenie daty z podanych wartości
SELECT make_date(2025, 12, 31); -- tworzy datę '2025-12-31'::date

CREATE OR REPLACE FUNCTION is_weekend(d DATE)
RETURNS BOOLEAN AS $$
DECLARE
    day_num INT;
BEGIN
    day_num := EXTRACT(ISDOW FROM d); -- ISO day of week (1=Monday, 7=Sunday)
    RETURN day_num IN (6, 7); -- 6 = Saturday, 7 = Sunday
END;
$$ LANGUAGE plpgsql;
```

##### Funkcje formatujące

```sql
-- to_char - formatowanie daty lub liczby do stringa
SELECT to_char(now(), 'YYYY-MM-DD HH24:MI:SS'); -- formatowanie
-- to_date - konwersja stringa do daty
SELECT to_date('2025-12-15', 'YYYY-MM-DD'); -- rzutowanie stringa na datę
-- to_number - konwersja stringa do liczby
SELECT to_number('12345.67', '99999.99'); -- rzutowanie stringa na liczbę

--::type cast -- '123'::INT -- rzutowanie stringa na int
SELECT CAST('123' AS INT); -- alternatywna składnia rzutowania
```

#### 5. Funkcje warunkowe

```sql
-- COALESCE - zwraca pierwszą nie-NULL wartość z listy
SELECT COALESCE(NULL, NULL, 'Pierwsza nie-NULL wartość', 'Inna wartość');
-- NULLIF - zwraca NULL jeśli dwie wartości są równe
SELECT NULLIF(10, 10); -- zwraca NULL
SELECT NULLIF(10, 5);  -- zwraca 10
-- CASE - instrukcja warunkowa
SELECT
    CASE
        WHEN warunek THEN wynik1
        WHEN inny_warunek THEN wynik2
        ELSE domyślny_wynik
    END;

-- Przykład użycia z kolumną
SELECT form_id,
    CASE
        WHEN response_count >= 100 THEN 'Popularny'
        WHEN response_count >= 50 THEN 'Średnio popularny'
        ELSE 'Mało popularny'
    END AS popularity
FROM forms;
```

#### Funkcje agregujące:

```sql
-- COUNT - liczy liczbę wierszy
SELECT COUNT(*) FROM forms;
-- SUM - suma wartości w kolumnie
SELECT SUM(response_count) FROM forms;
-- AVG - średnia wartość w kolumnie;
SELECT AVG(response_count) FROM forms;
-- MIN - minimalna wartość w kolumnie
SELECT MIN(response_count) FROM forms;
-- MAX - maksymalna wartość w kolumnie
SELECT MAX(response_count) FROM forms;
-- STRING_AGG - łączy wartości stringów z grupy w jeden string
SELECT STRING_AGG(title, ', ') FROM forms;
-- ARRAY_AGG - tworzy tablicę z wartości kolumny
SELECT array_agg(title) FROM forms; -- zwraca tablicę tytułów
-- json_agg - tworzy tablicę JSON z wartości kolumny
SELECT json_agg(row_to_json(forms)) FROM forms; -- zwraca tablicę JSON obiektów
```

#### Podsumowanie

Jakie są pluy stosowania funkcji w PostgreSQL?

Zamiast używać api do przetwarzania danych, możemy to zrobić bezpośrednio w bazie danych za pomocą funkcji.
Zmniejsza to ilość przesyłanych danych i obciążenie aplikacji klienckiej.
Spójność danych jest lepiej utrzymywana, ponieważ logika biznesowa jest scentralizowana w bazie danych.
Można wtedy odpytywać api bezpośrednio z bazy danych.
Bezpieczeństwo -- slq injection jest trudniejsze do przeprowadzenia, gdy logika jest w bazie danych.
Można stworzyć funkcje, które mają określone uprawnienia dostępu.

```SQL
-- Przykład funkcji zliczającej liczbę danych w formularzu
CREATE OR REPLACE FUNCTION get_question_count(form_id_in INT)
RETURNS BIGINT AS $$
-- nie trzeba deklarować zmiennej jeżeli nie jest potrzebna (działać bezpośrednio na danych z zapytania)
    SELECT COUNT(1)
    FROM questions 
    WHERE form_id = form_id_in;
$$ LANGUAGE sql; -- język sql jeżeli nie ma logiki proceduralnej jak w plpgsql

-- Wywołanie funkcji
SELECT get_question_count(1); -- zwraca liczbę pytań dla formularza o form_id = 1
```


Zadanie -- chcemy nadać status użytkownikowi na podstawie liczby formularzy które posiada.

```sql
-- Tworzenie funkcji nadającej status użytkownikowi
CREATE OR REPLACE FUNCTION get_user_status(user_id_in INT) -- warto podwać inną niż w tabeli nazwę zmiennej 
RETURNS VARCHAR AS $$
DECLARE
    form_count INT;
    user_status VARCHAR;
BEGIN
    -- chcemy wiedzieć ile formularzy ma użytkownik
    SELECT COUNT(1) INTO form_count -- użycie into przypisze ilość formularzy do zmiennej form_count
    FROM forms
    WHERE owner_id = user_id_in;

    IF form_count >= 5 THEN
        user_status := 'GOLD PARTNER';
    ELSIF form_count >= 0 THEN
        user_status := 'SILVER PARTNER';
    ELSE user_status := 'BRONZE PARTNER';
    END IF;
    RETURN user_status;
END;
$$ LANGUAGE plpgsql;

-- Wywołanie funkcji
SELECT get_user_status(1); -- zwraca status użytkownika o user_id = 1
```

Funkcja przejścia po wierszach oddzielonego średnikami

```sql
CREATE OR REPLACE FUNCTION list_user_forms(user_id_in INT)
RETURNS TEXT AS $$
DECLARE
    r RECORD; -- zmienna do przechowywania wiersza
    output TEXT := ''; -- zmienna do przechowywania wyniku
BEGIN
    FOR r IN
        SELECT title
        FROM forms
        WHERE owner_id = user_id_in
    LOOP-- pętla po wierszach
        output := output || r.title || ';'; -- || służy do konkatenacji (łączenia) stringów
    END LOOP;
    RETURN output;
END;
$$ LANGUAGE plpgsql;

-- Wywołanie funkcji
SELECT list_user_forms(1); -- zwraca tytuły formularzy użytkownika o user_id = 1 oddzielone średnikami
```

## 2026-01-12
Napisz funkcję generate_order_code(user_id INT), która wygeneruje kod zamówienia w formacie: ORD-[ROK]-[ID_USERA]-[LOSOWE_3_CYFRY]. Przykład: ORD-2023-15-492

```sql
CREATE OR REPLACE FUNCTION generate_order_code(user_id_in INT)
RETURNS TEXT AS $$
DECLARE
    current_year INT;
    random_number INT;
    order_code TEXT;
BEGIN
    -- Aktualny rok
    current_year := EXTRACT(YEAR FROM CURRENT_DATE); -- EXTRACT służy do wyciągania części daty
    -- LOSOWE_3_CYFRY
    random_number := FLOOR(RANDOM() * 900) + 100; -- losowa liczba od 100 do 999
    -- Formatowanie ORD-[ROK]-[ID_USERA]-[LOSOWE_3_CYFRY]
    order_code := FORMAT('ORD-%s-%s-%s', current_year, user_id_in, random_number);
    RETURN order_code;
END;
$$ LANGUAGE plpgsql;
-- Wywołanie funkcji
SELECT generate_order_code(15); -- Przykład wywołania dla user_id = 15
```

Procedury

"Bardziej rozszeżona funkcje" funkcje wywołuje się przez Select, a procedurę wywołuje się przez CALL.
Select musi zwracać jakść wartość, 
a procedura nie musi musieć zwracać wartości.

Trasnakcyjność
Jeżeli chodzi o transakcje to można zarządzać transackcjami
Nie można jej używać w formacie zapytaniowym np. join, select itp.

Służą do:
Operacji biznesowych itp.
Archiwizacja i czyszczenie danych

Może nią być

Gdy chcemy wykonać wielokrokową operację
Możemy albo nie użyć jej jako transakcji albo nie i zapisać commitem.

Jeżeli proces wymaga złożonych działąń

Jeżeli chodzi o składnię to:

```sql

CREATE OR REPLACE PROCEDURE nazwa_procedury(parametry)
LANGUAGE plpgsql AS $$
DECLARE
    -- deklaracje zmiennych
BEGIN
    -- ciało procedury
END;

$$;
```

Zadanie:

```sql
--dodaj nowego użytkownika
--  user_id |              email              |   password_hash   |          created_at           | manager_id 
-- ---------+---------------------------------+-------------------+-------------------------------+------------
CREATE OR REPLACE PROCEDURE user_add( 
    user_email VARCHAR(255),
    user_password_hash TEXT,
    manager_id INT
)
LANGUAGE plpgsql AS $$
-- TUTAJ NAPRAWIAMY BŁĄD: Deklaracja zmiennej lokalnej
DECLARE
    manager_email_found VARCHAR(255);
BEGIN
    -- 1. Sprawdzenie, czy użytkownik już istnieje
    IF EXISTS (
        SELECT 1 FROM users WHERE email = user_email
    ) THEN
        -- RAISE EXCEPTION służy do zgłaszania błędów w procedurze bez przerwania działania 
        RAISE EXCEPTION 'Użytkownik %, już istnieje w tabeli users', user_email;
    END IF;

    -- 2. Wstawienie nowego rekordu
    INSERT INTO users (email, password_hash, manager_id)
    VALUES (user_email, user_password_hash, manager_id);

    -- 3. Pobranie emaila managera
    -- Używamy prostej konstrukcji IF, aby uniknąć błędów przy NULL
    IF manager_id IS NOT NULL THEN
        SELECT email INTO manager_email_found 
        FROM users 
        WHERE user_id = manager_id;

        -- Jeśli manager_id nie istnieje w bazie (np. błędne ID)
        IF manager_email_found IS NULL THEN
            manager_email_found := 'Nieznany (brak w bazie)';
        END IF;
    ELSE
        manager_email_found := 'Brak (użytkownik root)';
    END IF;

    -- 4. Informacja zwrotna
    RAISE NOTICE 'Dodano użytkownika: %', user_email;
    RAISE NOTICE 'Manager: % (ID: %)', manager_email_found, manager_id;
END;
$$;

-- Wywołanie procedury
CALL user_add('Przyklad@poczta.pl', 'hash_example', NULL);
```

Zadanie2 : Procedura tworząca nam formularz

```sql
CREATE OR REPLACE PROCEDURE create_form_with_questions(
    p_owner_id INT,
    p_title form_title,
    p_questions TEXT[],
    INOUT p_form_id INT DEFAULT NULL,
    INOUT p_questions_count INT DEFAULT NULL
)
LANGUAGE plpgsql AS $$
DECLARE
    v_question TEXT;
BEGIN
    p_questions_count := array_length(p_questions, 1);
    
    -- utwórz formularz
    INSERT INTO forms (title, owner_id)
    VALUES (p_title, p_owner_id)
    RETURNING form_id INTO p_form_id;
    
    -- dodaj pytania
    FOREACH v_question IN ARRAY p_questions
    LOOP
        INSERT INTO questions (form_id, question_text, question_type)
        VALUES (p_form_id, v_question, 'text');
    END LOOP;
    
    RAISE NOTICE 'Utworzono formularz ID: % z % pytaniami', p_form_id, p_questions_count;
END;
$$;

-- Aby wywołać procedurę i uzyskać wartości OUT, możemy użyć bloku DO
DO $$
DECLARE
    v_new_form_id INT;
    v_count INT;
BEGIN
    CALL create_form_with_questions(1, 'Nowy Formularz', ARRAY['Pytanie 1', 'Pytanie 2'], 
    v_new_form_id, v_count);
    RAISE NOTICE 'Form ID: %, Questions Count: %', v_new_form_id, v_count;
END;
$$;


-- Wywołanie procedury
CALL create_form_with_questions(1, 'Nowy Formularz', ARRAY['Pytanie 1', 'Pytanie 2']);
```

## 2026-01-19

Kiedy używwać triggerów?

-- do automatyzacji
-- do audytów
-- do walidacji przed zapisem
    -- gdy dodajemy parametr to może on weryfikować dane i uzupełniać inne dane
    -- soft delete --przenoszenie do archiwum (zamiast usuwania)

Nie używać triggerów PSQL do:
-- prostej walidacji -- lepiej użyć
-- logiki biznesowej -- lepiej użyć procedur składowanych
-- do raportowania -- lepiej użyć narzędzi ETL lub dedykowanych

```sql

CREATE OR REPLACE FUNCTION nazwa_logiki_dla_triggera()
RETURNS TRIGGER AS $$

BEGIN
    -- logika triggera
    RETURN NEW; -- lub RETURN OLD/Null w zależności od typu triggera
    -- przy tworzeniu mamy 
    -- insert - NEW.nazwa_kolumny 
    -- update - NEW.nazwa_kolumny, OLD.nazwa_kolumny (wartość nadpisywana)
    -- delete - tylko OLD.nazwa_kolumny (wartość usuwana)
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER nazwa_triggera()
{BEFORE} -- kiedy ma się uruchamiać (BEFORE|AFTER|INSTEAD OF)
{INSERT} -- na jakiej operacji ma działać INSERT|UPDATE|DELETE

FOR EACH ROW -- dla każdego  (ROW|STATEMENT)
[WHEN ()] -- opcjonalny warunek uruchomienia triggera np czy hasło nie było użyte wcześniej

EXECUTE FUNCTION nazwa_logiki_dla_triggera();
```

Zmienne są:
OLD - zmienna ROW, wartość przed zmianą
NEW - wartość po zmianie
TG_OP - operacja która wywołała trigger (INSERT, UPDATE, DELETE)

Możemy zrobić warunek typu

TG_TABLE_NAME = 'nazwa_tabeli'
TG_TABLE_SCHEMA = 'nazwa_schematu''
TG_WHEN = 'BEFORE' lub 'AFTER'
TG_LEVEL = 'ROW' lub 'STATEMENT'
TG_NARGS = liczba argumentów przekazanych do triggera
TG_ARGV - tablica argumentów przekazanych do triggera

IF TG_OP = 'INSERT' THEN
ELSIF TG_OP
END IF;

-- Przykład triggera, który nie pozwala na usunięcie użytkownika jeżeli posiada formularze

```sql
-- Funkcja triggera
CREATE OR REPLACE FUNCTION prevent_user_deletion()
RETURNS TRIGGER AS $$
DECLARE
    v_form_count INT;
BEGIN
    -- logika triggera
    -- Sprawdzenie czy użytkownik posiada formularze
    SeLECT COUNT(1) INTO v_form_count
    FROM forms
    WHERE owner_id = OLD.user_id; -- OLD bo delite

    -- Jeżeli ma to wyrzuć błąd
    IF v_form_count > 0 THEN
        RAISE EXCEPTION 'Nie można usunąć użytkownika %, ponieważ posiada % formularzy. Najpierw przenieś lub usuń formularze.', OLD.email, v_form_count;
    END IF;

    RETURN OLD; -- zwarcamy OLD bo usuwamy ID'ka, w returnie można przypisać to co chcę więc można usunąć nie to co chcemy
END;
$$ LANGUAGE plpgsql;


-- Wyzwalacz

CREATE TRIGGER trg_user_prevent_deletion

BEFORE 

DELETE ON users

FOR EACH ROW

EXECUTE FUNCTION prevent_user_deletion();

```

Cel: Zablokuj możliwość publikacji formularza (is_published = true), jeśli właściciel formularza (users.is_active) jest nieaktywny.

Stwórz funkcję check_owner_active().
Pobierz status właściciela z tabeli users na podstawie NEW.owner_id.
Jeśli użytkownik nieaktywny i NEW.is_published jest prawdą -> RAISE EXCEPTION.
Podepnij trigger BEFORE INSERT OR UPDATE do tabeli forms.

```sql
-- Utworzenie tabeli users i forms, jeżeli nie istnieją
CREATE TABLE IF NOT EXISTS users (user_id SERIAL PRIMARY KEY, email TEXT, is_active BOOLEAN DEFAULT true);
CREATE TABLE IF NOT EXISTS forms (form_id SERIAL PRIMARY KEY, owner_id INT, title TEXT, is_published BOOLEAN DEFAULT false);
```

```sql
-- Dostowowanie istniejących tabel do zadania
ALTER TABLE users ADD COLUMN IF NOT EXISTS is_active BOOLEAN DEFAULT true;
ALTER TABLE forms ADD COLUMN IF NOT EXISTS is_published BOOLEAN DEFAULT false;
```

```sql
-- Zadanie 
-- Cel: Zablokuj możliwość publikacji formularza (is_published = true), jeśli właściciel formularza (users.is_active) jest nieaktywny.

-- Stwórz funkcję check_owner_active().
CREATE OR REPLACE FUNCTION check_owner_active()
RETURNS TRIGGER AS $$
DECLARE
    v_is_active BOOLEAN;
BEGIN
    -- Pobierz status właściciela 
    SELECT is_active INTO v_is_active
    -- z tabeli users 
    FROM users
    -- na podstawie NEW.owner_id.
    WHERE user_id = NEW.owner_id;

    -- Jeśli użytkownik nieaktywny
    IF v_is_active = false 
    -- i NEW.is_published jest prawdą 
    AND NEW.is_published = true THEN
    -- -> RAISE EXCEPTION.
        RAISE EXCEPTION 'Publikacja formularza jest niemożliwa: Właściciel jest nieaktywny.';
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql; 

-- Podepnij trigger 
CREATE TRIGGER trg_check_owner_active
-- BEFORE INSERT OR UPDATE do tabeli forms.
BEFORE INSERT OR UPDATE ON forms
FOR EACH ROW
EXECUTE FUNCTION check_owner_active();
```

AD. do opisu parametrów INSTEAD OF, używamy tylko w widokach (VIEW).

Zadanie 2: 
Cel: Loguj zmiany tytułów formularzy do nowej tabeli title_history, ale tylko wtedy, gdy tytuł faktycznie się zmienił.
Stwórz tabelę title_history (form_id INT, old_title TEXT, new_title TEXT, changed_at TIMESTAMP).
Stwórz funkcję logującą.
Podepnij trigger AFTER UPDATE na tabeli forms.
Kluczowe: Użyj klauzuli WHEN, aby trigger nie uruchamiał się, gdy zmieniono tylko pole is_published, a tytuł został ten sam.

```sql
-- Stwórz tabelę title_history (form_id INT, old_title TEXT, new_title TEXT, changed_at TIMESTAMP).
CREATE TABLE IF NOT EXISTS title_history (
    form_id INT, 
    old_title TEXT, 
    new_title TEXT, 
    changed_at TIMESTAMP
);

-- Stwórz funkcję logującą.
CREATE OR REPLACE FUNCTION log_wgen_title_change()

RETURNS TRIGGER AS $$

BEGIN
    -- Wstawienie rekordu do title_history
    INSERT INTO title_history (form_id, old_title, new_title, changed_at)
    VALUES (NEW.form_id, OLD.title, NEW.title, CURRENT_TIMESTAMP);
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Podepnij trigger AFTER UPDATE na tabeli forms.
CREATE TRIGGER trg_log_title_change
AFTER UPDATE ON forms
FOR EACH ROW
-- Kluczowe: Użyj klauzuli WHEN, aby trigger nie uruchamiał się, gdy zmieniono tylko pole is_published, a tytuł został ten sam.
WHEN (OLD.title IS DISTINCT FROM NEW.title)  -- IS DISTINCT FROM sprawdza czy wartości są różne, uwzględniając NULL
EXECUTE FUNCTION log_wgen_title_change();
```

Trochę o JSON i JSONB

JSON -- Tekstowy, nieindeksowalny, trudniejszy do parsowania

JSONB -- Binarny, indeksowalny, szybszy w parsowaniu

```sql
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    specs JSONB -- Tu dzieje się magia
);

INSERT INTO products (name, specs) VALUES
('Laptop Pro', '{ "cpu": "M1", "ram": "16GB", "ports": ["usb-c", "hdmi"], "available": true }'),
('Running Shoes', '{ "size": 42, "color": "red", "brand": "Nike", "available": true }'),
('Smart Watch', '{ "brand": "Apple", "features": {"gps": true, "lte": false} }');
``` 

- Aby się odwoływać 
    * -> operator -> zwraca JSON w cudzysłowie

    * ->> operator ->> zwraca czysty tekst

```sql
SELECT name, specs->>'ram' AS ram
FROM products
WHERE specs? 'ram'; -- sprawdza czy klucz istnieje
```

Tworzenie indeksu na danym JSON'ie

```sql
CREATE INDEX idx_products_specs on products USING GIN (specs); -- jest to wyszukiwanie "full table scan"
```

-- @> - oznacza "zawiera"

```sql
SELECT * FROM products
WHERE specs @> '{"available": true}'; -- sprawdza czy specs zawiera dany fragment JSON

SELECT * FROM products
WHERE specs @> '{"brand": "Apple"}'; -- sprawdza czy specs zawiera dany fragment JSON
```

Wyszukiwanie zagnieżdżonych elementów

```sql
UPDATE products
SET specs = jsonb_set(specs, '{features, lte}', 
'true'::jsonb)
WHERE name = 'Smart Watch';
```

Aby usuwać zagnieżdżone elementy
- `-` -- usuwa klucz z JSON'a

```sql

UPDATE products
SET specs = specs - '{available}'   
WHERE name = 'Laptop Pro';
```

## 2026-01-26 - Indexy i Optymalizacja Zapytan

- Indeksu powodóją szybsze wyszukiwanie danych w tabeli
- Działają zn zasadzie tworzenia dodatkowego pliku, który posiada metadane o lokalizacji danych w tabeli w przestrzeni dyskowej
- Indeksy mogą być tworzone na pojedynczych kolumnach lub na wielu kolumnach (indeksy złożone)

```sql
INSERT INTO users (email, password_hash, manager_id)
SELECT 'user' || i || '@test.com', -- generuje email
md5(random()::text), -- generuje hash hasła
1
FROM generate_series(1, 1000000) AS i; -- generuje 1 milion użytkowników
```

```sql
EXPLAIN ANALYZE
SELECT * FROM users WHERE email = 'user500000@test.com';
```

```sql
ALTER TABLE users DROP CONSTRAINT IF EXISTS users_email_key; -- usunięcie unikalnego indeksu jeżeli istnieje

CREATE INDEX idx_users_email_lower ON users(LOWER(email)); -- tworzenie unikalnego indeksu na kolumnie email

-- Użycie lower bardzo przyśpiesza wyszukiwanie caseinsitive 
```

```sql
ALTER TABLE forms ADD COLUMN IF NOT EXISTS is_active BOOLEAN DEFAULT true;
UPDATE forms SET is_active = false WHERE form_id % 2 = 0; -- ustawienie co drugiego formularza jako nieaktywny
```

```sql
CREATE INDEX idx_forms_active ON forms(owner_id) WHERE is_active = true; -- indeks częściowy na aktywne formularze

-- Stosowane ponieważ źle tworzone indeksy potrafią ważyć więcej niż sama tabela (marnowanie przestrzeni dyskowej)
```

Jak wykorystać taki index?

```sql
EXPLAIN ANALYZE
SELECT * FROM forms WHERE owner_id = 1 AND is_active = true;
```

