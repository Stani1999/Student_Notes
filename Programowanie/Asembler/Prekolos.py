import random # For testing a program with random variable
'''
P1: Napisz program, który do komórki 'x' wpisz 1 jeśli liczba w
komórce 'y' jest ujemna.
'''
#.data
yP1= random.randrange(-10,10)

xP1=5

#function to 
def ZeroIfYBRN (x, y):
    if y < 0: # BRN -> x = 0
        x = 0 # STO 0 -> x
        yD = ",y is negative so x =" # Part of resoult message
    else :
        x = x
        yD = ",y is positive, so x isn't change, x =" # Part of resoult message
    return x, yD

'''Assembler

.data 0
x = 10              ; 0000    00010  ; wartość w komórce x wskazuje 10
y = -1              ; 0001    10001  ; wartość w komórce y n - poz. -n  - neg

.code 100
begin : 
        CPA y       ; 0100    10001  ; Kopiowanie wartości z pod adresu y do akumulatora
        BRN make1   ; 0101    70103  ; Jeżeli ujemna  idź do make1
        BRA end     ; 0102    60105  ; Idz na konie
make1:  CPA (1)     ; 0103    92101  ; dodaj wart 1 do akumulatora
        STO x       ; 0104    20000  ; Zapisanie akumulatora = 1 do komórki x
end:    HLT         ; 0105    00000  ; Zatrzymanie programu

'''

#start of function
xP1, yP1D = ZeroIfYBRN (xP1 , yP1)

#resoult of function
print (f"\nP1 For y = {yP1} {yP1D} {xP1}\n")


'''
P2: Liczba w komórce 'y' ma wartość 0 lub 1. Napisz program, który
pomnoży wartość w komórce 'x' przez 2 jeśli liczba w komórce 'y' jest
równa 1.
'''
yP2 = random.randrange(0,2) #random libary every time return 0 if i put argument 0,1 i getback only 0, so i decidet to put range 0,2
if yP2 == 2: # If random generate 2 
    yP2 = 1  # I turn 2 in to 1 (...'y' ma wartość 0 lub 1...)
xP2 = 15

def Mux2IfYIsZero(x ,y):
    if y == 0: # BRZ
        x = x
    else:
        x = x * 2
    return x

'''Assembler

.data 0

y = 0 lub 1         ; 0000    000[0/1]  wartość y 0 lub 1
x = 10              ; 0001    00010     wartość x = 10

.code 100

begin :
        CPA y       ; 0100    10000
        BRZ end     ; 0101    80105
        CPA x       ; 0102    10001
        MUX (2)     ; 0103    92502
        STO x       ; 0104    20001
end :   HLT         ; 0105    00000

'''

xP2 = Mux2IfYIsZero(xP2, yP2)
print (f"P2 y is {yP2} so x is {xP2}\n")


'''
P3: Napisz program, który wypełni wszystkie komórki od adresu 'x' do
adresu 'y' liczbą 0.
'''

#A memory list with 20 cells (ranging from 0 to 19) filled with the value 3.
MemoryCellsP3 = [3]*20

# Range for function ZerosIfInRamge (indexs of cells memory)
xP3 = 2  # start indeks
yP3 = 11  # end indeks 

# Function to change in 0 element in raneg x-y
def ZerosIfInRamge(Memo, x, y):
    # Check range
    if x < 0 or y >= len(Memo) or x > y:
        return "Invalid range!"

    # Fill in range by 0
    for i in range(x, y + 1):
        Memo[i] = 0
    return Memo

'''Assembler

.data 0
n = x               ; 0000    0002 wskazuje adres x 
m = y               ; 0001    0006 wskazyje adres końcowy y
x   = ?             ; 0002    ?????   
x+1 = ?             ; 0001    ?????
x+2 = ?             ; 0002    ?????
...                             
y = ?               ; 0006    ?????

.code 100

begin:
loop:   CPA n       ; 0100 10000 ; A := x Wczytaj z pod adresu n wartość x - początek przestrzeni pamięci do wyzerowania 
        SUB m       ; 0101 40001 ; A := x - y Odjęcie ostatniego adresu od adresu początkowego
        BRN zeros   ; 0102 70105 ; Jeżeli warość w akumulatorze jest ujemna idź do zeros
        BRZ zeros   ; 0103 80105 ; Jeżeli warość w akumulatorze jest zerowa idź do zeros
        BRA end     ; 0104 60108 ; Bezwarunkowy skok na koniec 
zeros:  CPA (0)     ; 0105 92100 ; Do akumulatora załaduj 0
        STO [n]     ; 0106 94200 ; Do adresu wskazanego pod n zapisz wartość z akumulatora = 0
        INC n       ; 0107 01000 ; Podnieś wartość pod adresem n o 1 (zwiększ licznik)
        BRA loop    ; 0108 60100 ; Bezwarunkowy skok na początek pętli
        HLT         ; 0109 00000 ; Zakończ program

'''

# Perform operation
EpromMemoryAddress = ZerosIfInRamge(MemoryCellsP3, xP3, yP3)


print("P3 Memory adter zeros", EpromMemoryAddress)
print()


'''
P4: Napisz program, który kopiuje wartość z adresu 'from' do adresu
'to'.
'''
# A memory list with 20 cells (ranging from 0 to 19).
MemoryCellsP4 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# Indices for copying operation
fromP4 = 12  # Source index
toP4 = 2     # Target index

