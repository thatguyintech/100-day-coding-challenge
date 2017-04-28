question of the day: https://leetcode.com/problems/01-matrix/#/description

Given a matrix consists of 0 and 1, find the distance of
the nearest 0 for each cell.

The distance between two adjacent cells is 1.

*Example 1:*

Input:

```ruby
0 0 0
0 1 0
0 0 0
```

Output:

```ruby
0 0 0
0 1 0
0 0 0
```

*Example 2:*

Input:

```ruby
0 0 0
0 1 0
1 1 1
```

Output:

```ruby
0 0 0
0 1 0
1 2 1
```

Assumptions we can make:

1. The number of elements of the given matrix will not exceed 10,000.  
2. There are at least one 0 in the given matrix.  
3. The cells are adjacent in only four directions: up, down, left and right.  

## Ideas

This is like drawing out a contour map. The 0's are the peaks of
hills and mountains, while the parts of the matrix that are far away
from any 0's are like the valleys.

We can start from each peak and go outwards. It'd be a BFS-like
approach. Do a search through the whole matrix once first and find
where all the 0's are. Add each of those positions into a queue,
and then use that queue to start off a BFS. During this BFS, we
check the neighboring cells to see what the minimal value is that
we can place in this cell.

## Code

[Ruby](./matrixCountours.rb)

## Follow up