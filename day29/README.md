question of the day: https://codefights.com/interview/vzzkv5NHFMELWSwAS

Given an integer len, count the number of different good strings that
have a length of exactly len. A good string is a string for which the
following conditions are true:

1. A good string contains only lowercase English letters.
2. Each character in a good string is unique.
3. Exactly one character in a good string is lexicographically greater
than the character that precedes it.

**Example**

For `len = 2`, the output should be
`goodStringsCount(len) = 325`.

If the first symbol is 'a', there are 25 possible good strings: "ab", "ac", ...  
If the first symbol is 'b', there are 24 possible good strings: "bc", "bd", ...

If the first symbol is 'z', there are 0 possible good strings because there is
no character that is lexicographically greater.

There are 25 + 24 + 23 + ... + 0 = 325 good strings that have a length of 2.

For len = 1, the output should be goodStringsCount(len) = 0.

The 3rd rule for good strings can't be true if there is only one character in the string.

## Ideas

Brute force: enumerate all possible permutations and check whether the
constraints are satisfied. In this solution, 'aa', 'ab', etc. will be checked,
but so will 'za', 'zb', 'zc', ..., 'zz', etc. which is a lot of wasted
work. It also runs in `O(26**len)` which is exponential time which is horrible.

How do we save work? Let's look at the constraints and factor them into the
enumeration of permutations. We should never use upper case letters. We should
not use duplicate letters, i.e. if we've placed the letter 'a' as we're
constructing a good string, we should not place another letter 'a' in the same
good string. And likewise, we shouldn't place letters into the good string
if they are lexicographically less than the characters that precede it.

len = 2  
'ab', 'ac', 'ad', 'ae', ... 'az' -> 25 possible strings

len = 3
'abc', 'abd', 'abe', ... 'abz' -> 24 possible strings  
'acd', 'ace', ... , 'acz' -> 23 possible strings  
...  
'ayz' -> 1 possible strings  
'az' -> 0 possible strings

'bcd' -> 23
'bde' -> 22

0 1 -> 25  
1 2 -> 24  
2 3 -> 23  
3 4 -> 22  
...
25 26 -> 1  

0 1 2 -> 24  
1 2 3 -> 23  
2 3 4 -> 22  
3 4 5 -> 21  
..
23 24 25 -> 1
24 25 _  -> 0

## Code

[Python](./goodStringscount.py)

## Follow up

I cheated today: http://blog.codefights.com/goodstringscount-solution/

Be sure to read this and understand the combinatorics theory! I think it'd be
a great exercise to break down a couple more combination questions. A lot of 
companies seem to ask these kinds of questions, and it's a really useful math
skill for calculating possibilities / probabilities / counting.


