class Node:

    def __init__(self, key = None, val = None, prev = None, next = None) -> None:

        self.key = key
        
        self.val = val

        self.prev = prev

        self.next = next


class DLL_Map:

    def __init__(self) -> None:
        
        self.sentinel = Node(None, None, None, None)

        self.sentinel.prev = self.sentinel

        self.sentinel.next = self.sentinel

        self.size = 0

    

    def insert(self, key, value):

        new_node = Node(key, value, self.sentinel.prev.next, self.sentinel)

        self.sentinel.prev.next = new_node

        self.sentinel.next = new_node

        self.size += 1
    


    def find(self, key):

        curr_node = self.sentinel.next

        while curr_node is not None:

            if curr_node.key == key:

                return curr_node.data
            
            curr_node = curr_node.next




    def update(self, key, value):

        curr_node = self.sentinel.next

        while curr_node is not None:

            if curr_node.key == key:

                curr_node.data = value
            
            curr_node = curr_node.next



    def remove(self, key):

        curr_node = self.sentinel.next

        while curr_node is not None:

            if curr_node.key == key:

                curr_node.prev.next = curr_node.next

                curr_node.next.prev = curr_node.prev
            
            curr_node = curr_node.next

        self.size -= 1

    
    def __eq__(self, other) -> bool:

        pass


    def __hash__(self):

        pass

    
    def __str__(self) -> str:

        curr = self.sentinel.next

        while curr is not None:

            print(curr.data, end=' ')

            curr = curr.next


def hash(val):

    enco_val = val.encode('utf-8')


    for i in enco_val:

        