class Node:
    
    def __init__(self, data, next) -> None:
        
        self.data = data
        self.next = next

class SingleLinkedList:

    def __init__(self) -> None:
        
        self.header = Node(None, None)

    def add(self):
        pass