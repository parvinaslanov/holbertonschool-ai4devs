# Fix Validation

I tested each corrected file using the example inputs and additional edge cases where appropriate. The results below reflect the tests run on these files.

## Bug 1 – `bug1_fixed.py`

- **Test 1 input:** `[78, 85, 92, 66]`
- **Expected output:** `80.25`
- **Actual output:** `80.25` ✅
- **Test 2 input:** `[]`
- **Expected output:** `0` (handles an empty list without dividing by zero)
- **Actual output:** `0` ✅
- **Result:** PASS

## Bug 2 – `bug2_fixed.py`

- **Test input:** `[32, 50, 67, 49, 82, 91]`, minimum score `50`
- **Expected output:** `[50, 67, 82, 91]`
- **Actual output:** `[50, 67, 82, 91]` ✅
- **Result:** PASS

## Bug 3 – `bug3_fixed.js`

- **Test input:** Three users; the second user's `profile` is `null`.
- **Expected output:**
  - `Amina: Baku`
  - `Murad: Unknown`
  - `Rashad: Ganja`
- **Actual output:**
  - `Amina: Baku`
  - `Murad: Unknown`
  - `Rashad: Ganja` ✅
- **Result:** PASS. Optional chaining and a fallback value prevent the null-property runtime error.

## Bug 4 – `bug4_fixed.js`

- **Test input:** `["apple", "banana", "cherry", "date"]`
- **Expected output:** Each of the four items printed once, in order.
- **Actual output:**
  - `apple`
  - `banana`
  - `cherry`
  - `date` ✅
- **Result:** PASS. The loop stops when `i` is less than `items.length`, so it does not access an out-of-range index.

## Bug 5 – `bug5_fixed.c`

- **Test input:** `{2, 4, 6, 8, 10, 12}`
- **Expected output:** Count `6`, followed by all six values.
- **Actual output:**
  - `Count: 6`
  - `2`
  - `4`
  - `6`
  - `8`
  - `10`
  - `12` ✅
- **Result:** PASS. The array length is calculated using `sizeof(values) / sizeof(values[0])`.

## Overall result

All five corrected files passed the tests listed above. No manual changes beyond the documented fixes were needed for these test cases. These tests verify the stated examples; they do not guarantee that every possible input has been tested.
