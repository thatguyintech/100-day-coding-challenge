Question of the day:

Given an `n` by `m` matrix of integer values, and a pair of
coordinates `(x1, y1)` and `(x2, y2)` representing the top left
and bottom right indices of a rectangle, return the sum of all
the integers encompassed by the rectangle in the matrix.

For example, given this matrix:

```python
1  2  3  4  5  
6  7  8  9  10  
11 12 13 14 15  
16 17 18 19 20  
```

and the pair of coordinates:

`(0,2)`, `(2,4)`

the sum to return is:

`3+4+5+8+9+10+13+14+15 = 81`

## Ideas

A brute force solution is to calculate the sum using the relevant
indices. So for `(0,2)` (top left) and `(2,4)` (bottom right), the
relevant row indices are `0, 1, 2`, and the relevant column indices
are `2, 3, 4`. As we access each coordinate, add the number to an
accumulating sum.

This solution would take `O(n)` time where `n` is the size of the
rectangle formed by the given top left and bottom right corner
coordinates.

Can we do better?

Kinda. We can do a little bit of pre-processing on the original
matrix to make it faster for us later. If we calculate the sums
of the rectangles formed by the top left coordinate `(0,0)` and each
coordinate in the matrix as the bottom right coordinate, we can use
these sums to then return the relevant sums we're looking for 
in constant time. For rectangles that do not start at the `(0,0)`
for the top left coordinate, we can just do some subtraction using
other rectangles.

## Code

## Followup