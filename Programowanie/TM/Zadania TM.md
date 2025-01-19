Wyjaśnienie początkowe 

Z definicji Maszyny turinga wynika, że:

"Σ ... Zbiór ten musi zawierac co najmniej dwa specjalne symbole: P (symbol pusty) i K (symbol końcowy);" => Σ {a,b,c} + {P,K}

Ponieważ taśma jest z założenia nie skończona to symbol końca jest opcjolanly, gdyby jednak wystąpił (np. jako koniec ciągu bitów itp.) można opisać go następująco:    

| Symbol \ Stan |           S            |  np. Stan szukania C  | ... | K - Stan końcowy |
|:-------------:|:----------------------:|:---------------------:|:---:|:----------------:|
|       K       |         K, -, -        |        K, -, -        | ... |      Koniec      |

## 1. Maszyna Turinga akceptującą napis gdy napotka na symbol c bezpośrednio występujący po symbolu a(zbiór dopuszczalnych symboli to {a, b, c}) .

### MT = <Q, S, Σ, δ>

| gdzie |                             |                                                             |
|:-----:|-----------------------------|-------------------------------------------------------------|
|   Q   | Zbiór stanów                | {S, SC - szykania c}                                        |
| S = S | Stan początkowy              | wyróżniony stan, od któego maszyna rozpoczyna działanie     |
|   Σ   | Zbiór symboli taśmowych     | {a,b,c} + {P,K}, gdzie P - symbol pusty, K - symbol końcowy |
|   δ   | Funkcja następnego ruchu    | (Q ∪ {k,t, n} x Σ) x {←, →, -}                              |
| dla δ | k, t, n to kolejno          | stan końcowy, stan akceptacji, stan odrzucenia              | 

### Funkcje następnego ruchu:

| Symbol \ Stan |           S            |  SC - Stan szukaj c   |  t - Stan akceptacji   |
|:-------------:|:----------------------:|:---------------------:|:----------------------:|
|       a       |        SC, a, →        |        SC, a, →       |         KONIEC         |
|       b       |        S, b, →         |        S, b, →        |         KONIEC         |
|       c       |        S, c, →         |        t, c, -        |         KONIEC         |
|       P       |        S, P, →         |        S, P, →        |         KONIEC         |

### Operacje na taśmie:

| Bierzący stan |   Aktualna pzozycja głowicy na taśmie    | Bierzący symbol | Nowy stan | Nowy symbol | Ruch głowicy |
|:-------------:|:----------------------------------------:|:---------------:|:---------:|:-----------:|:------------:|
|       S       | b  a  P [a] b  c  P  a  c  a  P  a  c  a |        a        |     SC    |      a      |      →       |
|       SC      | b  a  P  a [b] c  P  a  c  a  P  a  c  a |        b        |     S     |      b      |      →       |
|       S       | b  a  P  a  b [c] P  a  c  a  P  a  c  a |        c        |     S     |      c      |      →       |
|       S       | b  a  P  a  b  c [P] a  c  a  P  a  c  a |        b        |     S     |      b      |      →       |
|       S       | b  a  P  a  b  c  b [a] c  a  P  a  c  a |        a        |     SC    |      a      |      →       |
|       SC      | b  a  P  a  b  c  b  a [c] a  P  a  c  a |        c        |     t     |      c      |      -       |
|       t       | b  a  P  a  b  c  b  a [c] a  P  a  c  a |        -        |     -     |      -      |      -       |

## 2.TM akceptującą napis gdy po raz trzeci odczyta symbol c (zbiór dopuszczalnych symboli to {a, b, c}). Każda odczytana litera c powinna zostać zamieniona na literę dużą, tj. C.

### MT = <Q, S, Σ, δ>

| gdzie |                             |                                                                            |
|:-----:|-----------------------------|----------------------------------------------------------------------------|
|   Q   | Zbiór stanów                | {S, C1, C2, A},gdzie Cn - stan zliczania n wystąpień,                      |
| S = S | Stan początkowy              | wyróżniony stan, od któego maszyna rozpoczyna działanie                    |
|   Σ   | Zbiór symboli taśmowych     | {a,b,c} + {P,K}, gdzie P - symbol pusty, K - symbol końcowy                |
|   δ   | Funkcja następnego ruchu    | (Q ∪ {k,t, n} x Σ) x {←, →, -}                                             |
| dla δ | k, t, n to kolejno          | stan końcowy, stan akceptacji, stan odrzucenia                             | 

