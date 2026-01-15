# Programowanie obiektowe 1 

## 2025-10-08 <br> Wykład I

Elementy programowania obiektowego

- hermetyzacja

- abstrakcja –  

- dziedziczenie

- polimorfizm

- klasa – szablon definiujący własności pola i jego zachowanie (metody, funkcje)

 W klasie występuje konstruktor i destruktor klasy, pola zawierają atrybuty o stanie obiektu

JDK – służy do tworzenia oprogramowania

JRE – do wykonania

JVM – Wirtualny do otwierania kodu w innym systemie

Będziemy używać edytorem wysokiego poziomu  

Interigej  -- specyficzna platforma, która ma już wszystko, nawet budowanie formularza z zewnętrznego oprogramowania.

Eclipse Java  

NetBeans – plus że pobiera sam program JDK

Każdy kompilator zostawia znak wodny przy kompilacji programu, który zawiera informacje o tym z jakiej licencji korzystał twórca

 JFrame -- okno główne aplikacji

Button (x,y,xdelta,zdelta) – umieści przycisk na współżendnych x,y o rozmiarach xdelta,ydelta.

- Obiekt (np. konkretna instancja klasy, struktua)

## 2025-10-14

Ćwiczenia I

Intellij  -- instalacja z archiwum zip – brak pakietu instalcyjnego na Linux Mint 

Bite short int long int

Pytanie o wyjaśnienie reprezentacji liczby w java’ie char

Nont a number  

Aby wyświetlić \ należy w string’u napisać \\

## 2025-10-15 <br> Wykład II

Funkcja trim (odetnij  -- znajdź jak się pisze)

Funkcja round zaokrągla (może do określonej pozycji po przecinku)

Java enumerated – wyliczeniowy (tablica susecyjna)

Null – nie oznacza pusty, to jest obiekt (wartość specjalna) – obiekt nie jest z niczym powiązany.

W javie jest klasa scaner zamiast cin jak w C++

System jest klasą której nie trzeba importować  

W javie jest metoda consola w której nie ujawnia się wpisywany tekst np. jak hasło w linux (terminal Sudo).

Printf – jest bardziej zaawansowany od cout – możemy w nim formatować liczby, stosując swego rodzaju znaczniki, można robić konkretne typy danych np. d dla decimal (prezentacja dziesiętna)

Zasięg blokowy (przepływ sterowania) to te jebane klamerki.

Instrukcja warunkowa pełna(if + else) i półpełna (samo if)

Pętle – warunek sprawdzany na wejściu lub wyjściu.

Wybór wielokierunkowy (instrukcja wyboru), jest to inny byt jak instrukcja warunkowa np. switch-case

Backpoint – brake – instrukcje przerywające działanie  

2025-10-21
Ćwiczenia II

Pierdolenie o tym ,że będziemy robić sprawozdania na tydzień poprzedzający kolokwium.

System.out.println()

Metoda System podmetoda out

Klasa Skaner we = new (gdzie new to nowa instancja klasy, która została wcześniej już zdefiniowana, nowy obiekt)

Java sama się pozbywa nieużywanych obiektów -- Garbage colection  

Całość  

Import java.util.Scaner;
Scaner we = new Scaner(System.in);
String imie = we.nextLine(); 
we.close(); 

Skorzystać z łączenia łańcuchów concate, do łączenia imienia z klawiatury wraz z poprzednio napisanym (tydzień temu) Hellow. 

 

Aktualnie nie używa się pętli do obsługi błędów 
Do tego stosuje się aktualnie wyjątki Try-catch  

Próba dodania Consloe liczba = System.console() 

 

Czy można skożystać z czegoś innego niż try catch ,  

Aby program działał z obsługą CLI musi być skompilowany z terminala a nie środowiska graficznego. 

 

2025-10-22 
Wykład III 

- Prosty 

- Zorientowany obiektowo 

- Jest sieciowy – można zbudować architekturę klient – serwer 

- Jest niezawodny 

- Jest bezpieczny 

- Niezależny od architektury, przenoszalna 

- Interpretowany – nie jest trudny w nauczeniu aby zrozumieć – interpreter Javy może wykonać każdy kod binarny… 

- Jest wysokowydajny, wielowątkowy – potrafi sobie poradzić z wielordzeniowym procesorem 

- Jest dynamiczny 

