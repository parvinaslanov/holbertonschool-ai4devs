# Bug Descriptions

## bug1.py
- **Intended Behavior**: `get_last_n_items` should return the last `n` items from a list, and `calculate_average` should safely calculate the average of non-negative numbers.
- **Current Issue**: `get_last_n_items` contains an off-by-one slicing error (`len(items) - n + 1`), returning `n-1` elements. `calculate_average` triggers an unhandled `ZeroDivisionError` when given a list with no non-negative numbers.

## bug2.js
- **Intended Behavior**: `fetchUserData` should asynchronously fetch and return user details. `processPrices` should apply a discount to every price in an array.
- **Current Issue**: `fetchUserData` returns `null` synchronously before `setTimeout` populates data. `processPrices` uses an off-by-one loop condition (`i <= prices.length`), executing out-of-bounds and appending `NaN`.

## bug3.java
- **Intended Behavior**: `removeOddNumbers` should purge all odd numbers from an `ArrayList`. `checkAccountName` should evaluate whether two string objects represent identical text values.
- **Current Issue**: `removeOddNumbers` mutates the list while iterating forward, causing adjacent odd numbers to be skipped. `checkAccountName` compares reference equality (`==`) instead of string values (`.equals()`).

## bug4.cpp
- **Intended Behavior**: Allocate memory dynamically for an array, sum its elements, and deallocate the memory before exiting.
- **Current Issue**: Memory leak caused by omitting `delete[] data` prior to the function returning.

## bug5.py
- **Intended Behavior**: `append_to_cache` should initialize a clean list when no target list is passed. `parse_user_age` should safely retrieve a user's age attribute.
- **Current Issue**: `append_to_cache` uses a mutable default argument (`cache=[]`), persisting state between calls. `parse_user_age` raises an unhandled `KeyError` if the `"age"` key is missing.
