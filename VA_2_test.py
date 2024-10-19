import unittest

from MA2 import *

variables_init = {"ans": 0.0, "E": math.e, "PI": math.pi}


class Test(unittest.TestCase):


    def test_functions(self):
        print('\n\nTesting functions')
        variables = variables_init
        tests = {'5*min(2,1,3)': 5.,
                 'min(3,2,1) + 2*5': 11.,
                 }
        for line, answer in tests.items():
            print(f'{line:30s} expects {answer:-8}', end='\t')
            wtok = TokenizeWrapper(line)
            result = statement(wtok, variables)
            print(f'got {round(result,15):-8}')
            self.assertAlmostEqual(result, answer)

    def test_integer_functions(self):
        print('\n\nTesting functions returning int')
        variables = variables_init
        tests = {
            'fib(4)': 3,
            'fib(10)': 55,
            'fib(100)': 354224848179261915075,
            'fib(103)': 1500520536206896083277
        }
        for line, answer in tests.items():
            print(f'{line:10s} expects {answer:-27}', end=' ')
            wtok = TokenizeWrapper(line)
            result = statement(wtok, variables)
            print(f'got {round(result,25):-27}')
            self.assertEqual(result, answer)

    def test_exceptions(self):
        print('\n\nTesting exceptions')
        variables = variables_init

        tests = ['std(1,2 3), min()']

        for line in tests:
            print(f'{line:30s} expects SyntaxError', end=' \t \t ')
            wtok = TokenizeWrapper(line)
            with self.assertRaises(SyntaxError):
                result = statement(wtok, variables)
            print('Got it')

        tests = ['fib(-1)', 'fib(1.5)']
        for line in tests:
            print(f'{line:30s} expects EvaluationError', end=' \t \t ')
            wtok = TokenizeWrapper(line)
            with self.assertRaises(EvaluationError):
                result = statement(wtok, variables)
            print('Got it')

if __name__ == "__main__":
    print('\n\nThe testcode initializes variables to\n', variables_init)
    unittest.main()

"""
Answers can be provided here:

What is the output of the calculator if the line is std() without arguments?

Are you able to change the value of PI? 

If yes, how can you fix this?

What technique did you use to calculate large Fibonacci numbers?

"""
