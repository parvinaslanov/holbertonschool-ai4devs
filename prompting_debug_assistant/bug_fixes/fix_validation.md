# Fix Validation

The five corrected programs were executed and checked. Python functions were also tested with assertions. The JavaScript files were run with Node.js, and the C file was compiled with GCC using warnings treated as errors.

## Bug 1 – `bug1_fixed.py`

- **Issue addressed:** Empty input could cause division by zero.
- **Test 1 input:** `[78, 85, 92, 66]`
- **Expected:** `80.25`
- **Actual:** `80.25` — PASS
- **Test 2 input:** `[]`
- **Expected:** `0`
- **Actual:** `0` — PASS
- **Additional check:** The average function returned the expected result for both tests using Python assertions.

## Bug 2 – `bug2_fixed.py`

- **Issue addressed:** The passing-score filter must include scores equal to the minimum.
- **Test 1 input:** `[32, 50, 67, 49, 82, 91]`, minimum `50`
- **Expected:** `[50, 67, 82, 91]`
- **Actual:** `[50, 67, 82, 91]` — PASS
- **Test 2 input:** `[]`, minimum `50`
- **Expected:** `[]`
- **Actual:** `[]` — PASS
- **Test 3 input:** `[49, 50, 51]`, minimum `50`
- **Expected:** `[50, 51]`
- **Actual:** `[50, 51]` — PASS

## Bug 3 – `bug3_fixed.js`

- **Issue addressed:** Accessing `city` when a user's `profile` is `null` can throw a runtime error.
- **Test input:** Three users, including one whose `profile` is `null`.
- **Expected output:**
  - `Amina: Baku`
  - `Murad: Unknown`
  - `Rashad: Ganja`
- **Actual output:** Matched all three expected lines — PASS
- **Validation:** Executed with Node.js. Optional chaining and nullish coalescing provide a safe fallback.

## Bug 4 – `bug4_fixed.js`

- **Issue addressed:** The loop must not read beyond the end of the array.
- **Test input:** `["apple", "banana", "cherry", "date"]`
- **Expected output:** Each item printed exactly once and in the original order.
- **Actual output:** `apple`, `banana`, `cherry`, `date` — PASS
- **Validation:** Executed with Node.js. The loop condition `i < items.length` keeps the index within valid bounds.

## Bug 5 – `bug5_fixed.c`

- **Issue addressed:** The array element count must be calculated rather than hard-coded.
- **Test input:** `{2, 4, 6, 8, 10, 12}`
- **Expected output:** `Count: 6`, followed by all six values.
- **Actual output:** Count and values matched the expected output — PASS
- **Validation:** Compiled with GCC using `-std=c11 -Wall -Wextra -Werror`, then executed successfully.

## Overall result

All five supplied corrected files executed successfully in the available test environment. The Python edge cases passed assertions, both JavaScript programs ran successfully with Node.js, and the C program compiled without warnings and produced the expected output.

These checks cover the test cases documented above; they do not prove correctness for every possible input.
