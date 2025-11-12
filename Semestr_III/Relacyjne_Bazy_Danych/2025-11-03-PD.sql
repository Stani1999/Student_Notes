-- Zadanie 1: ENUM dla dni tygodnia
CREATE TYPE days_of_week AS ENUM (
  'poniedziałek',
  'wtorek',
  'środa',
  'czwartek',
  'piątek',
  'sobota',
  'niedziela'
);

-- Zadanie 2: Typ złożony dla osoby
CREATE TYPE full_name AS (
  first_name TEXT,
  last_name  TEXT
);

-- Zadanie 3: Walidacja adresu e-mail
CREATE DOMAIN email_address AS TEXT
CHECK (
   VALUE ~ '.+@.+'
);

--Zadanie 4: Tabela z własnym typem
CREATE TABLE contacts (
  id SERIAL PRIMARY KEY,
  person full_name
);

-- Dodawanie rekordu
INSERT INTO contacts (person)
VALUES (ROW('Jasper', 'Zalewski'));

-- Zadanie 5: Domena dla oceny w skali 1-10
CREATE DOMAIN rating_scale AS smallint
CHECK (
   VALUE BETWEEN 1 AND 10
);

-- Zadanie 6: Typ złożony dla produktu w magazynie
CREATE TYPE inventory_item AS (
  product_name TEXT,
  price        NUMERIC(10, 2),
  quantity     INTEGER
);

-- Zadanie 7: Stwórz numer telefonu
CREATE DOMAIN us_phone_number AS VARCHAR(15)
CHECK (
   VALUE ~ '^\(\d{3}\) \d{3}-\d{4}$'
);

-- Zadanie 8: Tabela z tablicą typów złożonych
CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  items inventory_item[]
);

-- Zadanie 9: Stwórz domenę bez wartości NULL
CREATE DOMAIN non_empty_text AS TEXT
DEFAULT '(brak)'
NOT NULL
CHECK (VALUE <> '');   -- eliminuje możliwość wpisania 'pustego stringa'

-- Zadanie 10: Modyfikacja typu ENUM
ALTER TYPE days_of_week
ADD VALUE 'Dzień Roboczy'
BEFORE 'poniedziałek';

-- Zadanie 11: Zagnieżdżony typ złożony
CREATE TYPE employee AS (
  contact_info full_name,
  position     TEXT
);

-- Zadanie 12: Domena dla "silnego" hasła
CREATE DOMAIN strong_password AS TEXT
CHECK (
   LENGTH(VALUE) >= 8
   AND VALUE ~ '[0-9]'
   AND VALUE ~ '[a-z]'
   AND VALUE ~ '[A-Z]'
);

-- Zadanie 14: Domena oparta na innej domenie
CREATE DOMAIN privileged_email AS email_address
CHECK (
   VALUE LIKE '%@admin.example.com'
);
