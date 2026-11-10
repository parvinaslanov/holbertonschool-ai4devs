# Data Model - AI-Powered Task & Route Optimizer

## Entity Relationship Summary

+------------------+         1 : N         +------------------+
|      Route       |-----------------------|       Task       |
+------------------+                       +------------------+
         |                                           |
         | 1 : N                                     | 1 : N
         v                                           v
+-------------------------------------------------------------+
|                         StatusLog                           |
+-------------------------------------------------------------+

---

## Entities Definition

### 1. Route
Represents an individual delivery run or optimization session.

| Field Name     | Data Type | Constraints               | Description                                  |
|----------------|-----------|---------------------------|----------------------------------------------|
| id             | UUID      | Primary Key, Not Null     | Unique identifier for the route              |
| title          | String    | Not Null                  | Name or identifier for the delivery run      |
| date           | Date      | Not Null                  | Date of execution                            |
| status         | Enum      | Draft, Optimized, Active  | Lifecycle stage of the route                 |
| total_distance | Float     | Default 0.0               | Accumulated distance in kilometers           |
| total_duration | Integer   | Default 0                 | Total estimated travel duration in minutes   |
| created_at     | Timestamp | Default NOW()             | Record creation timestamp                    |

### 2. Task (Stop)
Represents a specific delivery stop associated with a route.

| Field Name     | Data Type | Constraints               | Description                                  |
|----------------|-----------|---------------------------|----------------------------------------------|
| id             | UUID      | Primary Key, Not Null     | Unique identifier for the task               |
| route_id       | UUID      | Foreign Key (Route.id)    | Parent route reference                       |
| recipient_name | String    | Not Null                  | Contact person or business name              |
| address        | String    | Not Null                  | Physical delivery street address             |
| stop_sequence  | Integer   | Default 0                 | Order position in optimized sequence         |
| status         | Enum      | Pending, In Transit, Done | Current delivery status                      |
| time_window    | String    | Optional                  | Target time window (e.g., "09:00 - 11:00")  |
| created_at     | Timestamp | Default NOW()             | Record creation timestamp                    |

### 3. StatusLog
Tracks historical state changes and status updates for audit and feedback reporting.

| Field Name     | Data Type | Constraints               | Description                                  |
|----------------|-----------|---------------------------|----------------------------------------------|
| id             | UUID      | Primary Key, Not Null     | Unique identifier for the log entry          |
| task_id        | UUID      | Foreign Key (Task.id)     | Reference to updated task                    |
| previous_status| Enum      | Pending, In Transit, Done | Status before update                         |
| new_status     | Enum      | Pending, In Transit, Done | Status after update                          |
| notes          | Text      | Optional                  | Optional failure or delivery notes           |
| updated_at     | Timestamp | Default NOW()             | Timestamp when status change occurred        |
