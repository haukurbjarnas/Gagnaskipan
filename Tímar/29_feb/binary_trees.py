class Node:

    def __init__(self, data = None, left = None, right = None) -> None:
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:

    def __init__(self) -> None:
        self.root = None

    def populate_tree(self):
        
        self.root = self.populate_tree_recursive()

    
    def populate_tree_recursive(self):
        
        val = input('Enter value: ')

        if val == None:
            return None

        newnode = Node(val)

        newnode.left = self.populate_tree_recursive()
        newnode.right = self.populate_tree_recursive()

        return newnode
    
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



        
tree = BinaryTree()
tree.populate_tree()
tree.print_preorder()
tree.print_inorder()
tree.print_postorder()     