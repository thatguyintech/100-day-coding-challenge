Question of the day: http://www.techiedelight.com/find-kth-smallest-element-array/

Given an array and positive integer `k`, find kth smallest element
in the array.

Example:

arr = [7, 4, 6, 3, 9, 1]
k = 3

Output:

4

## Ideas

1) Sort the array in `O(nlogn)` time and then access the kth index of the
   array to get the answer.

2) Min-heapify the array in `O(n)` time and then pop from the min heap `k`
   times in `O(klogn)` time. Overall runtime `O(n + klogn)`.

3) Max-heapify the first `k` elements of the array in `O(k)` time and then
   repeatedly remove the max element, replacing it with a new element from
   the input array, until there are no more unused elements from the input
   array in `O(nlogk)` time. Once there are no more elements, the root in
   the max heap will be the kth smallest element of the input array.

Let's implement all three.

## Code

[Python](./day47.py)

## Follow up
