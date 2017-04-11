Question of the day: https://leetcode.com/problems/min-stack/#/description

## Ideas ##

In a basic stack, `push`, `pop`, and `peek` or `top` are already doable in
constant time. The `getMin` seems to be the tricky thing in this problem.
If I use a basic stack, finding the minimum value would take `O(n)` time
because I'd need to iterate through all the elements in the stack. I think
I can figure out a way to keep track of the minimum while I `push` and `pop`.

Since a Stack data structure is basically a special linked list, I think
if I just have an extra pointer in the nodes of the linked list, I'll be
able to simultaneously track the default FIFO stuff and also the series
of minimum values that change as I add nodes.

I'll implement a `Node` class to use within my `MinStack` class so that
I can have that extra `prevMin` pointer.
