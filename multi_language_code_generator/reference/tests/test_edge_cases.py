import pytest
from log_analyzer import LogAnalyzer

@pytest.fixture
def analyzer():
    return LogAnalyzer()

def test_whitespace_only(analyzer):
    result = analyzer.analyze(["   ", "\n"])
    assert result["total_requests"] == 0
    assert result["malformed_lines_count"] == 0

def test_malformed_count(analyzer):
    lines = [
        '1.1.1.1 - - [10/Nov/2026:10:00:00 +0000] "GET /api HTTP/1.1" 200 10',
        'INVALID LINE'
    ]
    result = analyzer.analyze(lines)
    assert result["malformed_lines_count"] == 1
    assert result["total_requests"] == 1
