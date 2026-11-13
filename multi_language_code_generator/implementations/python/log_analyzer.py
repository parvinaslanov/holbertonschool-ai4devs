# log_analyzer.py

class LogAnalyzer:
    def parse_line(self, line: str) -> dict:
        parts = line.split()
        if not parts:
            return {"status": 0}
        try:
            status = int(parts[8])
        except (IndexError, ValueError):
            status = 0
        return {"status": status}

    def analyze(self, lines: list) -> dict:
        total = len(lines)
        if total == 0:
            return {"total_requests": 0, "error_rate": 0.0}
        
        errors = sum(1 for line in lines if line.strip() and self.parse_line(line)["status"] >= 400)
        return {"total_requests": total, "error_rate": (errors / total) * 100}
