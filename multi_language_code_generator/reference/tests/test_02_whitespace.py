import pytest
from log_analyzer import LogAnalyzer

def test_whitespace_log():
    analyzer = LogAnalyzer()
    result = analyzer.analyze(["   ", "\n", "\t"])
    assert result["total_requests"] == 0
