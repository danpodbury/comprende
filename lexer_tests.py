import lexer

def test_indexes():
    test_string = "12 + 15 + abcdf"
    expected_indicies = [0, 3, 5, 8, 10, 15]
    l = lexer.Lexer(test_string)
    output = l.lex()
    out_indexes = [x.start_pos for x in output]

    return expected_indicies == out_indexes

def test_types():
    test_string = '12 + 15 * abcdf "string" '
    expected_tokens = [lexer.Tokens.num, lexer.Tokens.plus, lexer.Tokens.num,
                         lexer.Tokens.times, lexer.Tokens.iden, lexer.Tokens.string, lexer.Tokens.EOF]
    l = lexer.Lexer(test_string)
    output = l.lex()
    out_tokens = [x.t_type for x in output]

    return expected_tokens == out_tokens

def test_parse_string():
    test_string = '"string_of_length_19'    # notice the missing end quote
    expected_len = 19
    l = lexer.Lexer(test_string)
    output = l.lex()

    out_type_correct = output[0].t_type == lexer.Tokens.string
    out_len = len(output[0].text[slice(1, -1)])

    return expected_len == out_len and out_type_correct

def run_tests():
    print(f"Running lexer tests...")

    result = "Passed" if test_indexes() else "Failed"
    print(f"Test: test_indexes() {result}")

    result = "Passed" if test_types() else "Failed"
    print(f"Test: test_types() {result}")

    result = "Passed" if test_parse_string() else "Failed"
    print(f"Test: test_parse_string() {result}")


run_tests()