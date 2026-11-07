# Bug Fix Validation Report

## Bug 1 – bug1_fixed.py
- **Input**: [1,2,3,4,5], n=3  
- **Expected Output**: [3,4,5]  
- **Actual Output**: [3,4,5] ✅
- **Notes**: Mənfi indeksləmə (`lst[-n:]`) istifadə olunaraq son `n` element qaytarıldı.

## Bug 2 – bug2_fixed.py
- **Input**: "hello"  
- **Expected Output**: "olleh"  
- **Actual Output**: "olleh" ✅
- **Notes**: Slicing step `-1` istifadə olunaraq mətn tərsinə çevrildi.

## Bug 3 – bug3_fixed.py
- **Input**: [10, 20, 30, 40]  
- **Expected Output**: 25.0  
- **Actual Output**: 25.0 ✅
- **Notes**: Boş siyahı xətasının qarşısını almaq üçün şərt əlavə olundu və ədədi orta hesablandı.
