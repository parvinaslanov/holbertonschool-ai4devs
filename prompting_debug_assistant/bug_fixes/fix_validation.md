# Bug Fix Validation Report

## Bug 1 – bug1_fixed.py
- **Input**: [1,2,3,4,5], n=3  
- **Expected Output**: [3,4,5]  
- **Actual Output**: [3,4,5] ✅
- **Notes**: AI düzəlişinə əsasən mənfi indeksləmə (`lst[-n:]`) istifadə olundu və test uğurla keçdi.
