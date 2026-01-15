bmi w h
 | bmi <= chudy    = "Jedz wiecej!"
 | bmi <= normalny = "W normie"
 | bmi <= gruby    = "Nie zryj tyle"
 | otherwise          = "Uprawiaj sumo"
  where 
    bmi = w / (h ^ 2) 
    (chudy, normalny, gruby) = (18.5, 25.5, 30.0)

delta a b c
    | d < 0     = "Brak rozwiazan"
    | d == 0    = "Jedno rozwiazanie" 
    | otherwise = "Dwa rozwiazania"
  where 
    d  = b^2 - 4*a*c

suma a b = a + b

zw1= suma 1

-- komendy do testowania w GHCi:
-- map zw1 [1,3,5]
-- (wynik) [2,4,6]

-- map ((+)1) [1,3,5] -- tak działą ponieważ interpretuje 1 jako liczbę a nie jako łańcuch "-1"
-- (wynik) [2,4,6]

-- (reverse. init) "Ala ma kota"
-- (wynik) "tok ma alA"
-- reverse (init "Ala ma kota")
-- (wynik) "tok ma alA"
-- (init, reverse) "Ala ma kota" -- błąd trzeba użyć kropki do kompozycji funkcji

-- Operatory złożenia :

-- reverse. init $ "Ala ma kota"
-- (wynik) "tok ma alA"
-- tail. reverse $ "Ala ma kota"
-- (wynik) "tok am alA"  

--ghci> map (\x-> reverse(init x)) ["Ala", "ma", "kota"]
--(wynik)["lA","m","tok"]
--ghci> map (reverse.init) ["Ala", "ma", "kota"]
--(wynik)["lA","m","tok"]
