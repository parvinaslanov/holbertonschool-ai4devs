# Cross-Language Specification - API Request Log Analyzer

## 1. Algorithm Description
The **API Request Log Analyzer** parses standard Apache/Nginx Combined Log Format files to extract, aggregate, and compute key performance and security metrics. 

The algorithm processes each line sequentially, extracts key components (Client IP, Timestamp, HTTP Method, Request Path, HTTP Status Code, Response Size, Referrer, and User-Agent), filters out malformed lines gracefully, and computes the following metrics:
- **Total Requests:** Total number of valid parsed log entries.
- **Unique Visitors:** Count of distinct client IP addresses.
- **Error Rate:** Percentage of requests resulting in client errors (4xx) or server errors (5xx) relative to total requests.
- **Top Paths:** The top 3 most frequently requested URL paths.
- **Method Breakdown:** Request counts categorized by HTTP method (GET, POST, PUT, DELETE, etc.).

---

## 2. Input Format
Plain text log file where each line conforms (or attempts to conform) to the **Combined Log Format**:
```text
<client_ip> - - [<timestamp>] "<method> <path> <http_version>" <status_code> <bytes> "<referrer>" "<user_agent>"
