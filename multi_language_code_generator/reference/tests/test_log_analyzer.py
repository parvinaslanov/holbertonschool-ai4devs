import pytest
from log_analyzer import LogAnalyzer

@pytest.fixture
def analyzer():
    return LogAnalyzer()

def test_empty_log(analyzer):
    result = analyzer.analyze([])
    assert result["total_requests"] == 0
    assert result["unique_visitors"] == 0
    assert result["error_rate_percentage"] == 0.0
    assert result["malformed_lines_count"] == 0

def test_whitespace_log(analyzer):
    result = analyzer.analyze(["   ", "\n", "\t"])
    assert result["total_requests"] == 0
    assert result["malformed_lines_count"] == 0

def test_single_valid_get_request(analyzer):
    line = '127.0.0.1 - - [10/Nov/2026:10:00:00 +0000] "GET /index.html HTTP/1.1" 200 1024'
    result = analyzer.analyze([line])
    assert result["total_requests"] == 1
    assert result["unique_visitors"] == 1
    assert result["error_rate_percentage"] == 0.0
    assert result["status_code_counts"] == {"200": 1}
    assert result["method_breakdown"] == {"GET": 1}
    assert result["top_paths"] == [{"path": "/index.html", "count": 1}]

def test_malformed_entry(analyzer):
    lines = [
        '127.0.0.1 - - [10/Nov/2026:10:00:00 +0000] "GET /index.html HTTP/1.1" 200 1024',
        'MALFORMED LOG LINE DATA'
    ]
    result = analyzer.analyze(lines)
    assert result["total_requests"] == 1
    assert result["malformed_lines_count"] == 1

def test_error_rate_calculation(analyzer):
    lines = [
        '10.0.0.1 - - [10/Nov/2026:10:00:00 +0000] "GET /success HTTP/1.1" 200 500',
        '10.0.0.2 - - [10/Nov/2026:10:01:00 +0000] "POST /notfound HTTP/1.1" 404 300',
        '10.0.0.3 - - [10/Nov/2026:10:02:00 +0000] "GET /servererror HTTP/1.1" 500 120'
    ]
    result = analyzer.analyze(lines)
    assert result["total_requests"] == 3
    assert result["error_rate_percentage"] == 66.67

def test_unique_visitors_counting(analyzer):
    lines = [
        '192.168.1.1 - - [10/Nov/2026:10:00:00 +0000] "GET /a HTTP/1.1" 200 100',
        '192.168.1.1 - - [10/Nov/2026:10:01:00 +0000] "GET /b HTTP/1.1" 200 100',
        '192.168.1.2 - - [10/Nov/2026:10:02:00 +0000] "GET /a HTTP/1.1" 200 100'
    ]
    result = analyzer.analyze(lines)
    assert result["unique_visitors"] == 2
