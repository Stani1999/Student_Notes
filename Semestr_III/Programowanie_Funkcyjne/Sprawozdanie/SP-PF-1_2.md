## <center>Sprawozdanie z zajęć komputerowych: <br> Programowanie Obiektowe I <center>

## <center>2025-11-27, Płock, Jakub Staniszewski, Grupa II<center>

### Zajęcia 2025-10-16

#### 1. Funkcja i zmienne w Haskellu

##### Tworzenie zmiennych i funkcji w GHCi

```hs
GHCi, version 9.4.7: https://www.haskell.org/ghc/  :? for help
ghci> a = 10
ghci> A = 10

<interactive>:19:1: error: Not in scope: data constructor ‘A’
ghci> 
ghci> kwadrat n = n * n
ghci> kwadrat 2
4
ghci> let f x = x + 2
ghci> f 3
5
ghci> :t kwadrat
kwadrat :: Num a => a -> a
ghci> :t f
f :: Num a => a -> a
```

##### Tworzenie bloku funkcji wieloliniowej:

```hs
ghci> silnia :: Int -> Int

<interactive>:4:1: error:
    Variable not in scope: silnia :: Int -> Int
ghci> 
ghci> :{
ghci| silnia :: Int -> Int
ghci|silnia 0 = 1 
ghci|silnia n = n * silnia (n-1)
ghci|:}
ghci| sumator3 :: Int -> Int -> Int -> Int
ghci| sumator3 a b c = a+b+c
ghci> :{
ghci| sumator3
ghci| 3 4 3
ghci| :}
10

ghci> q

<interactive>:17:1: error: Variable not in scope: q
ghci> :q
```

##### Wnioski

* Zmienne tylko z małych liter, (19:1)
* `let` nie jest wymagane (w tej wersji GHCi.)
* Zakres funkcji `:{` i `:}` (4:1)
* Zakres działa także dla podawania argumentów do funkcji
* `:` poprzedza polecenia (17:1)

---

### Zajęcia 2025-10-23

#### 2. Listy i krotki

##### 1. Tworzenie

```hs
ghci> :t cos
cos :: Floating a => a -> a
ghci> cos = 2
ghci> :t cos
cos :: Num a => a
ghci> 

ghci> cos1 = [1, 2, 3, 4, 5..10]

<interactive>:13:22: error: parse error on input ‘..’
ghci> cos1 = [5..10]
ghci> cos1
[5,6,7,8,9,10]
ghci> cos1 = [5..10] + [20,30]
ghci> cos1

<interactive>:17:1: error:
    • No instance for (Num [Integer]) arising from a use of ‘it’
    • In the first argument of ‘print’, namely ‘it’
      In a stmt of an interactive GHCi command: print it
ghci> cos1 = [5..10] ++ [20,30]
ghci> cos1
[5,6,7,8,9,10,20,30]
```

Polecenia `show` i `read`

```hs
ghci> liczbaNaString = 67
ghci> stringNaLiczba = "69"
ghci> liczbaNaString
67
ghci> stringNaLiczba
"69"
ghci> read stringNaLiczba
*** Exception: Prelude.read: no parse
ghci> read stringNaLiczba :: Int
69
ghci> show liczbaNaString
"67"
```

##### Wnioski 1

* Nie nadpisywać funkcji domylśnych takich jak `cos`!!!
* [..] nie działa z więcej jak 3 liczbami (13:22),
* Listy[] są homogeniczne,
* Krotki() przyjmują wszystkie typy,
* Do łączenia list używamy operatora `++` (17:1)
* `show` konwertuje na string,
* `read` konwertuje ze stringa na dowolny typ.
* Przy użyciu `read` podaj typ! (Exception: Prelude.read: no parse...)
* listy i krotki mogą być zagnieżdżone.

---

##### 2. Operatory

