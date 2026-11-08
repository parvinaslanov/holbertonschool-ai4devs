import pytest
from log_analyzer import LogAnalyzer

@pytest.fixture
def analyzer():
    return LogAnalyzer()

def test_top_paths_ranking(analyzer):
    lines = [
        '1.1.1.1 - - [10/Nov/2026:10:00:00 +0000] "GET /pathA HTTP/1.1" 200 10',
        '1.1.1.1 - - [10/Nov/2026:10:01:00 +0000] "GET /pathB HTTP/1.1" 200 10',
        '1.1.1.1 - - [10/Nov/2026:10:02:00 +0000] "GET /pathA HTTP/1.1" 200 10',
        '1.1.1.1 - - [10/Nov/2026:10:03:00 +0000] "GET /pathC HTTP/1.1" 200 10',
        '1.1.1.1 - - [10/Nov/2026:10:04:00 +0000] "GET /pathC HTTP/1.1" 200 10',
        '1.1.1.1 - - [10/Nov/2026:10:05:00 +0000] "GET /pathC HTTP/1.1" 200 10',
    ]
    result = analyzer.analyze(lines)
    top_paths = result["top_paths"]
    assert top_paths[0]["path"] == "/pathC" and top_paths[0]["count"] == 3
    assert top_paths[1]["path"] == "/pathA" and top_paths[1]["count"] == 2
    assert top_paths[2]["path"] == "/pathB" and top_paths[2]["count"] == 1

def test_method_breakdown(analyzer):
    lines = [
        '1.1.1.1 - - [10/Nov/2026:10:00:00 +0000] "GET /api HTTP/1.1" 200 10',
        '1.1.1.1 - - [10/Nov/2026:10:01:00 +0000] "POST /api HTTP/1.1" 201 20',
        '1.1.1.1 - - [10/Nov/2026:10:02:00 +0000] "DELETE /api/1 HTTP/1.1" 204 0'
    ]
    result = analyzer.analyze(lines)
    assert result["method_breakdown"] == {"GET": 1, "POST": 1, "DELETE": 1}

def test_status_code_aggregation(analyzer):
    lines = [
        '1.1.1.1 - - [10/Nov/2026:10:00:00 +0000] "GET / HTTP/1.1" 200 10',
        '1.1.1.1 - - [10/Nov/2026:10:01:00 +0000] "GET / HTTP/1.1" 200 10',
        '1.1.1.1 - - [10/Nov/2026:10:02:00 +0000] "GET /404 HTTP/1.1" 404 10'
    ]
    result = analyzer.analyze(lines)
    assert result["status_code_counts"] == {"200": 2, "404": 1}

def test_high_volume_stress_batch(analyzer):
    line = '192.168.1.10 - - [10/Nov/2026:12:00:00 +0000] "GET /status HTTP/1.1" 200 450'
    lines = [line for _ in range(100)]
    result = analyzer.analyze(lines)
    assert result["total_requests"] == 100
    assert result["unique_visitors"] == 1
    assert result["error_rate_percentage"] == 0.0
    assert result["top_paths"][0]["count"] == 100
