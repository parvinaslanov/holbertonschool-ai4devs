# Cross-Language Specification - API Request Log Analyzer

## Algorithm Description
The API Request Log Analyzer parses standard Apache/Nginx Combined Log Format files to extract, aggregate, and compute key performance and security metrics. The algorithm processes each line sequentially, extracts components like Client IP, Method, Path, and Status Code, filters out malformed lines gracefully, and computes total requests, unique visitors, error rates, top paths, and method breakdowns.

## Inputs
- Sample log files (plain text files containing standard log entries).

## Outputs
- JSON format with statistics including total requests, unique visitors, error rate percentage, status code counts, method breakdown, and top paths.

## Edge Cases
1. Empty File: File is 0 bytes or contains only whitespace.
2. Malformed Entry: Lines missing quotes, containing invalid formats, or missing status codes.
3. Missing Optional Fields: Lines with missing or hyphenated referrers or user-agents.
4. Extremely Large Files: Handled via streaming/line-by-line reading.

## Test Cases
- log_small.txt -> 100 requests, 20 errors
- log_empty.txt -> 0 requests
- log_malformed.txt -> 7 valid requests, 3 malformed entries
- log_errors.txt -> 50 requests, 100.0 percent error rate
- log_ranking.txt -> 3 unique visitors, correct path ranking
