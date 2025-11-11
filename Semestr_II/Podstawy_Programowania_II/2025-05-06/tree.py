"""
W drzewach mniejsze elementy idą w lewo, a większe w prawo
np drzewo 3 1 2          2 3 1
"""
#        [3]              [2]
#        /                  \
#       /                    \
#     [1]                    [3]
#       \                    /
#        \                  /      
#        [2]              [2]   

"""
W drzewach BST
Służy do wyszukiwań w bazach danych
np drzewo 3 1 2          2 3 1    
"""    
#            [3]           [2]
#             /            / \
#            /            /   \
#          [1]          [1]   [3]
#           \
#            \
#           [2]


tree = [1, 2, 3, 4, 5, 6, 7]

def get_left_child(index):
    """Zwraca lewe dziecko o danym indeksie"""
    return 2 * index + 1

def get_right_child(index):
    """Zwraca prawe dziecko o danym indeksie"""
    return 2 * index + 2

def get_parent(index):
    """Zwraca rodzica węzła o podanym indeksie"""
    return (index-1) // 2

# Dostęp do elementów drzewa
index = 0 # Korzeń drzewa
left_child_index = get_left_child(index)
rigth_child_index = get_right_child(index)

print(f"Zawartość korzenia: {tree[index]}")
print(f"Lewe dziecko korzenia: {tree[left_child_index]}")
print(f"Prawe dziecko korzenia: {tree[rigth_child_index]}")


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.rigth = None
        self.parent = None

# lista [3, 5, 7, 10, 20]
root = Node(10)
root.left = Node(5)
root.rigth = Node(20)
root.left.left = Node(3)
root.left.rigth = Node(7)


class BST:
    def  __init__(self, value):
        self.value = value
        self.left = None
        self.rigth = None
        self.parent = None

    def insert(self, new_value):
        if new_value < self.value:
            if self.left is None:
                self.left = BST (new_value)
                self.parent = self 
            else:
                self.left.insert(new_value)
        else:
            if self.rigth is None:
                self.rigth = BST (new_value)
                self.parent = self
            else:
                self.rigth.insert(new_value)

## do domy jak zrobić drzewo obliczjące (2+4)*7/4

    def search(self, search_value):
        if search_value == self.value:
            return self
        elif search_value < self.value and self.left is not None:
            return self.left.search(search_value)
        elif search_value > self.value and self.right is not None:
            return self.right.search(search_value)
        return None
    
    def find_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current
    
    def find_max(self):
        current = self
        while current.rigth is not None:
            current = current.rigth
        return current
    
    def delate(self, value):
        if value < self.value:
            if self.left is not None:
                self.left = self.left.delate(value)
        elif value > self.value:
            if self.rigth is not None:
                self.rigth = self.rigth.delate(value)
        
        else:
            # Usuwanie węzła 
            if self.left is None and self.rigth is None:
                return None
            elif self.left is None:
                self.left.parent = self.parent
                return self.left
            else:
                # węzeł z dwam dziaćmi
                min_node = self.rigth.find_min()
                self.value = min_node.value
                self.rigth = self.rigth.delate(min_node.value)
            return self