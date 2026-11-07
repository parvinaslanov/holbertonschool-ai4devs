# Fix Validation

All five supplied corrected source files were executed in this environment. Python 3, Node.js, and GCC were available.

## Bug 1 – `bug1_fixed.py`

- **Command:** `python3 bug1_fixed.py`
- **Input:** `[78, 85, 92, 66]` and `[]` (as defined in the file)
- **Expected output:**
  ```text
  80.25
  0
  ```
- **Actual output:**
  ```text
  80.25
  0
  ```
- **Additional assertions:** `calculate_average([1, 2, 3]) == 2`, `calculate_average([]) == 0`, and `calculate_average([-2, 2]) == 0`.
- **Result:** PASS. The script and all additional assertions exited successfully.

## Bug 2 – `bug2_fixed.py`

- **Command:** `python3 bug2_fixed.py`
- **Input:** `[32, 50, 67, 49, 82, 91]`, minimum score `50` (default)
- **Expected output:**
  ```text
  [50, 67, 82, 91]
  ```
- **Actual output:**
  ```text
  [50, 67, 82, 91]
  ```
- **Additional assertions:** Verified the example input, an empty list, a custom threshold of `15`, and inclusion of a score exactly equal to the minimum.
- **Result:** PASS. The script and all additional assertions exited successfully.

## Bug 3 – `bug3_fixed.js`

- **Command:** `node bug3_fixed.js`
- **Input:** Three users; the second user's `profile` is `null`.
- **Expected output:**
  ```text
  Amina: Baku
  Murad: Unknown
  Rashad: Ganja
  ```
- **Actual output:**
  ```text
  Amina: Baku
  Murad: Unknown
  Rashad: Ganja
  ```
- **Result:** PASS. Optional chaining and the nullish-coalescing fallback handle the missing profile without a runtime error.

## Bug 4 – `bug4_fixed.js`

- **Command:** `node bug4_fixed.js`
- **Input:** `["apple", "banana", "cherry", "date"]`
- **Expected output:**
  ```text
  apple
  banana
  cherry
  date
  ```
- **Actual output:**
  ```text
  apple
  banana
  cherry
  date
  ```
- **Result:** PASS. Each item is printed once, in order, and the loop terminates at `items.length`.

## Bug 5 – `bug5_fixed.c`

- **Compile command:** `gcc -std=c11 -Wall -Wextra -Werror bug5_fixed.c -o bug5_test`
- **Run command:** `./bug5_test`
- **Input:** `{2, 4, 6, 8, 10, 12}`
- **Expected output:**
  ```text
  Count: 6
  2
  4
  6
  8
  10
  12
  ```
- **Actual output:**
  ```text
  Count: 6
  2
  4
  6
  8
  10
  12
  ```
- **Result:** PASS. Compilation succeeded with warnings treated as errors, and the executable produced the expected output.

## Overall result

**5/5 source files passed their execution checks.** The two Python files also passed the listed additional assertions. The C file compiled cleanly with `-Wall -Wextra -Werror`.

**Environment note:** The Python runtime emitted a spreadsheet warm-up diagnostic on standard error during startup. It did not cause a non-zero exit status or change the programs' standard output. No changes to the supplied source files were needed. The validation report was updated to reflect tests actually run in this environment.
