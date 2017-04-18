Question: #2 from this [CS170 discussion](https://d1b10bmlvqabco.cloudfront.net/attach/ixmn3a7kjp7186/hktxrll0pr53jq/iz0mn2w8l3du/sec4sol.pdf)

Alien Alphabet

Suppose you have a dictionary of an alien language which
lists words in some sorted lexicographical ordering. For
example, given the following list of words:

`[baa abcd abca cab cad]`

You can conclude the ordering of the alphabet is

`b < d < a < c`

Write a program to determine the lexicographical
ordering for any input list.

## Ideas

This alphabet ordering reminds me of depency graphs. Based
on the words list, some letters come before other letters.
Some letters have multiple letters that precede it in the 
words list. The trick is to find how those letters relate to
each other.

If I can represent the words/letters as a dependency graph,
I can then linearize the graph to get the final lexicographical
ordering of the letters.

I can represent the letters in each of the words in the word
list as a node in a dependency graph. To construct this graph,
I look at pairs of neighboring words and compare corresponding
letters from left to right in the word. If a letter in the 
left word is different than the letter in the right word, I
know that the first letter comes before the second letter, so
in my dependency graph I'll add a directed edge going from
the first letter to the second letter. Then I shift over one
pair to move on to the next two words to compare. If the
letters are the same, I compare the next pair of letters. In
the worst case, this process will iterate over all but two
of the words in the word list (assuming len > 2) twice, which
makes the runtime `O(letters)` where `letters` is the total
number of nodes in the dependency graph.

Once the graph is constructed, running topological sort, aka
a DFS on the graph to linearize the dependencies takes
`O(letters)`. Thus the overall runtime is `O(letters)` and the
space complexity is `O(letters)`.

## Code

[Python](./alienalphabet.py)

## Follow up

This code took me sooooo long to write. Definitely not sustainable
for me to code problems of this size with this amount of testing,
if I keep going at this rate. 1) I need to get faster at coding
and stop freezing up when I'm sensing some friction in my thought
process and 2) this was a really good review of linearization.

Also, I'm currently not accounting for edge cases like when I have
letters that I don't know where to place in the order. Currently
I just tack them onto the end of the alphabet. If I wanted to make
this a little more useful, instead of just tacking it on, I'd
output a separate set of unclassified letters.


