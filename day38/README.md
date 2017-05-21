Today I'm going to implement a min heap.

What is a heap?

From http://www.cprogramming.com/tutorial/computersciencetheory/heap.html:

"A heap is a partially sorted binary tree. Although a heap is not completely
in order, it conforms to a sorting principle: every node has a value less
(for the sake of simplicity, we will assume that all orderings are from
least to greatest) than either of its children. Additionally, a heap is
a "complete tree" -- a complete tree is one in which there are no gaps
between leaves. For instance, a tree with a root node that has only one
child must have its child as the left node. More precisely, a complete tree
is one that has every level filled in before adding a node to the next level,
and one that has the nodes in a given level filled in from left to right,
with no breaks."

Basically, a one-node min heap might look something like this:

```
7
```

And a two-node min heap might look something like this:

```
  7
 /
9
```

three nodes:

```
   7
  / \
 9   8
```

four nodes:

```
    7
   / \
  10 18
 /
19
```

and so on.

Here are some specs for my basic min heap that contains `n` integers:

getMin  - takes no arguments, extracts and returns the minimum value in the heap.
          The rest of the heap is reorganized so that the min value is still at
          the top. Finishes in `O(n)` time.

peek    - takes no arguments, returns the minimum value in the heap. Should return
          in `O(1)` time.

push    - takes an integer as an argument and adds it into the heap, returning
          nothing. Should complete in `O(logn)` time.

heapify - takes an array of integers and forms a heap out of them. Should run in
          `O(n)` time.

size    - takes no arguments and returns the number of integers in the heap `n`
          in `O(1)` time.

isEmpty - takes no arguments and returns `True` if there are no elements in the
          heap, and `False` if there ARE elements in the heap in `O(1)` time.

## Code

[Python](./heap.py)

## Follow-up

Why use a heap?

If some kind of ordering is required, i.e. max or min ordering, a heap is an
efficient way to maintain that ordering even when elements are being deleted
and added. The tree structure of the heap allows you to find elements in
`O(logn)` time rather than `O(n)` time like in a normal array or linked list.

---

Some more thinking around heapify, aka just cram an unsorted array into
a binary tree, and then compare and swap unordered parent-children pairs,
from the bottom up:

arr = [7, 6, 5, 4, 3, 2, 1]

        1
       / \
      3   2 
     / \ / \
    4  6 7  5


arr = [4, 5, 7, 3, 9, 6, 1]

        4
       / \
      5   7 
     / \ / \
    3  9 6  1

len = 7
first parent = 7/2 = 3
index = 3-1
arr[index] == 7

7's children: arr[2*index + 1], arr[2*index + 2] aka 6, 1
1 < 6

        4
       / \
      5   1 
     / \ / \
    3  9 6  7

next parent -> index -= 1
arr[index] = 5

5's children: 3, 9
3 < 9

        4
       / \
      3   1 
     / \ / \
    5  9 6  7

next parent -> index -= 1
arr[index] = 4

4's children: 3, 1
1 < 3

        1
       / \
      3   4 
     / \ / \
    5  9 6  7

done.

Need to do one bubbleDown each parent node from the bottom up, and then done.  
On the bottom-most level, `n/2` nodes can move at most 0 levels down.  
Next level, `n/4` nodes can move at most 1 level down.  
etc.   

So it's a summation on i from 0 to logn:  

`n/(2**i) * i`

which turns out to be `O(n)` work!

Edit: fix `heapify` code.

For more information:  
- https://www.cs.umd.edu/~meesh/351/mount/lectures/lect14-heapsort-analysis-part.pdf  
- https://www.youtube.com/watch?v=MiyLo8adrWw  
