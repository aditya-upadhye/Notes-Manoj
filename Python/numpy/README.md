## `NumPy`
<p align = center>
<img src="https://numpy.org/doc/stable/_static/numpylogo.svg" />
</p>
NumPy is library for python. Which is used to store values in matrix. 
type. It is the fastest way of using array. It is faster than normal 
list. It uses `ndarray` object to increase the speed. It is partially
developed with python and C. Well, C is the fastest program comparing to
other program because other languages are derived from C so obviously C
is faster than other derived programs from C.

### BTW, What is `ndarray`?

In list the size of the list is constant, It will change it's data size 
dynamically but in the `ndarray` fixed size at creation. If the `ndarray`
size is changed then it will create a new array and delete the original.

The elements in a NumPy array are all required to be of the same data 
type, and thus will be the same size in memory. The exception: one can 
have arrays of (Python, including NumPy) objects, thereby allowing for 
arrays of different sized elements.

### Basic
#### To create a basic array in `ndarray`

```python
a = np.array([1, 2, 3, 4, 5])
print(a)
# Output: [1 2 3 4 5]
```
#### To create a array with full of zeros

```python
a = np.zeros(2)
print(a) 
# Output: [0. 0.]
```

#### To create a array with full of ones

```python
a = np.ones(2)
print(a)
# Output: [1. 1.]
```

#### To create a array elements within a range
It will generate the range of number from 0-n, where O is a default value.
```python
# arange() is similar to range()
a = np.arange(4)
print(a)
# Output: [0 1 2 3]

a = np.arange(3, 9, 3)
print(a)
# Output: [3 6]
```

#### To create an array with values that are spaced linearly
```python
np.linspace(0, 10, num=5)
# Output: [ 0.   2.5  5.   7.5 10. ]
```
<hr>

### Adding, removing, and sorting elements

#### Sort
Syntax:
> numpy.sort(a, axis=- 1, kind=None, order=None)


Parameters

>    **a**: array_like
> - Array to be sorted.

> **axis**: int or None, optional
> - Axis along which to sort. If None, the array is flattened before 
>sorting. The default is -1, which sorts along the last axis.

>**kind**: {‘quicksort’, ‘mergesort’, ‘heapsort’, ‘stable’}, optional
> - Sorting algorithm. The default is ‘quicksort’. Note that both 
> ‘stable’ and ‘mergesort’ use timsort or radix sort under the covers 
> and, in general, the actual implementation will vary with data type. 
> The ‘mergesort’ option is retained for backwards compatibility.

> **order**: str or list of str, optional
> - When a is an array with fields defined, this argument specifies 
>which fields to compare first, second, etc. A single field can be 
> specified as a string, and not all fields need be specified, but
> unspecified fields will still be used, in the order in which they 
> come up in the dtype, to break ties.

> **Returns** sorted_array: ndarray
> -   Array of the same type and shape as a.


```python
a = np.array([9, 3, 5, 4, 2, 1, 6, 8, 7])
print(np.sort(a))
# Output: [1 2 3 4 5 6 7 8 9]

a = np.array([[3, 5, 4, 2], [1, 6, 8, 7]])
# None will flattened the array
a = np.sort(a, axis=None)
print(a)
# Output: [1 2 3 4 5 6 7 8]
```

#### Concatenation

```python
a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9])
print(np.concatenate((a, b)))
# Output: [1 2 3 4 5 6 7 8 9]
```

#### Slicing
```python
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])
```

### To know the shape and size of an array

The array we are using in this topic

```python
a = np.array([[[0, 1, 2, 3],
               [4, 5, 6, 7]],
               [[0, 1, 2, 3],
               [4, 5, 6, 7]],
               [[0 ,1 ,2, 3],
               [4, 5, 6, 7]]])
```

#### Dimension

```python
print(a.ndim)
# Output: 3
```

#### Number of element

```python
print(a.size)
# Output: 24
```

#### Shape
```python
print(a.shape)
# Output: (3, 2, 4)
```
> (dimension, row, column)

### Reshape

```python
a = np.arange(6)
b = a.reshape(3, 2)
print(b)
# Output: [[0 1]
# [2 3]
# [4 5]]
```

