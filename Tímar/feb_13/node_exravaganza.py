class Node:

    def __init__(self) -> None:
        self.data = None
        self.next = None


def appe_back(head, data):

    if head.data == None:
        
        head.data = data

        head.next = Node()
    
    else:

        node = head

        while node.data != None:

            node = node.next
            
        node.data = data
        node.next = Node()


    return head  

            
def node_print(head):

    node = head

    while node.data != None:

        print(node.data)

        node = node.next



def rem_first(head):

    counter = 1

    node = head
    jumper = node.next

    while jumper.data != None:

        if counter == 1:

            node.data = jumper.data

            node = node.next

            jumper = jumper.next


    
    if jumper.data == None:
        node.data = None

    return head



def appe_first(head, data):
    if head is None or head.data is None: 
        head.data = data  
    else:

        new_node = Node()
        new_node.data = head.data
        new_node.next = head.next

        head.data = data
        head.next = new_node

    head.next = Node()
    return head


def rem_back(head):

    node = head

    while node.next != None:

        node = node.next

    node.data = None

    return head


bla = Node()

appe_first(bla, 1)
appe_back(bla, 2)
appe_first(bla, 3)
'''appe_back(bla, 4)'''
node_print(bla)
'''rem_first(bla)
node_print(bla)
rem_back(bla)
node_print(bla)
'''