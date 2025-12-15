-- W gołym terminalu napisać:
result = any (2==) [0,1,2,3,4,5] -- 
-- co zwróci True

result2 = any (>5) [0,1,2,3,4,5] -- zwraca False
-- bo 5 nie jest większe od 5 musiało by być równe

result3 = any (\x -> x * 3 >15) [1,2,3,4,5] -- zwraca folse 
-- bo 5*3=15 nie jest większe od 15, prwadziewe gdy jest 14.

-- Funkja any zwraca true gdy jeden z elementów listy spełnia warunek podany w funkcji
-- \ służy do pobrania każdego elementu listy i poddanie go warunkowi (działa jak lambda)


filtr = filter (>3) [1,2,3,4,5,6] -- zwraca [4,5,6]

filter2 = filter (\x -> length x > 3) ["ali", "sie", "zapali"]

filter3 = filter (\x -> length x == 4) ["ali", "baba", "zapali"]

-- Podsumowanie różnicy między any a filter
-- any zwraca True lub False w zależności czy któryś z elementów spełnia warunek (bool)
-- filter zwraca listę elementów które spełniają warunek

tw = takeWhile (<3) [0,1,3,2,5] 

tw2=  takeWhile ('w'>) "hellow kitty" 
-- w ma wartość 119 w ascii zaś h ma 104 natomiast y ma 121.
-- kiedy nasze w ma wartość 119 to 

tw3=  takeWhile ('w'>) "hellow kytty" 

tw4 = takeWhile (\x -> x * 3 <14) [0..5]

tw5 = takeWhile (\x -> x * 3 <14) [3..7]

tw6 = takeWhile (\x -> x * 3 >14) [5..10]

-- (wyżej ^)wyświetle elementy spełniające te równanie, dopóki warunek jest prawdziwy

tw7 = takeWhile (\x -> x * 3 <14) [0,1,3,2,5,4]
-- warunek spełnia się kiedy x=0,1,3,2 a po 5 wychodzi więc nie bierze 4 pod uwagę

dw1 = dropWhile (\x -> x * 3 <14) [0,1,3,2,5,4]

dw2 = dropWhile (\x -> x * 3 >14) [0..40]

12