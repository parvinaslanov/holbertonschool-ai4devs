# High-Level Architecture Plan — AI Computer & IT Troubleshooting Assistant

## 1. System Overview
The **AI Computer & IT Troubleshooting Assistant** follows a clean **Client-Server (3-Tier) Web Architecture** designed for rapid MVP development by a solo developer while remaining modular enough to support future multimodal features (screenshot/error log analysis).

```text
+-------------------+       HTTPS / REST API       +-----------------------+
|                   | <--------------------------> |                       |
|  Frontend Client  |                              |    Backend Server     |
|  (HTML/JS/React)  |                              |   (Python / FastAPI)  |
|                   |                              |                       |
+-------------------+                              +-----------+-----------+
                                                               |
                                       +-----------------------+-----------------------+
                                       |                                               |
                                       v                                               v
                        +-----------------------------+                 +-----------------------------+
                        |   AI Diagnostic Engine      |                 |     Relational Database     |
                        |   (LLM API + System Prompt) |                 |     (SQLite / PostgreSQL)   |
                        +-----------------------------+                 +-----------------------------+
