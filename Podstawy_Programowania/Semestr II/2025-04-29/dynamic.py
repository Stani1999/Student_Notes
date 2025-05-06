''' 
Programowanie dynamiczne 
Metoda rozwiązywania problemu polegająca na rozbijaniu ich na mniejsze podproblemy.
Każdy problem rozwiązuje się tylko raz zapisując jego wyniki.
++ Optymalizacja pamięci

-- Problem plecakowy 
--- praremtry typu wielkość i waga
--- oblicza się na podstawie wzoru.
'''

def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    
    # Śledzenie wybranych przedmiotów
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i-1)  # Indeks przedmiotu
            w -= weights[i-1]
    
    selected_items.reverse()  # Aby zachować kolejność dodawania
    return dp[n][capacity], selected_items

def main():
    print("Problem plecakowy (0-1 Knapsack)")
    print("---------------------------------")
    
    values = list(map(int, input("Podaj wartości przedmiotów (oddzielone przecinkami): ").split(",")))
    weights = list(map(int, input("Podaj wagi przedmiotów (oddzielone przecinkami): ").split(",")))
    capacity = int(input("Podaj pojemność plecaka: "))
    
    if len(values) != len(weights):
        print("Błąd: Liczba wartości i wag musi być taka sama!")
        return
    
    if capacity < 0:
        print("Błąd: Pojemność plecaka nie może być ujemna!")
        return
    
    max_value, selected = knapsack(values, weights, capacity)
    
    print(f"\nMaksymalna wartość w plecaku: {max_value}")
    print("Wybrane przedmioty:")
    for idx in selected:
        print(f"- Przedmiot {idx+1}: wartość = {values[idx]}, waga = {weights[idx]}")
    
    print("\nPodsumowanie:")
    print(f"Liczba wybranych przedmiotów: {len(selected)}")
    print(f"Sumaryczna waga: {sum(weights[i] for i in selected)}/{capacity}")
    print(f"Sumaryczna wartość: {max_value}")

if __name__ == "__main__":
    main()