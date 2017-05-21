[Today's challenge is actually a follow-up on day37's challenge -- using a heap instead of radix sort]

Question of the day: https://leetcode.com/problems/top-k-frequent-elements/#/description

Given a non-empty array of integers, return the k most frequent elements.

For example,  
Given `[1,1,1,2,2,3]` and `k = 2`, return `[1,2]`.

Note:   
* You may assume k is always valid, 1 ≤ k ≤ number of unique elements.  
* Your algorithm's time complexity must be better than O(n log n), where
  n is the array's size.

## Ideas

Can't do a normal sort, since that alone will take `O(nlogn)` runtime.
The input array isn't sorted, so we need to keep track of a count and organize
that count somehow as we iterate through the integers in the array. There
doesn't seem to be any constraints on the types of integers on the array,
so I'll assume that possible elements in the array range from -maxInt to maxInt
. 

I think I can actually use radix sort again. Same idea as the challenge from
[Day 36](../day36).

## Code
[Day 37 - Python](../day37/topKFrequent.py)

## Follow-up

Over the past few days ([38](../day38), [39](../day39), [40](../day40)), I got a
little more familiar with the heap data structure and finally understand why
heapifying an unsorted array can be done in linear time. The operations involved
in heapify decrease exponentially over a logarithmic range, resulting in an overall
linear amount of work. Anyways, I can use this `O(n)` time to heapify an unsorted
array of frequencies, and then pop off the top `k` frequencies in `O(klogn)` time.
The overall runtime would now be at most `O(nlogn)` if `k` == `n`. However, the
real savings is in the `O(n)` space for storing all the elements of the heap.
Much better than the `O(max value of the input array)` I had before.

## Code
[Day 41 - Python](./topKFrequen.py)
