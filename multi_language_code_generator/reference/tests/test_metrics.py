import pytest
from log_analyzer import LogAnalyzer

@pytest.fixture
def analyzer():
    return LogAnalyzer()

def test_top_paths(analyzer):
    lines = [
        '1.1.1.1 - - [10/Nov/2026:10:00:00 +0000] "GET /pathA HTTP/1.1" 200 10',
        '1.1.1.1 - - [10/Nov/2026:10:01:00 +0000] "GET /pathB HTTP/1.1" 200 10',
        '1.1.1.1 - - [10/Nov/2026:10:02:00 +0000] "GET /pathA HTTP/1.1" 200 10'
    ]
    result = analyzer.analyze(lines)
    assert result["top_paths"][0]["path"] == "/pathA"
    assert result["top_paths"][0]["count"] == 2

def test_method_breakdown(analyzer):
    lines = [
        '1.1.1.1 - - [10/Nov/2026:10:00:00 +0000] "GET /api HTTP/1.1" 200 10',
        '1.1.1.1 - - [10/Nov/2026:10:01:00 +0000] "POST /api HTTP/1.1" 201 20'
    ]
    result = analyzer.analyze(lines)
    assert result["method_breakdown"] == {"GET": 1, "POST": 1}

def test_high_volume(analyzer):
    line = '192.168.1.10 - - [10/Nov/2026:12:00:00 +0000] "GET /status HTTP/1.1" 200 450'
    lines = [line for _ in range(50)]
    result = analyzer.analyze(lines)
    assert result["total_requests"] == 50
    assert result["unique_visitors"] == 1
    assert result["error_rate_percentage"] == 0.0
