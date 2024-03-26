class HeapNode:
    def __init__(self, priority, data = None, parent = None, left = None, right = None) -> None:
        self.priority = priority
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right
    
class PriorityQueue:
    def __init__(self) -> None:
        self.root = None
        self.last_node = None
    
    def add(self, priority, value):

        curr = self.root
        
        if self.root == None:

            self.last_node = self.root = HeapNode(priority, value)
        
        elif self.last_node is curr.left:

            pass

        elif self.last_node is curr.right:
            pass



if __name__ == '__main__':

    bla = PriorityQueue()
    print(bla)