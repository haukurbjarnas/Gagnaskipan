class SLL_Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        if self.next == None:
            return str(self.data)
        return str(self.data) + " " + str(self.next)
    
def sum_even_numbers(node):

    if node is None:
        return 0
    
    if node.data % 2 == 0:

        val = node.data

    else:
        val = 0

    node = node.next

    return val + sum_even_numbers(node)

def remove_even_numbers(node):

    if node is None:
        return node
    
    elif node.data % 2 == 0:

        node.next = node.next.next

        node = node.next

        remove_even_numbers(node)
    
    else:
        remove_even_numbers(node.next)


class DLL_Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self):
        self.header = DLL_Node("header node")
        self.tailer = DLL_Node("tailer node")
        self.header.next = self.tailer
        self.tailer.prev = self.header

    def __str__(self):
        ret_str = ""
        node = self.header.next
        while node != self.tailer:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str
    
    def push_back(self, value):
        new_node = DLL_Node(value)
        new_node.prev = self.tailer.prev
        new_node.next = self.tailer
        new_node.prev.next = new_node
        new_node.next.prev = new_node
    
    def remove_negative_values(self):
        
        iter_node = self.header.next

        while iter_node is not self.tailer:

            if iter_node.data < 0:

                iter_node.next.prev = iter_node.prev

                iter_node.prev.next = iter_node.next

            iter_node = iter_node.next

if __name__ == "__main__":
    print("testing sll recursion")
    head = SLL_Node(5, SLL_Node(7, SLL_Node(2, SLL_Node(6, SLL_Node(8, SLL_Node(1, SLL_Node(5)))))))
    print(head)
    print("sum", sum_even_numbers(head))
    head = remove_even_numbers(head)
    print("removed even numbers")
    print(head)
    print("sum", sum_even_numbers(head))
    print("testing dll")
    dll = DLL()
    dll.push_back(-7)
    dll.push_back(5)
    dll.push_back(-5)
    dll.push_back(3)
    dll.push_back(-2)
    dll.push_back(-8)
    dll.push_back(-15)
    dll.push_back(4)
    dll.push_back(6)
    dll.push_back(-1)
    print(dll)
    print("removing negatives")
    dll.remove_negative_values()
    print(dll)
