import unittest
import calculator

class CalculatorTestCase(unittest.TestCase):
    """Tests for calculator"""

    def testCalc(self):
        testCases = [
            {"infix": "18 - 6 * 2",                "res": 6},
            {"infix": "10 + 3 * ( 2 + 6 )",        "res": 34},
            {"infix": "50 - 10 * ( 4 - 2 ) + 6",   "res": 36},
            {"infix": "2 * 9 - 3 * ( 6 - 1 ) + 1", "res": 4}
        ]

        calc = calculator.DefaultCalculator()
        for testCase in testCases:
            assert calc.calc(testCase["infix"]) == testCase["res"]

if __name__ == '__main__':
    unittest.main()
