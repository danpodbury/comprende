# recursive decent parser

from __future__ import annotations
from lexer import Token, Tokens


class TokenParser:
    def __init__(self, tokens: list[Token]):
        self.tokens: list[Token] = tokens

    def parse(self):
        return self.Program()

    def _eat(self, expected_type):
        if len(self.tokens) == 0:
            print(f"Parsing error: Unexpected end of input! Was expecting {expected_type}")
            return None

        top = self.tokens.pop(0)
        if top.t_type != expected_type:
            print(f"Parsing error: Expected {expected_type} but found {top.t_type}!")
            return None

        return top

    def Program(self):
        # Program : Literal
        return {'type': 'Program',
                'Body': self.Literal()}

    def Literal(self):
        # Literal : NumLiteral | StringLiteral
        assert(len(self.tokens) > 0)
        assert(self.tokens[0].t_type == Tokens.num or self.tokens[0].t_type == Tokens.string)

        if self.tokens[0].t_type == Tokens.num:
            return self.NumLiteral()
        else:
            return self.StringLiteral()

    def NumLiteral(self):
        # NumLiteral : Number
        token = self._eat(Tokens.num)
        return {'type': 'NumLiteral',
                'value': float(token.text)}

    def StringLiteral(self):
        # StringLiteral : String
        token = self._eat(Tokens.string)
        return {'type': 'StringLiteral',
                'value': token.text[slice(1, -1)]}
