import pytest
from log_analyzer import LogAnalyzer

@pytest.fixture
def analyzer():
    return LogAnalyzer()

def test_empty_log(analyzer):
    """Test Case 1: Empty log file returns zero metrics."""
    result = analyzer.analyze([])
    assert result["total_requests"] == 0
    assert result["unique_visitors"] == 0
    assert result["error_rate_percentage"] == 0.0
    assert result["malformed_lines_count"] == 0

def test_whitespace_log(analyzer):
    """Test Case 2: Log with only whitespace lines."""
    result = analyzer.analyze(["   ", "\n", "\t"])
    assert result["total_requests"] == 0
    assert result["malformed_lines_count"] == 0

def test_single_valid_get_request(analyzer):
    """Test Case 3: Single valid GET request parsing."""
    line = '127.0.0.1 - - [10/Nov/2026:10:00:00 +0000] "GET /index.html HTTP/1.1" 200 1024'
    result = analyzer.analyze([line])
    assert result["total_requests"] == 1
    assert result["unique_visitors"] == 1
    assert result["error_rate_percentage"] == 0.0
    assert result["status_code_counts"] == {"200": 1}
    assert result["method_breakdown"] == {"GET": 1}
    assert result["top_paths"] == [{"path": "/index.html", "count": 1}]

def test_malformed_entry(analyzer):
    """Test Case 4: Malformed lines are caught and counted."""
    lines = [
        '127.0.0.1 - - [10/Nov/2026:10:00:00 +0000] "GET /index.html HTTP/1.1" 200 1024',
        'MALFORMED LOG LINE DATA'
    ]
    result = analyzer.analyze(lines)
    assert result["total_requests"] == 1
    assert result["malformed_lines_count"] == 1

def test_error_rate_calculation(analyzer):
    """Test Case 5: Correct error rate computation for 4xx/5xx status codes."""
    lines = [
        '10.0.0.1 - - [10/Nov/2026:10:00:00 +0000] "GET /success HTTP/1.1" 200 500',
        '10.0.0.2 - - [10/Nov/2026:10:01:00 +0000] "POST /notfound HTTP/1.1" 404 300',
        '10.0.0.3 - - [10/Nov/2026:10:02:00 +0000] "GET /servererror HTTP/1.1" 500 120'
    ]
    result = analyzer.analyze(lines)
    assert result["total_requests"] == 3
    assert result["error_rate_percentage"] == 66.67 # 2 out of 3 errors

def test_unique_visitors_counting(analyzer):
    """Test Case 6: Unique visitor calculation across shared IPs."""
    lines = [
        '192.168.1.1 - - [10/Nov/2026:10:00:00 +0000] "GET /a HTTP/1.1" 200 100',
        '192.168.1.1 - - [10/Nov/2026:10:01:00 +0000] "GET /b HTTP/1.1" 200 100',
        '192.168.1.2 - - [10/Nov/2026:10:02:00 +0000] "GET /a HTTP/1.1" 200 100'
    ]
    result = analyzer.analyze(lines)
    assert result["unique_visitors"] == 2

def test_top_paths_ranking(analyzer):
    """Test Case 7: Top 3 paths ordered by request frequency."""
    lines = [
        '1.1.1.1 - - [10/Nov/2026:10:00:00 +0000] "GET /pathA HTTP/1.1" 200 10',
        '1.1.1.1 - - [10/Nov/2026:10:01:00 +0000] "GET /pathB HTTP/1.1" 200 10',
        '1.1.1.1 - - [10/Nov/2026:10:02:00 +0000] "GET /pathA HTTP/1.1" 200 10',
        '1.1.1.1 - - [10/Nov/2026:10:03:00 +0000] "GET /pathC HTTP/1.1" 200 10',
        '1.1.1.1 - - [10/Nov/2026:10:04:00 +0000] "GET /pathC HTTP/1.1" 200 10',
        '1.1.1.1 - - [10/Nov/2026:10:05:00 +0000] "GET /pathC HTTP/1.1" 200 10',
    ]
    result = analyzer.analyze(lines)
    top_paths = result["top_paths"]
    assert top_paths[0]["path"] == "/pathC" and top_paths[0]["count"] == 3
    assert top_paths[1]["path"] == "/pathA" and top_paths[1]["count"] == 2
    assert top_paths[2]["path"] == "/pathB" and top_paths[2]["count"] == 1

def test_method_breakdown(analyzer):
    """Test Case 8: Breakdown of multiple HTTP methods."""
    lines = [
        '1.1.1.1 - - [10/Nov/2026:10:00:00 +0000] "GET /api HTTP/1.1" 200 10',
        '1.1.1.1 - - [10/Nov/2026:10:01:00 +0000] "POST /api HTTP/1.1" 201 20',
        '1.1.1.1 - - [10/Nov/2026:10:02:00 +0000] "DELETE /api/1 HTTP/1.1" 204 0'
    ]
    result = analyzer.analyze(lines)
    assert result["method_breakdown"] == {"GET": 1, "POST": 1, "DELETE": 1}

def test_status_code_aggregation(analyzer):
    """Test Case 9: Proper grouping of diverse status codes."""
    lines = [
        '1.1.1.1 - - [10/Nov/2026:10:00:00 +0000] "GET / HTTP/1.1" 200 10',
        '1.1.1.1 - - [10/Nov/2026:10:01:00 +0000] "GET / HTTP/1.1" 200 10',
        '1.1.1.1 - - [10/Nov/2026:10:02:00 +0000] "GET /404 HTTP/1.1" 404 10'
    ]
    result = analyzer.analyze(lines)
    assert result["status_code_counts"] == {"200": 2, "404": 1}

def test_high_volume_stress_batch(analyzer):
    """Test Case 10: Performance and correctness on a batch of 100 identical lines."""
    line = '192.168.1.10 - - [10/Nov/2026:12:00:00 +0000] "GET /status HTTP/1.1" 200 450'
    lines = [line for _ in range(100)]
    result = analyzer.analyze(lines)
    assert result["total_requests"] == 100
    assert result["unique_visitors"] == 1
    assert result["error_rate_percentage"] == 0.0
    assert result["top_paths"][0]["count"] == 100
