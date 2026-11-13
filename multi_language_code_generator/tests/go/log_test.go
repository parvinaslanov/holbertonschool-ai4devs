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
