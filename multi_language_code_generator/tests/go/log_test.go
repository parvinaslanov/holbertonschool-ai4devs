package main

import (
	"testing"
	loganalyzer "holbertonschool-ai4devs/multi_language_code_generator/implementations/go"
)

func TestLogParserCounts(t *testing.T) {
	analyzer := loganalyzer.NewLogAnalyzer()
	entries := []string{"200 OK", "404 NOT FOUND", "200 OK"}
	stats := analyzer.Analyze(entries)

	if stats["total_requests"] != 3 {
		t.Errorf("Expected total_requests to be 3, got %v", stats["total_requests"])
	}

	errorRate, ok := stats["error_rate"].(float64)
	if !ok || errorRate < 33.2 || errorRate > 33.4 {
		t.Errorf("Expected error_rate around 33.3, got %v", stats["error_rate"])
	}
}

func TestLogParserEdgeCases(t *testing.T) {
	analyzer := loganalyzer.NewLogAnalyzer()
	
	// Empty list case
	stats := analyzer.Analyze([]string{})
	if stats["total_requests"] != 0 || stats["error_rate"] != 0.0 {
		t.Errorf("Expected 0 total and 0.0 error rate for empty input")
	}

	// Malformed and blank lines
	entries := []string{"", "   ", "short line"}
	stats = analyzer.Analyze(entries)
	if stats["total_requests"] != 3 || stats["error_rate"] != 0.0 {
		t.Errorf("Expected 3 total and 0.0 error rate for malformed inputs")
	}

	// Server error 5xx validation
	entries = []string{`127.0.0.1 - - [10/Oct/2000:13:55:36 -0700] "GET /test HTTP/1.0" 500 2326`}
	stats = analyzer.Analyze(entries)
	if stats["total_requests"] != 1 || stats["error_rate"] != 100.0 {
		t.Errorf("Expected 1 total and 100.0 error rate for server error")
	}
}
