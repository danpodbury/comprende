# Comprende

> A custom barebones interpreter written in python.

## Currently features

### Lexer supporting the following tokens
- plus (+)
- times (*)
- number literals
- string literals
- comments

### Parser
- single String or Number literal
- multiple expressions
- additive expressions
- multiplicative expressions

## Usage

    py comprende.py <sourcefile.txt>
    py comprende.py "> source code here"

- if no file is specified comprende will run scripts/default_code.txt

## Current Limitations
- indentifiers can only be alphabetical