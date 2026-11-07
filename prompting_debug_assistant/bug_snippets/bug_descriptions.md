## Bug 1 - bug1.py
**Intended Behavior**: Calculate the arithmetic mean of a list of numbers.
**Issue Type**: Syntax and Logical error.
**Notes**: The `for` loop is missing a colon (`:`), and the `if` statement uses assignment (`=`) instead of equality comparison (`==`).

## Bug 2 - bug2.js
**Intended Behavior**: Return the first `n` items from an array.
**Issue Type**: Off-by-one loop logic issue.
**Notes**: The loop condition uses `<=` instead of `<`, which attempts to process one element too many and causes out-of-bounds behavior.

## Bug 3 - bug3.java
**Intended Behavior**: Retrieve a username string by ID and return its length.
**Issue Type**: Runtime exception.
**Notes**: Fails with a `NullPointerException` if the database entry at the specified index is `null`.

## Bug 4 - bug4.cpp
**Intended Behavior**: Calculate the sum of elements in a vector.
**Issue Type**: Misuse of data types / Loop logic issue.
**Notes**: Uses an unsigned type (`size_t`) with a condition `i >= 0`, which is always true and leads to an infinite loop or undefined behavior.

## Bug 5 - bug5.py
**Intended Behavior**: Print a countdown from a given starting number down to 1.
**Issue Type**: Logical error.
**Notes**: The loop increments the counter instead of decrementing it, resulting in an infinite loop.
