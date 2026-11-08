import pytest
from log_analyzer import LogAnalyzer

def test_high_volume_stress():
    analyzer = LogAnalyzer()
    line = '192.168.1.10 - - [10/Nov/2026:12:00:00 +0000] "GET /status HTTP/1.1" 200 450'
    result = analyzer.analyze([line for _ in range(10)])
    assert result["total_requests"] == 10
