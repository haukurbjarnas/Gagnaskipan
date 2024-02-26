class Stack:

    def __init__(self) -> None:
        self.size = 0
        self.capacity = 4
        self.arr = [0]*self.capacity


    def push(self, value):

        if self.capacity == self.size:
            self.resize()
        
        self.arr[self.size] = value

        self.size += 1


    def pop(self):

        clone = self.arr[self.size-1]

        self.arr[self.size-1] = 0

        self.size -= 1

        return clone
    

    def resize(self):

        self.capacity = self.capacity * 2

        lis_clone = [0]*self.capacity

        counter = 0

        while counter <= self.size-1:

            lis_clone[counter] = self.arr[counter]

            counter += 1


        self.arr = lis_clone
    
    def __str__(self):

        return_string = ''
        for elem in self.arr:
            elem_str = str(elem) + (', ')
            return_string += elem_str
            
        return return_string[:-2]



class Queue:

    def __init__(self) -> None:
        self.size = 0
        self.capacity = 4
        self.arr = [0]*self.capacity

    def add(self, value):
        
        if self.size == self.capacity: self.resize()

        self.arr[self.size] = value

        self.size += 1

    
    
    
    def remove(self):
        
        clone = self.arr[0]

        self.arr[0] = 0

        counter = 0
        shift_counter = 1

        while counter <= self.size:

            self.arr[counter] = self.arr[shift_counter]

            counter += 1
            shift_counter += 1


        self.size -= 1

        return clone

    
    
    
    def resize(self):

        self.capacity = self.capacity * 2

        lis_clone = [0]*self.capacity

        counter = 0

        while counter <= self.size-1:

            lis_clone[counter] = self.arr[counter]

            counter += 1


        self.arr = lis_clone

    def __str__(self):

        return_string = ''
        for elem in self.arr:
            elem_str = str(elem) + (', ')
            return_string += elem_str
            
        return return_string[:-2]
    

class Deque:

    def __init__(self) -> None:
        self.size = 0
        self.capacity = 4
        self.arr = [0]*self.capacity

    def pop_front(self):
        
        clone = self.arr[0]

        self.arr[0] = 0

        counter = 0
        shift_counter = 1

        while counter <= self.size:

            self.arr[counter] = self.arr[shift_counter]

            counter += 1
            shift_counter += 1


        self.size -= 1

        return clone

    def pop_back(self):

        if self.size == self.capacity: self.resize()

        clone = self.arr[self.size-1]

        self.arr[self.size-1] = 0

        self.size -= 1

        return clone

    def push_front(self, value):

        if self.size == self.capacity: self.resize()

        self.arr[self.size-1] = value

    def push_back(self):

        if self.size == self.capacity: self.resize()

    def resize(self):

        self.capacity = self.capacity * 2

        lis_clone = [0]*self.capacity

        counter = 0

        while counter <= self.size-1:

            lis_clone[counter] = self.arr[counter]

            counter += 1


        self.arr = lis_clone

    
    def __str__(self):

        return_string = ''
        for elem in self.arr:
            elem_str = str(elem) + (', ')
            return_string += elem_str
            
        return return_string[:-2]
    

queue = Queue()
queue.add(1)
queue.add(2)
print(queue)


stack = Stack()
stack.push(1)
stack.push(2)
print(stack)