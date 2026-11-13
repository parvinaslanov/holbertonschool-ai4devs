# Translation Guide - Log Analyzer

## Python → Go
- **List comprehensions** → Idiomatic `for` loops with explicit slice allocations.
- **Dicts** → Strongly typed maps (`map[string]int`, `map[string]interface{}`).
- **Exceptions** → Explicit multi-value returns (`(result, error)` or status codes) rather than `try/except` blocks.

## Python → Rust
- **Dynamic typing** → Strict static typing with enums/structs to handle polymorphic return types.
- **Garbage Collection (GC)** → Ownership model and affine type system managing memory safety at compile-time.
- **Iterators** → Borrow checker rules and explicit reference lifetimes.

## Common Pitfalls
- **Type Mismatches**: Ensuring numerical types (`total_requests` as integer vs float) maintain exact structural schemas across languages.
- **String Slicing & Parsing**: Handling whitespace, blank lines, and empty payloads consistently across runtime environments.

## Best Practices
- Define uniform API signatures and return dictionary schemas early.
- Reuse identical test datasets and edge-case criteria across all implementations to verify true functional equivalence.
