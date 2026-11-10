# System Architecture - AI-Powered Task & Route Optimizer

## High-Level System Overview

+-----------------------------------------------------------------------+
|                          Client Browser                               |
|                                                                       |
|   +-----------------------+               +-----------------------+   |
|   |   React / Next.js UI  |               |  Tailwind CSS UI      |   |
|   |  - Route / Task Tab   |               |  - Responsive Layout  |   |
|   |  - Assistant Chat Tab |               |  - Toast & Alert System|  |
|   +-----------+-----------+               +-----------+-----------+   |
+---------------+---------------------------------------+---------------+
                |                                       |
                | REST APIs / JSON                      | Websocket / HTTP
                v                                       v
+-----------------------------------------------------------------------+
|                       Backend Application                             |
|                           (Node.js / Express)                         |
|                                                                       |
|   +-----------------------+               +-----------------------+   |
|   |   Route Controller    |               |  Optimization Engine  |   |
|   |  - CRUD API Endpoints |               |  - AI Route Solver    |   |
|   |  - Validation Logic   |               |  - Heuristic Matrix   |   |
|   +-----------+-----------+               +-----------+-----------+   |
+---------------+---------------------------------------+---------------+
                |                                       |
                v                                       v
+-------------------------------+       +-------------------------------+
|     External Mapping API      |       |      Database / Storage       |
|  - Geocoding & Distance Matrix|       |   (Supabase / PostgreSQL)     |
|  - Distance / Time Calculations|      |   - Routes, Tasks, Logs       |
+-------------------------------+       +-------------------------------+

## Architecture Components

1. Frontend Layer:
   - Framework: React / Next.js with Tailwind CSS.
   - Responsiveness: Responsive Flexbox/Grid layouts with desktop & mobile support.
   - State & UX: Tabbed navigation state, reactive toast notifications, and form validation error alerts.

2. Backend API Layer:
   - Server Environment: Node.js with Express.js REST endpoints.
   - Core Responsibilities: Input validation, request routing, state synchronization, data transformation for CSV exports.

3. Optimization & AI Layer:
   - AI Route Solver: Calculates matrix distances and reorders stops using distance-matrix heuristics or external route optimization APIs (e.g., OpenRouteService / Mapbox).

4. Persistence Layer:
   - Database: Supabase / PostgreSQL database for persistent storage of routes, tasks, and status logs.
