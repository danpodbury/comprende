from enum import Enum, auto


class Tokens(Enum):
    num = auto()
    plus = auto()
    times = auto()
    string = auto()
    iden = auto()
    comment = auto()
    EOF = auto()


class Token:
    def __init__(self, start_pos: int, t_type: Tokens, text: str = ""):
        self.t_type = t_type
        self.text = text
        self.start_pos = start_pos

    def __str__(self):
        return f"index = [{self.start_pos}], type = {self.t_type}, text = '{self.text}'"


class Lexer:
    def __init__(self, input_string: str):
        self.input_string = input_string
        self.tokens = []

    def display(self):
        for t in self.tokens:
            print(t)

    def lex(self):
        # constructs a list of tokens from a text string
        self.tokens = []
        pos = 0
        input_len = len(self.input_string)

        while pos < input_len:
            tokenpos = pos
            look_ahead = self.input_string[pos]

            # step through characters and identify tokens
            if look_ahead.isspace():
                pos += 1
            elif look_ahead == "+":
                self.tokens.append(Token(tokenpos, Tokens.plus))
                pos += 1
            elif look_ahead == "*":
                self.tokens.append(Token(tokenpos, Tokens.times))
                pos += 1
            elif look_ahead.isdigit():
                text = ""
                while pos < input_len and self.input_string[pos].isdigit():
                    text += self.input_string[pos]
                    pos += 1
                self.tokens.append(Token(tokenpos, Tokens.num, text=text))
                pos += 1
            elif look_ahead.isalpha():
                text = ""
                while pos < input_len and self.input_string[pos].isalpha():
                    text += self.input_string[pos]
                    pos += 1
                self.tokens.append(Token(tokenpos, Tokens.iden, text=text))
                pos += 1
            elif look_ahead == '"':
                text = '"'
                pos += 1  # skip the quotation
                while pos < input_len:
                    if self.input_string[pos] != '"':
                        text += self.input_string[pos]
                    else:
                        break
                    pos += 1
                text += '"'
                self.tokens.append(Token(tokenpos, Tokens.string, text=text))
                pos += 1
            elif look_ahead == "'":
                text = "'"
                pos += 1  # skip the quotation
                while pos < input_len:
                    if self.input_string[pos] != "'":
                        text += self.input_string[pos]
                    else:
                        break
                    pos += 1
                text += "'"
                self.tokens.append(Token(tokenpos, Tokens.string, text=text))
                pos += 1
            elif look_ahead == "~":
                text = ""
                pos += 1
                while pos < input_len:
                    if "\n" not in self.input_string[pos]:
                        text += self.input_string[pos]
                    else:
                        break
                    pos += 1
                self.tokens.append(Token(tokenpos, Tokens.comment, text=text))
                pos += 1
            else:
                print(f"Unknown Token at {tokenpos}")
                pos += 1

        self.tokens.append(Token(input_len, Tokens.EOF))
        return self.tokens
