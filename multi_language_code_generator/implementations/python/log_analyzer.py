# log_analyzer.py
from collections import Counter
import re

class LogAnalyzer:
    def __init__(self, log_data: str):
        self.logs = log_data.strip().split('\n') if log_data else []

    def get_unique_visitors(self) -> int:
        visitors = set()
        for line in self.logs:
            if not line.strip():
                continue
            parts = line.split()
            if parts:
                visitors.add(parts[0])
        return len(visitors)

    def get_top_paths(self, limit: int = 5) -> dict:
        path_counts = Counter()
        pattern = re.compile(r'"[A-Z]+\s+([^\s]+)\s+HTTP/[0-9.]+"')
        
        for line in self.logs:
            if not line.strip():
                continue
            match = pattern.search(line)
            if match:
                path = match.group(1)
                path_counts[path] += 1
                
        return dict(path_counts.most_common(limit))

    def get_method_breakdown(self) -> dict:
        methods = Counter()
        pattern = re.compile(r'"([A-Z]+)\s+[^"]+"\s+[0-9]+')
        
        for line in self.logs:
            if not line.strip():
                continue
            match = pattern.search(line)
            if match:
                method = match.group(1)
                methods[method] += 1
                
        return dict(methods)
