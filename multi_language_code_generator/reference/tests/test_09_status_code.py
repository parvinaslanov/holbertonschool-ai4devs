import pytest
from log_analyzer import LogAnalyzer

def test_status_code_aggregation():
    analyzer = LogAnalyzer()
    lines = ['1.1.1.1 - - [10/Nov/2026:10:02:00 +0000] "GET /404 HTTP/1.1" 404 10']
    result = analyzer.analyze(lines)
    assert result["status_code_counts"] == {"404": 1}
