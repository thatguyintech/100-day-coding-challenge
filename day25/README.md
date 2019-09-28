question of the day: https://codefights.com/challenge/CA2ShAfLkb5D5JHCG

Given a text, reverse its characters and shift all of the vowels in a cycle.

The vowels are 'a', 'e', 'i', 'o', and 'u' and can be upper- and lowercase.

Example

For cycle = 1 and text = "potato", the output should be
changeOfVowelsInCycle(cycle, text) = "ototap".

Reversed, the text becomes "otatop". The vowels in the text are 'o', 'a' and 'o' (in this exact order). When shifted by one, they become 'o', 'o' and 'a', so the final answer is "ototap".

## Ideas

I needa do two things: 1) reverse the string, 2) do the cycly thingy with the vowels.
The cycly thingy is the slightly tricky part. However, I can just think of the
vowels as a kind of circularly linked list where I can forget about parts of the list
when I'm done with them. I can use a queue to hold the vowels that are in the process
of being swapped into a new position. And I'll pop from this queue as I go through
the indices of vowels that I need to swap.

part 1 is `O(n)` runtime, and requires `O(n)` space because I create a list using the 
characters of the string before I do the reversal.

part 2 is `O(n)` runtime as well because in the worst case, all the input characters
are vowels.

So overall `O(n)` runtime, `O(n)` space. Is there a better solution? Maybe.

## Code

[Python](./changeOfVowelsInCycle.py)

## Follow up

#test
