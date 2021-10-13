import unittest
from comprende import *
from utils import write_to_json, read_json

class TestComprende(unittest.TestCase):

    def test_write_json(self):
        # does write_to_json output in expected format
        test_AST = {'type': NodeType.Program,
                    'Body': [{'type': NodeType.ExpressionStatement,
                              'expression': {'type': NodeType.NumLiteral, 'value': 5.0}}]}

        expected = read_source("./output/test_AST_valid.json")

        write_to_json(test_AST, "./output/test_AST.json" )
        output = read_source("./output/test_AST.json")

        self.assertEqual(expected, output)


    def test_read_json(self):
        # does reading a json file correcting import an AST
        test_AST = {'type': 'Program',
                    'Body': [{'type': 'ExpressionStatement',
                              'expression': {'type': 'BinaryExpression', 'operator': '+',
                                             'left': {'type': 'NumLiteral', 'value': -2.0},
                                             'right': {'type': 'NumLiteral', 'value': 10.0}}}]}

        write_to_json(test_AST, "./output/test_AST.json" )
        output = read_json("./output/test_AST.json")

        expected = {'type': 'Program', 'Body': [{'type': 'ExpressionStatement', 'expression': {'type': 'BinaryExpression', 'operator': '+', 'left': {'type': 'NumLiteral', 'value': -2.0}, 'right': {'type': 'NumLiteral', 'value': 10.0}}}]}

        self.assertDictEqual(expected, output)
