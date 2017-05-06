question of the day: https://codefights.com/challenge/szuSfd9RjD3jwKtwj

If we write out all the [binomial coefficients](https://en.wikipedia.org/wiki/Binomial_coefficient)
`C(N, K)` for all `N ≤ 5`, here's what we'll get:

``` python
N = 0: [1]
N = 1: [1, 1]
N = 2: [1, 2, 1]
N = 3: [1, 3, 3, 1]
N = 4: [1, 4, 6, 4, 1]
N = 5: [1, 5, 10, 10, 5, 1]
```

This set of lists is often referred to as [Pascal's Triangle](https://en.wikipedia.org/wiki/Pascal%27s_triangle).
As we can see, 17 out of 21 numbers in it are not divisible by 5.

Given an integer num and a prime number, calculate the number of all the binomial coefficients for all i ≤ num that are not divisible by prime.

Example

For `num = 5` and `prime = 5`, the output should be

`countingBinomialCoefficient(num, prime) = 17`.