(Offtop) TopCat – usługa serwera otwierająca na porcie program w przeglądarce (otwiera je z archiwum zip na wybranym porcie) 

Java jako obiekt obiektowy został napisany od zera. 

 

Java nadzoruje pamięć komputera, została pozbawiona wskaźników, odbywa się on przez referencje. „Bezpieczny wskaźnik,” wydzielony obszar który jest nie do ruszenia. 

Każda próba dostępu do pamięci jest kontrolowana. 
Automatyczne sprzątanie nieużywanych obiektów (GabrydżColekszyn) 
Java przez rezerwację pamięci może  zamulać sprzęty o małej jej ilości. 

Jest stosunkowo niewielka – pomyślana dla małych urządzeń np. do zegarka. 

Jest stosunkowo szybka – w porówna z językami interpretowanymi ale wolniejsza od języka C, np. przy komunikacji sieciowej 

W niektórych przypadkach w momencie pisania wynik pojawia się z latencją, C nie ma tego problemu. 

Może korzystać z bibliotek napisanych w innych językach. 

Środowiska wysokoprogramowe, kiedy piszemy klasę bądź coś innego to przy dostępie do Internetu mogą pobrać je automatycznie nawet w czasie działania programu 

Maszyna może robić kompilacje w tak zwanym locie (podczas pracy programu) 

W przypadku intelij i java, od razu jest tworzony wykonywalny plik binarny. 

W android Studio Kotlin jest uruchamiany na środowisku Java pod spodem. 

Można się spotkać z aplikacjami desktopowymi, graficznie z biblioteki swing, java fx, Maven 

Środowisko działające w trybie konsoli, 

Współpracuje z bazami danych, najlepiej działa ze swoją (Oracle) 

ORACLE CSE – darmowa wersja bazy danych. 

DB2 – stara baza danych (być może kiedyś wywodziła się z Paradox) 

 

Przepływ sterowania,  w niektórych przypadkach można zdefiniować przerwanie pętli przy jej zapętleniu  

Jest coś takiego jak wielkie liczby Big Intiger i Big Decimal – obie są klasami.  

Daje więc radę z bardzo dużymi liczbami. 

Java w porówniaiu do C ma API Stream, do środowisk graficznych. 

 

Inicjacja zmiennej tablicowej w JAVA  
int a[] lub  
int [] a , obie wersje są poprawne  

 

Powołanie tablicy: 
int [] tab = new	 
	int[5];   - jest to rezerwacja tablicy do 5 znaków w tym przypadku int 

5 Element to pozycja o index’ie 4 (liczy się od 0) 

Pętla for each przeszukuje dany obszar i kończy działanie, w Javie podaje się kolekcje, z której mamy czytać, np. listę. 
for (el:a) 
{ 
	System.out.println(el); 

} 

Wypisze wszystkie elementy z a, może to być lista, struktura itp, kończy on tam, gdzie znajdzie el w przeszukiwanym obszarze, Warto dodać tekst aby sprawdzić czy ten for się wykona 
Programiści odeszli od słowa in dal tej pętli, ponieważ jest on używany w System.in, 
Przetwarza elementy tablicy, ale nie wartości, odczytuje co jest pod daną pozycją, ale jej to nie interesuje. 

Istnieje coś takiego jak kopiowanie tablicy (w takim przypadku obie zmienne wskazują na tą samą tablicę). 

W Java jest możliwość tworzenia tablic anonimowych –  
int [] a = {1,2,3,4,5} 
 

SmallPrine 

= int[] {1,2,3,4,5} , opcja skrócona. 

Metody w klasie Arryas .sort(a) – służy do sortowania 
Jest to metoda algorytmiczna QS   

Tablica dwuwymiarowa (już wielowymiarowa ) 
a = int [] [] {1,2,3,4,5} 

W C występuje tablica wielowymiarowa posiadającą jeszcze podtablicę. 
W Java nie ma prawdziwych tablic wielowymiarowych, są one symulowane przez tablicę tablic. 
„Tablica postrzępiona” –  odwoływanie się do podtablic, przechowywanych w poziomach zejścia. Tablice są więc tworzone dynamicznie, 
Ita tablica jest częścią Ytej tablicy 
Każda tablica może mieć różną długość. 

AD. Z dnia 2025-10-29: 

 

 

 

 
 

 

 

2025-10-28 
Ćwiczenia III 

