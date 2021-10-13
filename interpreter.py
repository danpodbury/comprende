class Interpreter:
    def __init__(self):
        self.expression_stream = []

    def interp(self, n):

        if n is None: return None

        # parse expression list
        if type(n) == list:
            for expr in n:
                self.expression_stream.append(self.interp(expr))

            return self.expression_stream

        if n['type'] == 'dummyVal':             return n['value']
        if n['type'] == 'Program':              return self.interp(n['Body'])
        if n['type'] == "ExpressionStatement":  return self.interp(n['expression'])
        if n['type'] == "BinaryExpression":
            if n['operator'] == '+':            return self.interp(n['left']) + self.interp(n['right'])
            if n['operator'] == '*':            return self.interp(n['left']) * self.interp(n['right'])

        if n['type'] == 'NumLiteral':           return n['value']
        if n['type'] == 'StringLiteral':        return n['value']

