# Pull Request: Add Task Filtering and Status Summary Endpoint

## Summary
Implements flexible task filtering by status and due date, along with an aggregated status summary calculation. Adds a new API endpoint `/tasks/filter` to allow client applications to query specific task subsets without pulling full datasets.

## Changes
- Added `filter_tasks()` query builder and helper functions in `tasks.py` (~120 LOC).
- Updated `Task` model schema in `models.py` to support query parameters and indexable filter fields.
- Created `/tasks/filter` endpoint handler with query validation in `api/routes.py`.
- Added 6 new unit and integration tests covering filter edge cases and empty state responses in `tests/test_tasks.py`.

## Context
~160 LOC total added across core logic, API route handlers, and unit tests. 
Addresses feature request for lightweight query filtering to reduce frontend payload sizes during list views.
Related issue: #42.
