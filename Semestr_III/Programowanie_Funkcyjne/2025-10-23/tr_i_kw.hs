poleHerona :: Double -> Double -> Double -> Double
poleHerona a b c = 
    sqrt (po * (po - a) * (po - b) * (po - c))
    where
        po = (a + b + c) / 2