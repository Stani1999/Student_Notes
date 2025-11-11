## Lista jednokierunkowa

class Node:
    """Klasa reprezentująca pojedynczy węzeł listy jednokierunkowej.
        - data: przechowuje wartość danego węzła
        - next wskoźnik do następnego węzła (domylśnie NODE)"""

    def __init__(self, data):
        """Inicjalizacja data"""
        self.data = data  # Przechowuje wartość danego węzła
        self.next = None  # Ustaw next na None
        

class SingelyLinkedList: 
    """Klasa reprezentująca listę jednokierunkową."""
#     
    def __init__(self):
        """Inicjalizacja pustej listy"""
        # head: wskaźnik na pierwszy węzeł (domylśnie None)
        self.head = None   # - Inicjalizacja head jako None
    
    def append(self, data):
        """Dodaje nowy węzeł z danymi na koniec listy.
        
        Args:
            data: Wartość do dodania.
        """
        new_node = Node(data)  # Utwórz nowy wenzeł z wartością data
        
        if self.head is None:        # Jeśli Head jest None:
            self.head = new_node# Ustaw head na nowy węzeł
        else: # W przeciwnym razie:
        # Przejdź pezez listę do ostatniego węzła
            lastNode = self.head
            while lastNode.next is not None: 
                lastNode = lastNode.next
            lastNode.next = new_node # Ustaw next ostatniego węzłą na nowy węzeł

    def display(self):
        """Wyświetla zawartość listy"""
        if self.head is None: # Jeżeli hed jest Node:
            print("Lista jest puszta")# Wyświetl "Lista jest pusta"
        else: # W przeciwnym razie:
            i = self.head# zaczynając od head
            while i is not None: # Przejdź przez każdy węzeł
                print(i.data, end=" --> " if i.next else "")
                i = i.next# Wyświetl wartość każdego węzła po kolei
            print() #Nowa linia

    def delete(self, data):
        """Usuwa (pierwszą) pozycję z kolejki"""
        if self.head is None: # Jeżeli head jest Node:
            print("Lista jest pusta") # Wyświetl "Lista jest pusta"
            return # Zakończ operację

        if self.head == data: # Jeśli wartość head.data równa się data:
            self.head = self.head.next # Ustaw head na head.next (usuń pierwszy element)
            return # Zajkończ operację

        i = self.head
        #  Przejdź przez listę, szukając węzła z wartością data
        while i.next is not None and i.next.data != data:
            i = i.next
        
        if i.next is not None:  # Jeśli znajdziesz taki węzeł:
            i.next = i.next.next # Usuń go ustawiając wskaźnik poprzedniego węzłą na następny węzeł

# Przykład użycia
if __name__ == "__main__":
    # Tworzymy listę
    singelist = SingelyLinkedList()
    
    # Dodajemy elementy
    singelist.append(6)
    singelist.append(9)
    singelist.append(20)
    
    # Wyświetlamy listę
    print("Lista przed usunięciem:")
    singelist.display()  # 6 -> 9 -> 20
    
    # Usuwamy element
    singelist.delete(20)
    print("\nLista po usunięciu 20:")
    singelist.display()  # 6 -> 9
    
    # Próba usunięcia nieistniejącego elementu
    print("\nPróba usunięcia 99:")
    singelist.delete(99)  # Nic się nie dzieje
    singelist.display()   # 6 -> 