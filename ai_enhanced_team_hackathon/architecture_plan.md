# Architecture Plan

## System Overview
The application follows a 3-Tier Client-Server Architecture consisting of a Frontend Client, a FastAPI Backend Server, and an SQLite Database integrated with an LLM AI Diagnostic Engine.

## Components
1. Frontend Client: HTML/JS interface for symptom submission and step-by-step checklists.
2. Backend Server: Python FastAPI application handling business logic and API routing.
3. Database: SQLite database storing users, sessions, and messages.
4. AI Diagnostic Engine: External LLM API configured with system prompts for IT troubleshooting.

<!-- COMPLETED -->
