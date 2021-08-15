#======================
#| Binary Search Tree |
#======================
#
#
# This file contains insertion, deletion, and searching
# =====================================================
#
#
# Referred from:
# ==============
# https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
# https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
 
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key)
        inorder(root.right)
 
 
def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node
  
def minValueNode(node):
    current = node
 
    while(current.left is not None):
        current = current.left
 
    return current

def maxValueNode(node):
    current = node
 
    while(current.right is not None):
        current = current.right
 
    return current
  
 
def deleteNode(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
 
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key) 
    return root
 
 
def searchNode(root, key):
     
    if root is None or root.key == key:
        return root
 
    if root.key < key:
        return searchNode(root.right,key)
   
    return searchNode(root.left,key)

root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)
 
print("Inorder traversal of the given tree")
inorder(root)

min = minValueNode(root)
print("\nMinimum value in the given tree")
print(min.key)

max = maxValueNode(root)
print("\nMaximum value in the given tree")
print(max.key) 

print("\nDelete 20")
root = deleteNode(root, 20)
print("Inorder traversal of the modified tree")
inorder(root)
 
print("\nDelete 30")
root = deleteNode(root, 30)
print("Inorder traversal of the modified tree")
inorder(root)
 
print("\nDelete 50")
root = deleteNode(root, 50)
print("Inorder traversal of the modified tree")
inorder(root)

min = minValueNode(root)
print("\nMinimum value in the modified tree")
print(min.key)

max = maxValueNode(root)
print("\nMaximum value in the modified tree")
print(max.key)

print("\nSearching for 60 in tree")
key=searchNode(root, 60)
if key:
    print(key.key)
else:
    print("Key not found")

print("\nSearching for 50 in tree")
key=searchNode(root, 50)
if key:
    print(key.key)
else:
    print("Key not found")
