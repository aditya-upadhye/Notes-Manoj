'''
Basic Binary Tree in Array Representation

Referred from:
www.javatpoint.com/program-to-implement-binary-tree-using-the-linked-list
'''

class Node:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_node(self, data):
        new_node = Node(data)

        # Check whether tree is empty
        if(self.root == None):
            self.root = new_node
            return;
        else:
            queue = []
            # Add root to the queue
            queue.append(self.root)

            while(True):
                node = queue.pop(0)
                # If node has both left and right child, add both the child to queue
                if(node.left != None and node.right != None):
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    # If node has no left child, make new_node as left child
                    if(node.left == None):
                        node.left = new_node
                        queue.append(node.left)
                    else:
                        # If node has left child but no right child, make new_node as right child
                        node.right = new_node
                        queue.append(node.right)
                    break
    # Inorder traversal
    # Left -> Root -> right
    # Root is IN between left and right that why it is called INorder
    def inorder_traversal(self, root):
        if(root):
            self.inorder_traversal(root.left)
            print(root.value, end=' => ')
            self.inorder_traversal(root.right)

    # Preorder traversal
    # Root -> Left -> right
    # Root comes before left and right that why it is called PREorder
    def preorder_traversal(self, root):
        if(root):
            print(root.value, end=' => ')
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)

    # Preorder traversal
    # Left -> right -> Root
    # Root comes after left and right that why it is called POSTorder
    def postorder_traversal(self, root):
        if(root):
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.value, end=' => ')

# Creating object
BT = BinaryTree()
# Inserting_node
BT.insert_node('A')
BT.insert_node('B')
BT.insert_node('C')
BT.insert_node('D')
BT.insert_node('E')
#====Inorder traversal====#
print("InOrder Traversal")
BT.inorder_traversal(BT.root)
#====Preorder traversal====#
print("\nPreOrder Traversal")
BT.preorder_traversal(BT.root)
#====Postorder traversal====#
print("\nPostOrder Traversal")
BT.postorder_traversal(BT.root)
print()
