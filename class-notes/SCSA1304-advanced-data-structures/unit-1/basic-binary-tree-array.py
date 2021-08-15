'''
Basic Binary Tree in Array Representation

=============
| formulae: |
=============

    Parent:
    =======
        If i > 1; i = (i/2)
        else if i = 0; **i = 2i

    Left child:
    ===========
        2i

    Right child:
    ============
        2i+1
 '''
 #Where i is from (1...n)
 #since array starts from 0 we will add 1 in these formulae

# Declaring an array with None so that we can find the array is inserted or not
# and for inserting with index number, the list has to have some size without
# that we can insert
binary_tree=[None]*15

# This function is used to insert value in root
def insert_root(value):
    if binary_tree[0] == None:
        binary_tree[0]=value
        return
    print("Root already exist")

# This function is used to insert value in left side of the parent
def insert_left(value, parent):
    # Checking the existence of parent node
    if binary_tree[parent] == None:
        print("No parent found")
    # Inserting node in left if parent exit
    else:
        index = (parent * 2) + 1
        binary_tree[index] = value

def insert_right(value, parent):
    # Checking the existence of parent node
    if binary_tree[parent] == None:
        print("No parent found")
    # Inserting node in right if parent exit
    else:
        index = (parent * 2) + 2
        binary_tree[index] = value

# Inserting nodes in array
insert_root('A')
insert_left('B', 0)
insert_right('C', 0)
insert_left('D', 1)
insert_right('F', 1)
insert_left('I', 3)
insert_right('J', 3)
insert_left('G', 2)
insert_right('H', 2)
insert_right('K', 5)

# This array wiil show the example of the below tree image
# https://i.imgur.com/O3naLA3.png
print(binary_tree)
