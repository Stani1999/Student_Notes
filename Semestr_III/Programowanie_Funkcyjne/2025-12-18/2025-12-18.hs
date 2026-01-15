znak :: Char -> String
znak z = 
-- musimy porównać zamykamy z bo grupa znaków jest od a do z <a-z>
 if z >= 'a' && z <= 'z' 
 then "Malutka literka"
 else if z >= 'A' && z <= 'Z'
  then "Duuuza literka"
  else if z >= '0' && z <= '9'
   then "Cyfra"
   else "Inny znak najprawdopodobniej specjalny"

znak2 :: Char -> String
znak2 z
-- musimy porównać zamykamy z bo grupa znaków jest od a do z <a-z>
 | z >= 'a' && z <= 'z' = "Malutka literka"
 | z >= 'A' && z <= 'Z' = "Duuuza literka"
 | z >= '0' && z <= '9' = "Cyfra"
 | otherwise            = "Inny znak najprawdopodobniej specjalny"

abc x = case x of
-- trójmnian kwadratowy służący do obliczanie delty
    (-1) -> "brak miejsc zerowych"
    0   -> "jedno miejsce zerowe"
    1   -> "dwa miejsca zerowe"
    _   -> "to nie jest wartość dopuszczalna"
-- obliczanie algorytmu delty który porównujemy z ww case'em
deltaX :: Double -> Double -> Double -> Int
deltaX a b c = 
    let delta = b^2 - 4*a*c
    in if delta < 0 then -1
       else if delta == 0 then 0
       else 1