import unittest
from lexer import Token, Tokens, Lexer


class TestLexer(unittest.TestCase):

    def test_indexes(self):
        test_string = "12 + 15 + abcdf"
        tokens = Lexer(test_string).lex()
        output = [x.start_pos for x in tokens]

        expected = [0, 3, 5, 8, 10, 15]

        self.assertListEqual(expected, output)

    def test_types(self):
        test_string = '12 + 15 * abcdf "string" '
        tokens = Lexer(test_string).lex()
        output = [x.t_type for x in tokens]

        expected = [Tokens.num, Tokens.plus, Tokens.num, Tokens.times, Tokens.iden, Tokens.string, Tokens.EOF]

        self.assertListEqual(expected, output)

    def test_parse_string(self):
        test_string = '"string_of_length_19'    # notice the missing end quote
        tokens = Lexer(test_string).lex()

        out_type_correct = tokens[0].t_type == Tokens.string
        self.assertIs(out_type_correct, True)

        out_len = len(tokens[0].text[slice(1, -1)])
        expected = 19
        self.assertEqual(expected, out_len)

