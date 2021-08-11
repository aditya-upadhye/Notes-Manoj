# SCSA1304 Advanced Data Structures

### UNIT 1 BASIC TREE CONCEPTS

Trees - Ordinary and Binary trees terminology, Properties of Binary trees, Implementation using Array and Linked  list  - 
Binary tree ADT representations, recursive and non recursive traversals - Binary Search Tree - Insertion and Deletion.

#### Trees

In data structure the tree is represented as normal tree but it is taken as upside down

<table>
<tr>
<td>Natural tree</td>
<td align="center"><img src="https://i.imgur.com/qoSjVIh.png" width="49%"/>
</td>
</tr>
<tr>
<td>Tree representation in data structure</td>
<td align="center"><img src="https://i.imgur.com/cOPVZpy.png" width="49%" rotate="20px"></td>
</tr>
</table>

#### Terminologies

![Terminologies](https://www.tutorialandexample.com/wp-content/uploads/2020/10/image-68.png)
 
#### Binary Tree - Rules

-  No node in a binary tree can have degree more than 2 degrees
-  A binary tree may be empty
-  The sub-trees are ordered


Example:
```
        A
      /   \
     /     \
    B       C
   / \     /
  /   \   /
 D     E F
```

#### Basic types in binary tree:

- Skewed Tree
  - Left Skewed
  - Right Skewed
- Complete Binary Tree
- Full Binary Tree

### Skewed Tree

#### Left skewed

A left skewed tree will not have right child

```
+=================+
|Level|   Tree    |
|_____|___________|
|  1  |         5 |
|     |        /  |
|  2  |       4   |
|     |      /    |
|  3  |     3     |
|     |    /      |
|  4  |   2       |
|     |  /        |
|  5  | 1         |
+=====+===========+
```

#### Right skewed

A right skewed tree will not have left child

```
+=================+
|Level|   Tree    |
|_____|___________|
|  1  | 5         |      
|     |  \        |           
|  2  |   4       |         
|     |    \      |            
|  3  |     3     |           
|     |      \    |      
|  4  |       2   |   
|     |        \  |      
|  5  |         1 |
+=====+===========+
```

#### Complete Binary Tree

**Rule 1:** A complete binary tree is a tree that is
completely filled, with the possible exception of
the bottom level.

**Rule 2:** The bottom level is filled from left to right

Example:
```
+----------------+----------------+--------------+
|Level           |Level           |Level         |
|                |                |              |
|1        A      |1        A      |1        A    |      
|       /   \    |       /   \    |       /   \  |       
|2     B     C   |2     B     C   |2     B     C |     
|     / \   / \  |     / \   / \  |     / \   /  |      
|3   D   E F   G |3   D   E F   G |3   D   E F   |     
|   / \          |   /   / \      |   / \        |      
|4 H   I         |4 H   I   J     |4 H   I       |
|                |                |              |
|   VALID TREE   |  INVALID TREE  | INVALID TREE |                          
+----------------+----------------+--------------+
```

The second tree is invalid complete binary tree because the last level should fill from left to right<br>
Here, `D` is not having any right child and `I` and `J` is filled. Here `I` must be in `D` right child and `J` in `E` left child


The third tree is also invalid complete binary tree because the last before level is not completely filled.<br>
Here, the `C` is not having any right child so it is not valid tree. It is not following the rule 1

#### Full Binary Tree

In full binary tree all nodes should have 2 or 0 child. It is also known as proper binary tree

```
+----------------+--------------+---------------+
|Level           |Level         |Level          |
|                |              |               |
|0        A      |0      A      |0         A    |
|       /   \    |     /   \    |        /   \  |
|2     B     C   |1   B     C   |1      B     C |
|     / \   / \  |   / \   / \  |      / \   /  |
|3   D   E F   G |2 D   E F   G |2    D   E F   |
|   / \          |     / \      |    / \        |
|4 H   I         |3   I   J     |3  H   I       |
|                |              |               |
|   VALID TREE   |   VALID TREE | INVALID TREE  |
+----------------+--------------+---------------+
```

Third tree is invalid since it has only one child in `C`

#### Perfect Binary Tree
A perfect binary tree is a type of binary tree in which every internal node has exactly two child nodes and all the leaf nodes are at the same level.

```
+----------------+----------------+---------------+
|Level           |Level           |Level          |
|                |                |               |
| 0       A      | 0       A      | 0        A    |
|                |       /   \    |        /   \  |
| 1              | 1    B     C   | 1     B     C |
|                |     / \   / \  |      / \   /  |
| 2              | 2  D   E F   G | 2   D   E F   |
|                |                |    / \        |
| 3              | 3              | 3 H   I       |
|                |                |               |
|  VALID TREE    |    VALID TREE  |  INVALID TREE |
+----------------+----------------+---------------+
```
