// log_analyzer.rs
use std::collections::HashMap;

pub struct LogAnalyzer;

impl LogAnalyzer {
    pub fn new() -> Self {
        LogAnalyzer
    }

    pub fn parse_line(&self, line: &str) -> HashMap<String, i32> {
        let mut result = HashMap::new();
        if line.trim().is_empty() {
            result.insert("status".to_string(), 0);
            return result;
        }
        let parts: Vec<&str> = line.split_whitespace().collect();
        let status = if parts.len() > 8 {
            parts[8].parse::<i32>().unwrap_or(0)
        } else {
            0
        };
        result.insert("status".to_string(), status);
        result
    }

    pub fn analyze(&self, lines: &[String]) -> HashMap<String, f64> {
        let mut result = HashMap::new();
        let total = lines.len();
        if total == 0 {
            result.insert("total_requests".to_string(), 0.0);
            result.insert("error_rate".to_string(), 0.0);
            return result;
        }

        let mut errors = 0;
        for line in lines {
            if !line.trim().is_empty() {
                let parsed = self.parse_line(line);
                if let Some(&status) = parsed.get("status") {
                    if status >= 400 {
                        errors += 1;
                    }
                }
            }
        }

        let error_rate = (errors as f64 / total as f64) * 100.0;
        result.insert("total_requests".to_string(), total as f64);
        result.insert("error_rate".to_string(), error_rate);
        result
    }
}
