class Stack:

    def __init__(self) -> None:
        self.size = 0
        self.capacity = 4
        self.arr = [0]*self.capacity

    # O(1)
    def pop(self):

        val = self.arr[self.size-1]
        
        self.arr[self.size-1] = 0

        self.size -= 1

        return val

    # O(1)
    def push(self, value):

        if self.size == self.capacity:
            self.resize()
        
        self.arr[self.size] = value

        self.size += 1

    def resize(self):
        self.capacity = self.capacity*2

# circular buffer aðferð
class Queue:

    def __init__(self) -> None:
        self.size = 0
        self.capacity = 4
        self.arr = [None]*self.capacity
        self.head = 0
        self.tail = 0


    def resize(self):
        new_arr = [None] * (self.capacity * 2)

        for i in range(self.size):
            new_arr[i] = self.arr[(self.head + i) % self.capacity]

        self.arr = new_arr
        self.head = 0
        self.tail = self.size
        self.capacity *= 2

    # O(1)
    def add(self, value):

        if self.size == self.capacity:
            self.resize()

        self.arr[self.tail] = value

        self.tail = (self.tail + 1) % self.capacity

        self.size += 1

    # O(1)
    def remove(self):
        
        val = self.arr[self.head]

        self.arr[self.head] = None

        self.head = (self.head + 1) % self.capacity

        self.size -= 1

        return val


class Deque:

    def __init__(self) -> None:
        self.size = 0
        self.capacity = 4
        self.arr = [None] * self.capacity
        self.head = 0
        self.tail = 0
    
    def resize(self):
        new_arr = [None] * (self.capacity * 2)

        for i in range(self.size):
            new_arr[i] = self.arr[(self.head + i) % self.capacity]

        self.arr = new_arr
        self.head = 0
        self.tail = self.size
        self.capacity *= 2


    def push_front(self, value):
        pass

    def push_back(self, value):
        pass

    def pop_front(self):
        pass

    def pop_back(self):
        pass