import calculator
from sys import stdin


calc = calculator.DefaultCalculator()

while True:
    input = stdin.readline().strip('\n')
    if input == "q": quit()

    tokens = input.split(' ')
    print(calc.calc(tokens))
    

