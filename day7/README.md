Question of the day: #2 Alien Alphabet from this [discussion worksheet](./https://d1b10bmlvqabco.cloudfront.net/attach/ixmn3a7kjp7186/hktxrll0pr53jq/iz0mn2w8l3du/sec4sol.pdf)

Suppose you have a dictionary of an alien language which
lists words in some sorted lexicographical ordering. For
example, given the following list of words:

`[baa, abcd, abca, cab, cad]`

You can conclude the ordering of the alphabet is

`b < d < a < c`

Write a function to determine the lexicographical ordering
for any input list.

## Ideas 

The lexicographical ordering requirement reminds me of dependency
graphs. I can model the words in the input list as having
dependencies on previous words that come earlier in the 
lexicographical ordering. Once I create this directed acyclic
graph (DAG), I can run through and linearize the graph using
Topological sort and DFS.

The creation of the DAG takes O(words*letters) and running
DFS on the created DAG takes O(words*letters).