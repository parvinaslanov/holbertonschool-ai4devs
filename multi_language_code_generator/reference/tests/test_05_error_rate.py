import pytest
from log_analyzer import LogAnalyzer

def test_error_rate_calculation():
    analyzer = LogAnalyzer()
    lines = ['10.0.0.1 - - [10/Nov/2026:10:00:00 +0000] "GET /success HTTP/1.1" 500 500']
    result = analyzer.analyze(lines)
    assert result["error_rate_percentage"] == 100.0
