# AI Review Log

## Overview
- **PR:** Add Task Filtering and Status Summary Endpoint (#42)
- **Review Personas Applied:** Security Engineer, Performance Specialist, Code Maintainability Architect
- **Total Comments Collected:** 10 (7 Inline Comments, 3 Global Feedback items)

---

## Inline Comments

1. **`api/routes.py` (Line 24) — [Security Persona]**
   - *Comment:* SQL injection risk detected in parameter parsing. User input from `status` query param is interpolated directly into query execution instead of using parameterized bindings. Pass filter values as parameter tuples.

2. **`tasks.py` (Line 42) — [Maintainability Persona]**
   - *Comment:* Non-descriptive parameter name `st`. Rename `st` to `status_filter` for consistency with codebase style guidelines.

3. **`tasks.py` (Line 58) — [Performance Persona]**
   - *Comment:* Potential $O(N)$ memory overload. `filter_tasks()` loads all matching DB records into memory before applying date filtering in Python. Move the due-date clause directly into the database query statement.

4. **`api/routes.py` (Line 71) — [Security Persona]**
   - *Comment:* Input validation missing. The `limit` and `offset` query parameters are not sanitized or bounded, allowing negative values or excessively large limits (`limit=1000000`) that could cause a Denial of Service (DoS).

5. **`models.py` (Line 103) — [Performance Persona]**
   - *Comment:* Missing database index. Filtering on `status` and `due_date` will trigger full table scans as dataset grows. Add a composite index on `(status, due_date)`.

6. **`tasks.py` (Line 118) — [Maintainability Persona]**
   - *Comment:* Unhandled type error risk. Explicit conversion `datetime.strptime(due_date, "%Y-%m-%d")` lacks a `try-except ValueError` block, causing unhandled 500 errors on invalid date format input.

7. **`tests/test_tasks.py` (Line 85) — [Maintainability Persona]**
   - *
