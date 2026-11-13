#[cfg(test)]
mod tests {
    use super::*; // Adjust module path as needed based on your structure
    // Assuming LogAnalyzer is imported from implementations/rust/log_analyzer.rs

    #[test]
    fn test_log_parser_counts() {
        let analyzer = LogAnalyzer::new();
        let entries = vec![
            "200 OK".to_string(),
            "404 NOT FOUND".to_string(),
            "200 OK".to_string(),
        ];
        let stats = analyzer.analyze(&entries);

        match stats.get("total_requests") {
            Some(MetricValue::Int(val)) => assert_eq!(*val, 3),
            _ => panic!("Invalid or missing total_requests"),
        }

        match stats.get("error_rate") {
            Some(MetricValue::Float(val)) => assert!((val - 33.33).abs() < 1.0),
            _ => panic!("Invalid or missing error_rate"),
        }
    }
}