```hs
ghci> 7/2
3.5
ghci> 7 div 2

<interactive>:8:1: error:
    • Could not deduce (Integral a0)
      from the context: (Integral a, Num t1,
                         Num ((a -> a -> a) -> t1 -> t2))
        bound by the inferred type for ‘it’:
                   forall {a} {t1} {t2}.
                   (Integral a, Num t1, Num ((a -> a -> a) -> t1 -> t2)) =>
                   t2
        at <interactive>:8:1-7
      The type variable ‘a0’ is ambiguous
      Potentially matching instances:
        instance Integral Integer -- Defined in ‘GHC.Real’
        instance Integral Int -- Defined in ‘GHC.Real’
        ...plus one other
        ...plus one instance involving out-of-scope types
        (use -fprint-potential-instances to see them all)
    • In the ambiguity check for the inferred type for ‘it’
      To defer the ambiguity check to use sites, enable AllowAmbiguousTypes
      When checking the inferred type
        it :: forall {a} {t1} {t2}.
              (Integral a, Num t1, Num ((a -> a -> a) -> t1 -> t2)) =>
              t2
ghci> 7 `div` 2
3
ghci> 7 `mod` 3
1
ghci> 2 ^ 3
8
ghci> 4 ^ (-2)
*** Exception: Negative exponent
ghci> 4 ^^ (-2)
6.25e-2
ghci> 2.0 ^ 3.5

<interactive>:14:5: error:
    • Could not deduce (Integral b0) arising from a use of ‘^’
      from the context: Fractional a
        bound by the inferred type of it :: Fractional a => a
        at <interactive>:14:1-9
      The type variable ‘b0’ is ambiguous
      Potentially matching instances:
        instance Integral Integer -- Defined in ‘GHC.Real’
        instance Integral Int -- Defined in ‘GHC.Real’
        ...plus one other
        ...plus one instance involving out-of-scope types
        (use -fprint-potential-instances to see them all)
    • In the expression: 2.0 ^ 3.5
      In an equation for ‘it’: it = 2.0 ^ 3.5

<interactive>:14:7: error:
    • Could not deduce (Fractional b0) arising from the literal ‘3.5’
      from the context: Fractional a
        bound by the inferred type of it :: Fractional a => a
        at <interactive>:14:1-9
      The type variable ‘b0’ is ambiguous
      Potentially matching instances:
        instance Fractional Double -- Defined in ‘GHC.Float’
        instance Fractional Float -- Defined in ‘GHC.Float’
        ...plus one instance involving out-of-scope types
        (use -fprint-potential-instances to see them all)
    • In the second argument of ‘(^)’, namely ‘3.5’
      In the expression: 2.0 ^ 3.5
      In an equation for ‘it’: it = 2.0 ^ 3.5
ghci> 2.0 ^^ 3.5

<interactive>:15:5: error:
    • Could not deduce (Integral b0) arising from a use of ‘^^’
      from the context: Fractional a
        bound by the inferred type of it :: Fractional a => a
        at <interactive>:15:1-10
      The type variable ‘b0’ is ambiguous
      Potentially matching instances:
        instance Integral Integer -- Defined in ‘GHC.Real’
        instance Integral Int -- Defined in ‘GHC.Real’
        ...plus one other
        ...plus one instance involving out-of-scope types
        (use -fprint-potential-instances to see them all)
    • In the expression: 2.0 ^^ 3.5
      In an equation for ‘it’: it = 2.0 ^^ 3.5

<interactive>:15:8: error:
    • Could not deduce (Fractional b0) arising from the literal ‘3.5’
      from the context: Fractional a
        bound by the inferred type of it :: Fractional a => a
        at <interactive>:15:1-10
      The type variable ‘b0’ is ambiguous
      Potentially matching instances:
        instance Fractional Double -- Defined in ‘GHC.Float’
        instance Fractional Float -- Defined in ‘GHC.Float’
        ...plus one instance involving out-of-scope types
        (use -fprint-potential-instances to see them all)
    • In the second argument of ‘(^^)’, namely ‘3.5’
      In the expression: 2.0 ^^ 3.5
      In an equation for ‘it’: it = 2.0 ^^ 3.5
ghci> 2.0 ** 3.5
11.313708498984761

ghci> log (exp 1)
1.0
ghci> logBase 10 

<interactive>:19:1: error:
    • No instance for (Show (Double -> Double))
        arising from a use of ‘print’
        (maybe you haven't applied a function to enough arguments?)
    • In a stmt of an interactive GHCi command: print it
ghci> logBase 10 100
2.0
ghci> exp 1
2.718281828459045
ghci> sqrt 9
3.0

```

