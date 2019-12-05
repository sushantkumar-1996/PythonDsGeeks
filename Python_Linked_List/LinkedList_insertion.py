"""Three Methods to insert a new node in Linked List
1. At the front of Linked List
2. After a given Node
3. At the end of the Linked List

1. At front of Linked List(4 Step process)---- Newly added node becomes the head of the given linked list following is the function implementing a node in front
    This function would be in Linked List class

def push(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node

2. Adding a node after a given node(5 step process) ---New Node is inserted after a given node . following is the function that implements The functnality

def insertAfter(self, prev_node, new_data):
    if prev_node is None:
        print("the prev Node is head node")
        return
    new_node = Node(new_data)
    new_node.next = prev_node.next
    prev_node.next = new_node


3. Adding a Node at the end of the list(6 Step Process)----we have to traverse the list to the end and then change the m=next of last node to new node


def append(self, new_data):
    new_node = Node(new_data)
    if self.head is None:
        self.head = new_node
        return

    last = self.head
    while(last.next):
        last = last.next
    last.next = new_node

"""
"""Program to Implement Insertion of Node At all 3 positions"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertInBeginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def InsertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("First node in linked list")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def InsertAtEnd(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def PrintList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.InsertAtEnd(6)
    llist.insertInBeginning(5)
    llist.insertInBeginning(10)
    llist.insertInBeginning(11)
    llist.insertInBeginning(12)
    llist.InsertAfter(llist.head.next.next, 8)
    llist.PrintList()
