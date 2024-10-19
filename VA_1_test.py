# https://docs.python.org/3/library/unittest.html
import unittest

from VA_1 import *

class Test(unittest.TestCase):

    def test_zippa(self):
        print('\nTests zippa')
        self.assertEqual(zippa([], []), [])
        self.assertEqual(zippa([], [3]), [3])
        self.assertEqual(zippa([2], []), [2])
        l1 = [1, 3, 5, 7, 9]
        l2 = [2, 4, 6]
        l3 = zippa(l1, l2)
        self.assertEqual(l3, [1, 2, 3, 4, 5, 6, 7, 9],
                         msg="zippa doesn't produce the right output")
        self.assertEqual(l1, [1, 3, 5, 7, 9],
                         msg='zippa destroys the first argument')
        self.assertEqual(l2, [2, 4, 6],
                         msg='zippa destroys the second argument')
        l1.append(42)
        l2.append(43)
        l3.append(44)
        self.assertEqual(l1, [1, 3, 5, 7, 9, 42],
                         msg='The involved lists are linked together')
        self.assertEqual(l2, [2, 4, 6, 43],
                         msg='The involved lists are linked together')
        self.assertEqual(l3, [1, 2, 3, 4, 5, 6, 7, 9, 44],
                         msg='The involved lists are linked together')
        l1 = [1, 2]
        l2 = zippa(l1, [])
        l1.append(3)
        self.assertEqual(l2, [1, 2],
                         msg='The zippa result is affected by later appends to the parameter list')
        l2.append(5)
        self.assertEqual(l1, [1, 2, 3],
                         msg='The parameter list is affected by later appends to the zippa result')


if __name__ == "__main__":
    unittest.main()
