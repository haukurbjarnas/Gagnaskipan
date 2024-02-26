
class Node:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self):
        self.size = 0
        self.sentinel = Node()
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel
        self.curr = self.sentinel.next.prev


    def insert(self, data):

        new_node = Node(data)

        if self.curr is None or self.curr == self.sentinel:
            new_node.next = self.sentinel.next
            new_node.prev = self.sentinel
            self.sentinel.next.prev = new_node
            self.sentinel.next = new_node
            
        else:
            new_node.prev = self.curr.prev
            new_node.next = self.curr
            self.curr.prev.next = new_node
            self.curr.prev = new_node

        self.curr = new_node
        self.size += 1
        
        



    def remove(self):

        clone = self.curr
        
        self.curr.prev.next = self.curr.next

        self.curr = self.curr.next

        self.size -= 1

    def get_value(self):
        return self.curr.data

    def move_to_next(self):
        
        if self.curr.next is self.sentinel:
            pass

        else:
            self.curr = self.curr.next

    def move_to_prev(self):
        
        if self.curr.prev is self.sentinel:
            pass

        else:
            self.curr = self.curr.prev

    def move_to_pos(self, pos):
        
        counter = 0

        curr_node = self.sentinel.next

        while counter != pos:
            curr_node = curr_node.next
            counter += 1

        self.curr = curr_node


    def clear(self):
        
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

        self.size = 0

    def get_first_node(self):
        return self.sentinel.next

    def get_last_node(self):
        return self.sentinel.prev

    def partition(self, low, high):

        counter = 2

        self.curr = low

        iter_node = self.curr.next

        while counter <= self.size-1:
            
            if iter_node.data < self.curr.data:
                iter_node.prev.next = iter_node.next
                iter_node.next.prev = iter_node.prev
                self.curr.prev.next = iter_node
                self.curr.prev = iter_node

            elif iter_node.data >= self.curr.data:
                iter_node.prev.next = iter_node.next
                iter_node.next.prev = iter_node.prev
                high.prev.next = iter_node
                high.prev = iter_node

            counter += 1
            iter_node = self.curr.next

    def sort(self):
        pass

    def __len__(self):
        return self.size

    def __str__(self):
        ret_str = ""
        current_node = self.sentinel.next
        while current_node != self.sentinel:
            ret_str += f'{current_node.data} '
            current_node = current_node.next
        
        return ret_str

if __name__ == "__main__":
    #create tests here if you want
    skrillex = DLL()
    skrillex.insert(20)
    skrillex.insert(2)
    skrillex.insert(1)
    skrillex.insert(5)
    skrillex.insert(14)
    skrillex.insert(7)
    skrillex.insert(5)
    print(skrillex)
    skrillex.partition(skrillex.get_first_node(), skrillex.get_last_node())
    

    
    print(skrillex)
    

    