Plik txt jest najtrudniejszy w obróbce ponieważ nie wiemy jaka będzie jego zawartość. 

Aby zaczytać plik w Java używamy funkcji Scaner: 

 

Temat poboczny związany z programowaniem: 
Programowanie w przemyśle jest bardzo znacząca, należy wykonywać oprogramowanie według wytycznych, aby nie dostać etykiety wilczego bilety, jeżeli coś z samowolki. 
Można jednak rzucać propozycje 

AD. 2025-10-29: 

Dlaczego nie można stosować innych klas lub funkcji, która nie jest zalecana. 
Ponieważ zdarzają się stare klasy, mogą mieć status duplicatet, i zna jej lukę to może dobrać się przez taką metodę uzyskać dostęp do naszego kodu. 
Np. mysqli_ jest metodą nowszą, zabezpieczoną w porównaniu do mysql_. 
Linux jeżeli używa się tylko środowiska konsolowego to domyślnie nie sprawdza aktualizacji, 
W GUI są aplikacje pilnujące aktualizacji, dając użytkownikowi wybór czy chce je przeprowadzić. 

CVE – to baza podatności, jeżeli się tam pojawi wpis to producent  

 

 

2025-10-29 
Wykład IV 

Klasa – jest to szablon z którego tworzy się obiekty. 
Konstruując obiekt robimy instancje klasy. 
W języku C main musi wystąpić, kompilator nie uruchomi programu. 
W java nazwa pliku musi pokrywać się z nazwą klasy, co zastępuje main’a. 
W podstawowej bibliotece Java, istnieje dużo predefiniowanych klas.  
Służą one do odwoływania się w kodzie aby nie powielać ich treści itp. 

Każdy obiekt ma inną metodę, niektóre mogą mieć podobne lub takie same, 
Pytanie czy jest tego sens? 

Kluczowe pojęcie związane z obiektami to Hermetyzacja. 
Jest to w przypadku programowania ukrywanie danych. 
Umieszczanie danych w jednym pakiecie i ukrywanie danych implementacyjnych przed użytkownikiem. 
Dane, które są zawarte w obiekcie to składowe obiektu a operują na nich metody. 
Zestaw takich wartości określa się aktualnym stanem obiektu, który w czasie może się zmienić. 

Aby hermetyzacja spełniała swoje zadanie to składowe klas nie mogą być wywoływane na inne niż klasa własne. 
Dane obiektowe powinny być używane tylko za pośrednictwem danych obiektu zawierających te dane. 

Jeżeli jedna metoda jest niebezpieczna to wtedy powinna być napisana od nowa, a użytkownik powinien zaprzestać z jej korzystać. 

Klasy można budować przez tak zwane rozszerzenie (to znaczy na podstawie innych klas). 
EXTENDED 
Kiedy rozszerzamy kolejną klasę to ona dziedziczy wszystkie cech od poprzedniej 
Nowe metody pola są dostępne tylko w nowej klasie  
Odbywa się wtedy tak zwane dziedziczenie. 

Obiekty – Trzy podstawowe cechy: 

Zachowanie. 

Stan obiektu – jak reaguje na wywoływane przez nas metody. 
Każdy obiekt przechowuje informacje jak aktualnie wygląda z punktu widzenia kodu 
Może mieć wpływ na jego zachowanie. 

Tożsamość obiektu – jak odróżnić go od innych obiektów. 

Obiekt może być zmieniany ale niesamodzielnie, musi być ona wynikiem wywołania metody, jeżeli do tego doszło to złamano hermetyzację – ktoś się włamał. 

Obiekt może odmówić wykonania metody, która może dodać lub usunąć dane. 
Np. może zatrzymać wysłanie nieopłaconego lub pustego zamówienia.  

(Dezasemblacja klasy)  

W systemie proceduralnym musi być tak zwana góra a w obiektowym nie  (sprawdź) 

Netykieta -- ??  
Zalecany dodatek JAVA FORM DESIGNER. 

 

2025-11-04 
Ćwiczenia V 

Zamiana struktury poprzedniego kodu, służącego do wypisania pliku. 
Wniosek : Kiedy nie będziemy mogli załadować pliku można skorzystać z sourcePath.toAbsolutePath(); - i odczytać z niego ścieżkę. 

W JAVA pętla for może mieć konstrukcję jak w C ale też for each. 

