## Section 1 - PaymentProcessor::validate()

- **Plain English**: Validates credit card number and expiry.
- **Pattern**: Uses nested if-else instead of guard clauses.
- **Issues**: No logging, weak validation.
- **Improvements**: Replace with regex validation + unit tests.

## Section 2 - UserManager::authenticate()

- **Plain English**: Authenticates user credentials against the database.
- **Pattern**: Mixed database queries and response rendering inline.
- **Issues**: SQL injection vulnerability, unhashed password comparisons.
- **Improvements**: Use prepared statements and password hashing libraries.

## Section 3 - ReportGenerator::exportCSV()

- **Plain English**: Queries all user records and streams them directly into a raw CSV string output.
- **Pattern**: Procedural string concatenation with high memory overhead.
- **Issues**: Memory exhaustion (OOM) on large datasets without pagination.
- **Improvements**: Implement chunked streaming and buffered iterators.

## Section 4 - SessionManager::checkTimeout()

- **Plain English**: Checks if the user session has expired based on last activity timestamp stored in global state.
- **Pattern**: Relies on global mutable state and side effects within a conditional check.
- **Issues**: Race conditions in multi-threaded environments, difficult to mock in tests.
- **Improvements**: Encapsulate session state into a dedicated service class and inject dependencies.
