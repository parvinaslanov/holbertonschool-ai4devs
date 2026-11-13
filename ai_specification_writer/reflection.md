# Reflection on AI-Assisted Specification Writing

## Introduction

In this project, I used generative AI to draft product requirements, technical specifications, and system architecture diagrams for a ride-sharing platform. Translating high-level ideas into structured engineering documentation normally requires substantial manual effort. Integrating AI allowed me to rapidly produce baseline user stories, data models, API endpoints, and Mermaid diagrams before refining them into clear, consistent artifacts.

## Influence of Structure on AI Output

Prompt structure directly determined the quality of AI-generated specifications. When given open-ended instructions, the AI produced inconsistent formatting, omitted payload parameters, and drifted between naming conventions. Conversely, providing clear Markdown templates, explicit headings, and concrete examples constrained the model to follow engineering standards. Structured skeletons acted as guardrails, keeping system components, data models, and API contracts aligned across files.

## Examples of Success and Failure

- **Successes:** AI excelled at structural scaffolding and syntax translation. Given a basic list of services (Authentication, Ride Matching, and Payment Gateway), it immediately generated valid Mermaid `graph TD` syntax mapping traffic through an API gateway. It also suggested useful edge-case fields for the `Ride` and `Payment` models, including timestamps, foreign keys, and status enums.
- **Failures:** Unconstrained drafts suffered from vagueness and cross-file inconsistencies. Early outputs contained generic user stories ("As a driver, I want to log in so that I can use the app") and inconsistent routes (`POST /login` instead of `POST /auth/login`), requiring manual edits to enforce domain precision and uniform naming.

## Easier vs. Harder Prompt Types

Working across tasks revealed a clear contrast between easier and harder prompts. **Easier prompts** involved deterministic formatting, boilerplate generation, and syntax translation—such as converting service lists into a Mermaid diagram or formatting CRUD endpoints as Markdown bullets. **Harder prompts** required cross-file state synchronization and architectural reasoning—such as ensuring every parameter in `POST /rides/book` matched the exact attributes of the `Ride` model while enforcing security rules. Complex specifications succeeded only when broken into sequential steps.

## Key Prompt Elements: Role, Tone, and Placeholders

Three prompt elements proved essential for reliable outputs:

- **Role:** Assigning a specific persona—such as *"Act as a senior backend architect writing API documentation"*—shifted the model from casual summaries to rigorous technical language.
- **Tone:** Requesting a concise, objective engineering tone removed unnecessary prose and made user stories and endpoints directly testable.
- **Placeholders:** Using explicit bracketed placeholders (like `POST /[service]/[action] { [param_1], [param_2] }`) prevented formatting drift and forced the AI to populate concrete field names.

## Human Role

Human review remained indispensable throughout the workflow. Acting as an editor and architect, I audited every draft for cross-document consistency, security, and clarity. Manual refinement was critical to standardize API routes, define exact request parameters, upgrade vague user stories into testable acceptance criteria, and ensure strict compliance with formatting requirements.

## Future Improvements

To improve AI-assisted specification workflows in future projects, I will apply three practices:

1. **Reusable Prompt Templates:** Maintain standardized templates pre-configured with explicit roles, technical tone rules, and bracketed placeholders.
2. **Chained Modular Workflows:** Generate specifications sequentially—using finalized components to constrain data models, and finalized models to generate exact API payloads.
3. **Automated Validation Checks:** Pair AI drafting with linters like Mermaid CLI and OpenAPI validators to catch syntax and schema errors early.
