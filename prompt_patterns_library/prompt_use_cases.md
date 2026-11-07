# Prompt Use Cases

## Code Quality
- **Refactoring**
  - **Goal**: Improve readability and performance
  - **Input**: Source function in [LANGUAGE]
  - **Output**: Optimized code + explanation
- **Style Enforcement**
  - **Goal**: Enforce consistent naming and formatting
  - **Input**: Code block
  - **Output**: Rewritten code with consistent style
- **Code Review Simulation**
  - **Goal**: Identify potential code smells and design flaws before submission
  - **Input**: Pull request diff or source file
  - **Output**: List of constructive critiques and improvement suggestions

## Debugging
- **Error Explanation**
  - **Goal**: Understand the root cause of a specific stack trace or error log
  - **Input**: Error message and relevant code snippet
  - **Output**: Step-by-step breakdown of why the error occurs and how to fix it
- **Edge Case Identification**
  - **Goal**: Find hidden bugs or boundary conditions that might break the code
  - **Input**: Function definition and its business logic
  - **Output**: List of scenarios (e.g., null inputs, empty arrays) to guard against

## Documentation
- **API Docstring Generation**
  - **Goal**: Automatically document functions and methods using standard formats (e.g., JSDoc, Sphinx)
  - **Input**: Undocumented source code
  - **Output**: Code updated with comprehensive inline documentation and parameter descriptions
- **README Authoring**
  - **Goal**: Create clear, user-friendly instructions for setting up and running a repository
  - **Input**: Project structure details, tech stack, and installation steps
  - **Output**: Structured Markdown file with setup guides and usage examples

## Testing
- **Unit Test Generation**
  - **Goal**: Achieve comprehensive test coverage for a specific component
  - **Input**: Source function and the preferred testing framework (e.g., Jest, PyTest)
  - **Output**: Suite of test cases covering happy paths and error states
- **Mock Data Creation**
  - **Goal**: Generate realistic datasets for local development or integration tests
  - **Input**: Database schema or JSON structure description
  - **Output**: Array of diverse dummy records fitting the required types
