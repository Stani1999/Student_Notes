# **Przygotowanie bazy PostgreSQL**

## **Zabezpieczenie**

Użytkownik **`postgres`** jest domyślnym, powszechnie znanym kontem superadmina w każdej instalacji PostgreSQL. Korzystanie z niego bezpośrednio zmniejsza bezpieczeństwo — atakujący zna już nazwę użytkownika i musi odgadnąć tylko hasło.

Tworząc i używając osobnego, unikatowego konta superadmina (`u_<Twoj_Nr_Legitymacji>`), zwiększasz bezpieczeństwo, ponieważ atakujący musi odgadnąć zarówno **nazwę użytkownika**, jak i **hasło**. To podstawowa reguła Defence in Depth (obrona w głąb).

---

### Krok 1: Logowanie do PostgreSQL jako domyślny superadmin (`postgres`)

Aby móc utworzyć nowe konto superadministratora (`u_<Twoj_Nr_Legitymacji>`), musisz najpierw zalogować się jako domyślny użytkownik PostgreSQL — **`postgres`**.

Zrobisz to poleceniem:

```bash
sudo -u postgres psql
```

Po jego wykonaniu znajdziesz się w konsoli:

```
postgres=#
```

i możesz wykonywać polecenia administracyjne, takie jak tworzenie nowego użytkownika, baz danych czy zmiana uprawnień.

---

### Krok 2: Utworzenie nowego Superadmina

#### 1. W konsoli `psql` (zalogowany jako superadmin, np. `postgres`) wykonaj:

```sql
-- Utworzenie nowego użytkownika superadmina
CREATE USER u_<Twoj_Nr_Legitymacji> 
WITH PASSWORD 'SilneHasloStudenckie!' 
SUPERUSER;
```
#### 2. Możesz teraz opuścić pqsl, aby to zrobić wpisz poniższą komendę:

```sql
\q
```

---

### Krok 3: Konfiguracja automatycznego logowania (.pgpass) 

Dzięki plikowi `.pgpass` nie będziesz musiał wpisywać hasła za każdym razem.

#### A. Utworzenie pliku

```bash
touch ~/.pgpass
```

#### B. Ustawienie właściwych uprawnień

PostgreSQL akceptuje `.pgpass` tylko jeśli ma on uprawnienia:

```bash
chmod 600 ~/.pgpass
```

#### C. Dodanie wpisu logowania

Edytuj plik:

```bash
nano ~/.pgpass
```

Dodaj wpis:

```text
# host:port:baza:użytkownik:hasło 
localhost:5432:*:u_<Twoj_Nr_Legitymacji>:SilneHasloStudenckie!
# * oznacza możliwość logowania się do dowolnej bazy 
```

Zapisz plik.

---

### Krok 4: Ustawienie logowania hasłem (zmiana `peer` → `md5`)

W niektórych systemach operacyjnych — szczególnie **Ubuntu** i innych dystrybucjach Linux — PostgreSQL domyślnie używa metody uwierzytelniania **`peer`**.
Oznacza to, że logowanie jest możliwe *tylko wtedy*, gdy **nazwa użytkownika systemowego = nazwa użytkownika PostgreSQL**, a hasło jest ignorowane.

Aby móc logować się jako `u_<Twoj_Nr_Legitymacji>` **z użyciem hasła**, musisz zmienić metodę logowania na **`md5`**.

---

#### 1. Sprawdź lokalizację aktywnego pliku `pg_hba.conf`

W konsoli `psql` wpisz:

```sql
SHOW hba_file;
```

Zwróci to np.:

```
/etc/postgresql/16/main/pg_hba.conf
```

To właśnie **ten** plik musisz edytować.

---

#### 2. Edycja `pg_hba.conf` — zmiana metody logowania

Otwórz wskazany plik:

```bash
sudo nano /etc/postgresql/16/main/pg_hba.conf
```

Znajdź linię podobną do:

```
local   all             all                                     peer
```

Zmień `peer` na `md5`:

```
local   all             all                                     md5
```

**Wyjaśnienie:**
Metoda `md5` umożliwia logowanie przy użyciu nazwy użytkownika PostgreSQL i hasła — co jest konieczne, jeśli logujesz się jako `u_<Twoj_Nr_Legitymacji>` z dowolnego konta systemowego.
Bez tej zmiany `psql` może odrzucać połączenia, nawet jeśli hasło jest poprawne.

---

#### 3. Restart PostgreSQL (WAŻNE!)

Po zapisaniu pliku wykonaj:

```bash
sudo systemctl restart postgresql
```

---

### Krok 5: Utworzenie bazy danych `rbd`

Zaloguj się jako nowy superadmin:

```bash
psql -U u_<Twoj_Nr_Legitymacji>
```

Następnie utwórz bazę:

```sql
CREATE DATABASE rbd;
```

---

### Krok 6: Łączenie się z bazą danych

Dzięki `.pgpass` nie będzie wymagane hasło:

```bash
psql -U u_<Twoj_Nr_Legitymacji> -d rbd #nazwa użytkownika musi zaczynać się literą, wszystkie małe!!!
```

* `-U u_<Twoj_Nr_Legitymacji>` – wskazuje użytkownika
* `-d rbd` – wskazuje bazę

---

### Krok 7: (Wykonaj opcjonalne) Zablokowanie konta `postgres`

**Zrób ten krok dopiero wtedy, kiedy potwierdzisz, że możesz poprawnie zalogować się jako `u_<Twoj_Nr_Legitymacji>` i masz pełne uprawnienia superadministratora.**

Aby uniemożliwić logowanie się na domyślne konto:

```sql
ALTER USER postgres WITH NOLOGIN;
```

### Przywracanie w razie potrzeby

Jeśli chcesz odblokować konto `postgres` (z nowego konta superadmina):

```sql
ALTER USER postgres WITH LOGIN;
```