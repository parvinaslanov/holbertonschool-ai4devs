# Reflection on AI-Assisted Specification Writing

## Introduction

Throughout this project, I utilized generative AI to accelerate the creation of product requirements, technical specifications, and system architecture diagrams for a ride-sharing platform. Translating high-level business concepts into structured engineering documentation typically requires significant manual effort and repetitive formatting. Integrating an AI assistant into this workflow allowed me to rapidly draft baseline artifacts—including user stories, data models, RESTful API endpoints, and Mermaid diagrams—before refining them into production-ready documentation.

## AI Strengths

AI excelled at overcoming the blank-page problem and establishing structural scaffolding. Within seconds, the model generated well-organized Markdown documents containing standard industry sections, logical service decompositions (such as separating Authentication, Ride Matching, and Payment Gateways), and standard CRUD endpoints. A surprising success was its ability to translate prose descriptions of system components directly into valid Mermaid syntax for the architecture diagram, accurately mapping traffic flow from the mobile client through an API gateway to downstream microservices. Additionally, AI proved highly effective at brainstorming edge-case attributes for data models, automatically suggesting essential fields like timestamps, foreign keys, and status enumerations that are easy to overlook during initial drafting.

## AI Weaknesses

Despite its speed, the AI frequently produced generic, overly high-level outputs that lacked domain-specific precision and consistency across artifacts. For instance, early drafts included vague user stories ("As a driver, I want to log in so that I can use the app") and inconsistent endpoint naming conventions (such as `POST /login` instead of a versioned or namespaced path like `POST /auth/login`). Furthermore, the model occasionally exhibited formatting drift—such as omitting explicit request payload schemas unless specifically prompted, or failing to maintain strict alignment between database fields defined in the data model section and parameters expected by the API endpoints. Without tight constraints, AI tends to optimize for plausible-sounding prose rather than strict engineering rigor.

## Human Role

Human intervention was critical during the review, validation, and refinement phases. Acting as an editor and system architect, I had to audit every generated artifact for cross-document consistency, security implications, and clarity. Specifically, manual refinement was essential to enforce strict naming conventions across API routes, specify exact request and response parameters, and upgrade vague user stories into actionable, testable acceptance criteria. Moreover, ensuring that deliverables adhered strictly to project submission formats and automated grading checks required careful human verification that the AI could not reliably guarantee on its own.

## Lessons Learned

Using AI for real-world specification writing works best when treated as an iterative, human-in-the-loop collaboration rather than a one-shot automation tool. First, prompt specificity directly governs output quality: providing concrete examples, explicit schemas, and structural templates yields far more accurate specifications than open-ended requests. Second, specifications should be generated modularly—drafting system components first, then deriving data models and API contracts from those components—to minimize inconsistencies. Ultimately, while AI dramatically reduces the time required to draft and format technical documentation, human engineers remain indispensable for architectural judgment, security validation, and ensuring unambiguous clarity for development teams.
