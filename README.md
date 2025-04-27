# bubble
Bubble sort DSA with Python

## Manual Run Through
Before we implement the Bubble Sort algorithm in a programming language, let's manually run through a short array only one time, just to get the idea.

**Step 1:** We start with an unsorted array.

[7, 12, 9, 11, 3]

**Step 2:** We look at the two first values. Does the lowest value come first? Yes, so we don't need to swap them.


[`7, 12,` 9, 11, 3]

**Step 3:** Take one step forward and look at values 12 and 9. Does the lowest value come first? No.

[7, `12, 9,` 11, 3]

**Step 4:** So we need to swap them so that 9 comes first.

[7, `9, 12,` 11, 3]

**Step 5:** Taking one step forward, looking at 12 and 11.

[7, 9, `12, 11,` 3]

**Step 6:** We must swap so that 11 comes before 12.

[7, 9, `11, 12,` 3]

**Step 7:** Looking at 12 and 3, do we need to swap them? Yes.

[7, 9, 11, `12, 3`]

**Step 8:** Swapping 12 and 3 so that 3 comes first.

[7, 9, 11, `3, 12`]


## Bubble Sort Implementation
To implement the Bubble Sort algorithm in a programming language, we need:

1. An array with values to sort.
2. An inner loop that goes through the array and swaps values if the first value is higher than the next value. This loop must loop through one less value each time it runs.
3. An outer loop that controls how many times the inner loop must run. For an array with n values, this outer loop must run `n-1` times.
