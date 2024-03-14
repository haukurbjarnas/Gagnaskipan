class Node:

    def __init__(self, data = None) -> None:
        
        self.data = data
        self.next = None

class Bucket:

    def __init__(self) -> None:
        
        self.head = Node(None, None, None)

    def insert(self, key, data):
        
        curr = self.head.next

        while curr is not None:

            pass

    def update(self, key, data):
        pass

    def find(self, key):
        pass

    def contains(self, key):
        pass