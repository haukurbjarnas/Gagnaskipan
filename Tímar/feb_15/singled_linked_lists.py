class Node:

    def __init__(self) -> None:
        self.data = None
        self.next = None





def app(head, val):

    while head.data != None:

        head = head.next

    head.data = val

    head.next = Node()

    return head


def prt(head):

    while head.data != None:

        print(head.data, end=' ')

        head = head.next



def length(head):

    counter = 0

    while head.data != None:

        counter += 1

        head = head.next

    return counter

def ordered(head, val):

    last_val = -99999999999999999999999


    while head.data != None:

        if val > last_val and val < head.data:

            last_val = head.data

            head.data = val

        last_val = head.data

        head = head.next

    if head.data == None:
        head.data = val

    head.next = Node()

    return head

node = Node()
ordered(node, 5)
ordered(node, 9)
ordered(node, 2)
prt(node)

