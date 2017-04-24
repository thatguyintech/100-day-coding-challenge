Question of the day: https://code.google.com/codejam/contest/8294486/dashboard

Problem

Annie is a bus driver with a high-stress job. She tried to unwind
by going on a Caribbean cruise, but that also turned out to be
stressful, so she has recently taken up horseback riding.

Today, Annie is riding her horse to the east along a long and
narrow one-way road that runs west to east. She is currently at
kilometer `0` of the road, and her destination is at kilometer `D`;
kilometers along the road are numbered from west to east.

There are `N` other horses traveling east on the same road; all of
them will go on traveling forever, and all of them are currently
between Annie's horse and her destination. The `i`-th of these horses
is initially at kilometer K<sub>i</sub> and is traveling at its
maximum speed of S<sub>i</sub> kilometers per hour.

Horses are very polite, and a horse H<sub>1</sub> will not pass
(move ahead of) another horse H<sub>2</sub> that started off ahead
of H<sub>1</sub>. (Two or more horses can share the same position
for any amount of time; you may consider the horses to be single
points.) Horses (other than Annie's) travel at their maximum
speeds, except that whenever a horse H1 catches up to another
slower horse H<sub>2</sub>, H<sub>1</sub> reduces its speed to
match the speed
of H2.

Annie's horse, on the other hand, does not have a maximum speed and
can travel at any speed that Annie chooses, as long as it does not
pass another horse. To ensure a smooth ride for her and her horse,
Annie wants to choose a single constant "cruise control" speed for
her horse for the entire trip, from her current position to the
destination, such that her horse will not pass any other horses.
What is the maximum such speed that she can choose?

## Ideas

To get an intuition for the math behind this problem, let's draw
some horses.

(horse drawing tba)

The crucial idea that took me a couple of tries to validate is that
the horse that takes the longest time to reach the end is the 
horse that Annie must be aware of not crossing. If we get the time
of that horse, then we can calculate the average pace Annie should
travel at.

`(Annie's pace) = (total distance) / (slowest horse's completion time)`

The time it would take to calculate the slowest horse's completion
time would be `O(n)` where `n` is the number of horses on the path.

## Code

[Python](./cruise-control.py)

