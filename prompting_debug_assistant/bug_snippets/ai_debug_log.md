# AI Debugging Log

This document records the AI-assisted analysis of the five intentionally buggy programs. For each example, the original problem was reviewed, a correction was selected, and the corrected behavior was checked with a test.

## Bug 1 – `bug1.py`

**AI Prompt:**  
"This code throws an error / doesn't behave as expected. Can you identify and explain the issue and how to fix it?"

**AI Diagnosis:**  
The `if` statement is missing a colon (`:`) at the end of its condition. Python requires a colon before the indented body of an `if` statement. Because of this syntax error, Python cannot parse the file and the function never runs.

**Suggested Fix:**  
Add a colon to the condition:

```python
if len(numbers) == 0:
```

**Corrected Code:**

```python
def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

scores = [78, 85, 92, 66]
print("Average:", calculate_average(scores))
```

**Alternative Fixes Tested:**  
No alternative was needed. Adding the missing colon is the direct correction.

**Result:**  
The corrected program runs. The sample list returns an average of `80.25`. An empty list returns `0`, as intended.

---

## Bug 2 – `bug2.py`

**AI Prompt:**  
"This code throws an error / doesn't behave as expected. Can you identify and explain the issue and how to fix it?"

**AI Diagnosis:**  
The comparison uses `score < minimum`, which selects scores below the passing threshold. The function is supposed to return scores that are equal to or greater than the threshold. This is a logical error: the program runs, but its result is the opposite of what is intended.

**Suggested Fix:**  
Change the comparison from:

```python
if score < minimum:
```

to:

```python
if score >= minimum:
```

**Corrected Code:**

```python
def passing_scores(scores, minimum=50):
    passed = []
    for score in scores:
        if score >= minimum:
            passed.append(score)
    return passed

results = [35, 50, 67, 82, 49, 91]
print("Passing scores:", passing_scores(results))
```

**Alternative Fixes Tested:**  
A list comprehension could also solve the problem:

```python
passed = [score for score in scores if score >= minimum]
```

Both approaches use the same condition and produce the same result. The original loop with the corrected comparison was retained because it is easier to compare with the starting code.

**Result:**  
The corrected function returns `[50, 67, 82, 91]` for the sample data. It also includes a score exactly equal to the minimum, which is part of the intended behavior.

---

## Bug 3 – `bug3.js`

**AI Prompt:**  
"This code throws an error / doesn't behave as expected. Can you identify and explain the issue and how to fix it?"

**AI Diagnosis:**  
The function directly accesses `user.profile.name`. However, one object in the array has `profile: null`. JavaScript cannot read the `name` property of `null`, so it throws a `TypeError` and stops the `forEach` callback before all users are processed.

**Suggested Fix:**  
Check that the user, profile, and name are available before calling `toUpperCase()`. Return a fallback value when the data is missing.

**Corrected Code:**

```javascript
function getDisplayName(user) {
    if (!user || !user.profile || typeof user.profile.name !== "string") {
        return "Unknown";
    }
    return user.profile.name.toUpperCase();
}

const users = [
    { profile: { name: "Amina" } },
    { profile: null },
    { profile: { name: "Rashad" } }
];

users.forEach((user) => {
    console.log(getDisplayName(user));
});
```

**Alternative Fixes Tested:**  
Optional chaining (`user?.profile?.name`) can prevent an exception when a property is missing or null. However, the result still needs to be checked before calling `toUpperCase()`. The explicit validation above was selected because it also handles a missing or non-string name and provides a clear fallback.

**Result:**  
The corrected program processes all three users and prints `AMINA`, `Unknown`, and `RASHAD`. The null profile no longer stops the program.

---

## Bug 4 – `bug4.js`

**AI Prompt:**  
"This code throws an error / doesn't behave as expected. Can you identify and explain the issue and how to fix it?"

**AI Diagnosis:**  
The loop condition is `i <= items.length`. JavaScript array indexes start at `0`, so the last valid index is `items.length - 1`. When `i` equals `items.length`, the code accesses an element outside the array and prints `undefined`. This is an off-by-one error.

**Suggested Fix:**  
Change the loop condition from:

```javascript
i <= items.length
```

to:

```javascript
i < items.length
```

**Corrected Code:**

```javascript
function printItems(items) {
    console.log("Items in the list:");
    for (let i = 0; i < items.length; i++) {
        console.log(i + ": " + items[i]);
    }
    console.log("Finished printing items.");
}

const groceries = ["bread", "milk", "apples", "rice"];
printItems(groceries);
```

**Alternative Fixes Tested:**  
A `for...of` loop can also visit each item without manually managing an index. However, because the intended output includes each item's position, the indexed `for` loop is the clearer choice here.

**Result:**  
The corrected loop prints four items at indexes `0` through `3`. It does not attempt to access index `4`, so no `undefined` item is printed.

---

## Bug 5 – `bug5.c`

**AI Prompt:**  
"This code throws an error / doesn't behave as expected. Can you identify and explain the issue and how to fix it?"

**AI Diagnosis:**  
The element-count expression is reversed. `sizeof(values[0])` gives the size of one integer, while `sizeof(values)` gives the size of the complete array. Dividing the size of one element by the size of the whole array results in an integer value of `0` for this example. Consequently, the loop does not print any array elements.

**Suggested Fix:**  
Divide the total array size by the size of one element:

```c
int count = sizeof(values) / sizeof(values[0]);
```

**Corrected Code:**

```c
#include <stdio.h>

int main(void) {
    int values[] = {4, 8, 15, 16, 23, 42};
    int count = sizeof(values) / sizeof(values[0]);

    printf("Number of values: %d\n", count);
    printf("Array contents: ");

    for (int i = 0; i < count; i++) {
        printf("%d ", values[i]);
    }

    printf("\n");
    return 0;
}
```

**Alternative Fixes Tested:**  
The number of elements could be stored separately as a constant, but that creates a value that must be updated whenever the array changes. The `sizeof` calculation was retained because it calculates the element count directly for this array in the same scope.

**Result:**  
The corrected program reports `6` values and prints `4 8 15 16 23 42`. The loop visits every element.

---

## Overall Reflection

Using AI to debug these examples made it easier to understand not only what was wrong, but also why each issue occurred. The suggestions were useful starting points, but they still needed to be checked against the intended behavior. Testing the corrected versions was important because a change can remove an error without necessarily solving the original problem. Overall, AI was helpful for explaining errors and suggesting fixes, while testing provided the evidence that the fixes worked.
