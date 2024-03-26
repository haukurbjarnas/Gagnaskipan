class BST_Node:

    def __init__(self, data = None, left = None, right = None) -> None:
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree:

    def __init__(self) -> None:
        self.root = None
    
    def add(self, value):
        self.root = self.add_recur(self.root, value)
        
    def add_recur(self, node, value):
        if node is None:
            return BST_Node(data = value)
        
        elif node.data > value:
            node.left = self.add_recur(node.left, value)

        elif node.data < value:
            node.right = self.add_recur(node.right, value)

        return node

    def contains(self, value):
        return self.contains_recur(self.root, value)

    def contains_recur(self, node, value):
        if node == None:
            return False
        
        elif node.data > value:
            return self.contains_recur(node.left, value)
        
        elif node.data < value:
            return self.contains_recur(node.right, value)

        elif node.data == value:
            return True
        
    def count_nodes(self, node):
        if node is None:
            return 0
        
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)
    
    def __len__(self):
        return self.count_nodes(self.root)
    
    def preorder_recur(self, node):

        if node is None:
            return ''
        
        result = ''
        result +=  f'{node.data} '
        result += self.preorder_recur(node.left)
        result += self.preorder_recur(node.right)

        return result
    
    def __str__(self) -> str:
        
        return self.preorder_recur(self.root)
    

    def remove(self, value):
        
        self.root = self._remove_recur(self.root, value)

    def _remove_recur(self, node, value):

        if node is None:
            return node


        
        if node.data < value:
            node.right = self._remove_recur(node.right, value)

        elif value < node.data:
            node.left = self._remove_recur(node.left, value)

            '''The node to remove has been found'''
        else:
            
            # 1. tilfelli: Nóða hefur engin börn
            if node.left is None and node.right is None:
                return None

            # 2. tilfelli: Nóða hefur eitt barn
            elif node.left is None:
                return node.right

            elif node.right is None:
                return node.left

            # 3. tilfelli: Nóðahefur tvö börn
            else:
                '''The node has two children'''
                
                successor = self._left_most(node.right)
                print(successor.data)

                node.data = successor.data

                node.right = self._remove_recur(node.right, successor.data)


        return node

    def _left_most(self, node):
        
        if node.left is None:
            return node
        
        return self._left_most(node.left)
    


    def _right_most(self, node):
        
        if node.right is None:
            return node
        
        return self._right_most(node.right)
        
if __name__ == '__main__':

    bts = BinarySearchTree()
    bts.add(5)
    bts.add(2)
    bts.add(1)
    bts.add(8)
    bts.add(10)
    bts.add(4)
    bts.add(7)
    print(bts)
    bts.remove(8)
    print(bts)