// log_analyzer.go
package loganalyzer

import (
	"strconv"
	"strings"
)

type LogAnalyzer struct{}

func NewLogAnalyzer() *LogAnalyzer {
	return &LogAnalyzer{}
}

func (l *LogAnalyzer) ParseLine(line string) map[string]int {
	result := map[string]int{"status": 0}
	trimmed := strings.TrimSpace(line)
	if trimmed == "" {
		return result
	}
	parts := strings.Fields(trimmed)
	if len(parts) > 8 {
		if status, err := strconv.Atoi(parts[8]); err == nil {
			result["status"] = status
		}
	}
	return result
}

func (l *LogAnalyzer) Analyze(lines []string) map[string]interface{} {
	result := make(map[string]interface{})
	total := len(lines)
	if total == 0 {
		result["total_requests"] = 0
		result["error_rate"] = 0.0
		return result
	}

	errors := 0
	for _, line := range lines {
		if strings.TrimSpace(line) != "" {
			parsed := l.ParseLine(line)
			if status, ok := parsed["status"]; ok && status >= 400 {
				errors++
			}
		}
	}

	errorRate := (float64(errors) / float64(total)) * 100.0
	result["total_requests"] = total
	result["error_rate"] = errorRate
	return result
}
