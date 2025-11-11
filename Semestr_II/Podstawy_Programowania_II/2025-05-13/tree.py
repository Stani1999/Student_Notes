# Drzewa zbalanmsowane
# Drzewa AVL (modyfikacja drzewa BST. tak aby były) 


#Napisz drzewo AVL, które będzie miało następujące metordy
# Pre order
# In order
# Post order

# Wyskoość drzewa n-elemenowego drzewa AVL wynosi O(log n)
# Drzewo AVL jest drzewem BTS, które jest zbalanbsiowane 

# Rodzaje rotacji w drzewach AVL
## Ruch w lewo LL (left-left)
# Chodzi w niej o to, że węzeł jest dodawany do lewego poddrzewaa

# Ruch w prawo RR (rigth-rigth)
# Chodzi w niej o to, że węzeł jest dodawany do prawego poddrzewia

# Ruch w lewo-prewo LR (left-rigth)
# Chodzi w niej o to, że węzeł jest dodawany do prawego poddrzewia lewego węzłą.

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None 
        self.right = None
        self.height = 1

class AVLTree:
    # Get height of a node
    def get_height(self, node):
        if not node:
            return 0
        return node.height
    
    # Get balance factor of a node
    def get_balance(self, node):
        if not node:
            return 0 
        return self.get_height(node.left) - self.get_height(node.right)
    
    # Right rotation for LL case
    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y 
        y.left = T2 

        # Update heights
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x
    
    # Left rotation for RR case
    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y
    
    def insert(self, root, key): 
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Check balance
        balance = self.get_balance(root)
        
        # LL Case
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        
        # RR Case
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        
        # LR Case
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        
        # RL Case
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root
    
    # Tree traversal methods
    def preorder(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
    
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)
    
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end=" ")


# Test the AVL tree
if __name__ == "__main__":
    tree = AVLTree()
    root = None
    keys = [10, 20, 30, 40, 50, 25]
    
    for key in keys:
        root = tree.insert(root, key)
    
    print("Preorder AVL tree is:")
    tree.preorder(root)
    print("\nInorder AVL tree is:")
    tree.inorder(root)
    print("\nPostorder AVL tree is:")
    tree.postorder(root)