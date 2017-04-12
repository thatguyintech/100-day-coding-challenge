Question of the day: https://leetcode.com/problems/linked-list-random-node/#/description

First draft of thought process:

Two solutions come to mind immediately, with a tradeoff between
space and time (that's always the tradeoff).

1) Store all the elements of the incoming linked list in an array,
   then use a random number generator to select an index. Storing
   the elements in an array would take up `O(n)` space, but then
   accessing them with the `O(1)` randomly generated index would
   still be `O(1)` since it's just a matter of indexing into the 
   array.

2) Reverse the first idea. Generate the index from the random number
   generator first and then move a pointer down the nodes of the
   linked list to find the value to return. Since we're not storing
   anything in this implementation, it'd be `O(1)` space, but every
   time we call `getRandom` it would cost us `O(N)` time.

While pondering this question, I became really curious about random
number generation. Like.. how does it work?! Is anything truly
random in this world? If you think about things from a physics point
of view, every atom has its role in changing the world from one
moment to the next. So for the purposes of generating a random
index for my linked list, to keep things practical, I need to know
**how random** I need the random index to be. I'll just go ahead
and assume I don't need something that's random to the point of
cryptographic security.

[..2 hours of wikipedia surfing later..]

In that case, there is the [random](https://docs.python.org/2/library/random.html#random.random)
python library that's implemented using a [Mersenne Twister](https://en.wikipedia.org/wiki/Mersenne_Twister)
generator that'll suit my needs just fine.

## Code ##
(Python)[./randomnode.py]

## Follow up ##

I noticed this Leetcode user's (and many others') [solution](https://discuss.leetcode.com/topic/53738/o-n-time-o-1-space-java-solution) that uses the idea of
(Reservoir Sampling)[https://en.wikipedia.org/wiki/Reservoir_sampling]
to randomly choose an element from the linked list. It's an optimization
on my solution because in my code I first count how many elements `n`
there are, and then use that `n` to generate a random number, so my total
runtime is `O(1.5n)`, which is still asymptotically `O(n)`, but technically
slower. Reservoir Sampling brings it down to `O(0.5n)` (still asymptotically `O(n)`).
