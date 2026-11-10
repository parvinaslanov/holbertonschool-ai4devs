# AI Review Log

## Overview
- **PR:** Add Task Filtering and Status Summary Endpoint (#42)
- **Review Personas Applied:** Security Engineer, Performance Specialist, Code Maintainability Architect
- **Total Comments Collected:** 10 (7 Inline Comments, 3 Global Feedback items)

---

## Inline Comments

1. **`api/routes.py` (Line 24) — [Security Persona]**
   - **Comment:** Unsanitized user input from `status` is directly concatenated into SQL query strings, creating a severe SQL injection vulnerability. Update the database call to use parameterized query bindings like `cursor.execute(query, (status,))` to properly sanitize inputs.

2. **`tasks.py` (Line 42) — [Maintainability Persona]**
   - **Comment:** The single-letter parameter `st` in the function signature is non-descriptive and reduces code readability. Rename `st` to `status_filter` across the module to adhere to project naming standards and PEP 8 guidelines.

3. **`tasks.py` (Line 58) — [Performance Persona]**
   - **Comment:** Filtering records in Python memory after fetching all database rows causes severe memory bottlenecks under heavy load. Move the due-date filter logic directly into the SQL `WHERE` clause so the database engine executes the query efficiently.

4. **`api/routes.py` (Line 71) — [Security Persona]**
   - **Comment:** The `limit` and `offset` pagination parameters lack maximum bound checks, exposing the endpoint to potential Denial of Service (DoS) attacks. Enforce explicit upper bounds such as `min=1, max=100` alongside default values for incoming query parameters.

5. **`models.py` (Line 103) — [Performance Persona]**
   - **Comment:** The database schema is missing an index on frequently queried columns used in filtering operations. Create a composite database index on `(status, due_date)` to prevent full table scans and maintain low query latency as dataset size grows.

6. **`tasks.py` (Line 118) — [Maintainability Persona]**
   - **Comment:** Calling `datetime.strptime()` without error catching will throw unhandled exceptions when clients send malformed date strings. Wrap date parsing in a `try-except ValueError` block to return a clean HTTP 400 response with descriptive error feedback.

7. **`tests/test_tasks.py` (Line 85) — [Maintainability Persona]**
   - **Comment:** The unit test `test_filter_by_status()` relies on hardcoded primary keys, making test runs fragile and dependent on execution order. Refactor assertions to validate dynamic entity
