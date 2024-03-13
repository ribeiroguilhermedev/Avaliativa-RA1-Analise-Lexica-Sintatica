# Math Operations Analysis

## Group Information
- **Group**: RA1 18
- **Author**: Guilherme Ribeiro Thomaz
- **Course**: Fundamentos de Sistemas Ciberfísicos

## File Descriptions

### MathOperations.interp
This file aids in interpreting mathematical operations defined in a grammar. It contains information about token types and rules, such as mathematical operators, numbers, and whitespaces, as well as demonstrating how the grammar is internally represented for analysis.

### MathOperations.tokens
A file that maps token names to numeric values, like numbers or mathematical operators ('+', '-', etc.), making it easier to identify parts of the input text during analysis.

### MathOperationsLexer.interp and MathOperationsLexer.py
These files are part of the process that breaks down text input into tokens (basic units of meaning), like numbers or operators. They include details on which characters or keywords are recognized.

### MathOperationsParser.py
This file is responsible for organizing tokens according to the grammar's rules, determining how different parts of a mathematical expression fit together to make sense.

### MathOperationsListener.py
Defines actions that occur when entering or exiting specific parts of the grammar during analysis, allowing reactions to different parts of the processed mathematical expressions.

### main.py
The starting point for the program that uses ANTLR to analyze mathematical operations. It includes initial setup, necessary imports, and the definition of how to handle syntax errors, using the grammar and generated files to analyze and respond to mathematical operations.

## Compilation Command

The command `antlr4 -Dlanguage=Python3 MathOperations.g4 -o output` is essential for converting the grammar defined in the MathOperations.g4 file into executable Python code that can be used to parse mathematical expressions. The MathOperations.g4 file contains the definition of a custom grammar for mathematical operations, including rules that specify how to interpret expressions made up of numbers, arithmetic operators (such as '+', '-', '*', '/', '^', '%', '|'), and special keywords ('MEM' and 'RES').

## Testing Infrastructure

### tests Folder
The `tests` folder contains `.txt` files with the mathematical operations that will be tested by the program. These files serve as input to verify the program's capability to accurately analyze and interpret the defined mathematical expressions according to the custom grammar.

### tests/reports Folder
The `tests/reports` folder will contain the compliance report for each test `.txt` file. There will be an error file, demonstrating the errors found by the analyzer, and a success file demonstrating the semantic tree. This structure is designed to facilitate detailed analysis and debugging of the program's performance on test inputs, ensuring that the analyzer can accurately process and understand the mathematical expressions as intended.
