# Prompt Use Cases

## 1. Code Quality

### 1.1 Code Refactoring
- **Goal:** Improve code readability, maintainability, and performance without changing its functionality.
- **Input:** An existing source code function or file written in a specified programming language.
- **Expected Output:** Refactored and optimized code with a clear explanation of the improvements made.

### 1.2 Style Enforcement
- **Goal:** Ensure consistent coding standards, naming conventions, indentation, and formatting throughout a project.
- **Input:** A source code file or code snippet that needs formatting and style improvements.
- **Expected Output:** Rewritten code that follows consistent naming conventions, formatting rules, and best practices.

### 1.3 Code Review Simulation
- **Goal:** Identify code smells, inefficient logic, security concerns, and potential design flaws before submission.
- **Input:** A pull request diff, source code file, or selected code snippet.
- **Expected Output:** A structured code review containing identified issues, constructive feedback, and specific recommendations for improvement.

## 2. Debugging

### 2.1 Error Explanation
- **Goal:** Understand the root cause of programming errors and learn how to resolve them.
- **Input:** An error message, stack trace, and the relevant source code.
- **Expected Output:** A step-by-step explanation of the error, its likely cause, and a corrected solution.

### 2.2 Edge Case Identification
- **Goal:** Discover hidden bugs and unexpected scenarios that could cause a program to fail.
- **Input:** A function, its source code, and a description of its intended behavior.
- **Expected Output:** A list of potential edge cases, such as null values, empty arrays, invalid inputs, and boundary conditions, along with suggestions for handling them.

### 2.3 Bug Fixing
- **Goal:** Locate and fix logical or runtime errors while preserving the intended functionality of the program.
- **Input:** Source code containing a bug, together with a description of the unexpected behavior.
- **Expected Output:** Corrected code, an explanation of the identified bug, and a summary of the changes made.

## 3. Documentation

### 3.1 API Docstring Generation
- **Goal:** Improve code documentation by automatically generating clear descriptions of functions, methods, and parameters.
- **Input:** Source code containing undocumented functions or methods.
- **Expected Output:** Updated code with comprehensive documentation using an appropriate standard, such as JSDoc, Python docstrings, or Sphinx.

### 3.2 README Authoring
- **Goal:** Create clear and accessible documentation that helps users understand, install, and run a software project.
- **Input:** Project structure, programming languages, technologies used, dependencies, and installation instructions.
- **Expected Output:** A well-organized README.md file containing a project overview, setup instructions, usage examples, and relevant documentation.

### 3.3 Technical Documentation Generation
- **Goal:** Explain how a software application, system, or individual component works so that developers can understand and maintain it.
- **Input:** Source code, system architecture details, and descriptions of important components and workflows.
- **Expected Output:** Structured technical documentation covering system functionality, component descriptions, workflows, dependencies, and implementation details.

## 4. Testing

### 4.1 Unit Test Generation
- **Goal:** Improve software reliability by creating tests that verify individual functions and components.
- **Input:** Source code, the expected behavior of the component, and a preferred testing framework, such as Jest or PyTest.
- **Expected Output:** A collection of unit tests covering normal scenarios, edge cases, and error conditions, with clear test descriptions.

### 4.2 Mock Data Creation
- **Goal:** Generate realistic sample data for development, testing, and debugging without relying on production information.
- **Input:** A database schema, JSON structure, or description of the required data fields and data types.
- **Expected Output:** A structured collection of realistic dummy records that follow the specified schema and include diverse test scenarios.

### 4.3 Test Case Generation
- **Goal:** Identify different scenarios that should be tested to verify that an application or feature works correctly.
- **Input:** A feature description, functional requirements, user stories, or application specifications.
- **Expected Output:** A comprehensive set of test cases containing test descriptions, preconditions, execution steps, expected results, and relevant test scenarios.
