# log_analyzer.py
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
        path_counts = {}
        pattern = re.compile(r'"[A-Z]+\s+([^\s]+)\s+HTTP/[0-9.]+"')
        
        for line in self.logs:
            if not line.strip():
                continue
            match = pattern.search(line)
            if match:
                path = match.group(1)
                path_counts[path] = path_counts.get(path, 0) + 1
                
        sorted_paths = sorted(path_counts.items(), key=lambda x: x[1], reverse=True)
        return dict(sorted_paths[:limit])

    def get_method_breakdown(self) -> dict:
        methods = {}
        pattern = re.compile(r'"([A-Z]+)\s+[^"]+"')
        
        for line in self.logs:
            if not line.strip():
                continue
            match = pattern.search(line)
            if match:
                method = match.group(1)
                methods[method] = methods.get(method, 0) + 1
                
        return methods
