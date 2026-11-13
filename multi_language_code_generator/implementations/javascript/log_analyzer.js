// log_analyzer.js
class LogAnalyzer {
    constructor(logData) {
        this.logs = logData ? logData.trim().split('\n') : [];
    }

    getUniqueVisitors() {
        const visitors = new Set();
        for (const line of this.logs) {
            if (!line.trim()) continue;
            // Assuming IP or visitor identifier is the first token
            const parts = line.split(' ');
            if (parts.length > 0) {
                visitors.add(parts[0]);
            }
        }
        return visitors.size;
    }

    getTopPaths(limit = 5) {
        const pathCounts = {};
        for (const line of this.logs) {
            if (!line.trim()) continue;
            // Extract path (e.g., GET /path HTTP/1.1)
            const match = line.match(/"[A-Z]+\s+([^\s]+)\s+HTTP\/[0-9.]+"/);
            if (match) {
                const path = match[1];
                pathCounts[path] = (pathCounts[path] || 0) + 1;
            }
        }
        return Object.entries(pathCounts)
            .sort((a, b) => b[1] - a[1])
            .slice(0, limit)
            .reduce((obj, [key, val]) => ({ ...obj, [key]: val }), {});
    }

    getMethodBreakdown() {
        const methods = {};
        for (const line of this.logs) {
            if (!line.trim()) continue;
            const match = line.match(/"([A-Z]+)\s+[^"]+"\s+[0-9]+/);
            if (match) {
                const method = match[1];
                methods[method] = (methods[method] || 0) + 1;
            }
        }
        return methods;
    }
}

module.exports = LogAnalyzer;
