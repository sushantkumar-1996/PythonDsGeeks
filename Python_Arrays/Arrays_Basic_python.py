"""Array is collection of items stored at contiguous memory locations, Array in python is handled by a module named "array" useful
 when we have to manipulate only a specific data type values , lists can also be treated as arrays ,however type of elements stored
 in a list cannot be constrained , if array is created using the array module all elements of the array must be of the same type
 """

#  Creating an Array-- Created by importing arrray module array(data_type, value_list) is used to create array with data type and value
#  list specified as arguments

import array as arr
a = arr.array('i', [1, 2, 3])  # creating an array of integer type
for i in range(0, 3):
    print(a[i])  # Printing original array

b = arr.array('d', [2.5, 3.2, 3.3])  # creating an array of float type
for i in range(0, 3):
    print(b[i])  # printing float array

"""Creating an array of different data types ---
TYPECODE --|-----CTYPE--------------|-----PYTHONTYPE----|----MINIMUMSIZE(BYTES)
    'b'    |    signed Char         |   int             |   1
    'B'    |    unsigned Char       |   int             |   1
    'u'    |    Py_Unicode          |   Unicode Char    |   2
    'h'    |    signed short        |   int             |   2
    'H'    |    unsigned short      |   int             |   2
    'i'    |    signed int          |   int             |   2
    'I'    |    unsigned int        |   int             |   2
    'l'    |    signed long         |   int             |   4
    'L'    |    unsigned Long       |   int             |   4
    'q'    |    signed long long    |   int             |   8
    'Q'    |    unsigned long long  |   int             |   8
    'f'    |    float               |   float           |   4
    'd'    |    double              |   float           |   8
"""

"""Adding Elements in Array--- Using built in insert() function--used to insert one or more data elements into an array
Using insert() can be added at beginning, end or at any given index
append() is also used to add the value mentioned in its arguments at the end of array"""

#import array as arr
a = arr.array('i', [1, 2, 3, 4])
for i in range(0, 4):  # Accessing 0, 1,2,3 elements
    print(a[i])  # Printing array before insertion

a.insert(2, 4)  # At index 2 insert 4
for i in a:
    print(i)  # Printing array after insertion.
# Same method for floating values also just instead of i as type code we will have to write f or d

"""Accessing Elements from an array--array items refer to the index number , use the index[] operator to access an item in the array
Index must be an integer. Program showing how to access an element in the array---"""

# import array as arr
ar = arr.array('i', [12, 14, 16, 17, 20])
print("First element is", a[0])
print("Second element is", a[1])
print("Third element is", a[2])
print("Fourth element is", a[3])

"""Removing Elements from an array---using built in remove() function but an error arises if element doesnt exist, it removes only
 one element at a time, to remove a range of elements iterator is used. pop() function can also be used to remove and return the 
 element from an array but as default it removes only last element to remove at specific position index is passed as argument to pop mehod
 remove method in list will only remove the first occurence of the searched element, Program example"""

# import array as arr
a1 = arr.array('i', [12, 15, 16, 17, 20, 20])
for i in range(0, 6):
    print(a1[i])  # Printing all elements of the array

print("Popped Element is:", a1.pop(3))  # pop deletes and returns the removed element
for i in a1:
    print(a1[i])  # printing after popping

a1.remove(20)
for i in a1:
    print(a1[i])  # Printing after removing first occurence of 20



