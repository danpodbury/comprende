import sys
from lexer import *
from token_parser import *
from interpreter import Interpreter
from utils import write_to_json, read_source

def main(source_code):

    lexer = Lexer(source_code)
    tokens = lexer.lex()

    AST = TokenParser(tokens).parse()

    write_to_json(AST, "./output/AST.json")

    inter = Interpreter()
    expression_stream = inter.interp(AST)
    [print(x) for x in expression_stream]


if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1:
        if args[1][:1] == ">":  # use string as input if no file specified
            source_code = args[1][1:]
        else:
            source_code = read_source(args[1])

        main(source_code)

    else:
        print("Usage: py comprende.py <sourcefile.txt>  OR")
        print("       py comprende.py '> source code...'")
        print("Please specify sourcefile or source string\n")
