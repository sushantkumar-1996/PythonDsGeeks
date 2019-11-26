"""Given a Key delete the first occurence of this key in the linked list
To delete a node in linked list we need to do following steps.
    1.Find previous node of the node to be deleted
    2.Change the next if previous node
    3.Free memory for the node to be deleted
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def InsertAtbeginning(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def DeleteNodeAtFrstOccurence(self,key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next
        temp = None

    def PrintList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp=temp.next

if __name__ == '__main__':
    llist = LinkedList()
    llist.InsertAtbeginning(4)
    llist.InsertAtbeginning(4)
    llist.InsertAtbeginning(6)
    llist.InsertAtbeginning(7)
    llist.InsertAtbeginning(8)
    llist.InsertAtbeginning(9)
    llist.PrintList()
    llist.DeleteNodeAtFrstOccurence(4)
    llist.PrintList()

