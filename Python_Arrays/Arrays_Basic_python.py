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


