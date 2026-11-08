import pytest
from log_analyzer import LogAnalyzer

def test_single_valid_get_request():
    analyzer = LogAnalyzer()
    line = '127.0.0.1 - - [10/Nov/2026:10:00:00 +0000] "GET /index.html HTTP/1.1" 200 1024'
    result = analyzer.analyze([line])
    assert result["total_requests"] == 1
