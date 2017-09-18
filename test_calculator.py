import unittest
import calculator

class CalculatorTestCase(unittest.TestCase):
    """Tests for calculator"""

    def testInfixCalc(self):
        testCases = [
            {"infix": "18 - 6 * 2",                "res": 6},
            {"infix": "10 + 3 * ( 2 + 6 )",        "res": 34},
            {"infix": "50 - 10 * ( 4 - 2 ) + 6",   "res": 36},
            {"infix": "2 * 9 - 3 * ( 6 - 1 ) + 1", "res": 4}
        ]

        calc = calculator.DefaultCalculator()
        for testCase in testCases:
            assert calc.calc(testCase["infix"].split(' ')) == testCase["res"]

    def testPostfixCalc(self):
        testCases = [
            {"rpn": "18 6 2 * -",                "res": 6},
            {"rpn": "10 3 2 6 + * +",            "res": 34},
            {"rpn": "50 10 4 2 - * - 6 +",       "res": 36},
            {"rpn": "2 9 * 3 6 1 - * - 1 +",     "res": 4}
        ]
       
        calc = calculator.DefaultCalculator()
        for testCase in testCases:
            assert calc.calcRPN(testCase["rpn"].split(' ')) == testCase["res"] 

if __name__ == '__main__':
    unittest.main()
