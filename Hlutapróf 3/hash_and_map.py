class Node:
    def __init__(self, key=None, data=None, next=None):
        self.key = key
        self.data = data
        self.next = next

class Map:
    def __init__(self):
        self.capacity = 4
        self.size = 0
        self.arr = [None] * self.capacity

    def insert(self, key, value):
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size] = Node(key, value)
        self.size += 1
    
    def insert_ordered(self, key, value):
        if self.size == self.capacity:
            self.resize()

        new_node = Node(key, value)
        i = self.size - 1
        while i >= 0 and self.arr[i].key > key:
            self.arr[i + 1] = self.arr[i]
            i -= 1
        self.arr[i + 1] = new_node
        self.size += 1

    def find(self, key):

        for i in range(self.size):

            if self.arr[i].key == key:
                return self.arr[i].data
    
    def update(self, key, value):

        for i in range(self.size):

            if self.arr[i].key == key:
                self.arr[i].data = value

    def remove(self, key):

        iter = 0
        jumper = 0

        for i in range(self.size):

            if self.arr[i].key == key:

                jumper += 1
            
            self.arr[iter] = self.arr[jumper]
            iter += 1
            jumper += 1
        
        self.size -= 1

    def resize(self):
        self.capacity *= 2
        new_arr = [None] * self.capacity

        for i in range(self.size):
            new_arr[i] = self.arr[i]

        self.arr = new_arr

    def __len__(self):

        sum = 0

        for i in range(self.capacity):
            if self.arr[i] is not None:
                sum += 1
        
        return sum

    def __str__(self):
        result = ""
        for i in range(self.size):
            if self.arr[i] is not None:
                result += f"({self.arr[i].key}: {self.arr[i].data}) "
        return result
    
    def __hash__(self, node) -> int:
        return hash(node.key)

    def __eq__(self, other) -> bool:
        
        for i in range(self.capacity):

            if self.arr[i] != other.arr[i]:
                return False
            return True


def hash(some_value):

        ret_val = ''

        
        hash_val = 0
        for char in some_value:
            hash_val = (hash_val * 79 + ord(char)) % 10**12
            if hash_val < 3919:
                hash_val = hash_val * 80 % 1234 
        return hash_val






if __name__ == '__main__':

    lis_size = 15
    di = dict()

    for i in range(lis_size):

        index = hash(str(i))

        if index in di:

            di[index] += 1
        
        else:
            di[index] = 1
    

    import math

    max = -99999999999999999999999999999999999999999999999999999999999999
    min = 9999999999999999999999999999999999999999999999999999999999

    for key, value in di.items():

        print(key, end=' ')
        
        if key > max:
            max = key
        elif key < min:
            min = key
    
    print()
    diff = max - min
    ratio = diff / max
    print(round(ratio, 2))




# difference = max - min
# ratio = difference / max
# perfect distribution == 0