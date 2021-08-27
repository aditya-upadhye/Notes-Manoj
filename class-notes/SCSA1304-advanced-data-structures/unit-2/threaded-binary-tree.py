# ========================
# | Threaded Binary Tree |
# ========================
#
#
# This file contains insertion, and traversal
# ===========================================
#
#
# Referred from:
# ==============
# https://www.geeksforgeeks.org/threaded-binary-tree-insertion/


class Node:
    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None
        self.lFlag = True
        self.rFlag = True


def insertThread(root: Node, key: int):
    # Storing root to another variable to manipulate that data
    # without disturbing root
    temp = root
    parent = None

    # Choosing the parent to insert
    while temp != None:
        if key == temp.key:
            print("Key already exists")
            return root

        # If key is not same as current node changing the root
        parent = temp

        # moving to left subtree
        if key < temp.key:
            # If flag is false then the parent node contains a
            # child
            if temp.lFlag == False:
                temp = temp.left
            else:
                break
        else:
            # If flag is false then the parent node contains a
            # child
            if temp.rFlag == False:
                temp = temp.right
            else:
                break

    newNode = Node(key)

    if parent == None:
        root = newNode
        newNode.left = None
        newNode.right = None
        # return newNode
    elif parent.key > key:
        newNode.left = parent.left
        newNode.right = parent
        parent.lFlag = False
        parent.left = newNode
    else:
        newNode.left = parent
        newNode.right = parent.right
        parent.rFlag = False
        parent.right = newNode
    return root


# Returns inorder successor's node using rFlag
def inorderSuccessor(ptr):

    # If pointer is not having any child then move to
    # threaded node
    if ptr.rFlag == True:
        return ptr.right

    # Else take the right node.
    ptr = ptr.right
    # If parent has left child then return the left
    # node.
    while ptr.lFlag == False:
        ptr = ptr.left
    return ptr


# Printing the threaded tree
def inorder(root):
    if root == None:
        print("Tree is empty")

    ptr = root
    # Move to leftmost node in threaded binary tree
    while ptr.lFlag == False:
        ptr = ptr.left

    # gets and prints all successors one by one
    while ptr != None:
        print(ptr.key, end=" ")
        ptr = inorderSuccessor(ptr)


if __name__ == "__main__":
    root = None

    root = insertThread(root, 40)
    root = insertThread(root, 20)
    root = insertThread(root, 10)
    root = insertThread(root, 50)
    root = insertThread(root, 80)
    root = insertThread(root, 70)
    root = insertThread(root, 90)
    root = insertThread(root, 30)
    # traversing the tree
    inorder(root)
