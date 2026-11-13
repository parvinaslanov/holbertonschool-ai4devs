// log_analyzer.js

class LogAnalyzer {
    parseLine(line) {
        const parts = line.trim().split(/\s+/);
        if (parts.length === 0 || line.trim() === "") {
            return { status: 0 };
        }
        let status = 0;
        try {
            // Apache log format status code is typically at index 8
            if (parts.length > 8) {
                status = parseInt(parts[8], 10);
                if (isNaN(status)) status = 0;
            }
        } catch (e) {
            status = 0;
        }
        return { status: status };
    }

    analyze(lines) {
        const total = lines.length;
        if (total === 0) {
            return { total_requests: 0, error_rate: 0.0 };
        }

        let errors = 0;
        for (const line of lines) {
            if (line && line.trim() !== "") {
                const res = this.parseLine(line);
                if (res.status >= 400) {
                    errors++;
                }
            }
        }
        return {
            total_requests: total,
            error_rate: (errors / total) * 100
        };
    }
}

module.exports = LogAnalyzer;
