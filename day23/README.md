question of the day: https://codefights.com/challenge/RWQS5cCEodqSWx4bR

Given an array of equal-length strings, check if it is possible to
rearrange the strings in such a way that after the rearrangement the
strings at consecutive positions would differ by exactly one character.

Example

* For `inputArray = ["aba", "bbb", "bab"]`, the output should be
`stringsRearrangement(inputArray) = false`.

All rearrangements don't satisfy the description condition.

* For `inputArray = ["ab", "bb", "aa"]`, the output should be
`stringsRearrangement(inputArray) = true`.

Strings can be rearranged in the following way: `"aa", "ab", "bb"`.

## Ideas

There's a smart way to do this problem and a not-as-smart way. I'm going
to use my knowledge of how to do permutations from [yesterday](../day22)
to implement the brute-force check by iterating over all permutations of
the input list and checking whether the current permutation is a possible
solution. If it is, break there and return `true`. Otherwise, keep going
until the last permutation has been checked, and then return `false`.

The permutations calculation would take `O(n!)` time just to generate
all possible permutations of the input list. Then I also need to do an
`O(n)` check each time to verify whether the permutation is a solution.
Where `n` is the number of strings in the input list, the overall runtime
is `O(n * n!)`.

## Code

[Python](./stringsRearrangement.py)

## Follow up
