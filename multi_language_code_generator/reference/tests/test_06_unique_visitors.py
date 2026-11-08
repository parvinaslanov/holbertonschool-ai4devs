import pytest
from log_analyzer import LogAnalyzer

def test_unique_visitors_counting():
    analyzer = LogAnalyzer()
    lines = [
        '192.168.1.1 - - [10/Nov/2026:10:00:00 +0000] "GET /a HTTP/1.1" 200 100',
        '192.168.1.1 - - [10/Nov/2026:10:01:00 +0000] "GET /b HTTP/1.1" 200 100'
    ]
    result = analyzer.analyze(lines)
    assert result["unique_visitors"] == 1
