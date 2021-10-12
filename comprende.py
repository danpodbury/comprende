import sys
from lexer import *
from token_parser import *

def read_source(filename: str):
    source_code = ""
    with open(filename, 'r') as file:
        source_code = file.read()
    return source_code

def write_to_json(string: str):
    with open("./output/AST.json", 'w') as file:
        file.write(string)

def main(source_code):

    print("Constructing Lexemes...")
    lexr = Lexer(source_code)
    lexr.lex()
    lexr.display()

    tokens = lexr.lex()

    print("\nConstructing AST...")
    AST = TokenParser(tokens).parse()
    print(AST)

    print("\nWriting to ./output/AST.json ...\n")
    write_to_json(str(AST))


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
