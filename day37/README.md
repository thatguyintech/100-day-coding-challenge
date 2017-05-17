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
[Python](./topKFrequent.py)

## Follow-up

redo this using python `collections` library
