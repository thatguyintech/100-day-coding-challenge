question of the day: https://leetcode.com/problems/search-a-2d-matrix-ii/#/description

Write an efficient algorithm that searches for a value in an `m` x `n`
matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.

Integers in each column are sorted in ascending from top to bottom.

For example,

Consider the following matrix:

```ruby
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```

Given *target* = `5`, return `true`.  
Given *target* = `20`, return `false`.  

## Ideas

Brute force solution: just iterate through every coordinate in the
matrix and compare value by value to see if any match. Return `true`
when a match is found, or `false` if the whole matrix has been searched
without finding a match. This is an `O(rows*columns)` runtime solution,
but doesn't take advantage of the existing ordering.

Now, unlike yesterday's problem where in addition to the elements
in each row being ordered in increasing order, the same property held
across rows. The matices in this problem are not like that. The
elements in each column are also increasing order now. This means I can't
do a binary search across all the elements in the matrix as easily.

Something I can still do right off the bat, is a binary search within
each row. For example, in the example matrix, if I'm going to look for 
`13`, I can start in the middle of the first row, then search the right half
(since `7` < `13`), then search the right half again (since `11` < `13`) and
finally give up on the row once I see `15` is the last option. I'd
move down to the next row and repeat the binary search. This solution
is a slight improvement, especially on larger matrices. It'd have a
`O(rows*log(columns))` runtime. However, I'm still not using the
increasing-down-columns property to my advantage.

At this moment, I can't think of a better way to solve this problem.

I'll just implement the binary search by rows solution for now.

## Code

[Ruby](./searchMatrix2.rb)

## Follow up

I can optimize this approach even further by checking which dimension
is longer (rows or columns) and doing binary search along the larger
valued dimension to maximize efficiency.

I'll update this soluiton once I think of an even more optimal approach.

@apengwin says there's a known `O(m + n)` solution to this problem and
that I should "Think about using the sorted-ness of the matrix to my
advantage". 


