Question of the day: https://leetcode.com/problems/permutations/#/description

Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:

```python
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```

## Ideas

This is a pretty basic question but while I was working on a different question
(which I'll save for tomorrow), I realized that the recursion for this problem
didn't really come naturally to me.

A good way to think about it is to assume that I have the first element of the
list, ready to go, and I have all possible permutations of the rest of the list,
already calculated for me. In this situation, I'd just take that first element
and insert it into each slot in each permutation, starting from 0, going to the
end.

i.e.

If I had the permutations `[[2, 3], [3, 2]]` calculated already, all I need to 
do to include the `1` is to "insert" it into each possible location in each of
the permutations, like this:

```python
[1, 2, 3]
[2, 1, 3]
[2, 3, 1]
[1, 3, 2]
[3, 1, 2]
[3, 2, 1]
```

This solution is `O((spots for the first elem to go in) * (num perms of the remaining list))`
where `(num perms of the remaining list)` is equal to
`(spots for the first elem to go in) * (num perms of the remaining list)` recursively.
So the runtime is `O(n!)`.

## Code

[Python](permutations.py)

## Follow up

This procedure has already been implemented in Python's built-in library:

```python
from itertools import permutations

permutations([1, 2, 3])
```

https://docs.python.org/2/library/itertools.html#itertools.permutations
