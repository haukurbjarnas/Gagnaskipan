class BinaryTreeNode:

    def __init__(self, data = None, left = None, right = None) -> None:
        
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:

    def __init__(self) -> None:
        
        self.root = None
    
    def populate_tree_recur(self):
        
        data_val = input()

        if data_val == '':
            return
        
        node = BinaryTreeNode(data = data_val)
        node.left = self.populate_tree_recur()
        node.right = self.populate_tree_recur()
        return node

    def populate_tree(self):

        self.root = self.populate_tree_recur()


    def preorder_recur(self, node):
        
        if node == None:
            return
        
        print(node.data, end=' ')
        self.preorder_recur(node.left)
        self.preorder_recur(node.right)

    def preorder(self):
        self.preorder_recur(self.root)




    def postorder_recur(self, node):
        
        if node == None:
            return
        
        self.postorder_recur(node.left)
        self.postorder_recur(node.right)
        print(node.data, end=' ')

    def postorder(self):
        self.postorder_recur(self.root)




    def inorder_recur(self, node):
        
        if node == None:
            return
        
        self.inorder_recur(node.left)
        print(node.data, end=' ')
        self.inorder_recur(node.right)

    def inorder(self):
        self.inorder_recur(self.root)



class GeneralTreeNode:

    def __init__(self) -> None:
        
        self.node = None
        self.children = []


class GeneralTree:

    def __init__(self) -> None:
        
        self.root = None

    
    def populate_tree_recur(self):
        
        children_len = int(input('Enter amount of children: '))

        node = GeneralTreeNode()

        while len(node.children) < children_len:
            data_val = input()
            node.data = data_val
            node.children.append(self.populate_tree_recur())

    def populate_tree(self):
        self.populate_tree_recur()


if __name__ == '__main__':

    gt = GeneralTree()
    gt.populate_tree()