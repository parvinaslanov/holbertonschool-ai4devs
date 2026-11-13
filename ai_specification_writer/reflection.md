# Reflection on AI-Assisted Specification Writing

## Introduction

Throughout this project, I utilized generative AI to accelerate the creation of product requirements, technical specifications, and system architecture diagrams for a ride-sharing platform. Translating high-level business concepts into structured engineering documentation typically requires significant manual effort. Integrating an AI assistant into this workflow allowed me to rapidly draft baseline artifacts—including user stories, data models, RESTful API endpoints, and Mermaid diagrams—before refining them into production-ready documentation.

## AI Strengths and Weaknesses

AI excelled at overcoming the blank-page problem and establishing structural scaffolding. Within seconds, the model generated well-organized Markdown documents containing standard industry sections, logical service decompositions (such as Authentication, Ride Matching, and Payment Gateways), and valid Mermaid syntax mapping traffic flow from the mobile client through an API gateway to downstream microservices. It also proved effective at brainstorming edge-case data model attributes like timestamps and status enumerations.

However, the AI frequently produced generic outputs lacking domain-specific precision and cross-document consistency. Early drafts included vague user stories ("As a driver, I want to log in so that I can use the app") and inconsistent endpoint naming (`POST /login` instead of `POST /auth/login`). Without tight constraints, the model exhibited formatting drift, occasionally omitting request payload schemas or failing to align database fields with API parameters.

## Easier vs. Harder Prompt Types

Working across multiple specification tasks highlighted clear differences between easier and harder prompt types. **Easier prompts** involved structural transformation, boilerplate generation, and syntax translation—such as converting a list of microservices into a Mermaid `graph TD` diagram or formatting standard CRUD endpoints into Markdown lists. Because these tasks follow deterministic patterns, the AI succeeded on the first attempt.

Conversely, **harder prompts** required open-ended architectural reasoning, cross-file state synchronization, and edge-case enforcement—such as ensuring every parameter in `POST /rides/book` strictly matched the attributes of the `Ride` data model while enforcing security constraints. Broad, underspecified prompts like "Write a technical spec for a ride-sharing app" consistently produced shallow results, proving that complex multi-artifact reasoning requires decomposed, step-by-step prompting.

## Key Prompt Elements: Role, Tone, and Placeholders

The quality of AI-generated specifications depended heavily on three core prompt engineering elements:

- **Role:** Explicitly assigning the AI a persona—such as *"Act as a senior backend architect writing production API documentation"*—shifted the output away from casual summaries toward rigorous, implementation-ready technical language.
- **Tone:** Specifying an objective, concise, and unambiguous engineering tone prevented marketing fluff and ensured user stories and endpoint descriptions were directly testable by developers.
- **Placeholders:** Providing structured templates with explicit placeholders (e.g., `POST /<service>/<action> { <param_1>, <param_
