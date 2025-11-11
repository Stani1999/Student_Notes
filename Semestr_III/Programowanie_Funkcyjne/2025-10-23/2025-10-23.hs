bazai = ["Jan", "V", "Elizabet", "Emil"]
liczba1 = [3, 123, 1.20]
liczba2 = (3, 123, 1.20)
auto = ("MG", "X-cros", 2.0, 2018)
lista1= [[1,1,1],[1],[2,3]]
cos1 = [(1,1,1),(1,1,2),(2,3,3)]
car = [("X", "Y", 3.0, 2000),("S", "T", 0.8, 1996)]
cos2 = ([1,1,1],[1,1,2],[2,3,3])

suma :: Int -> Int -> Int
suma a b = a + b

suma2 :: (Num x) => x -> x -> x
suma2 a b = a + b