### Funkcje następnego ruchu:

| Symbol \ Stan |   S - Stan początkowy   |  C1 - I c znalezione  |  C2 - II c znalezione |  t - Stan akceptacji   |
|:-------------:|:-----------------------:|:---------------------:|:---------------------:|:----------------------:|
|       a       |         S, a, →         |        C1, a, →       |        C2, a, →       |         KONIEC         |
|       b       |         S, b, →         |        C1, b, →       |        C2, b, →       |         KONIEC         |
|       c       |         C1, C, →        |        C2, C, →       |        t, C, -        |         KONIEC         |
|       P       |         S, P, →         |        C1, P, →       |        C2, P, →       |         KONIEC         |

### Operacje na taśmie:

| Bierzący stan |    Aktualna pzozycja głowicy na taśmie   | Bierzący symbol | Nowy stan | Nowy symbol | Ruch głowicy |
|:-------------:|:----------------------------------------:|:---------------:|:---------:|:-----------:|:------------:|
|       S       | b  a  P [a] b  c  P  a  c  a  c  a  c  a |        a        |     S     |      a      |      →       |
|       S       | b  a  P  a [b] c  P  a  c  a  c  a  c  a |        b        |     S     |      b      |      →       |
|       S       | b  a  P  a  b [c] P  a  c  a  c  a  c  a |        c        |     C1    |      C      |      →       |
|       C1      | b  a  P  a  b  C [P] a  c  a  c  a  c  a |        b        |     C1    |      b      |      →       |
|       C1      | b  a  P  a  b  C  b [a] c  a  c  a  c  a |        a        |     C1    |      a      |      →       |
|       C1      | b  a  P  a  b  C  b  a [c] a  c  a  c  a |        c        |     C2    |      C      |      →       |
|       C2      | b  a  P  a  b  C  b  a  C [a] c  a  c  a |        a        |     C2    |      a      |      →       |
|       C2      | b  a  P  a  b  C  b  a  C  a [c] a  c  a |        c        |     t     |      C      |      -       |
|       t       | b  a  P  a  b  C  b  a  C  a [C] a  c  a |        -        |     -     |      -      |      -       |

## 3. TM akceptującą napis gdy napotka na symbol a występujący trzykrotnie po sobie (a więc po przeczytaniu ciągu aaa maszyna powinna przejść do stanu akceptującego; zbiór dopuszczalnych symboli to {a, b, c}).

### MT = <Q, S, Σ, δ>

| gdzie |                             |                                                                              |
|:-----:|-----------------------------|------------------------------------------------------------------------------|
|   Q   | Zbiór stanów                | {S, A1, A2, A},gdzie An - stan zliczania n wystąpień a,                      |
| S = S | Stan początkowy              | wyróżniony stan, od któego maszyna rozpoczyna działanie                      |
|   Σ   | Zbiór symboli taśmowych     | {a,b,c} + {P,K}, gdzie P - symbol pusty, K - symbol końcowy                  |
|   δ   | Funkcja następnego ruchu    | (Q ∪ {k,t, n} x Σ) x {←, →, -}                                               |
| dla δ | k, t, n to kolejno          | stan końcowy, stan akceptacji, stan odrzucenia                               |  

### Funkcje następnego ruchu:

| Symbol \ Stan |           S            |  A1 - I a znalezione  |  A2 - II a znalezione |  t - Stan akceptacji   |
|:-------------:|:----------------------:|:---------------------:|:---------------------:|:----------------------:|
|       a       |        A1, a, →        |        A2, a, →       |        t, a, -        |         KONIEC         |
|       b       |        S, b, →         |        S, b, →        |        S, b, →        |         KONIEC         |
|       c       |        S, c, →         |        S, c, →        |        S, c, →        |         KONIEC         |
|       P       |        S, P, →         |        S, P, →        |        S, P, →        |         KONIEC         |

### Operacje na taśmie:

