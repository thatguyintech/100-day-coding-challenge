Question of the day: https://leetcode.com/problems/longest-consecutive-sequence/#/description

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,  
Given `[100, 4, 200, 1, 3, 2]`,  
The longest consecutive elements sequence is `[1, 2, 3, 4]`. Return its
length: `4`.  

Your algorithm should run in `O(n)` complexity.

## Ideas

Clarification questions: can I make any assumptions about the integers in the
input array? I.e. is there a range like 0 - 100? Are all integers in the input
array unique or can there be duplicates? Do duplicates count in consecutive
sequences?

Radix sort allows me to do a tradeoff on space for faster time complexity. The
radix I can use here instead of digit-by-digit, is to treat the max valued element
of the array as the limit of a single, theoretical digit. That way, in one
additional pass through, I will have the input sorted. In a third pass through,
I can count the longest consecutive sequence.

This approach is fine for input arrays with elements that aren't too large.
However, the runtime is actually proportional to the value of the largest element.
Both the runtime and space complexity are `O(k)` where `k` is the value of
the largest element.

Is there a better approach? Not sure. Let's code up the first solution and
see if I can think of anything by the end.

## Code

[Python](./longestConsecutive.py)

## Follow up

Welp.. didn't actually solve the problem under the right constraints. How can I 
be more efficient?