# Function to copy a value from one memory address to another
def CopyFromTo(Memo, x, y):
    # Check if indices are within valid range
    if x < 0 or x >= len(Memo) or y < 0 or y >= len(Memo):
        return "Invalid range!"

    # Copy the value from index x to index y
    Memo[y] = Memo[x]
    return Memo

'''Assembler

.data 0 

0000 00002 ; x: from          ; k. pamięci zawierająca z której k. pamići przenieść wartość
0001 00003 ; y: to            ; k. pamięci zawierająca do której k. pamięci przenieść wartość
0002 00005 ; from: wartość do przeniesienia   
0003 00000 ; to: cel do którego ma wartość trafić

.code 100

begin: 
        0100 94100 ; załaduj wartość z adresu wskazanego przez adres x (from) do akumulatora
        0101 94201 ; załaduj wartość z akumulatora do adresu wskazanego przez adres y (to)
end:    0102 00000 ; zakończ działanie programu


'''


# Perform the copy operation
EpromMemoryAddressP4 = CopyFromTo(MemoryCellsP4, fromP4, toP4)

# Print the memory after copying
print("P4 Memory after copying:", EpromMemoryAddressP4)
print()


'''
P5: Napisz program, który kopiuje wartość z adresu 'from' do adresu
'a' podanego pod adresem 'to'.
'''

# A memory list with 20 cells (ranging from 0 to 19).
MemoryCellsP5 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# Indices for copying operation
fromP5 = 19        
AdrA = MemoryCellsP4 [4]  # Source index
toP5 = AdrA               # Target index

# Function to copy a value from one memory address to another
def CopyFromTo(Memo, x, y):
    # Check if indices are within valid range
    if x < 0 or x >= len(Memo) or y < 0 or y >= len(Memo):
        return "Invalid range!"

    # Copy the value from index x to index y
    Memo[y] = Memo[x]
    return Memo

'''Assembler

.data 0 

0000 00002 ; x: from          ; k. pamięci zawierająca z której k. pamići przenieść wartość
0001 00003 ; to: a            ; k. pamięci zawierająca do której k. pamięci przenieść wartość
0002 00005 ; from: wartość do przeniesienia   
0003 00000 ; to: cel do którego ma wartość trafić

.code 100

begin: 
        0100 94100 ; załaduj wartość z adresu wskazanego przez adres x (from) do akumulatora
        0101 94201 ; załaduj wartość z akumulatora do adresu wskazanego przez adres to (a)
end:    0102 00000 ; zakończ działanie programu


'''

# Perform the copy operation
EpromMemoryAddressP5 = CopyFromTo(MemoryCellsP5, fromP5, toP5)

# Print the memory after copying
print("P5 Memory after copying from 'a':", EpromMemoryAddressP5)
print()


'''
P6: Dany jest wektor 'v' o 'n' składowych. Oblicz sumę wszystkich
składowych wektora i zapisz pod adresem 's'.
'''

EpromMemoryAddressP6 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
nP6 = int(12) #Number of components
vP6 = 1 #Address of first component 
sP6 = 0 #Resoult cell

print (f"Before P6 {EpromMemoryAddressP6}\n")

def AddComponents(Memo, vBegin, nOfComponents, s):
    Memo[s] = 0 # Clearing cell with final resoult
    if vBegin>nOfComponents:
        v=nOfComponents
        n=vBegin
    else:
        n=nOfComponents
        v=vBegin
    while True:
        if v == n + 1:
            break
        else:
            print (f"{v}, {Memo[v]}")
            Memo[s] = Memo[s] + Memo[v]
            v = v + 1 
    return Memo [s]
    
'''Assembler

.data 0 

0000 00000 ; s: wynik adres s - wynik
0001 00002 ; adres pod zawierający informace o ilości składowych wektorów n
0002 00003 ; adres pierwszego wektora v
0003 00001 ; pierwsza składowa wektora v
0004 00002 ;
0005 00004 ;

.code 100

begin:
0100 92100 ;       CPA (0) ; Do akumulatora Kopiuje 0
0101 20000 ;       STO s   ; Zeruje wynik 
0102 10000 ; loop: CPA s   ; Wczytuje aktualną wartość wyniku
0103 94302 ;       ADD [2] ; pierwszej składowej do akumulatora
0104 20000 ;       STO s   ; Zapisanie aktualnego wyniku
0105 02001 ;       DEC n   ; obniżam ilość pozostałych n składowych (licznik)
0106 10001 ;       CPA n   ; Kopiuje wartość licznika składowych do akumulatora
0107 80110 ;       BRZ end ; idź na koniec jeżeli akumulator przyjmuje wartość 0
0108 01002 ;       INC v   ; zwiększam wartość w adresie zawierającym dodawany aby wskazał kolejny potencjalny wektor
0109 60102 ;       BRA loop; wróć bezwarunkowo do początku pętli
0110 00000 ; end:  HLT     ; zakończenie programu 
   
'''

EpromMemoryAddressP6 = AddComponents(EpromMemoryAddressP6, vP6, nP6, sP6)

print (f"\nP6 Memory after addition all of components from {vP6} to {nP6} is", EpromMemoryAddressP6)