| Bierzący stan |    Aktualna pzozycja głowicy na taśmie    | Bierzący symbol | Nowy stan | Nowy symbol | Ruch głowicy |
|:-------------:|:-----------------------------------------:|:---------------:|:---------:|:-----------:|:------------:|
|       S       | [a] a  b  c  b  a  c  a  c  a  a  a  b  a |        a        |     A1    |      a      |      →       |
|       A1      |  a [a] b  c  b  a  c  a  c  a  a  a  b  a |        a        |     A2    |      a      |      →       |
|       A2      |  a  a [b] c  b  a  c  a  c  a  a  a  b  a |        b        |     S     |      b      |      →       |
|       S       |  a  a  b [c] b  a  c  a  c  a  a  a  b  a |        c        |     S     |      c      |      →       |
|       S       |  a  a  b  c [b] a  c  a  c  a  a  a  b  a |        b        |     S     |      b      |      →       |
|       S       |  a  a  b  c  b [a] c  a  c  a  a  a  b  a |        a        |     A1    |      a      |      →       |
|       A1      |  a  a  b  c  b  a [c] a  c  a  a  a  b  a |        c        |     S     |      c      |      →       |
|       S       |  a  a  b  c  b  a  c [a] c  a  a  a  b  a |        a        |     A1    |      a      |      →       |
|       A1      |  a  a  b  c  b  a  c  a [c] a  a  a  b  a |        c        |     S     |      c      |      →       |
|       S       |  a  a  b  c  b  a  c  a  c [a] a  a  b  a |        a        |     A1    |      a      |      →       |
|       A1      |  a  a  b  c  b  a  c  a  c  a [a] a  b  a |        a        |     A2    |      a      |      →       |
|       A2      |  a  a  b  c  b  a  c  a  c  a  a [a] b  a |        a        |     t     |      a      |      -       |
|       t       |  a  a  b  c  b  a  c  a  c  a  a [a] b  a |        -        |     -     |      -      |      -       |

## 4. TM akceptującą napis gdy napotka na symbol c, ale tylko wtedy gdy wcześniej przeczytała symbol a (a więc po przeczytaniu ciągu a*c, gdzie * oznacza ciąg dowolnych symboli różnych od c, maszyna powinna zatrzymać się; zbiór dopuszczalnych symboli taśmowych to {a, b, c}).


MT = <Q, S, Σ, δ>

| gdzie |                             |                                                                            |
|:-----:|-----------------------------|----------------------------------------------------------------------------|
|   Q   | Zbiór stanów                | {S, SAC},gdzie SAC - stan szukania ciągy od a do c,                     |
| S = S | Stan początkowy              | wyróżniony stan, od któego maszyna rozpoczyna działanie                    |
|   Σ   | Zbiór symboli taśmowych     | {a,b,c} + {P,K}, gdzie P - symbol pusty, K - symbol końcowy                |
|   δ   | Funkcja następnego ruchu    | (Q ∪ {k,t, n} x Σ) x {←, →, -}                                             |
| dla δ | k, t, n to kolejno          | stan końcowy, stan akceptacji, stan odrzucenia                             | 

### Funkcje następnego ruchu:

| Symbol \ Stan |           S            | SAC -Stan szukaj a*c  |  t - Stan akceptacji   |
|:-------------:|:----------------------:|:---------------------:|:----------------------:|
|       a       |        SAC, a, →       |        SAC, a, →      |         KONIEC         |
|       b       |        S, b, →         |        SAC, b, →      |         KONIEC         |
|       c       |        S, c, →         |        t, c, -        |         KONIEC         |
|       P       |        S, P, →         |        SAC, P, →      |         KONIEC         |

### Operacje na taśmie:

