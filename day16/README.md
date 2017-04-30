question of the day: https://leetcode.com/problems/spiral-matrix-ii/#/description

Given an integer n, generate a square matrix filled with elements
from 1 to n<sup>2</sup> in spiral order.

For example, given `n=3`, return the following matrix:

```python

[
  [1,2,3],
  [8,9,4],
  [7,6,5]
]
```

## Ideas

Brute force: create a matrix with placeholder values, copy over my
code from [day 11](../day11/spiralMatrix.py), and modify that spiral
motion code to replace values with ascending values of `1..n<sup>2</sup>`
.

That'd be `O(n^2)` space and runtime.

## Code
[Python](./spiralMatrix2.py)

## Follow up