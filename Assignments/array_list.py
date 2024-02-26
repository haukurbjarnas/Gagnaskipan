class IndexOutOfBounds(Exception):
    pass

class NotFound(Exception):
    pass

class Empty(Exception):
    pass

class NotOrdered(Exception):
    pass

class ArrayList:
    def __init__(self):
        # TODO: remove 'pass' and implement functionality
        self.capacity = 4
        self.size = 0
        self.arr = [0] * self.capacity

    #Time complexity: O(n) - linear time in size of list
    def __str__(self):
        # TODO: remove 'pass' and implement functionality
        return_string = ''
        for elem in self.arr:
            elem_str = str(elem) + (', ')
            return_string += elem_str
            
        return return_string[:-2]

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        # TODO: remove 'pass' and implement functionality
        
        return self.insert(value, 0)

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        # TODO: remove 'pass' and implement functionality

        if self.size >= self.capacity:
            self.resize()
        shift_counter = self.size
        arr_counter = self.size-1
        while shift_counter >= index:
            if shift_counter == index:
                self.arr[index] = value
                shift_counter -= 1
            else:
                self.arr[shift_counter] = self.arr[arr_counter]
                shift_counter -= 1
                arr_counter -= 1
        
        self.size += 1







        
        

    #Time complexity: O(1) - constant time
    def append(self, value):
        # TODO: remove 'pass' and implement functionality

        if self.size >= self.capacity:
            self.resize()
            self.arr[self.size] = value
            self.size += 1
        else:
            self.arr[self.size] = value
            self.size += 1

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        # TODO: remove 'pass' and implement functionality
        
        self.arr[index] = value

    #Time complexity: O(1) - constant time
    def get_first(self):
        # TODO: remove 'pass' and implement functionality
        
        try:
            return self.arr[0]
        except IndexError:
            raise Empty()

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        # TODO: remove 'pass' and implement functionality
        
        try:
            return self.arr[index]
        except IndexError:
            raise IndexOutOfBounds()

    #Time complexity: O(1) - constant time
    def get_last(self):
        # TODO: remove 'pass' and implement functionality
        
        try:
            return self.arr[self.size-1]
        except IndexError:
            raise IndexOutOfBounds()

    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        # TODO: remove 'pass' and implement functionality
        
        self.capacity = self.capacity * 2
        clone = [0]*self.capacity
        counter = self.size-1
        while counter >= 0:
            clone[counter] = self.arr[counter]
            counter -= 1
        self.arr = clone
        return self.arr

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        # TODO: remove 'pass' and implement functionality
        
        if index < 0 or index > self.size - 1:
            raise IndexOutOfBounds()
        
        for i in range(index, self.size-1):
            self.arr[i] = self.arr[i + 1]
        self.size -= 1
        self.arr[self.size] = 0

    #Time complexity: O(1) - constant time
    def clear(self):
        # TODO: remove 'pass' and implement functionality
        
        for i in range(self.size):
            self.arr[i] = 0

    #Time complexity: O(n) - linear time in size of list
    def insert_ordered(self, value):
        # TODO: remove 'pass' and implement functionality

        for i in range(1, self.size):

            if self.arr[i - 1] > self.arr[i]:
                raise NotOrdered()
            
        
        index = self.size-1

        while index >= 0:

            if value < self.arr[index] and value > self.arr[index-1]:
                self.insert(value, index)

            else:
                index -= 1

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value):
        # TODO: remove 'pass' and implement functionality
        
        raise NotFound()

    #Time complexity: O(n) - linear time in size of list
    def remove_value(self, value):
        # TODO: remove 'pass' and implement functionality
        pass


if __name__ == "__main__":
    array_lis = ArrayList()
    array_lis.append('a')
    array_lis.append(2)
    array_lis.insert(5, 7)
    try:
        array_lis.remove_at(8)
    except IndexOutOfBounds:
        print('Já sæll')
    print(array_lis)
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level