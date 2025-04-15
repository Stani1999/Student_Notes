graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 1, 'C': 5},
    'C': {'D': 8, 'F': 2},
    'D': {'F': 2},
    'F': {} 
}

    #ustawiamy wieszchołki na nieskońconość
    # pierwszy element ustawiamy na 0

    #pętla while dla nie odwiedzonych elementów

        # wybieramy wierzchołek o najmniejszej wartości

        # jeżeli nie ma wierzchołków to koniec

        # sprawdzamy sąsiadów wybranego wierzchołka
            # jeżeli trasa jest krótsza to aktualizujemy

        # zaznaczamy wieszhołek odwiedzony

        # zwróc dystans
        
# wywołanie


def dijkstra(graph, start_node):
    # Ustawiamy wszystkie wierzchołki na nieskończoność
    distances = {node: float('infinity') for node in graph}
    # Pierwszy element ustawiamy na 0
    distances[start_node] = 0
    visited = set()
    
    # Pętla while dla nieodwiedzonych elementów
    while True:
        # Wybieramy wierzchołek o najmniejszej wartości
        current_node = None
        min_distance = float('infinity')
        for node in graph:
            if node not in visited and distances[node] < min_distance:
                min_distance = distances[node]
                current_node = node
        
        # Jeżeli nie ma wierzchołków to koniec
        if current_node is None:
            break
            
        # Sprawdzamy sąsiadów wybranego wierzchołka
        for neighbor, weight in graph[current_node].items():
            distance = distances[current_node] + weight
            # Jeżeli trasa jest krótsza to aktualizujemy
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                
        # Zaznaczamy wierzchołek jako odwiedzony
        visited.add(current_node)
    
    return distances

# Wywołanie
start_node = 'A'
shortest_distances = dijkstra(graph, start_node)
print(f"Najkrótsze ścieżki z węzła {start_node}:")
for node, distance in shortest_distances.items():
    print(f"Do {node}: {distance}")