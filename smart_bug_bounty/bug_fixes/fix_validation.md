# Fix Validation

## bug1.py
- **Original Issue**: Off-by-one slicing error in `get_last_n_items` and unhandled `ZeroDivisionError` in `calculate_average`.
- **Fix Applied**: Adjusted slice syntax to `items[-n:]` and added `count == 0` check returning `0.0`.
- **Test Results**: All 3 test cases passed.

## bug2.js
- **Original Issue**: `fetchUserData` returned `null` synchronously; `processPrices` had an off-by-one loop condition causing `NaN` values.
- **Fix Applied**: Wrapped asynchronous timeout in a `Promise` returning resolved data; adjusted loop constraint to `i < prices.length`.
- **Test Results**: All 3 test cases passed.

## bug3.java
- **Original Issue**: List element skipping during forward loop deletion and string reference comparison using `==`.
- **Fix Applied**: Replaced manual loop with `removeIf` predicate and updated string comparison to `.equals()`.
- **Test Results**: All 3 test cases passed.

## bug4.cpp
- **Original Issue**: Memory leak caused by heap-allocated array not being freed before function return.
- **Fix Applied**: Inserted `delete[] data;` prior to function termination.
- **Test Results**: All 3 test cases passed.

## bug5.py
- **Original Issue**: State retention across invocations due to mutable default list argument `cache=[]` and unhandled `KeyError` on dictionary key access.
- **Fix Applied**: Changed default parameter value to `cache=None` initializing a new list inside function body; switched to `user_dict.get("age", None)`.
- **Test Results**: All 3 test cases passed.
