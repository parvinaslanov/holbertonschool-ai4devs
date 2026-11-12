# Data Model — AI Computer & IT Troubleshooting Assistant

## Entity-Relationship Overview
- A **User** can initiate multiple **DiagnosticSessions**.
- Each **DiagnosticSession** contains multiple sequential **Messages** (user descriptions, AI clarifying questions, and diagnostic steps).
- Each **DiagnosticSession** produces one or more **DiagnosticReports** summarizing root causes and resolution status.

---

## Entities

### 1. `User`
Stores account information and basic system profile defaults to speed up diagnostics.

| Field | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | UUID / Integer | Primary Key | Unique identifier for the user |
| `username` | String | Required, Unique | User's display name |
| `email` | String | Required, Unique | User's email address |
| `default_os` | String | Nullable (e.g., `Windows 11`) | Default operating system to tailor instructions |
| `created_at` | Timestamp | Default: `NOW()` | Account creation timestamp |

---

### 2. `DiagnosticSession`
Represents a single troubleshooting incident from initial symptom report to resolution.

| Field | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | UUID / Integer | Primary Key | Unique identifier for the session |
| `user_id` | UUID / Integer | Foreign Key -> `User.id` | Owner of the troubleshooting session |
| `title` | String | Required | Auto-generated summary of the problem (e.g., "Wi-Fi Disconnecting on Windows 11") |
| `category` | Enum | `HARDWARE`, `WINDOWS`, `BIOS_UEFI`, `DRIVER`, `NETWORK`, `OTHER` | Primary problem domain identified by AI |
| `status` | Enum | `OPEN`, `IN_PROGRESS`, `RESOLVED`, `ESCALATED` | Current state of the troubleshooting session |
| `created_at` | Timestamp | Default: `NOW()` | When the session started |
| `updated_at` | Timestamp | Auto-update | Last activity timestamp |

---

### 3. `Message`
Stores the conversational history between the user and the AI diagnostic engine within a session.

| Field | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | UUID / Integer | Primary Key | Unique identifier for the message |
| `session_id` | UUID / Integer | Foreign Key -> `DiagnosticSession.id` | Associated troubleshooting session |
| `sender` | Enum | `USER`, `AI` | Who sent the message |
| `content` | Text | Required | Plain-language symptom, follow-up question, or step-by-step instructions |
| `attachment_url` | String | Nullable | *(Future Scope)* URL/path to uploaded error screenshot or log |
| `created_at` | Timestamp | Default: `NOW()` | Timestamp of the message |

---

### 4. `DiagnosticResult`
Captures structured output from the AI analysis for quick reference and analytics.

| Field | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | UUID / Integer | Primary Key | Unique identifier for the diagnostic result |
| `session_id` | UUID / Integer | Foreign Key -> `DiagnosticSession.id` | Associated troubleshooting session |
| `probable_causes` | JSON / Text | Required | Ranked list of identified root causes |
| `recommended_steps` | JSON / Text | Required | Structured step-by-step fix instructions |
| `risk_level` | Enum | `LOW`, `MEDIUM`, `HIGH` | Risk level of suggested actions (e.g., `HIGH` for BIOS changes) |
| `was_helpful` | Boolean | Nullable | User feedback on whether the fix resolved the issue |
