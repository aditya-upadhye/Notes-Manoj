"""
Code Credits: Ajitesh Pathak

Referred from: https://www.geeksforgeeks.org/avl-tree-set-2-deletion/

Posting the same problem in GFG with slight modificaiton on variable name
for my comfortness
"""

class Node:
	def __init__(self, key) -> None:
		self.key = key
		self.left = None
		self.right = None
		self.height = 1
		pass

def insert(root, key):
	
	# Step 1 - Perform normal BST
	if not root:
		return Node(key)
	elif key < root.key:
		root.left = insert(root.left, key)
	else:
		root.right = insert(root.right, key)

	# Step 2 - Update the height of the
	# ancestor node
	root.height = 1 + max(getHeight(root.left),
					getHeight(root.right))

	# Step 3 - Get the balance factor
	balance = getBalance(root)

	# Step 4 - If the node is unbalanced,
	# then try out the 4 cases
	# Case 1 - Left Left
	if balance > 1 and key < root.left.key:
		return rightRotate(root)

	# Case 2 - Right Right
	if balance < -1 and key > root.right.key:
		return leftRotate(root)

	# Case 3 - Left Right
	if balance > 1 and key > root.left.key:
		root.left = leftRotate(root.left)
		return rightRotate(root)

	# Case 4 - Right Left
	if balance < -1 and key < root.right.key:
		root.right = rightRotate(root.right)
		return leftRotate(root)

	return root

# Recursive function to delete a node with
# given key from subtree with given root.
# It returns root of the modified subtree.
def delete(root, key):

	# Step 1 - Perform standard BST delete
	if not root:
		return root

	elif key < root.key:
		root.left = delete(root.left, key)

	elif key > root.key:
		root.right = delete(root.right, key)

	else:
		if root.left is None:
			temp = root.right
			root = None
			return temp

		elif root.right is None:
			temp = root.left
			root = None
			return temp

		temp = getMinkeyueNode(root.right)
		root.key = temp.key
		root.right = delete(root.right,
								temp.key)

	# If the tree has only one node,
	# simply return it
	if root is None:
		return root

	# Step 2 - Update the height of the
	# ancestor node
	root.height = 1 + max(getHeight(root.left),
						getHeight(root.right))

	# Step 3 - Get the balance factor
	balance = getBalance(root)

	# Step 4 - If the node is unbalanced,
	# then try out the 4 cases
	# Case 1 - Left Left
	if balance > 1 and getBalance(root.left) >= 0:
		return rightRotate(root)

	# Case 2 - Right Right
	if balance < -1 and getBalance(root.right) <= 0:
		return leftRotate(root)

	# Case 3 - Left Right
	if balance > 1 and getBalance(root.left) < 0:
		root.left = leftRotate(root.left)
		return rightRotate(root)

	# Case 4 - Right Left
	if balance < -1 and getBalance(root.right) > 0:
		root.right = rightRotate(root.right)
		return leftRotate(root)

	return root

def leftRotate(z):

	y = z.right
	T2 = y.left

	# Perform rotation
	y.left = z
	z.right = T2

	# Update heights
	z.height = 1 + max(getHeight(z.left),
					getHeight(z.right))
	y.height = 1 + max(getHeight(y.left),
					getHeight(y.right))

	# Return the new root
	return y

def rightRotate(z):

	y = z.left
	T3 = y.right

	# Perform rotation
	y.right = z
	z.left = T3

	# Update heights
	z.height = 1 + max(getHeight(z.left),
					getHeight(z.right))
	y.height = 1 + max(getHeight(y.left),
					getHeight(y.right))

	# Return the new root
	return y

def getHeight( root):
	if not root:
		return 0

	return root.height

def getBalance( root):
	if not root:
		return 0

	return getHeight(root.left) - getHeight(root.right)

def getMinkeyueNode( root):
	if root is None or root.left is None:
		return root

	return getMinkeyueNode(root.left)

def preOrder( root):

	if not root:
		return

	print(f"{root.key} ", end="")
	preOrder(root.left)
	preOrder(root.right)


root = None
nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]

for num in nums:
	root = insert(root, num)

# Preorder Traversal
print("Preorder Traversal after insertion")
preOrder(root)
print()

# Delete
key = 10
root = delete(root, key)

# Preorder Traversal//
print("Preorder Traversal after deletion")
preOrder(root)
print()

# This code is created by Ajitesh Pathak and published on GFG
