Question of the day: https://www.careercup.com/question?id=5642834636963840

Given a 2D array of digits, try to find the occurence of a given 2D
pattern of digits. For example, consider the following 2D matrix:

```python
7283455864  
6731158619  
8988242643  
3839505324  
9509505813  
3843845384  
6473530293  
7053106601  
0834282956  
4607924137  
```

Assume we need to look for the following 2D pattern:

```python
950  
384  
353  
```

Return a list of the top left indices of an occurence of the pattern in
the 2D matrix. If there are multiple occurences, return all of the
possible indices.

## Ideas

I'm going to make some assumptions to get myself started. I can explore
these assumptions more in the follow-up section later on.

1. We don't care about finding rotations of the 2D pattern inside the matrix.
2. We don't care about finding parts of the 2D patten inside the matrix
3. The dimensions of the 2D pattern are always less than or equal to the respective dimensions of the matrix.

A brute force solution would be to iterate through all possible locations
in the matrix and check if the 2D pattern matches starting at that
location. Let's define `width` and `height` to be the width and height
of the matrix. It would take `O(width*height)` time just to go through
all the possible starting locations. Let's define `pWidth` and `pHeight`
to be the width and height of the 2D pattern. So then if the pattern
matches, there would be an additional `O(pWidth*pHeight)` per location
with a possible start point, which excludes parts of the matrix. In the
worst case, the runtime to this brute force solution is
`O((width - pWidth) * (height - pHeight) * pWidth * pHeight)`. I do a
subtraction which is key, because in a matrix like this:

```python
11111  
11111  
11111  
11111  
11111  
```

with a 2D pattern like this:

```python
1111  
1111  
1111  
1111  
```

there are only 4 possible starting locations: `(0, 0), (0, 1), (1,0), (1,1)`.

I don't think it's possible to do this problem and faster. So it's not
a very complex problem, now I just have to write the code.

## Code

[Python](./2D-pattern-in-matrix.py)
