#[cfg(test)]
mod tests {
    use super::super::super::implementations::rust::log_analyzer::{LogAnalyzer, MetricValue};

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

    #[test]
    fn test_log_parser_edge_cases() {
        let analyzer = LogAnalyzer::new();
        
        // Empty list / edge cases
        let entries = vec![];
        let stats = analyzer.analyze(&entries);

        match stats.get("total_requests") {
            Some(MetricValue::Int(val)) => assert_eq!(*val, 0),
            _ => panic!("Invalid or missing total_requests"),
        }

        match stats.get("error_rate") {
            Some(MetricValue::Float(val)) => assert_eq!(*val, 0.0),
            _ => panic!("Invalid or missing error_rate"),
        }

        // Blank/malformed lines
        let malformed = vec!["".to_string(), "   ".to_string(), "short".to_string()];
        let stats_malformed = analyzer.analyze(&malformed);

        match stats_malformed.get("total_requests") {
            Some(MetricValue::Int(val)) => assert_eq!(*val, 3),
            _ => panic!("Invalid or missing total_requests"),
        }

        match stats_malformed.get("error_rate") {
            Some(MetricValue::Float(val)) => assert_eq!(*val, 0.0),
            _ => panic!("Invalid or missing error_rate"),
        }
    }
}
