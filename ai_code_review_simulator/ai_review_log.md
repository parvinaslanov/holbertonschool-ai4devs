## AI Review Log

### Inline Comments
- (line 15) [Security] Avoid hardcoding sensitive API keys or secrets directly in code; use environment variables instead.
- (line 42) [Maintainability] Variable `usr` should be renamed to `user` for clarity and readability.
- (line 78) [Performance] Unnecessary loop iteration over large dataset; consider using a hash map for $O(1)$ lookup time.
- (line 105) [Security] Input data passed to query is not sanitized; susceptible to SQL injection vulnerabilities.
- (line 120) [Maintainability] Add explicit type validation for the `status` parameter to prevent unexpected runtime errors.
- (line 164) [Performance] Database call inside a `for` loop detected; batch queries or preload relationships to avoid N+1 query issues.

### Global Feedback
- [Security] Ensure all endpoint handlers implement strict authentication checks and rate limiting to defend against brute-force attacks.
- [Performance] Implement caching (e.g., Redis) for frequently accessed, low-frequency write data to reduce database load.
- [Maintainability] Suggest adding robust error handling and logging for empty query results rather than returning implicit `null`.
- [Maintainability] Recommend splitting `filter_tasks()` into smaller, single-responsibility helper functions to improve testability.
