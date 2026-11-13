// log_analyzer.js
class LogAnalyzer {
    constructor(logData) {
        this.logs = logData ? logData.trim().split('\n') : [];
    }

    getUniqueVisitors() {
        const visitors = new Set();
        for (const line of this.logs) {
            if (!line.trim()) continue;
            const parts = line.trim().split(/\s+/);
            if (parts.length > 0) {
                visitors.add(parts[0]);
            }
        }
        return visitors.size;
    }

    getTopPaths(limit = 5) {
        const pathCounts = {};
        const pattern = /"[A-Z]+\s+([^\s]+)\s+HTTP\/[0-9.]+"/;
        for (const line of this.logs) {
            if (!line.trim()) continue;
            const match = line.match(pattern);
            if (match) {
                const path = match[1];
                pathCounts[path] = (pathCounts[path] || 0) + 1;
            }
        }
        const sortedPaths = Object.entries(pathCounts)
            .sort((a, b) => b[1] - a[1])
            .slice(0, limit);
        return Object.fromEntries(sortedPaths);
    }

    getMethodBreakdown() {
        const methods = {};
        const pattern = /"([A-Z]+)\s+[^"]+"/;
        for (const line of this.logs) {
            if (!line.trim()) continue;
            const match = line.match(pattern);
            if (match) {
                const method = match[1];
                methods[method] = (methods[method] || 0) + 1;
            }
        }
        return methods;
    }
}

module.exports = LogAnalyzer;
