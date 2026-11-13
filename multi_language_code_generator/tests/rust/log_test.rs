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
    fn test_empty_case() {
        let analyzer = LogAnalyzer::new();
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
    }

    #[test]
    fn test_malformed_and_blank_lines() {
        let analyzer = LogAnalyzer::new();
        let entries = vec!["".to_string(), "   ".to_string(), "short line".to_string()];
        let stats = analyzer.analyze(&entries);

        match stats.get("total_requests") {
            Some(MetricValue::Int(val)) => assert_eq!(*val, 3),
            _ => panic!("Invalid or missing total_requests"),
        }

        match stats.get("error_rate") {
            Some(MetricValue::Float(val)) => assert_eq!(*val, 0.0),
            _ => panic!("Invalid or missing error_rate"),
        }
    }

    #[test]
    fn test_server_error_5xx() {
        let analyzer = LogAnalyzer::new();
        let entries = vec![
            r#"127.0.0.1 - - [10/Oct/2000:13:55:36 -0700] "GET /test HTTP/1.0" 500 2326"#.to_string(),
        ];
        let stats = analyzer.analyze(&entries);

        match stats.get("total_requests") {
            Some(MetricValue::Int(val)) => assert_eq!(*val, 1),
            _ => panic!("Invalid or missing total_requests"),
        }

        match stats.get("error_rate") {
            Some(MetricValue::Float(val)) => assert_eq!(*val, 100.0),
            _ => panic!("Invalid or missing error_rate"),
        }
    }
}
