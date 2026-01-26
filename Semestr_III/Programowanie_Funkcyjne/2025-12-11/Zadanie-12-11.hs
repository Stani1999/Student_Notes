f1 = foldl (/) 512 [2, 16, 2, 4] -- = 2.0

s1 = scanl (/) 512 [2, 16, 2, 4] --  = 117

f2 =  foldl (\x y-> 3 * x -y) 5 [1,2,3]

s2 =  scanl (\x y-> 3 * x -y) 5 [1,2,3]
-- Zapisać błąd z f3 = foldl1 (/) 512 [2, 16, 2, 4]
f3 = foldl1 (/) [512, 2, 16, 2, 4] -- polega na tym że pobiera 2 elementy z listy, stosuje operator, wynik który zostaje zwrócony stanowi połączenie kolejnego

s3 = scanl1 (/) [512, 2, 16, 2, 4] 

-- dlaczego nie można użyć foldl1 kiedy jest używany scanl1,
-- scanl1 może działać jedynie na ...

f4 = foldl1 (&&) [1<1,1<1,1==1,1<=1,1>=1,1/=1]  -- 1/=1 oznacza różne

s4 = scanl1 (&&) [1<1,1<1,1==1,1<=1,1>=1,1/=1] 

r1 = foldr (/) 4 [8, 4, 2, 4] -- dzielnikiem jest 4, wynik uzyskiwany staje się pierwszym elementem listy
--                in       out  

q1= scanr (/) 4 [8, 4, 2, 4] -- lista lewa i prawa rigth reverse

r2 = foldr (\x y-> (x-y)/2) 108 [6, 4, 3, 2]

q2 = scanr (\x y-> (x-y)/2) 108 [6, 4, 3, 2]

r3= foldr1 (/) [4, 8, 4, 2, 4] 

q3= scanr1 (/) [4, 8, 4, 2, 4] 

r4 = foldr1 (\x y-> (x+y)/2) [54, 6, 4, 3, 2]

q4 = scanr1 (\x y-> (x+y)/2) [54, 6, 4, 3, 2]
