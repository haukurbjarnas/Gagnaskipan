class Node:

    def __init__(self, data=None, prev=None, next=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev


class DLL_Deque:

    def __init__(self) -> None:
        self.sentinel = Node(None, None, None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel


    # Problem 1
    def add_front(self, data):
        
        new_node = Node(data = data, prev = self.sentinel, next = self.sentinel.next)

        self.sentinel.next.prev = new_node

        self.sentinel.next = new_node

    # Problem 2
    def add_back(self, data):
        
        new_node = Node(data = data, prev = self.sentinel.prev , next = self.sentinel)

        self.sentinel.prev.next = new_node

        self.sentinel.prev = new_node

    # Problem 3
    def remove_front(self):
        
        self.sentinel.next = self.sentinel.next.next

        self.sentinel.next.prev = self.sentinel

    # Problem 4
    def remove_back(self):
        
        self.sentinel.prev = self.sentinel.prev.prev

        self.sentinel.prev.next = self.sentinel

    # Problem 5
    def get_val_front(self):
        
        val = self.sentinel.next.data

        return val

    # Problem 6
    def get_val_back(self):
        
        val = self.sentinel.prev.data

        return val



my_lis = DLL_Deque()

my_lis.add_front(3)
my_lis.add_front(2)
my_lis.add_front(1)
my_lis.add_back(4)
print(my_lis.get_val_front())
print(my_lis.get_val_back())

current_node = my_lis.sentinel.next
while current_node != my_lis.sentinel:
    print(current_node.data)
    current_node = current_node.next