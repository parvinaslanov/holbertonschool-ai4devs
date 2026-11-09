# Codebase Overview - Legacy System

## Age
First release in 2011, last major update in 2016.

## Size
~52,000 LOC across legacy modules.

## Dependencies
- PHP 5.4 / Legacy MySQL driver (`ext/mysql`)
- Outdated third-party authentication library (unsupported)
- Custom procedural helper utilities

## Issues
- Total lack of automated test coverage
- Tightly coupled business logic and UI templates
- Mixed procedural and object-oriented programming styles
- High vulnerability risk due to deprecated database drivers and outdated dependencies
