Question of the day: https://en.wikipedia.org/wiki/Eight_queens_puzzle

## Why this question? ##

After fudging up the recursion on yesterday's problem, I wanted
to get more practice with recursion. So I found this problem.

## Ideas ##

The context is that I have `n` Queens and I want to place them
on an `n`x`n` chessboard. Since they're Queens, no two pieces
can share the same row, column, or diagonal.

If I look at the problem where `n=0`, I'm done immediately because
I have `0` Queens to place anyways.

For `n=1`, I just put the one Queen onto the one spot and that's
done.

I can't solve this for `n=2` and `n=3`. I can only fit 2 Queens
on the `n=2` board and 2 Queens on the `n=3` board before they
start killing each other. I can visuallly verify these two cases quickly, but
in order to do it programmatically, I can do a brute force check:

1. place a queen on the board
2. look at all the remaining spaces and check if there is a spot where I can place another queen on the board

which means on a `n=3` board, I'm doing
`n<sup>2</sup> * (n<sup>2</sup> - 1) * (n<sup>2</sup> - 2)`
checks. Aka all permutations of `n` queens on an `n` by `n` board.
Aka `O(n<sup>n</sup>)`. Ok or not ok? Let's do a couple more `n`s
and then come back to this.

For `n=4`, it's taking me a little longer to figure out visually.
I feeeel like there is only one solution (assuming orientation
of the board doesn't matter). It looks like this:

||x|||
|-|-|-|-|
||||x|
|x||||
|||x||

My approach here was to do as many knight moves as I could fit,
since two queens in a knight's diagonal will not cross rows, columns
or diagonals. And looking at this solution, there's another solution

|||x||
|-|-|-|-|
|x||||
|||||x
||x|||

which is just a mirror version of the first one.

OH I just realized that the sample input/output on leetcode is
exactly the case for `n=4`, and they're defining distinct solutions
to include mirror images potentially. Ok, so for `n=4` there
are two distinct solutions.


really interesting wikipedia article on this question: https://en.wikipedia.org/wiki/Eight_queens_puzzle

something something backtracking