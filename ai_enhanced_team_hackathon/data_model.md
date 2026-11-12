# Data Model

## Entities

### 1. User
| Field | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | UUID / Integer | Primary Key | Unique identifier for the user |
| `username` | String | Required, Unique | User's display name |
| `email` | String | Required, Unique | User's email address |
| `default_os` | String | Nullable | Default operating system |
| `created_at` | Timestamp | Default: `NOW()` | Account creation timestamp |

### 2. DiagnosticSession
| Field | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | UUID / Integer | Primary Key | Unique identifier for the session |
| `user_id` | UUID / Integer | Foreign Key -> `User.id` | Owner of the session |
| `title` | String | Required | Summary of the problem |
| `category` | Enum | Required | Problem domain (HARDWARE, WINDOWS, NETWORK, etc.) |
| `status` | Enum | Required | Current state (OPEN, IN_PROGRESS, RESOLVED) |
| `created_at` | Timestamp | Default: `NOW()` | Session start timestamp |

### 3. Message
| Field | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | UUID / Integer | Primary Key | Unique identifier for the message |
| `session_id` | UUID / Integer | Foreign Key -> `DiagnosticSession.id` | Associated session |
| `sender` | Enum | Required | Sender type (USER, AI) |
| `content` | Text | Required | Message content |
| `created_at` | Timestamp | Default: `NOW()` | Message timestamp |

### 4. DiagnosticResult
| Field | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | UUID / Integer | Primary Key | Unique identifier |
| `session_id` | UUID / Integer | Foreign Key -> `DiagnosticSession.id` | Associated session |
| `probable_causes` | Text | Required | Ranked list of root causes |
| `recommended_steps` | Text | Required | Step-by-step fix instructions |
| `risk_level` | Enum | Required | Risk rating (LOW, MEDIUM, HIGH) |

<!-- COMPLETED -->
