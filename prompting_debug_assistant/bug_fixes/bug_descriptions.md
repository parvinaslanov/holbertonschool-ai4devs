# Bug Snippets – Intended Behavior

This collection contains five intentionally flawed programs in Python, JavaScript, and C. The examples cover different categories of common programming errors and are intended for an AI-assisted debugging exercise.

## Bug 1 – `bug1.py`
**Intended Behavior:** Calculate and return the arithmetic average of a list of numbers. If the list is empty, return `0`.

**Issue Type:** Syntax error.

**Notes:** The conditional statement checking whether the list is empty is missing required syntax. The program will fail before it can run.

## Bug 2 – `bug2.py`
**Intended Behavior:** Return a new list containing only scores that are equal to or greater than the minimum passing score.

**Issue Type:** Logical error.

**Notes:** The comparison currently selects scores below the minimum rather than scores that meet the passing requirement. The program runs, but its result is incorrect.

## Bug 3 – `bug3.js`
**Intended Behavior:** Return a user's name in uppercase and process all users in the array without crashing when a profile or name is unavailable.

**Issue Type:** Runtime exception.

**Notes:** One user has a `null` profile. Accessing `name` on that value causes a runtime error, interrupting the iteration.

## Bug 4 – `bug4.js`
**Intended Behavior:** Print each array item exactly once, together with its zero-based position.

**Issue Type:** Off-by-one / loop boundary error.

**Notes:** The loop condition allows the index to reach the array's length. That index is outside the valid range, so the final iteration attempts to print an undefined item.

## Bug 5 – `bug5.c`
**Intended Behavior:** Determine the number of integers in the `values` array, print that count, and then print every element.

**Issue Type:** Misuse of data types and the `sizeof` operator.

**Notes:** The expression used to calculate the element count divides the size of one element by the size of the entire array. The calculation is reversed, producing an incorrect count and preventing the loop from displaying all values.