| Bierzący stan |    Aktualna pzozycja głowicy na taśmie    | Bierzący symbol | Nowy stan | Nowy symbol | Ruch głowicy |
|:-------------:|:-----------------------------------------:|:---------------:|:---------:|:-----------:|:------------:|
|       S       | [b] c  b  b  a  b  b  a  c  b  a  c  a  c |        b        |     S     |      b      |      →       |
|       S       |  b [c] b  b  a  b  b  a  c  b  a  c  a  c |        c        |     S     |      c      |      →       |
|       S       |  b  c [b] b  a  b  b  a  c  b  a  c  a  c |        b        |     S     |      b      |      →       |
|       S       |  b  c  b [b] a  b  b  a  c  b  a  c  a  c |        b        |     S     |      b      |      →       |
|       S       |  b  c  b  b [a] b  b  a  c  b  a  c  a  c |        a        |    SAC    |      a      |      →       |
|      SAC      |  b  c  b  b  a [b] b  a  c  b  a  c  a  c |        b        |    SAC    |      b      |      →       |
|      SAC      |  b  c  b  b  a  b [b] a  c  b  a  c  a  c |        b        |    SAC    |      b      |      →       |
|      SAC      |  b  c  b  b  a  b  b [a] c  b  a  c  a  c |        a        |    SAC    |      a      |      →       |
|      SAC      |  b  c  b  b  a  b  b  a [c] b  a  c  a  c |        c        |     t     |      b      |      -       |
|       t       |  b  c  b  b  a  b  b  a [c] b  a  c  a  c |        -        |     -     |      -      |      -       |

## 5. TM akceptującą napis gdy napotka ciąg symboli symbol 1A3B (zbiór dopuszczalnych symboli to wszystkie możliwe do wprowadzenia znaki).

### MT = <Q, S, Σ, δ>

wszystkie możliwe do wprowadzenia znaki \ {A,B,C,1,2,3} = *

| gdzie |                             |                                                                            |
|:-----:|-----------------------------|----------------------------------------------------------------------------|
|   Q   | Zbiór stanów                | {S, 1A, A3, 3B} - stany szukania y po x, w zapisane xy : np dla 1A 1=x A=y |
| S = S | Stan początkowy              | wyróżniony stan, od któego maszyna rozpoczyna działanie                    |
|   Σ   | Zbiór symboli taśmowych     | {a,b,c} + {P,K}, gdzie P - symbol pusty, K - symbol końcowy                |
|   δ   | Funkcja następnego ruchu    | (Q ∪ {k,t, n} x Σ) x {←, →, -}                                             |
| dla δ | k, t, n to kolejno          | stan końcowy, stan akceptacji, stan odrzucenia                             | 

### Funkcje następnego ruchu:

| Symbol \ Stan |           S            |  1A - Szuka A po 1  |  A3 - Szuka 3 po A |  3B - Szuka B po 3 |  t - Stan akceptacji   |
|:-------------:|:----------------------:|:-------------------:|:------------------:|:------------------:|:----------------------:|
|       A       |        S, A, →         |       A3, A, →      |       S, A, →      |       S, A, →      |         KONIEC         |
|       B       |        S, B, →         |       S, B, →       |       S, B, →      |       t, B, -      |         KONIEC         |
|       C       |        S, C, →         |       S, C, →       |       S, C, →      |       S, C, →      |         KONIEC         |
|       1       |        1A, 1, →        |       S, 1, →       |       S, 1, →      |       S, 1, →      |         KONIEC         |
|       2       |        S, 2, →         |       S, 2, →       |       S, 2, →      |       S, 2, →      |         KONIEC         |
|       3       |        S, 3, →         |       S, 3, →       |       3B, 3, →     |       S, 3, →      |         KONIEC         |
|       *       |        S, *, →         |       S, *, →       |       S, *, →      |       S, *, →      |         KONIEC         |
|       B       |        S, B, →         |       S, B, →       |       S, B, →      |       S, B, →      |         KONIEC         |

### Operacje na taśmie:

