Question of the day: http://www.techiedelight.com/sort-k-sorted-array/

Given a k-sorted array, which is an array that is almost sorted, to the
point where each of the N elements in the array are at most `k` index
positions away from its correct sorted order, find an efficient
algorithm to sort the array.

## Ideas

Ignoring the interesting constraint, if we want to end up with a sorted
array, we can just use an efficient sorting algorithm such as merge sort
to sort the array and output it. An in-place merge sort would take `O(NlogN)`
time and `O(1)` space complexity. 

Using the k-sorted constraint to our advantage, we can pick a better sort,
insertion sort which would run in `O(Nk)` time. For each element in the array,
check its `k` nearest neighbors to find the right place to insert it.

However, the best time complexity lies in a heap solution. If we start off
by creating a min heap of size `k+1`, we can iterate through the array by
popping the min element out of the heap and adding a new element into the
heap from the array. For each element, we do one pop from the heap and one
push onto the heap, both of which are `O(logk)` time complexity. The total
time complexity would therefore be `O(Nlogk)`. The difference in runtime
would especially be noticeable for larger values of `k`. The space required
to maintain the heap would be `O(k)` and the space we need to store the
resulting sorted array would come out to `O(N)`.

## Code

[Python](./sortKSortedArray.py)

## Follow up

