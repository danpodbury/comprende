import unittest
from interpreter import Interpreter
from lexer import Lexer
from token_parser import *

class TestInterpreter(unittest.TestCase):

    def test_NumLiteral(self):
        expected = 2.0

        test_AST = {'type': 'NumLiteral', 'value': expected}
        output = Interpreter().interp(test_AST)

        self.assertEqual(expected, output)

    def test_stringLiteral(self):
        expected = 'this is a string'

        test_AST = {'type': 'StringLiteral', 'value': expected}
        output = Interpreter().interp(test_AST)

        self.assertEqual(expected, output)

    def test_dummy_value(self):
        expected = 5
        test_AST = {'type': 'dummyVal', 'value': expected}
        output = Interpreter().interp(test_AST)

        self.assertEqual(expected, output)


    def test_read_body(self):
        valueA = 5
        valueB = 10
        test_AST = [{'type': 'dummyVal', 'value': valueA}, {'type': 'dummyVal', 'value': valueB}]
        expected = [valueA, valueB]

        inter =  Interpreter()
        inter.interp(test_AST)
        output = inter.expression_stream

        self.assertListEqual(expected, output)

    def test_addition(self):
        val1 = -2.0
        val2 = 10.0
        test_AST = {'type': 'Program',
                    'Body': [{'type': 'ExpressionStatement',
                              'expression': {'type': 'BinaryExpression', 'operator': '+',
                                             'left': {'type': 'NumLiteral', 'value': val1},
                                             'right': {'type': 'NumLiteral', 'value': val2}}}]}

        output_stream = Interpreter().interp(test_AST)
        output = output_stream[0]

        expected = val1 + val2

        self.assertEqual(expected, output)

    def test_precedence(self):
        test_expression = "2 + 10 * 5;"

        lexer = Lexer(test_expression)
        tokens = lexer.lex()

        AST = TokenParser(tokens).parse()

        output_stream = Interpreter().interp(AST)
        output = output_stream[0]

        expected = 2 + (10 * 5)

        self.assertEqual(expected, output)