##### Wnioski 2

* `div` zamiast `/` dla liczb całkowitych, (8:1)
* `^` tylko dla nieujemnych całkowitych wykładników (14:5),(15:5)
* `^^` dla całkowitych wykładników (ujemnych też), (14:7),(15:8)
* `**` dla liczb zmiennoprzecinkowych,
* `logBase` najpierw podstawa potem liczba (19:1)

---

### Zajęcia 2025-10-30

#### 3. Operacje na listach i krotkach

##### 1. Tworzenie list

```hs
ghci> [1..4] -- zakres
[1,2,3,4]
ghci> [0,7..35] -- skok (o różnicę wartości indeksów przed `..`)
[0,7,14,21,28,35]
ghci> [0,7..33] -- skok (po `..` max liczba)
[0,7,14,21,28]
ghci> [1..] -- lista nieskończona, p.s. nie polecam w consoli :) 
[1,2,3,4,5,6,7,8,9,10,11,12,13,14...
... ["one eternity later"]]
```

```hs
ghci> [10,9..0] -- malejąca
[10,9,8,7,6,5,4,3,2,1,0]
ghci> [0.0,0.5..10.0] -- lista z ułamkami
[0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0,9.5,10.0]
```

##### Wniosek 1

* Listy mogą być tworzone na wiele ww. sposobów.

##### 2. Indeksowanie list

```hs
ghci> [1,2,3,4]!!0
1
ghci> [1,2,3,4]!!2
3
ghci> [1,2,3,4]!!4
*** Exception: Prelude.!!: index too large
CallStack (from HasCallStack):
  error, called at libraries/base/GHC/List.hs:1368:14 in base:GHC.List
  tooLarge, called at libraries/base/GHC/List.hs:1378:50 in base:GHC.List
  !!, called at <interactive>:28:10 in interactive:Ghci18
ghci> [1,2,3,4]!!0
1
```

##### Wnioski 2

* Indeksy list zaczynają się od 0,
* Próba dostępu do nieistniejącego indeksu kończy się błędem

##### 3. Listy złożone

```hs
ghci> [n*n|n<-[0..4]]
[0,1,4,9,16]
ghci> [n|n<-[3..18],n`mod`3==0]
[3,6,9,12,15,18]
ghci> [n|n<-[1..19],n`div`3==2 || n/=6]
[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
ghci> [n|n<-[1..19],n`div`3==2 || n/=6 || not (n==7)] 
[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
```

##### Wnioski 3

* Listy złożone pozwalają na tworzenie list z warunkami.
* Warunki mogą być łączone za pomocą `||` (OR) i `&&` (AND).

### Zajęcia 2025-11-06

#### 4. Kombinacje list i wbudowane funkcje na listach

##### 1. Kombinacje list

``` hs
ghci> [a++b | a<-["A","B","C"], b<-["1","2","3"]]
["A1","A2","A3","B1","B2","B3","C1","C2","C3"]
ghci> [a++b | a<-["A","B","C"], b<-["1","2","3"], b=="3"]
["A3","B3","C3"]
ghci> ["A3","B3","C3"]
["A3","B3","C3"]
ghci> [a++b | a<-["A","B","C"], b<-["1","2","3"], b/="3"]
["A1","A2","B1","B2","C1","C2"]
ghci> [a++b | a<-["A","B","C"], b<-["1","2","3"], b/="2" && a/="B" ||  a++b=="B2"]
["A1","A3","B2","C1","C3"]

ghci> [(a,ord a)| a <-"Politechnika"] -- wypisuje kody ASCII liter

<interactive>:1:5: error:
    Variable not in scope: ord :: Char -> b
    Suggested fix:
      Perhaps use one of these:
        ‘or’ (imported from Prelude), ‘odd’ (imported from Prelude)
ghci> import Data.Char -- import modułu z funkcją ord
ghci> [(a,ord a)| a <-"Politechnika"]
[('P',80),('o',111),('l',108),('i',105),('t',116),('e',101),('c',99),('h',104),('n',110),('i',105),('k',107),('a',97)]
```

