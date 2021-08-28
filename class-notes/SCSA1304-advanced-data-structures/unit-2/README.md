## UNIT 2 ADVANCED TREE CONCEPTS

> Threaded Binary Trees, AVL Tree, B-tree Insertion and deletion,
Splay trees - Heap trees - Heapify Procedure, Tries.

### Threaded Binary Tree

In a **binary search tree**, there are many nodes that have an
empty left child or empty right child or both.
<br>
To avoid wasting the data for `NULL`, we will replace that by
storing another node object for traversal

In **threaded binary tree**, it will follow inorder threading. 
<br>
- The **left child** will be threaded with the node's **inorder predecessor**
- The **right child** will be threaded with the node's **inorder successor**


There are two ways of threading the binary tree
- **One way threading**: A thread will appear in the right field of a node 
  and it will point to the next node in the inorder traversal
- **Two way threading**: A thread will appear in the both left and right and
  points to inorder predecessor or successor

<p align="center">
    <img alt="Threaded binary tree- Types" src="https://i1.wp.com/algorithms.tutorialhorizon.com/files/2016/03/Single-and-Double-threaded-binary-tree-1.png" width="70%">
</p>

**Threaded binary tree** makes ***inorder traversal faster*** without **stack and recursion**

In threaded binary tree traversal, It will start from **leftmost node** and follows the threaded binary tree flow.