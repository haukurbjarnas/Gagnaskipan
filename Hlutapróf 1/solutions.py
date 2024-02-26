class ArrayList:
    def __init__(self):
        self.capacity = 4
        self.size = 0
        self.array = [None] * self.capacity

    def __str__(self):
        ret_str = ""
        for i in range(0, self.size):
            ret_str += str(self.array[i]) + " "
        return ret_str
    
    def resize(self):
        if self.capacity == self.size:
            self.capacity *= 2
            temparr = [None] * self.capacity
            for i in range(0, self.size):
                temparr[i] = self.array[i]
            self.array = temparr

    def append(self, value):
        self.resize()
        self.array[self.size] = value
        self.size += 1

    def remove_largest(self):

        biggest = 0
        
        for elem in range(self.size-1):

            if self.array[elem] > biggest:
                biggest = self.array[elem]



        counter = 0
        shifter = 1

        while counter < self.size:

            if self.array[counter] == biggest:

                while counter < self.size:

                    self.array[counter] = self.array[shifter]
                    
                    counter += 1
                    shifter += 1

            

            else:
                counter += 1
                shifter += 1

        
        self.size -= 1





def count_in_range(lis, range_from, range_to):
    
    if len(lis) == 0:
        return 0
    
    if lis[0] >= range_from and lis[0] <= range_to:
        return 1 + count_in_range(lis[1:], range_from, range_to)
    
    else:
        return 0 + count_in_range(lis[1:], range_from, range_to)

def remove_odd_indexes(lis, counter=0):
    
    if counter == len(lis):
        return lis
    
    
    if counter % 2 == 0:
        counter += 1
        return remove_odd_indexes(lis, counter)

    else:
        lis.remove(lis[counter])
        counter += 1
        return remove_odd_indexes(lis, counter)

if __name__ == "__main__":
    print("Arraylist tests:")
    arrlis = ArrayList()
    arrlis.append(8)
    arrlis.append(62)
    arrlis.append(15)
    arrlis.append(19)
    arrlis.append(24)
    arrlis.append(7)
    print(arrlis)
    arrlis.remove_largest()
    print(arrlis)
    arrlis.remove_largest()
    print(arrlis)
    arrlis.remove_largest()
    print(arrlis)
    arrlis.remove_largest()
    print(arrlis)
    arrlis.remove_largest()
    print(arrlis)
    arrlis.remove_largest()
    print(arrlis)
    print("Recursion tests:")
    print(count_in_range([5,1,22,7,19,8,31,4,6,10,17,13], 5, 20))
    print(count_in_range([5,1,22,7,19,8,31,4,6,10,17,13], 1, 5))
    print(count_in_range([5,1,22,7,19,8,31,4,6,10,17,13], 0, 25))
    print(count_in_range([5,1,22,7,19,8,31,4,6,10,17,13], 0, 100))
    print(remove_odd_indexes([5,1,22,7,19,8,31,4,6,10,17,13]))
    