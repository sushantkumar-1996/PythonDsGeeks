'''
Linked list is linear data structure, not stored at contiguous locations, elements are linked using pointers
Limitations of array includes its fixed size so upper limit on the number of elements in advance, also inserting new element in array of elements is expensive
because room has to be created for new element and the remaining elements has to be shifted
Linked list has dynamic size allocation so that's a plus point over arrays also there is ease of insertion and deletion compared with arrays
Drawbacks of linked list includes that random access is not allowed, access must be sequential starting from first node, extra memory space is required for pointer and it is not
Cache friendly

Representation of linked list in python---->>
'''
'''
# Node class
class Node:
    #Function to initialize node object
    def __init__(self,data):
        self.data=data # assign data
        self.next = None #Initialize next as None

#Linked List Class
class LinkedList:
    def __init__(self):
        self.head=None
'''


# First Simple Linked List in Python with 3 nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


if __name__ == '__main__':
    # start with empty linked list
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)  # Three Nodes Created the references are head , second and third
    llist.head.next = second  # first node linked with second
    second.next = third  # Second node linked with third node
'''Now first node is linked to second and second to third'''


