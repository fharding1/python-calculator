from sys import stdin

class Calculator:
    def __init__(self, operators):
        for op, info in operators.iteritems():
            self.operators[op] = info

    def calc(self, s):
        return self.__calcRPN(self.__infixToRPN(s.split(' ')))

    def __isNumber(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def __infixToRPN(self, tokens):
        output = []
        opstack = []

        for tok in tokens:
            if self.__isNumber(tok):
                output.append(tok)
            elif tok in self.operators:
                while len(opstack) > 0 and self.operators[opstack[-1]]["prec"] >= self.operators[tok]["prec"] and self.operators[tok]["assoc"] == 'left':
                    output.append(opstack.pop())
                opstack.append(tok)
            elif tok == '(':
                opstack.append(tok)
            elif tok == ')':
                while opstack[-1] != '(':
                    output.append(opstack.pop())
                opstack.pop()
            else:
                raise ValueError("invalid token: {0} is not a number or an operator or parenthesis".format(tok))

        while opstack:
            output.append(opstack.pop())

        print(output)
        return output

    def __calcRPN(self, tokens):
        stack = []
        for tok in tokens:
            print(stack, tok)
            if tok in self.operators:
                op2, op1 = stack.pop(), stack.pop()
                stack.append(self.operators[tok]['lambda'](op1, op2))
            elif self.__isNumber(tok):
                stack.append(float(tok))
        return stack.pop()

class DefaultCalculator(Calculator):
    def __init__(self):
        self.operators = {
            '+': {'prec': 1, 'assoc': 'left', 'lambda': lambda a,b: a+b},
            '-': {'prec': 1, 'assoc': 'left', 'lambda': lambda a,b: a-b},
            '*': {'prec': 2, 'assoc': 'left', 'lambda': lambda a,b: a*b},
            '/': {'prec': 2, 'assoc': 'left', 'lambda': lambda a,b: a/b},
            '^': {'prec': 3, 'assoc': 'right', 'lambda': lambda a,b: a**b}
        }


print(DefaultCalculator().calc(stdin.readline().strip('\n')))
