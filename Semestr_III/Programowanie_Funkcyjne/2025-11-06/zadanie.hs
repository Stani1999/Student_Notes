import Data.Char

lista = [a++b | a<-["A","B","C"], b<-["1","2","3"], (a/="B" && b/="2") || (a=="B" && b=="2")]
lista2 = head ["a","b", "c"]                -- pierwszy element listy
lista3 = last ["a","b", "c"]                -- ostatni element  listy
lista4 = [(a, ord a) | a <- "Politechnika"] -- lista par (znak, kod ASCII)
lista5 = [(a, ord a) | a <- "0123456789"]   -- lista par (znak, kod ASCII)
lista6 = tail ["a","b", "c", "d"]           -- lista bez pierwszego elementu
lista7 = init [0..8]                        -- lista bez ostatniego elementu
lista8 = take 2 ["a","b", "c", "d"]         -- lista zawierająca pierwsze dwa elementy z podanej listy
lista9 = drop 3 ["a","b", "c", "d"]         -- lista zawierająca elementy z podanej listy bez pierwszych trzech elementów

lista10 = zip "DEA" [1,2,3,4,5] -- Zwraca listę krotek: [('D',1),('E',2),('A',3)], działa jak w funkcji argumentowi x przyporządkowujemy wartość y.
lista11 = unzip [('D',1),('E',2),('A',3)] -- Zwraca dwie listy: ("DEA",[1,2,3]), działa odwrotnie do funkcji zip.
lista12 = minimum [4,3,0,7]
lista13 = maximum [4,3,0,7]