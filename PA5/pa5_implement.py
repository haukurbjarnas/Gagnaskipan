class Array:

    def __init__(self) -> None:
        
        self.capacity = 4
        self.size = 0
        self.arr = [None]*self.size

    def resize(self):
        pass

class Node:

    def __init__(self) -> None:
        
        self.key = None
        self.data = None
        self.next = None


class Bucket:

    def __init__(self) -> None:


        self.head = None
        self.size = 0

    def insert(self, key, data):
        
        curr_head = self.head

        while curr_head is not None:

            if curr_head.key == key:
                raise ItemExistsException()

            curr_head = curr_head.next

        if curr_head is None:
            curr_head = Node()
            curr_head.data = data
            curr_head.key = key
            curr_head.next = None



    def update(self, key, data):
        
        curr_head = self.head

        while curr_head is not None:

            if curr_head.key == key:
                curr_head.data = Node(data = data)

    def find(self, key):
        
        curr_head = self.head

        while curr_head is not None:

            if key == curr_head.key:
                bucket_lis = curr_head.data

                while bucket_lis is not None:
                    ret_str = ''
                    ret_str += f'{bucket_lis.data} '

        return ret_str


    def contains(self, key):
        
        curr_node = self.head

        while curr_node is not None:

            if curr_node.key == key:
                return True
            
        return False

    def remove(self, key):
        pass

    def __setitem__(self, key, data):
        pass

    def __getitem__(self, key):
        pass

    def __len__(self):
        pass


class ItemExistsException:
    
    def __str__(self) -> str:
        
        return 'ERROR!!!'
    
if __name__ == '__main__':
    bökket = Bucket()
    bökket.insert(5, 4)