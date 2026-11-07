# Bug Snippets – Intended Behavior

This folder contains five intentionally flawed programs written in Python, JavaScript, and C. Each example demonstrates a different common programming error for an AI-assisted debugging exercise.

## Bug 1 – `bug1.py`
**Intended Behavior:** Calculate and return the arithmetic average of a list of numbers. If the list is empty, return `0`.

**Issue Type:** Syntax error.

**Notes:** The conditional statement that checks whether the list is empty is missing a required colon. Python cannot parse the program as written.

## Bug 2 – `bug2.py`
**Intended Behavior:** Return a new list containing only scores equal to or greater than the minimum passing score.

**Issue Type:** Logical error.

**Notes:** The comparison currently selects scores below the minimum instead of scores that meet the passing requirement. The program runs, but produces the wrong result.

## Bug 3 – `bug3.js`
**Intended Behavior:** Convert each user's name to uppercase and process all users without crashing when a profile or name is unavailable.

**Issue Type:** Runtime exception.

**Notes:** One user has a `null` profile. Attempting to access `name` on that value causes a runtime error and interrupts processing.

## Bug 4 – `bug4.js`
**Intended Behavior:** Print every array item exactly once, together with its zero-based position.

**Issue Type:** Off-by-one / loop boundary error.

**Notes:** The loop condition allows the index to reach the array's length. That index is outside the valid range, so the final iteration attempts to print an undefined item.

## Bug 5 – `bug5.c`
**Intended Behavior:** Calculate the number of integers in the `values` array, print the count, and then print every element.

**Issue Type:** Misuse of the `sizeof` operator.

**Notes:** The expression used to calculate the element count divides the size of one element by the size of the entire array. The calculation is reversed, resulting in an incorrect count and preventing the loop from displaying all values.
