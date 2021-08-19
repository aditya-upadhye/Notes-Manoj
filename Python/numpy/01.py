import numpy as np # importing NumPy

a = np.array([1, 2, 3, 4, 5])
print(a)
# Output: [1 2 3 4 5]

a = np.zeros(2)
print(a) 
# Output: [0. 0.]

a = np.ones(2)
print(a)
# Output: [1. 1.]

# arange() is similar to range()
a = np.arange(4)
print(a)
# Output: [0 1 2 3]

# arange() is similar to range()
a = np.arange(3, 9, 3)
print(a)
# Output: [3 6]

a = np.linspace(0, 10, num=5)
print(a)
# Output: [ 0.   2.5  5.   7.5 10. ]

a = np.array([9, 3, 5, 4, 2, 1, 6, 8, 7])
print(np.sort(a))
# Output: [1 2 3 4 5 6 7 8 9]

a = np.array([[3, 5, 4, 2], [1, 6, 8, 7]])
a = np.sort(a, axis=None)
print(a)
# Output: [1 2 3 4 5 6 7 8]

a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9])
print(np.concatenate((a, b)))
# Output: [1 2 3 4 5 6 7 8 9]

# Indexing
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1])
# Output: 2


# Slicing
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])
# Output: [2 3 4 5] 

## ======================
## For getting array info 
## ======================

a = np.array([[[0, 1, 2, 3],
               [4, 5, 6, 7]],
               [[0, 1, 2, 3],
               [4, 5, 6, 7]],
               [[0 ,1 ,2, 3],
               [4, 5, 6, 7]]])

print(a.ndim)
# Output: 3

print(a.size)
# Output: 24

print(a.shape)
# Output: (3, 2, 4)

## Reshape
a = np.arange(6)
b = a.reshape(3, 2)
print(b)
# Output: [[0 1]
# [2 3]
# [4 5]]

a = np.arange(6)
b = a.reshape(3, 1, 2)
print(b)
# Output: [[0 1]
# [2 3]
# [4 5]]

a = np.arange(6)
b = a.reshape(3, 1, -1)
print(b)
# Output: [[0 1]
# [2 3]
# [4 5]]


### Add new dimension
a = np.array([1, 2, 3, 4, 5, 6])
print(a.shape)
# Output: (6,)

a2 = a[np.newaxis, :]
print(a2.shape)
# Output: (1, 6)

a2 = a[: , np.newaxis]
print(a2.shape)
# Output: (6, 1)

b = np.expand_dims(a, axis=1)
print(b.shape)
# Output: (6, 1)

c = np.expand_dims(a, axis=0)
print(c.shape)
# Output:  (1, 6)

a = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a[a < 5])
# Output: [1 2 3 4]

five_up = (a > 5) | (a == 5)
print(five_up)
# Output: [[False False False False]
# [ True  True  True  True]
# [ True  True  True True]]

b = np.nonzero(a < 5)
print(b)
# Output: (array([0, 0, 0, 0]), array([0, 1, 2, 3]))

list_of_coordinates= list(zip(b[0], b[1]))
for coord in list_of_coordinates:
    print(coord)
# Output: (0, 0)
#(0, 1)
#(0, 2)
#(0, 3)

# Stacking

a1 = np.array([[1, 1],
               [2, 2]])

a2 = np.array([[3, 3],
               [4, 4]])

a = np.vstack((a1, a2))
print(a)
# Output: [[1, 1],
#       [2, 2],
#       [3, 3],
#       [4, 4]]

a = np.hstack((a1, a2))
print(a)

# Splitting
x = np.arange(1, 25).reshape(2, 12)
print(np.hsplit(x, 3))
# Output: [array([[ 1,  2,  3,  4],
# [13, 14, 15, 16]]), array([[ 5,  6,  7,  8],
# [17, 18, 19, 20]]), array([[ 9, 10, 11, 12],
# [21, 22, 23, 24]])]

# Copy vs View
arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()
print(x, y)
arr[2]=2
print(x, y)
