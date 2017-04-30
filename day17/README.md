Question of the day: https://leetcode.com/problems/search-a-2d-matrix/#/description

Write an efficient algorithm that searches for a value
in an `n` x `m` matrix. This matrix has the following
properties:

- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last
integer of the previous row.

Sample input:

```python
[  
  [1,   3,  5,  7],  
  [10, 11, 16, 20],  
  [23, 30, 34, 50]   
]
```

value to find: `3`

return `True`

## Ideas

So we want to search the matrix for a value. The way the integers
are sorted, if I were to stack each row one after the other, I'd
have an array of sorted integers, i.e.

`[1,3,5,7,10,11,16,20,23,30,34,50]`

and from here I could perform a binary search in `O(logn)` time.
If I wanted to actually stack the rows, I'd also need `O(n)` space
to create a new array of integers, and I think this can be optimized
if I'm careful about how I manipulate the row and column indicies
as I binary search through the original matrix

Let's say I start at the "middle" index of the matrix, with tie
breakers favoring smaller-valued inidces: I'd start by looking at
the `11` in the given matrix, which has a coordinate of `(1,1)`.
The dimensions `n` x `m` of the matrix (or `rows` x `cols`) are
`3` x `4`. So the calculation for the coordinates would be something
like:

`(dimension - 1) / 2`  
`(3 - 1) / 2 == 1`  
`(4 - 1) / 2 == 1`  

Now what if I have to explore the next "half" of the matrix? How
do I change my pointers to accurately find the next integer?

So let's say I'm ultimately looking for the `3`. That's located
at the coordinate: `(0, 1)`. Since `3` is less than `11`,  which
is located at `(1, 1)`, we want to go "backwards" in the matrix.

At this point I think it'd be really useful to have a translation
mechanism to go from matrix coordinate to array index. In order
to create this translation we just need the length of the rows in
the matrix.

`(0, 0)` <-> 0
`(0, 1)` <-> 1
`(0, 2)` <-> 2
`(0, 3)` <-> 3
`(1, 0)` <-> 4

when we get to `(1, 0)`, we've wrapped around the full length of
the row, so we increase the row index and reset the column index.
It's modular arithmetic. To go back from `4` to `(1, 0)`, we do

`4 % len(matrix) == 0` and `4 / len(matrix) == 1`

so our column index is 0 and our row index is 1.

Now that we have a translation mechanism, we can just do binary
search on the matrix, treating the coordinates like the indices
of a 1D array.

This solution is `O(log(n*m))` runtime and `O(1)` space since we no
longer need to use any memory.

## Code
[Python](./searchMatrix.py)

## Follow up

@apengwin mentioned that there is an "interesting variation to this
problem when the matrix is a [Young tableau](https://en.wikipedia.org/wiki/Young_tableau)"

not sure what this is yet but could be interesting to look into!

