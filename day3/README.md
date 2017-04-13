Question of the day: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/#/description

## Ideas ## 

Based on the sample input/output, it looks like the linked list is
produced by a preorder traversal on the binary tree. If I ran a
preorder traversal and created new nodes into a linked list, it'd be
a `O(n)` runtime, `O(n)` space complexity solution. That wouldn't 
work for this problem, since I'm not doing it in-place.

I think we can save space by just rearranging the nodes of the
tree. I want to rearrange the pointers so that as I traverse the
tree, the current node is always a child of the last node I had
visited. This will bring the space complexity down to `O(1)`.

What I need to do is to rearrange so that each node's right child
is the next node in the preorder traversal of the tree.

When I have a complete tree like this:
```
    1 
   / \ 
  2   5 
 / \ / \ 
3  4 6  7 
```

What I would do if I could cut and paste nodes of the tree into
different locations:
    
```
    1  
   / \     
  2   5  
 / \ / \  
3  4 6  7  
```

```
      1    
     / \    
    2   5  
   /   / \ 
  3    6  7  
 /  
4
```

```
          1  
         /  
        2  
       /  
      3  
     /  
    4  
   /  
  5  
 / \  
6   7  
```

```
            1  
           /  
          2  
         /  
        3  
       /  
      4  
     /  
    5  
   /  
  6  
 /  
7
```
  
but this is a linked list leaning to the left. The sample output
has a linked list leaning towards the right. One thing I could do is
to go down the linked list and swap the direction on each level.

How do I actually implement this? And wait.. why don't I just go
to the right to begin with? Let's try that.

Looking at the original tree, where `node` is the root node with `val` 1:

```
    1 
   / \
  2   5
 / \ / \
3  4 6  7
```

I actually want to do something like this:

```python
    save = node.right         # store the right child
    node.right = node.left    # move the left child over to the right
    node = node.right
    save2 = node.right        # store another right child
    node.right = node.left
    node = node.right         # connect the most recently stored back to the right
    node.right = save2
    node = node.right
    node.right = save         # connect the next most recently stored back to the right
    node = node.right
    save3 = node.right        # store a third right child
    node.right = node.left
    node = node.right         # connect the last saved node
    node.right = save3
```

store = [ (5) ]

    1 
     \
      2
     / \
    3   4

store = [ (5), (4) ]

    1 
     \
      2
       \
        3

store = [ (5) ]

    1 
     \
      2
       \
        3
         \
          4

store = [ ]

    1 
     \
      2
       \
        3
         \
          4
           \
            5
           / \
          6   7

store = [ 7 ]

    1 
     \
      2
       \
        3
         \
          4
           \
            5
             \
              6

store = [ ]

    1 
     \
      2
       \
        3
         \
          4
           \
            5
             \
              6
               \
                7

So the store would be a stack, and I think in the worst case
it would store up to `log(n)` references to nodes. So it's not
`O(1)` space, I guess.

## Code ##

[Python](./flatten.py)

## Follow Up ## 

(TODO) I'm pretty sure I can use recursion in this problem..