| Bierzący stan |    Aktualna pzozycja głowicy na taśmie     | Bierzący symbol | Nowy stan | Nowy symbol | Ruch głowicy |
|:-------------:|:------------------------------------------:|:---------------:|:---------:|:-----------:|:------------:|
|       S       | [1] A  *  *  A  *  *  1  B  *  1  A  3  B  |        1        |     1A    |      1      |      →       |
|       1A      |  1 [A] *  *  A  *  *  1  B  *  1  A  3  B  |        A        |     A3    |      A      |      →       |
|       A3      |  1  A [*] *  A  *  *  1  B  *  1  A  3  B  |        *        |     s     |      *      |      →       |
|       S       |  1  A  * [*] A  *  *  1  B  *  1  A  3  B  |        *        |     s     |      *      |      →       |
|       S       |  1  A  *  * [A] *  *  1  B  *  1  A  3  B  |        A        |     s     |      A      |      →       |
|       S       |  1  A  *  *  A [*] *  1  B  *  1  A  3  B  |        *        |     s     |      *      |      →       |
|       S       |  1  A  *  *  A  * [*] 1  B  *  1  A  3  B  |        *        |     s     |      *      |      →       |
|       S       |  1  A  *  *  A  *  * [1] B  *  1  A  3  B  |        1        |     1A    |      1      |      →       |
|       A1      |  1  A  *  *  A  *  *  1 [B] *  1  A  3  B  |        B        |     S     |      B      |      →       |
|       S       |  1  A  *  *  A  *  *  1  B [*] 1  A  3  B  |        *        |     s     |      *      |      →       |
|       S       |  1  A  *  *  A  *  *  1  B  * [1] A  3  B  |        1        |     1A    |      1      |      →       |
|       1A      |  1  A  *  *  A  *  *  1  B  *  1 [A] 3  B  |        A        |     A3    |      A      |      →       |
|       A3      |  1  A  *  *  A  *  *  1  B  *  1  A [3] B  |        3        |     3B    |      3      |      →       |
|       3B      |  1  A  *  *  A  *  *  1  B  *  1  A  3 [B] |        B        |     t     |      B      |      -       |
|       t       |  1  A  *  *  A  *  *  1  B  *  1  A  3 [B] |        -        |     -     |      -      |      -       |

## 6. TM akceptujący dane wejściowe tak długo jak odczytane znaki tworzą liczbę szesnastkową. Maszyna powinna zatrzymać się po natrafieniu na pierwszy znak, który nie jest poprawną cyfrą szesnastkowa (zbiór dopuszczalnych symboli to wszystkie możliwe do wprowadzenia znaki).

### MT = <Q, S, Σ, δ>

wszystkie możliwe do wprowadzenia znaki \ {1,2,3,4,5,6,7,8,9,A,B,C,D,E,F} = *

| gdzie |                             |                                                                            |
|:-----:|-----------------------------|----------------------------------------------------------------------------|
|   Q   | Zbiór stanów                | {S}                                                                        |
| S = S | Stan początkowy              | wyróżniony stan, od któego maszyna rozpoczyna działanie                    |
|   Σ   | Zbiór symboli taśmowych     | {a,b,c} + {P,K}, gdzie P - symbol pusty, K - symbol końcowy                |
|   δ   | Funkcja następnego ruchu    | (Q ∪ {k,t, n} x Σ) x {←, →, -}                                             |
| dla δ | k, t, n to kolejno          | stan końcowy, stan akceptacji, stan odrzucenia                             | 

### Funkcje następnego ruchu:

| Symbol \ Stan |           S            |  t - Stan akceptacji  |  n - Stan odrzucenia   |
|:-------------:|:----------------------:|:---------------------:|:----------------------:|
|    1-9,A-F    |        t, -, →         |        t, -, →        |         KONIEC         |
|       *       |        S, -, →         |        n, -, -        |         KONIEC         |
|       P       |        S, -, →         |        n, -, -        |         KONIEC         |

, gdzie dla t, -, → symbol - oznacza brak zmiany symbolu na taśmie.

### Operacje na taśmie:

| Bierzący stan | Aktualna pzozycja głowicy na taśmie      | Bierzący symbol | Nowy stan | Nowy symbol | Ruch głowicy |
|:-------------:|:----------------------------------------:|:---------------:|:---------:|:-----------:|:------------:|
|       S       | *  4  3  C [3] 4  A  9  P  1  *  5  F  D |        3        |     t     |      -      |      →       |
|       t       | *  4  3  C  3 [4] A  9  P  1  *  5  F  D |        4        |     t     |      -      |      →       |
|       t       | *  4  3  C  3  4 [A] 9  P  1  *  5  F  D |        a        |     t     |      -      |      →       |
|       t       | *  4  3  C  3  4  A [9] P  1  *  5  F  D |        9        |     t     |      -      |      →       |
|       t       | *  4  3  C  3  4  A  9 [P] 1  *  5  F  D |        P        |     t     |      -      |      →       |
|       t       | *  4  3  C  3  4  A  9  P [1] *  5  F  D |        1        |     t     |      -      |      →       |
|       t       | *  4  3  C  3  4  A  9  P  1 [*] 5  F  D |        *        |     n     |      -      |      →       |
|       n       | *  4  3  C  3  4  A  9  P  1 [*] 5  F  D |        -        |     -     |      -      |      -       |

