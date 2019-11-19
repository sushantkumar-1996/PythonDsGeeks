# Traversing the created linked list --->> we will use a general purpose function printList() that prints any list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    llist = LinkedList()  # start with empty list
    llist.head = Node(1)
    second = Node(2)
    third = Node(3) # three Nodes created with reference as head , second and third
    llist.head.next = second # Linking first node with second
    second.next = third # Linking Second node

    llist.printlist()


