Question of the day: #2 http://www.techiedelight.com/find-pair-with-given-sum-array/

Given an unsorted array of integers, find a pair with given sum in it.

For example:

Input:  
`arr = [8, 7, 2, 5, 3, 1]`  
`sum = 10`

Output:  
Pair found at indexes (0, 2) => `8 + 2 = 10`  
OR  
Pair found at indexes (1, 4) => `7 + 3 = 10`

## Ideas

My brute force solution is to iterate through the entire array once
for each element in the array. This `O(n<sup>2</sup>)` solution would
allow me to check every single pair of numbers.

I notice that in the brute force I'm doing unnecessary work when I
pair two numbers up that are too small or too big to be candidate pair
for the goal sum. If I want to gain some knowledge about increasing/
or decreasing sum, I can sort the array first in `O(nlogn)` time
and then set one pointer at the beginning, one pointer at the end,
and then iterate them towards the middle depending on whether my
running sum is smaller or greater than the goal sum.

If I'm okay with using some dynamic space allocation, an even faster
solution would be to use a hashmap to store the integers I've seen
previously as I move along, and then check if a complementary number
has been stored before I  move on to the next number in the array.
This approach would only require one pass through of the array so 
the run time would be `O(n)` and in the worst case I'd store almost
every element in the array, which would make the space complexity `O(n)`.

I'll implement the last one:

## Code

[Python](./twosum.py)
