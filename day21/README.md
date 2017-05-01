Question of the day: https://codefights.com/challenge/hT9JyzWh77Y6NR2Qd

Stephan is a little boy who loves math. It came as a revelation to him that
one can define the greatest common divisor for rational numbers, not just
for integers. He's decided to dig into the subject and analyze the properties
of this new-to-him GCD.

Stephan needs lots of GCDs to gather all possible information about them. But
Stephan is still a little boy and he can't calculate the GCD of two numbers as
quickly as he'd like. So he asks for your help: Given float numbers x and y,
calculate their greatest common divisor.

It is guaranteed that both x and y will have at most 5 digits after the decimal
point.

Example:

For `x = 2.4` and `y = 4.8`, the output should be
`helpingStephan(x, y) = 2.4`.

## Ideas

How do I even find GCD without decimals? uhhhhh....

Prime factorization? That seems complicated but doable for small numbers. 
I can get the prime factorization of each number by repeatedly dividing
primes in increasing magnitude up to the value of the number, and keeping
the number of times each prime divides into the number in a hash. Then get
the primes that each number has in common and get the `min` between them.

Let me just google this.. 

Aha! [Euclid's Algorithm](https://en.wikipedia.org/wiki/Greatest_common_divisor#Using_Euclid.27s_algorithm)
I totally learned this in Algorithms class in college but forgot it existed.

Not sure what the runtime is for this algorithm, but this stack overflow post
kinda explains it: http://stackoverflow.com/questions/3980416/time-complexity-of-euclids-algorithm

So I could just change the floats that I'm given into ints by multiplying by
a factor of 10, apply Euclid's Algorithm in `O(n)` runtime where `n` is
proportional to the value of the input numbers, and then divide by the earlier
factor of 10 I used to multiply.

## Code

[Python](helpingStephan.py)

## Follow up

Floats.. https://docs.python.org/2/tutorial/floatingpoint.html#tut-fp-issues
