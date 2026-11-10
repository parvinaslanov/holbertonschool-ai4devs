# AI Review Log

## Overview
- **PR:** Add Task Filtering and Status Summary Endpoint (#42)
- **Review Personas Applied:** Security Engineer, Performance Specialist, Code Maintainability Architect
- **Total Comments Collected:** 10 (7 Inline Comments, 3 Global Feedback items)

---

## Inline Comments

1. **`api/routes.py` (Line 24) — [Security Persona]**
   - **Comment:** SQL injection risk detected in raw query parameter construction. User input from the `status` query string parameter is concatenated directly into the SQL string execution rather than using parameterized placeholders. To prevent arbitrary SQL execution, sanitize the input using bound parameter tuples (e.g., `cursor.execute(query, (status,))`).

2. **`tasks.py` (Line 42) — [Maintainability Persona]**
   - **Comment:** Non-descriptive single-letter parameter name `st` used in function signature. Variable names should clearly communicate intent to maintain readability across team members. Rename `st` to `status_filter` to comply with standard PEP 8 and project style guidelines.

3. **`tasks.py` (Line 58) — [Performance Persona]**
   - **Comment:** High risk of $O(N)$ memory overload under peak query loads. The `filter_tasks()` implementation currently fetches all records from the database into memory before filtering by `due_date` using Python list comprehensions. Shift the date filtering directly into the SQL `WHERE` clause so the database engine performs the operation efficiently.

4. **`api/routes.py` (Line 71) — [Security Persona]**
   - **Comment:** Unbounded limit and offset pagination parameters permit Denial of Service (DoS) exploits. A malicious actor could request `limit=1000000`, causing excessive server memory allocation and database timeouts. Enforce strict numerical bounds (e.g., `min=1, max=100`) and default values on all incoming pagination
