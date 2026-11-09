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
