// LogAnalyzer.java
import java.util.*;

public class LogAnalyzer {
    
    public Map<String, Object> parseLine(String line) {
        Map<String, Object> result = new HashMap<>();
        if (line == null || line.trim().isEmpty()) {
            result.put("status", 0);
            return result;
        }
        
        String[] parts = line.trim().split("\\s+");
        int status = 0;
        try {
            if (parts.length > 8) {
                status = Integer.parseInt(parts[8]);
            }
        } catch (NumberFormatException e) {
            status = 0;
        }
        
        result.put("status", status);
        return result;
    }

    public Map<String, Object> analyze(List<String> lines) {
        Map<String, Object> result = new HashMap<>();
        int total = lines.size();
        if (total == 0) {
            result.put("total_requests", 0);
            result.put("error_rate", 0.0);
            return result;
        }

        int errors = 0;
        for (String line : lines) {
            if (line != null && !line.trim().isEmpty()) {
                Map<String, Object> parsed = parseLine(line);
                int status = (int) parsed.get("status");
                if (status >= 400) {
                    errors++;
                }
            }
        }

        double errorRate = ((double) errors / total) * 100.0;
        result.put("total_requests", total);
        result.put("error_rate", errorRate);
        return result;
    }
}
