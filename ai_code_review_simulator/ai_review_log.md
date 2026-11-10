## AI Review Log

### Inline Comments
- (line 24) [Security] Severity: High. Issue: Unsanitized `status` input is concatenated into raw SQL, creating an injection vulnerability. Action: Use parameterized bindings like `cursor.execute(query, (status,))` to sanitize inputs properly.
- (line 42) [Maintainability] Severity: Low. Issue: Single-letter parameter name `st` reduces code readability and breaks style guidelines. Action: Rename `st` to `status_filter` across the codebase to ensure consistency.
- (line 58) [Performance] Severity: High. Issue: In-memory filtering after fetching all DB rows causes severe memory bottlenecks. Action: Move due-date filtering directly into the SQL `WHERE` clause for execution efficiency.
- (line 71) [Security] Severity: Medium. Issue: Unbounded pagination parameters expose the endpoint to Denial of Service attacks. Action: Enforce explicit numerical bounds such as `min=1, max=100` on input parameters.
- (line 103) [Performance] Severity: Medium. Issue: Unindexed filter columns trigger expensive full table scans as dataset size grows. Action: Create a composite database index on `(status, due_date)` to optimize lookup speed.
- (line 118) [Maintainability] Severity: Medium. Issue: Calling `datetime.strptime()` without error handling crashes on malformed input strings. Action: Wrap parsing logic in a `try-except ValueError` block to return HTTP 400 errors.
- (line 85) [Maintainability] Severity: Low. Issue: Test `test_filter_by_status()` relies on static primary keys, causing test run fragility. Action: Assert dynamic entity attributes instead of hardcoded database IDs.

### Global Feedback
- [Security] Severity: High. Issue: Request parameter validation logic is fragmented across multiple route handlers. Action: Implement Pydantic schemas to validate and sanitize incoming payloads before reaching business logic.
- [Maintainability] Severity: Medium. Issue: Function `filter_tasks()` violates single-responsibility by combining query building and execution. Action: Split logic into `build_filter_query()` and `execute_paginated_query()` methods to improve testability.
- [Performance] Severity: Medium. Issue: Querying non-existent datasets causes unhandled `NoneType` crashes during metadata calculation. Action: Update exception handlers to return an HTTP 200 containing `[]` and zeroed metadata counts.
