Question of the day: https://leetcode.com/problems/reverse-string-ii/#/description

Given a string and an integer k, you need to reverse the first k characters
for every 2k characters counting from the start of the string. If there are
less than k characters left, reverse all of them. If there are less than
2k but greater than or equal to k characters, then reverse the first k
characters and leave the rest as they are.

Example:

```
Input: s = "abcdefg", k = 2  
Output: "bacdfeg"  
```

Restrictions:

1. The string consists of lowercase English letters only.  
2. Length of the given string and k will in the range [1, 10000]

## Ideas

1. break the sting into chunks of length `2k`  
2. reverse up to the first `k` of each chunk  
3. join the chunks together and return the result  


Although I logically want to break the string up into `2k` chunks right away,
I can just use some pointers as I move down the string so that I don't allocate
too much unnecessary memory. Reversing the relevant indices and returning at the
end will take `O(n)` runtime and `O(1)` space.

## Code
[Python](./reverseStr.py)

## Follow-up

