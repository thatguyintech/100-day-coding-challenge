Today's challenge is a continuation of [yesterday's](../day23)!

## Ideas

I wanted to take a different approach to this question; instead of doing a
full brute-force exploration on all combinations of the inputArray,
construct a graph and then do DFS from every node to find a possible 
Hamiltonian path. The existence of a path would verify whether there is
a desired arrangement of the strings.

I can construct the graph in `O(N<sup>2</sup>)` time where `N` is the number of 
elements in the inputArray, and also the number of vertices in my graph. I check
every possible pair of strings to see whether they differ by exactly one place,
and add an edge in the graph between the two if so.

I can then run DFS from each node in `N * O(N) = O(N<sup>2</sup>)` time (this
analysis doesn't seem right to me actually) to complete the algorithm.

Overall, it comes out to a runtime of `O(n<sup>2</sup>)`. The space complexity
scales in proportion to the number of vertices and edges I need to keep track
of in my graph. Vertices increase with every additional element in the inputArray.
Edges increase when there are higher frequencies of words in the inputArray
that are closer to each other in edit distance.

## Code

[Python](./stringsRearrangementBacktracking.py) (unfinished)

## Follow up

