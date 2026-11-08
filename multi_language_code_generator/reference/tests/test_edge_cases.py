import pytest
from log_analyzer import LogAnalyzer

@pytest.fixture
def analyzer():
    return LogAnalyzer()

def test_whitespace_only(analyzer):
    result = analyzer.analyze(["   ", "\n"])
    assert result["total_requests"] == 0
    assert result["malformed_lines_count"] == 0

def test_high_volume(analyzer):
    line = '192.168.1.10 - - [10/Nov/2026:12:00:00 +0000] "GET /status HTTP/1.1" 200 450'
    lines = [line for _ in range(50)]
    result = analyzer.analyze(lines)
    assert result["total_requests"] == 50
    assert result["unique_visitors"] == 1
    assert result["error_rate_percentage"] == 0.0
