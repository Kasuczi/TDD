import unittest
from src.fizzbuzz import fizzbuzz

class FizzTest(unittest.TestCase):

    def testfirstCase(self):
        """
        test fizzbuzz
        :return:
        """
        self.assertEqual(fizzbuzz(3), 'Fizz')
        self.assertEqual(fizzbuzz(5), 'Buzz')
        self.assertEqual(fizzbuzz(15), 'FizzBuzz')
        self.assertEqual(fizzbuzz(30), 'FizzBuzz')

