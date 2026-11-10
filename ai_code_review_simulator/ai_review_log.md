## AI Review Log

### Inline Comments
- (line 24) [Security] Unsanitized `status` input creates a severe SQL injection vulnerability. Update database calls to use parameterized bindings like `cursor.execute(query, (status,))` to sanitize inputs properly.
- (line 42) [Maintainability] Single-letter parameter `st` reduces code readability. Rename `st` to `status_filter` to follow standard project and PEP 8 guidelines.
- (line 58) [Performance] In-memory filtering after fetching all DB rows causes severe memory bottlenecks. Move due-date filtering directly into SQL `WHERE` clauses for efficiency.
- (line 71) [Security] Unbounded pagination parameters expose the endpoint to DoS attacks. Enforce explicit upper bounds such as `min=1, max=100` on input parameters.
- (line 103) [Performance] Unindexed filter columns trigger full table scans as dataset grows. Create a composite database index on `(status, due_date)` to improve query speed.
- (line 118) [Maintainability] Calling `datetime.strptime()` without catching errors crashes on malformed inputs. Wrap parsing in `try-except ValueError` returning HTTP 400.
- (line 85) [Maintainability] Test `test_filter_by_status()` relies on hardcoded primary keys (`id=1`). Assert dynamic entity attributes instead of static IDs to fix fragility.

### Global Feedback
- [Security] Request parameter validation is fragmented across handlers. Implement Pydantic schemas to validate and sanitize incoming payloads before reaching business logic.
- [Maintainability] `filter_tasks()` handles both query building and execution. Split logic into `build_filter_query()` and `execute_paginated_query()` methods to improve testability.
- [Performance] Empty query result sets crash with unhandled `NoneType` errors. Update exception handlers to return an HTTP 200 containing `[]` and zeroed metadata.
