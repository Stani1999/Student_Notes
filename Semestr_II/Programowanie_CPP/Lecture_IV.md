## **Wykład IV (13.03.2025)**  

### **IV. 1. Stringi w C**

#### **Reprezentacja**
- Tablica znaków `char[]` zakończona znakiem `'\0'` (null terminator)
- Wymagają ręcznego zarządzania pamięcią

#### **Podstawowe operacje**

**Inicjalizacja:**
```c
char str1[6] = "Hello";  // Statyczna alokacja
char *str2 = malloc(6 * sizeof(char)); // Dynamiczna alokacja
strcpy(str2, "World");
```

**Łączenie stringów:**
```c
char title[] = "Hello";
char unit[] = "World";

// 1. Obliczanie wymaganej pamięci
size_t len = strlen(title) + strlen(unit) + 1; // +1 dla '\0'

// 2. Alokacja pamięci
char *output = malloc(len);
if (output == NULL) {
    // Obsługa błędu alokacji
}

// 3. Kopiowanie
strcpy(output, title);
strcat(output, unit);

// 4. Użycie
printf("%s", output); // "HelloWorld"

// 5. Zwolnienie pamięci
free(output);
```

**Typowe problemy:**
- Zapomnienie o null terminatorze
- Przepełnienie bufora
- Wycieki pamięci (zapomnienie o `free`)

### **IV. 2. Stringi w C++ (`std::string`)**

#### **Reprezentacja**
- Klasa `std::string` z biblioteki standardowej
- Automatyczne zarządzanie pamięcią

#### **Podstawowe operacje**

**Inicjalizacja:**
```cpp
#include <string>

std::string s1 = "Hello";
std::string s2("World");
std::string s3(5, 'x'); // "xxxxx"
```

**Łączenie stringów:**
```cpp
std::string title = "Hello";
std::string unit = "World";

// Łączenie - 3 różne sposoby
std::string result1 = title + " " + unit; // "Hello World"
std::string result2 = title.append(unit); // "HelloWorld"
title += " " + unit; // "Hello World"
```

**Inne częste operacje:**
```cpp
// Długość stringa
size_t len = s1.length(); // lub s1.size()

// Dostęp do znaków
char c = s1[0]; // 'H'
char c2 = s1.at(0); // Bezpieczniejsza wersja

// Porównywanie
if (s1 == s2) { /* ... */ }

// Wyszukiwanie
size_t pos = s1.find("ell"); // Zwraca pozycję lub std::string::npos
```

#### **Porównanie C vs C++**

| **Cecha**              | **C**                                  | **C++ (`std::string`)**                     |
|------------------------|----------------------------------------|---------------------------------------------|
| **Reprezentacja**      | Tablica `char[]` + null terminator     | Klasa `std::string`                         |
| **Alokacja pamięci**   | Ręczna (`malloc`, `free`)              | Automatyczna                                |
| **Łączenie stringów**  | `strcat`, ręczne alokacje              | Operator `+`, `append()`                    |
| **Bezpieczeństwo**     | Niskie (ryzyko błędów)                 | Wysokie (automatyczne zarządzanie)          |
| **Wygoda użycia**      | Niska (funkcje z `string.h`)           | Wysoka (metody obiektowe)                   |

#### **Przykład konwersji między C a C++**

**Z `std::string` na C-style:**
```cpp
std::string cpp_str = "Hello";
const char* c_str = cpp_str.c_str(); // Tylko do odczytu!
```

**Z C-style na `std::string`:**
```cpp
const char* c_str = "World";
std::string cpp_str(c_str); // Automatyczna konwersja
```

#### **Zaawansowane techniki w C++**

**Rezerwacja pamięci:**
```cpp
std::string s;
s.reserve(100); // Rezerwuje pamięć dla 100 znaków
```

**Manipulacje:**
```cpp
s.substr(2, 5); // Zwraca podciąg
s.replace(0, 3, "Hi"); // Zamienia fragment
s.erase(5, 3); // Usuwa fragment
```

**Wczytywanie całych linii:**
```cpp
std::string line;
std::getline(std::cin, line); // Wczytuje całą linię
```

### **IV. 3. Struktury i Klasy w C**

#### **1. Podstawowe różnice**

