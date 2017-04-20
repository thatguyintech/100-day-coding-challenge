question of the day: print the contents of an `n` by `m` matrix
in a spiral.

For example:

input:

```python
[[1,  2,  3,  4],
[ 5,  6,  7,  8],
[ 9,  10, 11, 12],
[ 13, 14, 15, 16]]
```

output:

`1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10`

### Ideas

(quick preface):  
I've always been mildly allergic to these kinds of matrix and array
manipulation problems. Off-by-one errors, translating visual movements
into for-loop and while-loop logic blocks, etc. Therefore doing more
of these problems will help me conquer that weakness. And I think
just doing one of these per day is not enough, especially if I'm
skipping from topic to topic. What I'll do is clump a bunch of these
kinds of questions together, and do them as a series day to day
so that over time I can get a sense of some patterns. Pattern recognition
is what's going to be truly useful to me.

(actual ideas about the problem):  
Edge cases (?) include empty matrix, having only one row to print,
having only one column to print, having a row width vastly different
from the column height. 

Let's just assume we'll be printing in a clockwise fashion.

Here are some sample inputs and outputs:

| inputs | outputs |
|--------|---------|
|`[[]]`  |         |
|`[1,2]` | ` 1 2 ` |
|`[[1],`<br>`[2],`<br>`[3],`<br>`[4]]` | ` 1 2 3 4 ` |
|`[[8, 1],`<br>`[7, 2],`<br>`[6, 3],`<br>`[5, 4]]` | ` 1 2 3 4 5 6 7 8` |

Alright now let's get a brute force solution down and then see if
it's possible to optimize.

If I wanted to print row by row, that'd be easy: two nested for-loops
one to go through the rows, and one to go through each of the elements
in each of the rows. The trick with printing in a spiral is that
sometimes we want to go up, sometimes we want to go down in terms of
the index of the elements. So now I'm thinking we need to have some
cursor comprised of a row index `row` and column index `col`, and we
also need to be aware of the current direction we're iterating in so
that it's possible to change directions.

Let's have a direction variable `dir` which can be one of four integers  
`0` - right  
`1` - down  
`2` - left  
`3` - up  
we'll switch directions by `dir = (dir+1)%4`