Formatowanie czasu. Pisanie programu zakończyło się niepoprawnym wyświetlaniem formatu daty. Celem rozwiązania użyto metody toZonedDateTime()  

 
Rozpoczęcie programu z gotowego skryptu  
https://codegym.cc/pl/groups/posts/pl.660.klasa-java-util-date 
Example zamieniono na nazwę pliku, resztę parametrów odczytano z tablicy 
 

Na początku używano funckji Calendar, po czym zmieniono ją na  
GregorianCalendar: 

``` 
GregorianCalendar dur = new GregorianCalendar(2025,Calendar.NOVEMBER,05); 
System.out.println(dur.toZonedDateTime()); 
``` 

Teraz chcemy aby zwróciło nam mniej szczegółw, aktualnie zwraca : 
``` 
2025-11-05T00:00+01:00[Europe/Warsaw] 
```  
Chcemy uzyskać jedynie część dotyczącą dnia miesiąca i roku. 

Aby to zrobić zmieniono kod na 
``` 
GregorianCalendar gc = new GregorianCalendar(2025,Calendar.NOVEMBER,05);  
Date d = gc.getTime();  
System.out.println(d);  
DateTimeFormatter dtf = DateTimeFormatter.ofPattern("dd-MM-YYYY"); System.out.println(gc.toZonedDateTime().format(dtf));  
``` 

Wielkość liter ma znaczenie przy dużym dd zamiast 05 otrzymałem 309 

 

2025-11-05 
Wykład V 

Technika proceduralna : Zaczyna się od funkcji main (w CPP) 
W systemie obiektowym nie ma tego w wymaganiach (tak zwanej góry) 
Kompilator potrafi się upominać, że go nie ma 
Należy tu utworzyć klasy i nadać im metody. Np. System.out… 
Można to utożsamiać z Firmą, który zatrudnia podwykonawcę, który może posiadać kolejnego, rzadko zdarza się potrójne podwykonanie. 

Zasada nadawania nazw klasą – przeważnie przez rzeczownik. 
A metody można nazywać jako czasownik np. nextLine 
 
Dziedziczenie – (ciekawostka:  można dziedziczyć jedno pokolenie dalej) 

Zależność to zwizek który używa 

NP. Klasa zamówienie będzie używała klasy Konto, np. w celu zweryfikowania czy klient jest wypłacalny. 

Produkt nie jest powiązany z klasą konto, nie potrzebuje ono informacji do którego klienta należy. 

Zatem powiązania dotyczą klas zależnych od siebie, jeżeli metody jednej klasy używają obiektów drugiej klasy. 

Liczbę klas należy ograniczać do tak zwanego minimum 
Zmiany w klasie B nie wypływają na działanie klasy A – w oprogramowaniu jest to stopień powiązania między klasami 
 

Agregacja to związek który zawiera. 

Np. elementy na fakturze, id produktów i ich jednostki. 

W niektórych przypadkach istnieje asocjacja 

Może być to związek tabeli 

 

Dziedziczenie – związek który ma ze sobą Jest. 

Jest to wyrażenie związku pomiędzy klasą ogólną a klasą specjalną 
NP. Klasa szybkich zamówień (bez konta), może dziedziczyć wszystkie atrybuty lub tylko część z klasy zamówienia, np. atrybut add. 

W java’ie jeżeli klasa rozszerza to klasa pierwsza dziedziczy metody po klasie drugiej i może mieć od niej większe możliwości 

NP. Klasa trójkąt równoboczny i kwadrat może posiadać ten sam parametr tutaj bok 

 

 

Diagramy klas języka UML – stosuje się przy przekazywaniu kodu 

Symbol 

Znaczenie 

Opis 

Linia prosta i grot (→) 

dziedziczenie / generalizacja 

Klasa z grotem (trójkąt pusty) jest nadklasą (superklasą), a klasa bez grotu — podklasą (subklasą). Przykład: Student → Osoba. 

Linia przerywana i grot (---▷) 

realizacja (interface implementation) 

Klasa implementuje interfejs. Grot (trójkąt pusty) wskazuje interfejs, linia przerywana łączy go z klasą implementującą. 

Linia przerywana i znak „>” (----->) 

zależność (dependency) 

Oznacza, że jedna klasa używa drugiej (np. jako parametr metody, lokalny obiekt). Zależność jest luźna i nietrwała. 

«…» linia ciągła (np. «include», «extend») 

