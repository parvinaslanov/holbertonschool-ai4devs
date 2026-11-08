import pytest
from log_analyzer import LogAnalyzer

def test_empty_log():
    analyzer = LogAnalyzer()
    result = analyzer.analyze([])
    assert result["total_requests"] == 0
