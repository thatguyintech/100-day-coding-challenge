Question of the day: implement heapsort  
http://www.techiedelight.com/heap-sort-place-place-implementation-c-c/

## Ideas

We can implement the sort in-place or out-of-place.

In either case, the essential idea is that we take an input
array of unsorted elements and perform an `O(n)` heapify
operation on the array, and then collect the output of
successive pops from the heap until there are no more elements
left in the heap. The output of those pops, collected in
order, is the sorted result. Each pop is `O(logn)`, and there
are `n` pops, which brings the total runtime of this sort to
`O(n + nlogn)` which is asymptotically equivalent to the
runtimes of efficient searches such as mergesort and quicksort.

In the out-of-place version, we could rearrange the input
array into a heap and collect the results of heap popping
in a separate array, which would take `O(n)` space.

In the in-place version, you could use part of the input
array for storing the heap and part of the array for storing
the results of popping. One advantage that heapsort has
over both quicksort and mergesort is that it can be done
in-place like this, saving some memory.

## Code

[Python](./day49)

## Follow up

