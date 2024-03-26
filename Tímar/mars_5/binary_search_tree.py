class Node:
    
    def __init__(self, data = None, left = None, right = None) -> None:
        
        self.data = data
        self.left = left
        self.right = right
    

class BST:

    def __init__(self) -> None:
        self.root = None

    def populate_tree(self):
        val = input('Enter value: ')
        self.populate_tree_recursive(self.root, val)

    def populate_tree_recursive(self, node, val):

        if node is None:
            return Node(val)
        elif val < node.data:
            self.populate_tree_recursive(node.left, val)
        elif val > node.data:
            self.populate_tree_recursive(node.right, val)

        return node
    
    def print_preorder(self):
        self.print_preorder_recursive(self.root)
    
    def print_preorder_recursive(self, node):

        if node is None:
            return
        
        print(node, end=' ')
        self.print_preorder_recursive(node.left)
        self.print_preorder_recursive(node.right)
    
    def print_inorder(self):
        self.print_inorder_recursive(self.root)

    def print_inorder_recursive(self, node):
        
        if node is None:
            return
        
        self.print_inorder_recursive(node.left)

        print(node, end=' ')

        self.print_inorder_recursive(node.right)

    def print_postorder(self):
        self.print_postorder_recursive(self.root)

    def print_postorder_recursive(self, node):
        
        print(node, end=' ')
        self.print_postorder_recursive(node.right)
        self.print_postorder_recursive(node.left)  


class ADT:

    def __init__(self) -> None:
        self.tree = BST()

    def add(self, value):
        pass

    def contains(self, value):
        pass

    def remove(self, value):
        pass

    def __len__(self):
        pass

    def __str__(self):
        pass

    