import pytest
from log_analyzer import LogAnalyzer

def test_method_breakdown():
    analyzer = LogAnalyzer()
    lines = ['1.1.1.1 - - [10/Nov/2026:10:00:00 +0000] "POST /api HTTP/1.1" 201 20']
    result = analyzer.analyze(lines)
    assert result["method_breakdown"] == {"POST": 1}