| **Cecha**               | **Struktura (`struct`)** | **Klasa (`class`)**    |
|-------------------------|--------------------------|------------------------|
| **Domyślny dostęp**     | `public`                 | `private`              |
| **Typowe zastosowanie** | Przechowywanie danych    | Hermetyzacja + logika  |
| **Dziedziczenie**       | Domyślnie `public`       | Domyślnie `private`    |
| **Semantyka**           | "Zbiór danych"           | "Obiekt z zachowaniem" |

#### **2. Struktury w C i C++**

**W C:**
```c
struct Point {
    int x;
    int y;
};

// Użycie:
struct Point p1;  // Wymagane słowo kluczowe 'struct'
p1.x = 10;
```

**W C++ (ulepszenia):**
```cpp
struct Point {
    int x;
    int y;
    
    void print() {  // Metody dozwolone!
        cout << x << ", " << y;
    }
};

// Użycie:
Point p1;  // 'struct' nie jest wymagane
p1.x = 10;  // Domyślnie public
p1.print();
```

#### **3. Klasy w C++**

**Podstawowa składnia:**
```cpp
class BankAccount {
private:  // Domyślnie, można pominąć
    double balance;
    string owner;

public:
    // Konstruktor
    BankAccount(string name) : owner(name), balance(0) {}
    
    // Metody
    void deposit(double amount) {
        balance += amount;
    }
    
    void display() const {  // const - nie modyfikuje obiektu
        cout << owner << ": " << balance << " PLN";
    }
};

// Użycie:
BankAccount acc("Jan Kowalski");
acc.deposit(1000);
acc.display();
```

#### **4. Konstruktory i destruktory**

**Wspólne dla struct i class:**
```cpp
struct Student {
    string name;
    int age;
    
    // Konstruktor
    Student(string n, int a) : name(n), age(a) {}
    
    // Destruktor
    ~Student() {
        cout << "Usuwam studenta " << name;
    }
};
```

**Przykład klasy z zarządzaniem zasobami (RAII):**
```cpp
class FileHandler {
    FILE* file;
public:
    FileHandler(const string& filename) {
        file = fopen(filename.c_str(), "r");
        if (!file) throw runtime_error("Nie można otworzyć pliku");
    }
    
    ~FileHandler() {
        if (file) fclose(file);
    }
    
    // Usunięcie możliwości kopiowania
    FileHandler(const FileHandler&) = delete;
    FileHandler& operator=(const FileHandler&) = delete;
};
```

#### **5. Dziedziczenie**

**Domyślne zachowanie:**
```cpp
struct Base { int x; };
struct Derived : Base {};  // Domyślnie public inheritance

class BaseClass { int x; };
class DerivedClass : BaseClass {};  // Domyślnie private inheritance
```

**Przykład praktyczny:**
```cpp
class Animal {
protected:
    string name;
public:
    Animal(string n) : name(n) {}
    virtual void speak() = 0;  // Czysta funkcja wirtualna
};

class Dog : public Animal {
public:
    Dog(string n) : Animal(n) {}
    void speak() override {
        cout << name << " says: Woof!";
    }
};
```

#### **6. Kiedy używać struct vs class?**

**Używaj `struct` gdy:**
- Grupujesz pasywne dane (np. Point, Rectangle)
- Chcesz domyślny dostęp publiczny
- Tworzysz prosty typ wartościowy

**Używaj `class` gdy:**
- Implementujesz abstrakcję z zachowaniem
- Wymagana jest hermetyzacja danych
- Implementujesz wzorce projektowe

#### **7. Zaawansowane techniki**

**Struktury z metodami statycznymi:**
```cpp
struct MathUtils {
    static double pi() { return 3.14159; }
};
// Użycie:
double p = MathUtils::pi();
```

**Klasy z przyjaźnią:**
```cpp
class SecretKeeper {
    int secret;
    friend class BestFriend;  // Przyjazń
};

class BestFriend {
public:
    static void peek(const SecretKeeper& sk) {
        cout << "Znam sekret: " << sk.secret;
    }
};
```

#### **8. Wydajność**

- **Struct/class bez wirtualności**: Brak narzutu (jak w C)
- **Z wirtualnymi metodami**: Dodatkowy wskaźnik do vtable
- **Porada**: Używaj `final` gdy dziedziczenie nie jest potrzebne:
  ```cpp
  class NoMoreDerived final { /* ... */ };
  ```

**Źródło:** Wykład 4 - Programowanie w C++, Konrad Kosmatka

---