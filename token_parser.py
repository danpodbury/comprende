# recursive decent parser

from __future__ import annotations
from lexer import Token, Tokens
from enum import Enum

class NodeType(str, Enum):
    Program = 'Program'
    ExpressionStatement = "ExpressionStatement"
    BinaryExpression = "BinaryExpression"
    NumLiteral = "NumLiteral"
    StringLiteral = "StringLiteral"


class TokenParser:
    def __init__(self, tokens: list[Token]):
        self.tokens: list[Token] = tokens

    def parse(self):
        return self.Program()

    def _eat(self, expected_type):
        if len(self.tokens) == 0:
            print(f"Parsing Error: Unexpected end of input! Was expecting {expected_type}")
            return None

        top = self.tokens.pop(0)
        if top.t_type != expected_type:
            if expected_type == Tokens.expr_end and top.t_type == Tokens.EOF:
                print(f"Warning: Reached end of file before end of expression (are you missing a semicolon?)")
            else:
                print(f"Parsing Error: Expected {expected_type} but found {top.t_type}!")
            return None

        return top

    def Program(self):
        # Program : StatementList
        return {"type": NodeType.Program,
                "Body": self.StatementList()}

    def StatementList(self):
        # StatementList : StatementList Statement | Statement
        statementList = [self.Statement()]

        while len(self.tokens) > 1:
            statementList.append(self.Statement())

        return statementList

    def Statement(self):
        # Statement : ExpressionStatement
        return self.ExpressionStatement()

    def ExpressionStatement(self):
        # ExpressionStatement : Expression ';'
        expression = self.Expression()
        self._eat(Tokens.expr_end)
        return {"type": NodeType.ExpressionStatement,
                "expression": expression
        }

    def Expression(self):
        # Expression : Literal
        return self.AdditiveExpression()

    def AdditiveExpression(self):
        # AdditiveExpression : Literal | AdditiveExpression +/- Literal
        left = self.MultiplicativeExpression()
        while self.tokens[0].t_type == Tokens.plus or self.tokens[0].t_type == Tokens.minus:
            operator = self.Operator(self._eat(self.tokens[0].t_type).t_type)
            right = self.MultiplicativeExpression()

            left = {"type": NodeType.BinaryExpression,
                    "operator": operator,
                    "left": left,
                    "right": right}

        return left

    def MultiplicativeExpression(self):
        # MultiplicativeExpression : PrimaryExpression | MultiplicativeExpression * PrimaryExpression
        left = self.PrimaryExpression()
        while self.tokens[0].t_type == Tokens.times:
            operator = self.Operator( self._eat(Tokens.times).t_type )
            right = self.PrimaryExpression()

            left = {"type": NodeType.BinaryExpression,
                    "operator": operator,
                    "left": left,
                    "right": right}

        return left

    def PrimaryExpression(self):
        # PrimaryExpression : Literal
        return self.Literal()

    def Literal(self):
        # Literal : NumLiteral | StringLiteral
        assert(len(self.tokens) > 0)
        assert(self.tokens[0].t_type == Tokens.num or self.tokens[0].t_type == Tokens.string)

        if self.tokens[0].t_type == Tokens.num:
            return self.NumLiteral()
        else:
            return self.StringLiteral()

    def Operator(self, type):
        if type == Tokens.plus: return "+"
        if type == Tokens.minus: return "-"
        if type == Tokens.times: return "*"

    def NumLiteral(self):
        # NumLiteral : Number
        token = self._eat(Tokens.num)
        return {"type": NodeType.NumLiteral,
                "value": float(token.text)}

    def StringLiteral(self):
        # StringLiteral : String
        token = self._eat(Tokens.string)
        return {"type": NodeType.StringLiteral,
                "value": token.text[slice(1, -1)]}
