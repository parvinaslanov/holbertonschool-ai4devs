# Bug Fix Validation Report

## Bug 1 – bug1_fixed.py
- **Input**: [1, 2, 3, 4, 5], n=3
- **Expected Output**: [3, 4, 5]
- **Actual Output**: [3, 4, 5] ✅
- **Notes**: Corrected list slicing logic using negative indexing `lst[-n:]` to handle boundary conditions properly.

## Bug 2 – bug2_fixed.py
- **Input**: "hello"
- **Expected Output**: "olleh"
- **Actual Output**: "olleh" ✅
- **Notes**: Applied standard python string slicing `s[::-1]` to safely reverse any valid input string.

## Bug 3 – bug3_fixed.py
- **Input**: [10, 20, 30, 40]
- **Expected Output**: 25.0
- **Actual Output**: 25.0 ✅
- **Notes**: Added check for empty input lists to avoid zero division error and return accurate float average.
