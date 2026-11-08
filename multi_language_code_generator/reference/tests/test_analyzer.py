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

def test_single_request(analyzer):
    line = '127.0.0.1 - - [10/Nov/2026:10:00:00 +0000] "GET /index.html HTTP/1.1" 200 1024'
    result = analyzer.analyze([line])
    assert result["total_requests"] == 1
    assert result["unique_visitors"] == 1
    assert result["error_rate_percentage"] == 0.0

def test_error_rate(analyzer):
    lines = [
        '10.0.0.1 - - [10/Nov/2026:10:00:00 +0000] "GET /success HTTP/1.1" 200 500',
        '10.0.0.2 - - [10/Nov/2026:10:01:00 +0000] "POST /notfound HTTP/1.1" 404 300'
    ]
    result = analyzer.analyze(lines)
    assert result["total_requests"] == 2
    assert result["error_rate_percentage"] == 50.0

def test_unique_visitors(analyzer):
    lines = [
        '192.168.1.1 - - [10/Nov/2026:10:00:00 +0000] "GET /a HTTP/1.1" 200 100',
        '192.168.1.1 - - [10/Nov/2026:10:01:00 +0000] "GET /b HTTP/1.1" 200 100',
        '192.168.1.2 - - [10/Nov/2026:10:02:00 +0000] "GET /a HTTP/1.1" 200 100'
    ]
    result = analyzer.analyze(lines)
    assert result["unique_visitors"] == 2