## 7. (Zadanie własne) TM zamienia liczbę ujemną zapisaną w postaci znak (zawsze I bit) - moduł, niezależnie od jej długości (aby to było możliwe po ciągu bitów występuje symbola pusty - P) na liczbę uzupełnioną dwójkowo. Jeżeli licznna będzie dodatnia (0 jako symbol startowy), to maszyna przechodzi w stan odrzucenia (zbiór dopuszczalnycvh symboli to {0,1,P}). 

### Aby rozwiązać zadanie należy zrozumieć proces w jakim powstają liczby uzupełnione dwójkowo (przykład dotyczy liczb znak - moduł na 4 bitach)
Proces tworzenia tych liczb jest przedstawiony w poniższej tabeli (czyta się go kolumna po kolumnie).

| Liczba dziesiętna   | Jej reprezentacja binarna |   Wartość bezwględna z liczby    | Negacja ciągu wartości bezwględnej liczby binarnej | Zwiększenie wartości zanegowanego ciągu o 1 |
|:-------------------:|:-------------------------:|:----------------------------------------:|:------------------------------------------:|:-------------------------------------------:|
|  -1<sub>(10)</sub>  |   1 0 0 1<sub>(2)</sub>   | 1<sub>(10)</sub> = 0 0 0 1<sub>(2)</sub> |       1 1 1 0<sub>(negacja2)</sub>         |            1 1 1 1<sub>(U2)</sub>           |
|  -2<sub>(10)</sub>  |   1 0 1 0<sub>(2)</sub>   | 2<sub>(10)</sub> = 0 0 1 0<sub>(2)</sub> |       1 1 0 1<sub>(negacja2)</sub>         |            1 1 1 0<sub>(U2)</sub>           |
|  -3<sub>(10)</sub>  |   1 0 1 1<sub>(2)</sub>   | 3<sub>(10)</sub> = 0 0 1 1<sub>(2)</sub> |       1 1 0 0<sub>(negacja2)</sub>         |            1 1 0 1<sub>(U2)</sub>           |
|  -4<sub>(10)</sub>  |   1 1 0 0<sub>(2)</sub>   | 4<sub>(10)</sub> = 0 1 0 0<sub>(2)</sub> |       1 0 1 1<sub>(negacja2)</sub>         |            1 1 0 0<sub>(U2)</sub>           |
|  -5<sub>(10)</sub>  |   1 1 0 1<sub>(2)</sub>   | 5<sub>(10)</sub> = 0 1 0 1<sub>(2)</sub> |       1 0 1 0<sub>(negacja2)</sub>         |            1 0 1 1<sub>(U2)</sub>           |
|  -6<sub>(10)</sub>  |   1 1 1 0<sub>(2)</sub>   | 6<sub>(10)</sub> = 0 1 1 0<sub>(2)</sub> |       1 0 0 1<sub>(negacja2)</sub>         |            1 0 1 0<sub>(U2)</sub>           |
|  -7<sub>(10)</sub>  |   1 1 1 1<sub>(2)</sub>   | 7<sub>(10)</sub> = 0 1 1 1<sub>(2)</sub> |       1 0 0 0<sub>(negacja2)</sub>         |            1 0 0 1<sub>(U2)</sub>           |

Aby sprawdzić poprawność otrzymanych liczb trzeba odjąć wartość najbardziej znaczącego bitu od wartości odczytanej z pozostałych bitów.

np. dla -7

Ponieważ w celu utworzenia liczby uzupełnienia dwójkowego liczby ujemnej bierzemy pod uwagę jej wartość bezwględną (bit znaku zmienia się z 1 na 0), a następnie negujemy każdy z bitów (ponownie I bit przyjmuje wartość 1), to pomijamy jego zmianę.

### I. WARIANT:
Nie bierzemy pod uwagę liczba -0 (np 1000 znak-moduł - binarnie na 4 bitach), ponieważ nie istnieje ona w zapisie uzupełnienia dwójkowego. Zawsze jest to 0 (np. 0000 dla zapisu na 4 bitach).

