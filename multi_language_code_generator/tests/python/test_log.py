from multi_language_code_generator.implementations.python.log_analyzer import LogAnalyzer

def test_log_parser_counts():
    analyzer = LogAnalyzer()
    entries = ["200 OK", "404 NOT FOUND", "200 OK"]
    stats = analyzer.analyze(entries)
    assert stats['total_requests'] == 3
    assert stats['error_rate'] == 33.333333333333336 or abs(stats['error_rate'] - 33.3) < 1.0
