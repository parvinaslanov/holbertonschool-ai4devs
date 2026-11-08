import pytest
from log_analyzer import LogAnalyzer

def test_top_paths_ranking():
    analyzer = LogAnalyzer()
    lines = ['1.1.1.1 - - [10/Nov/2026:10:00:00 +0000] "GET /pathA HTTP/1.1" 200 10']
    result = analyzer.analyze(lines)
    assert result["top_paths"][0]["path"] == "/pathA"
