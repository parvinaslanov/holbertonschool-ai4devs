import pytest
from log_analyzer import LogAnalyzer

@pytest.fixture
def analyzer():
    return LogAnalyzer()

def test_parse_valid_line(analyzer):
    line = '127.0.0.1 - - [10/Nov/2026:10:00:00 +0000] "GET /index.html HTTP/1.1" 200 1024'
    parsed = analyzer.parse_line(line)
    assert parsed is not None
    assert parsed["ip"] == "127.0.0.1"
    assert parsed["method"] == "GET"
    assert parsed["path"] == "/index.html"
    assert parsed["status"] == 200

def test_parse_malformed_line(analyzer):
    line = "INVALID LOG LINE DATA"
    parsed = analyzer.parse_line(line)
    assert parsed is None
