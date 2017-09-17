from sys import stdin

class Calculator:
    def __init__(self, operators):
        self.operators = operators

    def calc(self, s):
        return self.__calcRPN(self.__infixToRPN(s.split(' ')))

    def __infixToRPN(self, tokens):
        output = []
        opstack = []

        for tok in tokens:
            if tok in self.operators:
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
                output.append(tok)
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
            else:
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