Stereotyp 

Używany do oznaczenia rodzaju relacji lub klasy specjalnego typu (np. «interface», «entity», «control», «boundary»). 

Linia ciągła 

asocjacja 

Oznacza trwały związek między klasami — jedna klasa ma odniesienie (pole) do drugiej. 

Ciągła linia z grotem (→) 

asocjacja skierowana 

Wskazuje kierunek powiązania – np. Klient → Zamówienie oznacza, że obiekt Klient zna swoje Zamówienia, ale nie odwrotnie. 

 
 

2025-11-12 
Wykład 

Klasy predefiniowane np. math 

Najpierw sprawdzić czy klasa istnieje i dopiero wtedy ją tworzyć 

Definiowanie klas 

Każda klasa ma w sobie metodę, 

Programy mogą składać się z więcej niż jednej klasy 

Zawsze musi istnieć jedna klasa główna tzw. main 

Prosta struktura klasy 
Class NK 
{ 
pole;  
… 
konstruktor;  
… 
metoda; 
} 

Każda klasa może mieć wiele pól, konstruktorów i metod. 

Podczas kompilacji tego kodu w programie powstaną nam bitkody dla main oraz utworzonej klasy. 

Kompilator buduje plik wyjściowy lecz w przypadku zmiany nazwy klasy wystąpi błąd (np. nie można usuwać bitkodu klasy), próba odwołania zakończy się wtedy błędem 

Możemy wpisywać własne komentarze w przypadku wystąpienia błędu. 

Warto wrzucać do pliku z logiem wszystkie błędy. 

Podczas uruchomienia klasy wydając polecenie interpreter tworzy obiekty w momencie ich wywołania. Przed tym interpreter zawsze włącza jedynie main. 

Kompilator jeżeli patern się zgadza to może nam skompilować program dopasowując wszystkie do symbolu wieloznacznego (*) to każdy się skompiluje oraz będą to pliki z rozszerzeniem class  

Kiedy kompilator napotka na klasę pracownik w pliku to będzie poszukiwał pliku który ma powstać, jeśli go nie znajdzie to poszuka kodu źródłowego, który skompiluje. 

W momencie kompilacji głównego pliku kompilator automatycznie znajdzie różnice w sygnaturze to skompiluje ją jeszcze raz. 

Jeżeli jakaś klasa nie będzie użyta to nie podda jej kompilacji, musi być do niego odwołanie np. w przypadku referencji  

Kompilator da błąd jeżeli metoda będzie z małej litery 

Konstruktor jest zawsze wykonywany przy operatorze new 

Obiekty w java są przechowywane na stercie 

Kompilator sam podpowie, kiedy stosować new 

Należy pamiętać aby nie tworzyć zmiennej lokalnej o nazwie pola klasy. 

Konstruktor zadeklaruje dwie zmienne o tej samej nazwie (jak pola) – będą one dostępne wyłącznie w konstruktorze w taki przypadku będą one „przesłaniane” pola klasy o tych samych nazwach 
Jeśli się tego nie dopilnuje można to znaleźć zastawiając tzw pułapki (jest to trudne) 

Przykładowa klasa 
```java 
class Pracownik 
{ 
// pola początek 
private String imie; 
private double waga; 
private int id; 

private date gur  			// godzina urodzenia 
private GregorianCalendar dur; 	// data urodzenia  
//pola koniec 
// konstruktor początek 

public Pracownik (String s, double w, int i_d, Date hdb, GC bd)  
// Konstruktor musi się nazywać jak nazwa jego klasy 
{ 

imiee= s  

waga = w 

id = i_d 
		GC dur = new GC(yyyy-mm-dd 

// powinno się pojawić set(do przypisania) oraz get(do otrzymania) 

} 

//koniec konstruktora 

//początek metod 

public String get Imie // w przypadku metod pisze się z dużej litery 

{ 

Return Imie; 

} 

} 

//koniec 

// w przypadku użycia set używa się operatora This 

// Ta metoda przypisywała by wartość do zmiennej 
``` 
Odczytanie samej wartości bez podania konkrety nie zwraca nic a zajmuje miejsce w pamięci  

 

 

 

2025-11-18 
Ćwiczenia VI 

Dzisiaj tworzymy klasę z wykłaoy 

Wspomienie o predyfiniiowaniu funkcji  

Kod też jest metodą zapisania algorytmu 

