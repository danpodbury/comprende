import unittest
from token_parser import TokenParser
from lexer import Token, Tokens, Lexer


class TestTokenParser(unittest.TestCase):
    def test_num_literal(self):
        # can you declare num literals
        test_string = "42;"
        tokens = Lexer(test_string).lex()
        output = TokenParser(tokens).parse()
        expected = {'type': 'Program',
                    'Body': [{'type': 'ExpressionStatement',
                              'expression': {'type': 'NumLiteral', 'value': 42.0}}]}
        self.assertDictEqual(output, expected)

    def test_string_literal(self):
        # can you declare string literals
        test_string = "'string';"
        tokens = Lexer(test_string).lex()
        output = TokenParser(tokens).parse()
        expected = {'type': 'Program',
                    'Body': [{'type': 'ExpressionStatement',
                              'expression': {'type': 'StringLiteral', 'value': 'string'}}]}
        self.assertDictEqual(output, expected)

    def test_addition(self):
        # can you add two numbers
        test_string = "10 + 5"
        tokens = Lexer(test_string).lex()
        output = TokenParser(tokens).parse()
        expected = {'type': 'Program',
                    'Body': [{'type': 'ExpressionStatement',
                              'expression': {'type': 'BinaryExpression', 'operator': '+',
                                             'left': {'type': 'NumLiteral', 'value': 10.0},
                                             'right': {'type': 'NumLiteral', 'value': 5.0}}}]}
        self.assertDictEqual(output, expected)

    def test_multiplication(self):
        # can you multiply two numbers
        test_string = "2 * 2"
        tokens = Lexer(test_string).lex()
        output = TokenParser(tokens).parse()
        expected = {'type': 'Program',
                    'Body': [{'type': 'ExpressionStatement',
                              'expression': {'type': 'BinaryExpression', 'operator': '*',
                                             'left': {'type': 'NumLiteral', 'value': 2.0},
                                             'right': {'type': 'NumLiteral', 'value': 2.0}}}]}
        self.assertDictEqual(output, expected)

    def test_order_of_ops(self):
        # do complex expressions obey BOD(MA)S
        test_string = "10 + 2 * 2 + 1;"
        tokens = Lexer(test_string).lex()
        output = TokenParser(tokens).parse()
        expected = {'type': 'Program',
                    'Body': [{'type': 'ExpressionStatement',
                              'expression': {'type': 'BinaryExpression', 'operator': '+',
                                             'left': {'type': 'BinaryExpression', 'operator': '+',
                                                      'left': {'type': 'NumLiteral', 'value': 10.0},
                                                      'right': {'type': 'BinaryExpression', 'operator': '*',
                                                                'left': {'type':'NumLiteral', 'value': 2.0},
                                                                'right': {'type': 'NumLiteral', 'value': 2.0}}},
                                             'right': {'type': 'NumLiteral', 'value': 1.0}}}]}
        self.assertDictEqual(output, expected)

    def test_expr_end_removed(self):
        # is expr_end token removed from AST
        test_stringA = "10 + 2 * 2 + 1;"
        test_stringB = "10 + 2 * 2 + 1"
        tokensA = Lexer(test_stringA).lex()
        outputA = TokenParser(tokensA).parse()

        tokensB = Lexer(test_stringB).lex()
        outputB = TokenParser(tokensB).parse()

        self.assertDictEqual(outputA, outputB)