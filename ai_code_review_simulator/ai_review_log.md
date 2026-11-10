# AI Review Log

## Overview
- **PR:** Add Task Filtering and Status Summary Endpoint (#42)
- **Review Personas Applied:** Security Engineer, Performance Specialist, Code Maintainability Architect
- **Total Comments Collected:** 10 (7 Inline Comments, 3 Global Feedback items)

---

## Inline Comments

1. **`api/routes.py` (Line 24) — [Security Persona]**
   - **Comment:** SQL injection risk detected in parameter parsing. User input from `status` is concatenated into raw query strings rather than using parameterized bindings. Sanitize inputs using bound parameter tuples (e.g., `cursor.execute(query, (status,))`).

2. **`tasks.py` (Line 42) — [Maintainability Persona]**
   - **Comment:** Non-descriptive single-letter parameter name `st` used in signature. Rename `st` to `status_filter` to improve readability and adhere to PEP 8 guidelines.

3. **`tasks.py` (Line 58) — [Performance Persona]**
   - **Comment:** High risk of memory overload under heavy query loads. The function currently fetches all database records before filtering dates in Python memory. Shift date filtering directly into SQL `WHERE` clauses for database efficiency.

4. **`api/routes.py` (Line 71) — [Security Persona]**
   - **Comment:** Unbounded pagination parameters permit Denial of Service (DoS) exploits. An attacker requesting `limit=1000000` causes excessive server memory allocation. Enforce strict numerical bounds (`min=1, max=100`) on pagination parameters.

5. **`models.py` (Line 103) — [Performance Persona]**
   - **Comment:** Missing composite index on frequently queried filter columns. Querying unindexed columns triggers full table scans as dataset size grows. Add a composite database index on `(status, due_date)` to optimize lookup speed.

6. **`tasks.py` (Line 118) — [Maintainability Persona]**
   - **Comment:** Unhandled type conversion error risk during string parsing. Calling `datetime.strptime()` without exception handling causes crashes on invalid inputs. Wrap parsing in a `try-except ValueError` block returning standard HTTP 400 errors.

7. **`tests/test_tasks.py` (Line 85) — [Maintainability Persona]**
   - **Comment:** Fragile test assertions dependent on static primary keys. `test_filter_by_status()` relies on fixed IDs (`id=1`), breaking when execution order shifts. Inspect dynamic entity attributes instead of hardcoded database IDs.

---

## Global Feedback

1. **Security & Validation Architecture — [Security Persona]**
   - **Feedback:** Parameter validation is currently fragmented across multiple controller functions. Centralize endpoint query parsing into Pydantic models to guarantee invalid types and unsafe payloads are rejected early.

2. **Refactoring & Modular Design — [Maintainability Persona]**
   - **Feedback:** `filter_tasks()` violates single-responsibility principles by handling query building and execution together. Split logic into `build_filter_query()` and `execute_paginated_query()` methods to streamline testing and readability.

3. **Error Handling & Edge Cases — [Performance & Stability Persona]**
   - **Feedback:** The API fails on empty query results by throwing unhandled `NoneType` errors. Update exception handlers to return an HTTP 200 OK containing `[]` and zeroed summary metadata.
