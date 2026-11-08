import re
from collections import Counter
from typing import Dict, Any, List

class LogAnalyzer:
    LOG_PATTERN = re.compile(
        r'^(?P<ip>\S+)\s+\S+\s+\S+\s+\[(?P<timestamp>[^\]]+)\]\s+'
        r'"(?P<method>[A-Z]+)\s+(?P<path>[^\s"]+)(?:\s+[^"]*)?"\s+'
        r'(?P<status>\d{3})\s+(?P<size>\S+)'
    )

    def parse_line(self, line: str) -> Dict[str, Any]:
        match = self.LOG_PATTERN.match(line.strip())
        if not match:
            return None
        data = match.groupdict()
        data["status"] = int(data["status"])
        return data

    def analyze(self, lines: List[str]) -> Dict[str, Any]:
        total_requests = 0
        malformed_lines_count = 0
        ips = set()
        status_counts = Counter()
        method_counts = Counter()
        path_counts = Counter()
        error_count = 0

        for line in lines:
            if not line.strip():
                continue
            
            parsed = self.parse_line(line)
            if not parsed:
                malformed_lines_count += 1
                continue

            total_requests += 1
            ips.add(parsed["ip"])
            status_counts[str(parsed["status"])] += 1
            method_counts[parsed["method"]] += 1
            path_counts[parsed["path"]] += 1

            if parsed["status"] >= 400:
                error_count += 1

        error_rate = (error_count / total_requests * 100) if total_requests > 0 else 0.0
        
        top_paths = [
            {"path": path, "count": count}
            for path, count in path_counts.most_common(3)
        ]

        return {
            "total_requests": total_requests,
            "unique_visitors": len(ips),
            "error_rate_percentage": round(error_rate, 2),
            "status_code_counts": dict(status_counts),
            "method_breakdown": dict(method_counts),
            "top_paths": top_paths,
            "malformed_lines_count": malformed_lines_count
        }