##### Wnioskek 4

* Do niektórych funkcji trzeba zaimportować moduły (1:5)

##### 5. Wbudowane funkcje na listach

```hs
ghci> head [10..20] -- zwraca pierwszy element listy
10
ghci> tail [1,2,3]
[2,3]
ghci> tail (1,2,3)

<interactive>:32:6: error:
    • Couldn't match expected type: [a]
                  with actual type: (a0, b0, c0)
    • In the first argument of ‘tail’, namely ‘(1, 2, 3)’
      In the expression: tail (1, 2, 3)
      In an equation for ‘it’: it = tail (1, 2, 3)
    • Relevant bindings include it :: [a] (bound at <interactive>:32:1)

ghci> last [20..30] -- zwraca ostatni element listy
30
ghci> init [0..9] -- zwraca listę bez ostatniego elementu
[0,1,2,3,4,5,6,7,8]
ghci> take 2 [0..9] -- zwraca pierwsze n elementów listy
[0,1]
ghci> drop 2 [0..9] -- zwraca listę bez pierwszych n elementów
[2,3,4,5,6,7,8,9]
ghci> zip "ELO" 

<interactive>:9:1: error:
    • No instance for (Show ([b0] -> [(Char, b0)]))
        arising from a use of ‘print’
        (maybe you haven't applied a function to enough arguments?)
    • In a stmt of an interactive GHCi command: print it
ghci> zip "ELO" [1,2,3,4] -- łączy dwie listy w listę krotek
[('E',1),('L',2),('O',3)]
ghci> unzip [('E',1),('L',2),('O',3)] -- rozdziela listę krotek na dwie listy
("ELO",[1,2,3])
ghci> sum[8,8,8,8] -- sumuje elementy listy
32
ghci> reverse["a1","b","c4","d"] -- odwraca kolejność elementów listy
["d","c4","b","a1"]
ghci> elem 1 [1,3,7,9] -- sprawdza czy dany element jest w liscie, krotce.
True
ghci> elem "a"["a","b","c","d"] 
True
ghci> elem "a"["b","c","d"]
False
ghci> snd ("s","2") -- zwraca drugi element 2 elementowej krotki
"2"
ghci> snd ("s",2)
2
ghci> ghci> elem 1 [1,3,7,9] 
ghci> snd ["s","2"] 

<interactive>:9:5: error:
    • Couldn't match expected type: (a0, b)
                  with actual type: [String]
    • In the first argument of ‘snd’, namely ‘["s", "2"]’
      In the expression: snd ["s", "2"]
      In an equation for ‘it’: it = snd ["s", "2"]
    • Relevant bindings include it :: b (bound at <interactive>:9:1)
```

##### Wnioski 5

* `head` zwraca pierwszy element listy,
* `tail` zwraca listę bez pierwszego elementu,
* `last` zwraca ostatni element listy,
* `init` zwraca listę bez ostatniego elementu,
* `take n` zwraca pierwsze n elementów listy,
* `drop n` zwraca listę bez pierwszych n elementów,
* `zip` łączy dwie! (9:1) listy w listę krotek, długości krótszej z nich,
* `unzip` rozdziela listę krotek na dwie listy.
* Dowolny `String` działa bo to lista Charów.
* WW. nie działają na krotkach!!! (32:6),
* NW. nie działają na listach!!! (9:5)
* `elem` sprawdza czy dany element jest w liście/krotce,
* `snd` zwraca drugi element TYLKO 2-elementowej krotki
* `snd` dla list nie działa.

