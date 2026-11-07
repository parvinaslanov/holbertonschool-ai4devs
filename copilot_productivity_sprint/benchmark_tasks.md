# Benchmark Tasks for Copilot Productivity Sprint

This document outlines the three standardized coding benchmark tasks designed to evaluate development velocity and quality across manual and AI-assisted workflows.

---

## Task 1 - REST API Endpoint with Input Validation
**Requirements**: Create a RESTful HTTP endpoint `POST /users` that validates incoming request payload schema (name and email), handles invalid inputs, and returns appropriate status codes.  
**Inputs**: JSON `{ "name": "string", "email": "string" }`  
**Outputs**: JSON `{ "id": "uuid-v4", "name": "string", "email": "string", "created_at": "ISO-8601 string" }`  
**Acceptance Criteria**:
- Returns `201 Created` with the newly assigned user object and valid UUID when data is valid.
- Returns `400 Bad Request` with an error message when the email format is invalid or required fields are missing.
- Includes automated unit tests asserting success and failure responses.

---

## Task 2 - Data Parsing and Transformation Pipeline
**Requirements**: Implement a data processing script that reads raw CSV records containing transaction data, filters out transactions under $10, converts currencies based on fixed rates, and calculates total sales by region.  
**Inputs**: CSV file with columns: `transaction_id`, `amount`, `currency`, `region`, `timestamp`  
**Outputs**: Structured JSON summary containing total aggregated revenue per region in USD and total valid transaction count.  
**Acceptance Criteria**:
- Successfully ignores malformed CSV rows and transactions below $10 threshold.
- Accurately converts non-USD amounts using standard rates (EUR to USD: 1.08, GBP to USD: 1.27).
- Returns aggregated result object sorted by region name alphabetically.

---

## Task 3 - Utility Function for Rate Limiting (Token Bucket)
**Requirements**: Write an in-memory Token Bucket rate limiter class/function that enforces request limits per client IP address.  
**Inputs**: `client_ip` (string), `max_tokens` (integer), `refill_rate` (tokens per second)  
**Outputs**: Boolean `true` if request is allowed, `false` if rate limit is exceeded.  
**Acceptance Criteria**:
- Consumes 1 token per request and refills tokens at the defined rate over time.
- Returns `true` and allows execution if tokens are available.
- Returns `false` immediately when bucket is empty.
- Unit tests verify time-based token refills correctly using mock timers/clocks.
