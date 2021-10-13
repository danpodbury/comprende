import sys
from lexer import *
from token_parser import *
from interpreter import Interpreter
import json

def read_source(filename: str) -> str:
    source_code = ""
    with open(filename, 'r') as file:
        source_code = file.read()
    return source_code

def write_to_json(AST: dict, filename: str) -> None:
    with open(filename, 'w') as file:
        json.dump(AST, file, indent = 4)

def read_json(filename) -> dict:
    with open(filename, 'r') as file:
        return json.load(file)


def main(source_code):

    print("Constructing Lexemes...")
    lexer = Lexer(source_code)
    lexer.lex()
    lexer.display()

    tokens = lexer.lex()

    print("\nConstructing AST...")
    AST = TokenParser(tokens).parse()

    print(AST)

    print("\nWriting to json ...")
    write_to_json(AST, "./output/AST.json")

    print("\nInterpreting AST ...")
    print("\n============")
    print("Output:")
    inter = Interpreter()
    expression_stream = inter.interp(AST)
    [print(x) for x in expression_stream]

    print()

if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1:
        print(type(args[1]))
        if args[1][:1] == ">":  # use string as input if no file specified
            source_code = args[1][1:]
        else:
            source_code = read_source(args[1])

        main(source_code)

    else:
        print("Usage: py comprende.py <sourcefile.txt>  OR")
        print("       py comprende.py '> source code...'")
        print("Please specify sourcefile or source string\n")
