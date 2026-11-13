# Documentation: Legacy Code Interpreter

## Overview
The legacy code interpreter module handles parsing, syntax tokenization, and code execution for the legacy runtime environment.

## Major Modules
- **Parser (`parser.py`)**: Responsible for breaking down source text strings into clean Abstract Syntax Tree (AST) tokens.
- **Executor (`executor.py`)**: Executes parsed operations, manages runtime memory states, and catches evaluation exceptions.
