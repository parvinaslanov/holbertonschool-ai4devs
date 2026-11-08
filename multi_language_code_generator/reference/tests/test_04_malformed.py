import pytest
from log_analyzer import LogAnalyzer

def test_malformed_entry():
    analyzer = LogAnalyzer()
    lines = ['INVALID LOG LINE DATA']
    result = analyzer.analyze(lines)
    assert result["total_requests"] == 0
    assert result["malformed_lines_count"] == 1
