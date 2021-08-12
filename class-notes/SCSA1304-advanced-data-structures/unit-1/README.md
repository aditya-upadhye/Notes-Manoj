# SCSA1304 Advanced Data Structures

## UNIT 1 BASIC TREE CONCEPTS

Trees - Ordinary and Binary trees terminology, Properties of Binary trees, Implementation using Array and Linked  list  - 
Binary tree ADT representations, recursive and non recursive traversals - Binary Search Tree - Insertion and Deletion.

### Trees

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

### Terminologies

![Terminologies](https://www.tutorialandexample.com/wp-content/uploads/2020/10/image-68.png)
#### More Terminologies:
- Degree: No. of Children of that node
- Ancestor: Any predecessor node on the path from root to that node
- Descendant: Any Successor node on the path from that node to leaf node
- Height: Each level is counted as height from top to bottom (1...n)
- Depth: Each level is counted as depth from bottom to top (1...n)
> **Consider a level 2 tree**<br>
> Level 0 - Height 1 - Depth 3<br>
> Level 1 - Height 2 - Depth 2<br>
> Level 2 - Height 3 - Depth 1

### Binary Tree - Rules

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

### Basic types in binary tree:

- Skewed Tree
  - Left Skewed
  - Right Skewed
- Complete Binary Tree
- Full Binary Tree
- Perfect Binary Tree
- Balanced Binary Tree

## Skewed Tree

### Left skewed

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

### Right skewed

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

### Complete Binary Tree

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

### Full Binary Tree

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

### Perfect Binary Tree
A perfect binary tree is a type of binary tree in which every internal node has exactly two child nodes and all the leaf nodes are at the same level.

```
+----------------+----------------+----------------+
|Level           |Level           |Level           |
|                |                |                |
| 0       A      | 0       A      | 0        A     |
|                |       /   \    |        /   \   |
| 1              | 1    B     C   | 1     B     C  |
|                |     / \   / \  |      / \   / \ |
| 2              | 2  D   E F   G | 2   D   E F   G|
|                |                |    / \         |
| 3              | 3              | 3 H   I        |
|                |                |                |
|  VALID TREE    |    VALID TREE  |  INVALID TREE  |
+----------------+----------------+----------------+
```

### Balanced Binary Tree

- Difference between the left and the right sub-tree for any node is not more than one
- The left sub-tree is balanced
- The right sub-tree is balanced

```
+-------------------------+-------------------+------------------------+
|Level                    |Level              |Level                   |
|                         |                   |                        |
|0 df=1        A          |0 df=0      A      |0 df=2        A         |
|            /   \        |          /   \    |            /   \       |
|2 df=1     B     C df=0  |1 df=0   B     C   |1 df=1     B     C df=0 |
|          / \   / \      |        / \   / \  |          / \           |
|3 df=0   D   E F   G df=0|2 df=0 D   E F   G |2 df=0   D   E          |
|        / \              |                   |        / \             |
|4 df=0 H   I df=0        |3                  |3 df=0 H   I            |
|                         |                   |                        |
|      VALID TREE         |     VALID TREE    |    INVALID TREE        |
+-------------------------+-------------------+------------------------+
```

Here df = **|Height of left tree - Height of right tree|**

### Proprieties of binary tree

- Maximum number of nodes possible at any level is **N = 2<sup>Level</sup>**
- Maximum number of nodes at height `H` is **N = 2<sup>H+1</sup>-1**
- Minimum number of nodes at height `H` is **N = H+1**
- Number of edges possible at n elements is **E = N-1**
- Number of internal node (non-leaf node) in complete binary tree is **CEIL(N/2)**
- Number of leaf node `L` in a perfect binary tree is **L = <sup>N+2</sup>/<sub>2</sub>**
- Maximum height of the tree with nodes N is **H = N-1**
- Minimum height of the binary tree with nodes N is **H >= LOG<sub>2</sub>(N+1)-1**
 - Minimum height of the complete binary tree with nodes N is  ***LOG*** **<sub>2</sub>(N)**
 - Minimum height of the perfect binary tree with nodes N is **FLOOR(***LOG***<sub>2</sub>(N+1)-1)**

## Binary tree can be stored in two ways
- Array
- LinkedList
### Binary tree in array representation
If a complete binary tree with n nodes is represented sequentially, then for any node with index i (1...n)

Where `i` is parent node i value

- Parent <br>
  If i > 1; **i = (i/2)**<br>
  else if i = 0; **i = 2i**

- Left child<br>
  **2i**

- Right child<br>
  **2i+1**

If any number is greater than n then it is not valid and the node doesn't exist.

**Try to practice the formulae in below picture**
![Tree in array](https://i.imgur.com/O3naLA3.png)

Disadvantages:
- Fixed size

### Binary tree in doubly Linked List

![Binary tree in doubly Linked List](https://i.imgur.com/EPHDmbB.png)


### Traversal of binary tree

- **Infix:** Left -> Root -> Right
- **Prefix order:** Root -> Left -> Right
- **Post-fix order:** Left -> Right -> Root

Where the prefix of fix word tells the root order

### Binary search tree

A Binary Search Tree is a binary Tree.
- It may be empty.
- If it is not empty then it satisfies the following properties:
  - Every element has a key and no two elements have the same key
  - The keys (if any) in the left sub-tree are smaller than the key in the root.
  - The keys (if any) in the right sub-tree are greater than the key in the root.
  - The left and right sub-trees are also binary search trees

### Efficiency
![Efficiency](https://i.imgur.com/lHEZwEz.png)