---

### Zajęcia 2025-11-20

#### 6. Funkcje list/krotek c.d.

##### 1. Funkcje na krotkach.

```hs
ghci> fst("a1","b")
"a1"
ghci> fst("a1","b","c")

<interactive>:39:4: error:
    • Couldn't match expected type: (a, b0)
                  with actual type: (String, String, String)
    • In the first argument of ‘fst’, namely ‘("a1", "b", "c")’
      In the expression: fst ("a1", "b", "c")
      In an equation for ‘it’: it = fst ("a1", "b", "c")
    • Relevant bindings include it :: a (bound at <interactive>:39:1)
ghci> fst["a1","b"]

<interactive>:40:4: error:
    • Couldn't match expected type: (a, b0)
                  with actual type: [String]
    • In the first argument of ‘fst’, namely ‘["a1", "b"]’
      In the expression: fst ["a1", "b"]
      In an equation for ‘it’: it = fst ["a1", "b"]
    • Relevant bindings include it :: a (bound at <interactive>:40:1)

ghci> hci> fst("a")  

<interactive>:42:1: error: Variable not in scope: hci
```

##### Wnioski:

* `fst` zwraca pierwszy element TYLKO 2-elementowej krotki (39:4, 40:4)
* `fst` także dla list nie działa (40:4)

##### 2. Listy c.d.

```hs
ghci> map sqrt [1,4,9,121,169] -- stosuje funkcję do każdego elementu listy (pierwiastek)
[1.0,2.0,3.0,11.0,13.0]
ghci> map reverse ["abc", "12" ,"cd"] -- odwraca każdy element listy
["cba","21","dc"]
ghci| :{
ghci| sumator :: Int -> Int -> Int
ghci| sumator a b = a + b
ghci| :}
ghci> zipWith sumator [10,9,8,7] [1,2,3,4] -- zipWi
[11,11,11,11]
ghci> zipWith (>) "ali" "baba" -- porównuje litera po literz tych dwóch wyrazów kody ASCI i zwraca listę Booli
[False,True,True]
```

##### Wnioski 2

* `map` stosuje funkcję do każdego elementu listy,
* `zipWith` łączy dwie listy stosując podaną funkcję

### Zajęcia 2025-11-27

#### 7. Funkcje wyższego rzędu: any, filter, takeWhile, dropWhile

##### 1. Funkcje wyższego rzędu na listach

```hs
ghci> filter(>3) [0,1,3,2,4,5] -- filtruje listę zwracając elementy spełniające warunek
[4,5]
ghci> filter(>1) [0,1,3,2,5]
[3,2,5]
ghci> takeWhile ('w'>) "hello world" -- zwraca elementy listy dopóki spełniają warunek 
-- dla ww kod ASCII mniejszy niż 'w'
"hello "
ghci> dropWhile (\x -> x*3 < 14) [0,1,3,2,5,4] -- usuwa elementy listy dopóki spełniają warunek
[5,4]
ghci> dropWhile [0,1,3,2,5,4]

<interactive>:34:11: error:
    • Couldn't match expected type: a -> Bool
                  with actual type: [a0]
    • In the first argument of ‘dropWhile’, namely ‘[0, 1, 3, 2, ....]’
      In the expression: dropWhile [0, 1, 3, 2, ....]
      In an equation for ‘it’: it = dropWhile [0, 1, 3, ....]
    • Relevant bindings include
        it :: [a] -> [a] (bound at <interactive>:34:1)
```

##### Wnioski:

* `filter` filtruje listę zwracając elementy spełniające warunek,
* `takeWhile` zwraca elementy listy dopóki spełniają warnek,
* `dropWhile` usuwa elementy listy dopóki spełniają warunek
* Podanie listy zamiast funkcji jako pierwszy argument kończy się błędem (34:11).
* Wyrażenie `\x -> ...` działą jako lambda.