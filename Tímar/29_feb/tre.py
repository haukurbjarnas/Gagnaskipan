class BT_Node:

    def __init__(self, data = None, left = None, right = None) -> None:
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:

    def __init__(self) -> None:
        self.root = None
    
    def populate_tree(self):
        self.root = self.populate_tree_recur()
    
    def populate_tree_recur(self):

        value = input('Enter node value: ')

        if value == '':

            return None

        newnode = BT_Node(value)

        newnode.left = self.populate_tree_recur()

        newnode.right = self.populate_tree_recur()

        return newnode

    def print_preorder(self):
        self.print_preorder_recur(self.root)
    
    def print_preorder_recur(self, node):
        if node is None:
            return
        print(node.data, end=' ')
        self.print_preorder_recur(node.left)
        self.print_preorder_recur(node.right)
    
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


ja = BinaryTree()


ja.populate_tree()
ja.print_preorder()
ja.print_inorder()
ja.print_postorder()