### MT = <Q, S, Σ, δ>

| gdzie |                             |                                                                                 |
|:-----:|-----------------------------|---------------------------------------------------------------------------------|
|   Q   | Zbiór stanów                | {S, NEG, INC} NEG - negacja liczb (0 => 1 1 => 0), INC - zwiększ liczbę o 1 bit |
| S = S | Stan początkowy              | wyróżniony stan, od któego maszyna rozpoczyna działanie                         |
|   Σ   | Zbiór symboli taśmowych     | {a,b,c} + {P,K}, gdzie P - symbol pusty, K - symbol końcowy                     |
|   δ   | Funkcja następnego ruchu    | (Q ∪ {k,t, n} x Σ) x {←, →, -}                                                  |
| dla δ | k, t, n to kolejno          | stan końcowy, stan akceptacji, stan odrzucenia                                  | 

### Funkcje następnego ruchu:

| Symbol \ Stan |           S            |         NEG         |        INC         | t - Stan akceptacji |  n - Stan odrzucenia   |
|:-------------:|:----------------------:|:-------------------:|:------------------:|:-------------------:|:----------------------:|
|       0       |        n, -, -         |      NEG, 1, →      |       t, 1, -      |       KONIEC        |         KONIEC         |
|       1       |       NEG, -, →        |      NEG, 0, →      |      INC, 0, ←     |       KONIEC        |         KONIEC         |
|       P       |        S, -, →         |      INC, -, ←      |  niemożliwe - nd.  |       KONIEC        |         KONIEC         |

### Operacje na taśmie:

| Bierzący stan | Aktualna pzozycja głowicy na taśmie      | Bierzący symbol | Nowy stan | Nowy symbol | Ruch głowicy |         Komentarz        |
|:-------------:|:----------------------------------------:|:---------------:|:---------:|:-----------:|:------------:|:-------------------------|
|       S       | 1  0  1 [P] 1  0  1  0  P  0  1  0  1  0 |        p        |     S     |      -      |      →       | Rozpoczęcie od symbolu P |
|       S       | 1  0  1  P [1] 0  1  0  P  0  1  0  1  0 |        1        |    NEG    |      -      |      →       | Pominięcie zmiany I bitu |
|      NEG      | 1  0  1  P  1 [0] 1  0  P  0  1  0  1  0 |        0        |    NEG    |      1      |      →       | Negacja bitu 0 -> 1      |
|      NEG      | 1  0  1  P  1  1 [1] 0  P  0  1  0  1  0 |        1        |    NEG    |      0      |      →       | Negacja bitu 1 -> 0      |
|      NEG      | 1  0  1  P  1  1  0 [0] P  0  1  0  1  0 |        0        |    NEG    |      1      |      →       | Negacja bitu 0 -> 1      |
|      NEG      | 1  0  1  P  1  1  0  1 [P] 0  1  0  1  0 |        1        |    INC    |      -      |      ←       | Symbol pusty, zwrot      |
|      INC      | 1  0  1  P  1  1  0 [1] P  0  1  0  1  0 |        1        |    INC    |      0      |      ←       | Zwiększenie ciągu bitów  |
|      INC      | 1  0  1  P  1  1 [0] 0  P  0  1  0  1  0 |        0        |     t     |      1      |      -       | Zwiększenie ciągu bitów  |
|       t       | 1  0  1  P  1  1 [1] 0  P  0  1  0  1  0 |        0        |     -     |      1      |      -       | Zatrzymanie maszyny      |


### II. Wariant 
Dopuszczenie liczby -0 (np 1000 znak-moduł - binarnie na 4 bitach), aby się zabezpieczyć dopuki w ciągu po 0 nie wystąpi liczba 1, a jedynie zbiór pusty, to maszyna wejdzie w stan ZERO - zerowania liczby. Jednk liczba musi się znajdować między dwoma symbolami pustymi. Musi jednak istnieć znak pusty P przed zamienianym ciągiem bitów (będzie to warunek zakończenia programu), jeżeli nie maszyna zatrzyma się dopiero na znaku 0 (II warunek zakończenia programu)

### MT = <Q, S, Σ, δ>

