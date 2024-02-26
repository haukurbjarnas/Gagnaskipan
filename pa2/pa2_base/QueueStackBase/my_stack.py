from array_deque import ArrayDeque
from my_linked_list import LinkedList

class Stack:
    def __init__(self):
        # Pick one of these to use.
        # Stack must have the container you dont choose for Queue
        
        self.container = LinkedList()
        #self.container = ArrayDeque()

    def push(self, data):
        
        node = self.container

        while node.head != None:

            node = node.tail

        node.head = data
    
    def pop(self):
        
        node = self.container

        if node.head == None:
            return None

        jumper = node.next

        while jumper.head != None:

            node = node.next

            jumper = node.next

        val = node.head

        node.head = None

        return val
    
    def get_size(self):
        
        counter = 1

        node = self.container

        while node.head != None:

            counter += 1

            node = node.tail
        
        
        
        return counter

    def __str__(self):
        return ""
