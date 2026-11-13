from multi_language_code_generator.implementations.python.log_analyzer import LogAnalyzer

def test_log_parser_counts():
    analyzer = LogAnalyzer()
    entries = ["200 OK", "404 NOT FOUND", "200 OK"]
    stats = analyzer.analyze(entries)
    assert stats['total_requests'] == 3
    assert abs(stats['error_rate'] - 33.33) < 0.1

def test_empty_case():
    analyzer = LogAnalyzer()
    stats = analyzer.analyze([])
    assert stats['total_requests'] == 0
    assert stats['error_rate'] == 0.0

def test_malformed_and_blank_lines():
    analyzer = LogAnalyzer()
    entries = ["", "   ", "short line"]
    stats = analyzer.analyze(entries)
    assert stats['total_requests'] == 3
    assert stats['error_rate'] == 0.0

def test_server_error_5xx():
    analyzer = LogAnalyzer()
    entries = ['127.0.0.1 - - [10/Oct/2000:13:55:36 -0700] "GET /test HTTP/1.0" 500 2326']
    stats = analyzer.analyze(entries)
    assert stats['total_requests'] == 1
    assert stats['error_rate'] == 100.0