| gdzie |                             |                                                                                                                      |
|:-----:|-----------------------------|----------------------------------------------------------------------------------------------------------------------|
|   Q   | Zbiór stanów                | {S, NEG_0, NEG, INC} NEG_0 - negacja zer, NEG - negacja liczb, INC - zwiększ liczbę o 1 bit, DEC - zmiana I bitu w 0 |
| S = S | Stan początkowy              | wyróżniony stan, od któego maszyna rozpoczyna działanie                                                              |
|   Σ   | Zbiór symboli taśmowych     | {a,b,c} + {P,K}, gdzie P - symbol pusty, K - symbol końcowy                                                          |
|   δ   | Funkcja następnego ruchu    | (Q ∪ {k,t, n} x Σ) x {←, →, -}                                                                                       |
| dla δ | k, t, n to kolejno          | stan końcowy, stan akceptacji, stan odrzucenia                                                                       |

### Funkcje następnego ruchu:

| Symbol \ Stan |      S       |      NEG_0       |      NEG      |        INC         |    ZERO    | t - Stan akceptacji |  n - Stan odrzucenia |
|:-------------:|:------------:|:----------------:|:-------------:|:------------------:|:----------:|:-------------------:|:--------------------:|
|       0       |   n, -, -    |    NEG_0, 1, →   |   NEG, 1, →   |       t, 1, ←      |  t, 0, -   |       KONIEC        |        KONIEC        |
|       1       |  NEG_0, -, → |    NEG, 0, →     |   NEG, 0, →   |      INC, 0, ←     | ZERO, 0, - |       KONIEC        |        KONIEC        |
|       P       |   S, -, →    |    ZERO, -, ←    |   INC, -, ←   |  niemożliwe - nd.  |  t, P, -   |       KONIEC        |        KONIEC        |

### Operacje na taśmie:

| Bierzący stan | Aktualna pzozycja głowicy na taśmie      | Bierzący symbol | Nowy stan | Nowy symbol | Ruch głowicy |         Komentarz        |
|:-------------:|:----------------------------------------:|:---------------:|:---------:|:-----------:|:------------:|:-------------------------|
|       S       | 1  0  1 [P] 1  0  0  0  P  0  1  0  1  0 |        p        |     S     |      -      |      →       | Rozpoczęcie od symbolu P |
|       S       | 1  0  1  P [1] 0  0  0  P  0  1  0  1  0 |        1        |   NEG_0   |      -      |      →       | Pominięcie zmiany I bitu |
|     NEG_0     | 1  0  1  P  1 [0] 0  0  P  0  1  0  1  0 |        0        |   NEG_0   |      1      |      →       | Negacja bitu 0 -> 1      |
|     NEG_0     | 1  0  1  P  1  1 [0] 0  P  0  1  0  1  0 |        0        |   NEG_0   |      1      |      →       | Negacja bitu 1 -> 0      |
|     NEG_0     | 1  0  1  P  1  1  1 [0] P  0  1  0  1  0 |        0        |   NEG_0   |      1      |      →       | Negacja bitu 0 -> 1      |
|     NEG_0     | 1  0  1  P  1  1  1  1 [P] 0  1  0  1  0 |        1        |   ZERO    |      -      |      ←       | Symbol pusty, zwrot aby: |
|      ZERO     | 1  0  1  P  1  1  1 [1] P  0  1  0  1  0 |        1        |   ZERO    |      0      |      ←       | Zerowanie liczny         |
|      ZERO     | 1  0  1  P  1  1 [1] 0  P  0  1  0  1  0 |        1        |   ZERO    |      0      |      ←       | Zerowanie liczny         |
|      ZERO     | 1  0  1  P  1 [1] 0  0  P  0  1  0  1  0 |        1        |   ZERO    |      0      |      ←       | Zerowanie liczny         |
|      ZERO     | 1  0  1  P [1] 0  0  0  P  0  1  0  1  0 |        1        |   ZERO    |      0      |      ←       | Zerowanie liczny         |
|      ZERO     | 1  0  1 [P] 0  0  0  0  P  0  1  0  1  0 |        1        |     t     |      -      |      -       | Symnol pusty, koniec     |
|       t       | 1  0  1 [P] 0  0  0  0  P  0  1  0  1  0 |        -        |     -     |      -      |      -       | Zakończ program          |