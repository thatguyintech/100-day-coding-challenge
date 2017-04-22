Question of the day: https://www.careercup.com/question?id=5672334801240064

You are tasked with defining and implementing a function. As input,
you are given an `n` by `m` matrix. `x` may appear any number of
times in a matrix. Your function should modify the matrix such that
any row and column where `x` originally appears are completely over-
written with `x`.

For example:

```
-----
-----
---x-
x----
-----
```

turns into:

x--x-
x--x-
xxxxx
xxxxx
x--x-

## Ideas

Go through each coordinate in the matrix and check if it contains
an `x`. For each one that contains an `x`, add the row and column
indices to a set to remember which rows and columns to fill with
`x`. Doing this "remembering" will prevent us from writing multiple
`x`s over the same spot. Finally, go over the matrix again and 
add `x`s to the matrix.

This solution runs in `O(n*m)` time because it iterates through
each spot in the matrix twice. It also requires `O(n+m)` space to
remember all possible indices that need `x`s added. Can we do
better?

Runtime wise, I don't think so. I can't think of a faster way to
find all the `x`s, so I'm bottlenecked at `O(n*m)` already. I could
also trade the space requirement for a slower runtime where every
time I find an `x`, I immediately overwrite the relevant spots in
the matrix, but this would bring my runtime up to `O((n*m)<sup>2</sup>)`.

If I knew my matrices would always be small, it could be worth
the tradeoff.

## Code

[Python](./writex.py)

## Follow up