Aby odczytać kilka osób naraz można utworzyć pętle for aby odczytać kilku pracowników 
 
 

 

2025-11-19 
Wykład 

Pola są rodzajem deklaracji  

Konstruktor – może być bezparametrowy 

Np. taki działający jak metoda  

System.output line nie przyjmuje parametru,  

Przy użyciu date i braku formatowania pokaże się ona z rokiem przesuniętym o 1970 /+ sprawdź +/ 

``` 

// pola 

public class Wsp{  -- jeżeli nie napiszemy public to z oddzielnego pliku trzeba go wskazać 

double  x; 

double y; 

} 

// konstruktor 

public Wsp (double a, double b){ 

x=a; 

y=b; 

} 

metody 

public void setWSP(double a, double b) {// void w paskalu to procedura w javie to funkcja 

x=a; 

y=b 

} 

} 

// Pola można zmieniać za pomocą metod 

Wsp w = new WSP (10.0,10.0); /* można zamiast stosowania N S i W E storować liczby dodatnie i  ujemne */ 

w.setwsp(-10.0,-20.0) 

this.x = -10.0; 

this.y = -20.0;  

Jest to obiekt na rzecz którego wywoływana jest metoda.  

Dane są wpisywane BEZPOŚREDNIA (this.) 

„this” jest zapisywany w kodzie i pozwala w prosty sposób odróżnić parametry od zmiennych lokalnych. 

Innym jego zastosowaniem jest kiedy w klasie są zmienne o tych samych nazwach jak parametry metod czy też konstruktorów. 

Przykład użycia w zapisie klasy 

public class Wsp{  -- jeżeli nie napiszemy public to z oddzielnego pliku trzeba go wskazać 

double  x; 

double y; 

} 

public Wsp (double x, double y){ 

this.x=x 

this.y=y 

} 

public void setWSP(double x, double y) {// void w paskalu to procedura w javie to funkcja 

} 

this.x=x 

this.y=y 

} 

Nie ma konstruktora który jest bezparametrowy. 

 

Prywatnie czy nie łatwiej żeby nasze pola były dostępne publicznie? – nie trzeba by było wtedy tworzyć metod. 

Chodzi o to że nasze pole jest tylko do odczytu ustawiając wartość za pomocą konstruktora, w ten sposób uzyskujemy gwarancje że nie zostanie ona zniszczona (uszkodzona) 

Czasami potrzebne jest pobranie składowej obiektu potrzebne są: 

-- pole prywatne 

-- publiczna metoda dostępu 

-- publiczna metoda mutator (modyfikator) 

Oznaczało by to więcej roboty  

Metoda ma też swoje zalety, można zmienić w kodzie tylko metodę klasy. 

W metodzie możemy sklejać składowe zmienne do imienia i nazwisk. 

Przy zapisie bazodanowym ma to swój plus ponieważ dopisuje się do jej rekordów. 

Prowadzi to do korzyści metody modyfikatora potrafią sprawdzać błędy  
Kod który po prostu przyjmuje wartość pola może nie mieć tej możliwości 

Nie ma potrzeby pisać metod zwracających referencje do zmiennych. 

Metoda ma dostęp do prywatnych danych obiektu tylko w obrębie swojej klasy, nie może sięgać do drugiej klasy, chyba że (co jest bez sensu) wywoła się w klasie 2 klasę. 

Lokalna i globalna zmienna o tej samej nazwie jest zgłaszana przez kompilator. 

 

Dane publiczne mogą być niebezpieczne – służy do tego konstruktor lub metoda,  

Jeżeli metoda nie może być usunięta przez dekonstruktor to znaczy, że jest ona nadal używana. 

W deklaracji pola klasy można używać słowa kluczowego final. 
Tego typu pole musi być zainicjalizowana, podczas kompilacji musi być dopisana do niej wartość, jest ona niezmienna. 

Static – jest to pole typu statycznego – tylko jeden egzemplarz tego typu może być przy klasie. 

Słowo kluczowe ID może być czasami zastrzeżone 

Pole static może być współdzielone w obrębie klasy przy np. przenoszeniu danych +n do numeru identyfikatora. 
Pole opisane jako statyczne będzie w tym monecie będzie tylko i wyłącznie jedno. 
Pole to też będzie istniało nawet jeżeli nie wstąpi z instancją klasy. 
Słowo static przy pisaniu GUI pojawia się przed jego zawartością. 

Można tego użyć do liczby Pi 

 

2025-11-25 
Ćwiczenia  

1. Przy dzieleniu klas należało wkleić importy do pliku w którym są wykonywane 

 

 

2025-11-26 
Wykład 

Przeciążenie sytuacja, w której kilka metod ma tą samą nazwę, zaś inne parametry 

Kompilator decytuje, którą wersję ma załadować 

Inteliji sam podpowiada w nawiasie parametry metody 

Nie potrafi on jednak zamieniać zmiennych miejscami  

Decyzje podejmuje po nagłówkach różnych metod przekazywanych podczas wywołania. 

Sama maszyna wywołująca bite kod decyduje której faktycznie metod ma użyć  

rsync –do narzędzie wiersza poleceń do synchronizacji plików i katalogów w systemie linux. 

Kiedy dopasowanie jest nieprawidłowe  
Występuje wtedy błąd kompilacji – overloading ?resolution?… <dopisz jakie> 

Jest coś takiego jak referencja 
Dobrym przykładem jest deklaracja łańcucha znaków  

Do obsługi bazy danych są od razu zaimplementowane metody w java 

 

Istnieje konstruktor pusty (bezargumentowy) 

Może być inicjujący (dane istnieją z domysłu)  
Np. kiedy wyświetla się formularz to może być podawany przykład co wpisać w polu. 
W konstruktorze może na przykład być aktualna data wstawiana automatycznie – potrafią to konstruktor bezargumentowe  

Metoda finalizacji ukończenia czegoś – jest wywoływana przez garbage collection 

Słowo kluczowe package – to nasze biblioteki w jednym segregatorze, znajdujące się w miejscu domyślnym lub <nie wiem co>  

W java nie trzeba tworzyć niewiadomo jak dużego programu może być podzielony na pakiet. 

Może istnieć bardzo wiele pakietów do jednego programu. 

 

Kompilator nie rozpoznaje sytuacji kiedy 

Import java.util.*; 
Import java.util.dowolny_pakiet; 

 

Przy programowaniu domenę wprowadza się odwrotnie jak w przeglądarce: 
pl.plock.pw 

 

W java istnieje import statyczny 
Polega na tym, że  
import Static java.util.System 

Daje to nam możliwość skrócenie  
Można wywołać 
out.println() 
zamiast System.out.println() 

 

 

Dziedziczenie 
extends 

2025-12-03 
Wykład  

1.  Klasa bazowa Object --  

Array list – lista tablicowa dośczęsto  

Klasy obliczeniowe 

Pojęcie objection 

Dziedziczenie jest to technika tworzenia klas na bazie już istniejących  
Podklasa może mieć metody, które nie są w klasie od której dziedziczy – to znaczy mogą posiadać nowe pola i metody 

Reflecs – ma dość szerokie możliwości, staje się więc metodą skomplikowaną,  

Wszystkie pola klasy oryginalnej mogą ale nie muszą być zachowane. 

Do połączenia relacji służy słowo extends -- dostć często stowowane w GUI. 

Podajemy klasęWyższą extends klasaNiższa, w tej chwili możemy mu podać nowe pola itp. 

W java’ie dziedziczenie może być wyłącznie publiczne. 

Klasa niższa jest wtedy traktowana jako SUPER – nadklasa (czyli ważniejsza). -- analogia drzewa, może być też traktowana jako klasa bazowa lub tak zwaną klasą macierzystą (parent class) 

Podklasa jest subclass’ą, 

Może też być klasa pochodna (potomna) 

Jeżeli metoda znajduje się w klasie która coś dziedziczy nie działa w klasie z której się wywodzi. 

Metody ogólnego przeznaczenia należy umieszczać w klasie najstarszej.  

Wyspecjalizowane zaś w podklasach. 

Override -- przesłonięcie -- polega na tym że w nadklasie mamy tą samą metodę co w podklasie np zwracająca informacja o stanowisku.  
W momencie wywołania takiej metody zostaje ona przysłonięta przez pierwotną (z klasy parent) 

Aby pobierać informację z starszej klasy należy używać getterów (bo pola są private). 

Słowo super jest odpowiednikiem this w konstruktorze. 

Słowo super nie jest referencją do obiektu, nakazuje ono jednak wykonanie kompilatorowi metod z klasy macierzystej 

Dziedziczenie nie umożliwia pozbycia się metody ani pól 

 

 
2025-12-10 
Wykład 

Przy rzutowaniu nadklasy na typ podklasy należy sprawdzić stan instance  
Ale tylko wtedy, jeżeli odpowiedź będzie  

Klasa Abstrakcyjne: są pewne cechy wspólne dla wszystkich klas  
 

 

2025-12-17 
Wykład 

Private używamy do hermetyzacji 

Protected – widoczny jest w wszystkich podklasach i w pakiecie. 

Public - widoczny wszędzie

Domyślny – widoczny w pakiecie

Wada zmiennej tablicowej – nie można zmienić jej rozmiaru w trakcie działania programu.

ArrayList – jest to klasa tablicowa, która może zmieniać swój rozmiar w trakcie działania programu. 

Klonowanie obiektu

Klasy pośrednie

Interfejsy – pewnego rodzaju pulpit zarządczy, Ogólnie opisują co w klasie robić ale nie określają w jaki sposób.

W Javie Interfacey nie są klasą. 

Metoda sort z kalasy Arrays musi mieć jeden warunek -- obiekty z klas muszą należeć do klasy Comparable.

Implementacja takiego interacu

Rozpoczyna się od 

public Interface NazwaInterfejsu{
... definiujemy obiekty które mają być w klasie
}

Załużmy że w naszym interface zadeklorowaliśmy metodę o nazwie porównaj
Kiedy wyjdzie 0  to zamień ze sobą elementy
Kiedy są równe to nic nie dotykaj

public Interface Porównanie{

}

mamy pewnego rodzaju argumeny załużmy że jest z klasy Obiekt

Wewnątrz kodu programista jes po to żeby to obsłużyć

Nie spotyka się w interface żeby przed metodą w nim deklarowana była słowo kluczowe public

W przypadku interfejsów wszystkie metody są domyślnie publiczne

Aby klasa implementowała interfejs należy zadeklarować że dana klasa korzysta z interfejsu

Należy zdefiniować wszystkie metody dla danego interfejsu

Java to język ze ścisłą kontrolą typów

Kopilator to weryfikuje

Własności interfaców nie są one klasą, nie można go powołać przez new
Ale dopuszczalne jest deklarowanie zmiennej typu interfejsowego

Konstruktory nie mogą mieć tych samych danych
Nie ma instrukcji wyborru konstruktora

Metody w interface są zawsze publiczne
A zmienne są finalne i też publiczne
Pomijamy więc zasadę hermetyzacji

Interfejsy możemy wymieniać jako szereg,
interfacy odzielamy przecinkami, (wymieniamy jeden za drugim, kolejność nie ma znaczenia)

Do interfacu odwołujemy się z klasy przez słowo implements
public class NazwaKlasy implements NazwaInterfejsu(ów){

}


Jeżeli robimy klasy rozszeżane to nie mieszać słów extends i implements (poprostu)

Klonowanie obiektu – jest dobrze zrobić na pewnego rodzaju przykładzie
Jak wygląda kopiowanie obiektu
Załużmy że jest przypisany do wartości w[0]
Klonowanie obiektów to jest nic innego jako w[1] = w[0]
W momęcie kiedy powołujemy nowy element to drugi ma do niego referencję (jest zachowany adres w pamięci)
Pieerwszy i drugi element mają inne adresy w pamięci

W przypadku porównywania zmiennych obiektowych

Metoda equals – porównuje zawartość obiektu nie jego adres w pamięci a zawartość

Znak porównania == porównuje adresy w pamięci (to dwa różne rozwiązania)

Jeżeli zrobimy coś takiego jak klonowanie obiektu
Możemy sklonować wszystkie oryginalne parametry obiektu, wtedy powołujemy kolejny obiekt

W przypadku klonowania rezerwowany jest nowy obszar pamięci

Oryginalny obiekt zajmuje przestrzeń w pamięci a przy klon jest rezerwowany nowy obszar niezależny od tego pierwszego
Zasoby zwiększają się dwukrotnie

Istnieją też pewnego rodzaju kopiowania płytkie
W przypadku kopiowania płytkiego, kture się wiele nie różni od zwykłego
Powstaje podobiekt (obiekt w obiekcie), pewne jego pola są powiązane z oryginałem
Ma za zadanie skopiować tylko ten obiekt klasy, który nas interesuje
