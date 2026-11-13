// LogAnalyzer.java
package implementations.java;

import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

public class LogAnalyzer {
    private final List<String> logs;

    public LogAnalyzer(String logData) {
        if (logData == null || logData.trim().isEmpty()) {
            this.logs = new ArrayList<>();
        } else {
            this.logs = Arrays.asList(logData.trim().split("\n"));
        }
    }

    public long getUniqueVisitors() {
        Set<String> visitors = new HashSet<>();
        for (String line : logs) {
            if (line.trim().isEmpty()) continue;
            String[] parts = line.trim().split("\\s+");
            if (parts.length > 0) {
                visitors.add(parts[0]);
            }
        }
        return visitors.size();
    }

    public Map<String, Integer> getTopPaths(int limit) {
        Map<String, Integer> pathCounts = new HashMap<>();
        Pattern pattern = Pattern.compile("\"[A-Z]+\\s+([^\\s]+)\\s+HTTP/[0-9.]+\"");
        
        for (String line : logs) {
            if (line.trim().isEmpty()) continue;
            Matcher matcher = pattern.matcher(line);
            if (matcher.find()) {
                String path = matcher.group(1);
                pathCounts.put(path, pathCounts.getOrDefault(path, 0) + 1);
            }
        }

        return pathCounts.entrySet().stream()
                .sorted(Map.Entry.<String, Integer>comparingByValue(Comparator.reverseOrder()))
                .limit(limit)
                .collect(Collectors.toMap(
                        Map.Entry::getKey,
                        Map.Entry::getValue,
                        (e1, e2) -> e1,
                        LinkedHashMap::new
                ));
    }

    public Map<String, Integer> getMethodBreakdown() {
        Map<String, Integer> methods = new HashMap<>();
        Pattern pattern = Pattern.compile("\"([A-Z]+)\\s+[^>]+\"\\s+[0-9]+");

        for (String line : logs) {
            if (line.trim().isEmpty()) continue;
            // Simplified method extraction
            String[] parts = line.split("\"");
            if (parts.length > 1) {
                String[] reqParts = parts[1].split("\\s+");
                if (reqParts.length > 0) {
                    String method = reqParts[0];
                    methods.put(method, methods.getOrDefault(method, 0) + 1);
                }
            }
        }
        return methods;
    }
}
