question of the day: https://codefights.com/challenge/ChcFLSa3rfJsKNgkC

The fight on whether to store numbers starting with their most 
significant digit or their least significant digit has been going 
on for years. It even got a name and is called the Endian War by 
some specialists.

Joe Stoy in his (excellent, by the way) book "Denotational Semantics",
tells the following story about Alan Turing: "...One early British
computer had numbers running from right to left (because the spot
on an oscilloscope tube runs from left to right, but in serial
logic the least significant digits are dealt with first). Turing
used to mystify audiences at public lectures when, quite by 
accident, he would slip into this mode even for decimal arithmetic,
and write things like 73+42=16...".

You are given an expression that was presumably written by Alan Turing.
Return true if it is a correct expression written in the little-endian
decimal format, or return false otherwise.

## Example

For expression = 73+42=16, the output should be
endianWar(expression) = true.

In the little-endian decimal format, the expression becomes
37 + 24 = 61, which is correct.

For expression = "5+8=13", the output should be
endianWar(expression) = false.

In the little-endian decimal format, the result of the expression should
be 31.

## Ideas

Let's break the expression string up and check the math. Reverse the
two addends and sum them, then check against the reversed little-endian
sum.

`O(n)` to do the splits on the expression, `O(n)` to reverse the numbers
and convert into ints. `O(1)` to check the math of the expression.

## Code

[Python](./endianWars.py)

## Follow up
