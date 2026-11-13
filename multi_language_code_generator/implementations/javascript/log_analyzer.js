// log_analyzer.js

class LogAnalyzer {
    parse_line(line) {
        if (!line || typeof line !== "string" || line.trim() === "") {
            return { status: 0 };
        }
        const parts = line.trim().split(/\s+/);
        let status = 0;
        try {
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
        if (!lines || !Array.isArray(lines)) {
            return { total_requests: 0, error_rate: 0.0 };
        }
        const total = lines.length;
        if (total === 0) {
            return { total_requests: 0, error_rate: 0.0 };
        }
        let errors = 0;
        for (const line of lines) {
            if (line && typeof line === "string" && line.trim() !== "") {
                const res = this.parse_line(line);
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
