import sys
import time
from lexer import *
from token_parser import *

def read_source(filename):
    source_code = ""
    with open(filename, 'r') as file:
        source_code = file.read()
    return source_code

def main(source_code):

    print("Constructing Lexemes...")
    lexr = Lexer(source_code)
    lexr.lex()
    lexr.display()

    tokens = lexr.lex()

    print("\nConstructing AST...")
    AST = TokenParser(tokens).parse()
    print(AST)



if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1:
        source_code = read_source(args[1])
    else:
        print("Usage: py comprende.py <sourcefile.txt>")
        print("Please specify sourcefile.\n")
        print("Running default source file...\n")

        source_code = read_source("./scripts/default_code.txt")
    main(source_code)