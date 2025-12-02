# Advent of code - day 2

## Part 1
The first part should just work well enough for this part, it might be able to be completed in a lower complexity.
We have `n = len(all_ranges)` ranges, and for each range we iterate from `start` to `end`. Let `R_i = end_i - start_i + 1` be the size of the i-th range.

For every number `j` in the range, we:
Convert it to a string: `O(d)` where `d = number of digits of j`
Split the string into halves: `O(d)`
Compare halves: `O(d)`
Total work per number `j` is `O(d)`.

`d_max` = max number of digits among all numbers in all ranges
`R` = sum of all `R_i`

So the total complexity results in: `O(R × d_max)`. Which might be reduced, but isn't that bad for a small code exercise.

## Part 2
This however, sucks hard if we look at its complexity.
The complexity of `isRepeated` is:
Let `n = len(string)` and `k = len(sub)`
The loop runs `n/k` times, each comparison is a substring of length `k`: `O(k)`
So `T_isRepeated(n, k) = O(n)`

The complexity of `isValid` is:
We know `n = len(string)`, and has a complexity of `O(n) x O(n) = O(n^2)`. Since the algorithm is based on the part 1 algorithm, we can describe it as: `O(n^2) = O(d_max^2)`. Therefore the total complexity becomes: `O(R x d_max^2)`. I'm certain that we can reduce this, however. Since this is a small code challenge. I will not do it for now (as well as I don't have time for it).