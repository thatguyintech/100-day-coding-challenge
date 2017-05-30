Question of the day: http://www.techiedelight.com/check-given-array-represents-min-heap-not/

Given an array of integers, check if it represents a Min-Heap
or not.

For example, this array represents a min heap:  
`[2, 3, 4, 5, 10, 15]`

While this array doesn't:  
`[2, 10, 4, 5, 3, 15]`

## Ideas

A min heap is a binary tree in which every parent node has two children
that have values greater than the parent. The second array failed the heap
check because the parent node with value `10` has children `5` and `3`, both
of which are smaller than it.

I think we can do a linear time check across all parent-children node
relationships in the heap.

Basically, check if the left sub-tree is a heap, check if the right sub-tree
is a heap, and then check if this node has the correct relationship with its
children.

I wonder if I can get a recursive solution to work with array and index
manipulation..

## Code

[Python](./day48.py)

## Follow up
