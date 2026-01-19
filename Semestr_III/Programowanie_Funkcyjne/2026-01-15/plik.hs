xSuma list = zSuma list 0

zSuma n lista = if lista == []
                then n
                else let x = head lista 
                         xd = tail lista
                in if even x  -- even oznacza "parzysta"
                     then zSuma (n + x) xd
                     else zSuma n xd

oSuma n lista = if lista == []
                then n
                else let x = head lista 
                         xd = tail lista
                in if odd x  -- odd oznacza "nieparzysta"
                     then oSuma (n + x) xd
                     else oSuma n xd

ooSuma list = zSuma list 0
    where
        zSuma n [] = n
        zSuma n (x:xd) = 
            if odd x
                then zSuma (n + x) xd
                else zSuma n xd