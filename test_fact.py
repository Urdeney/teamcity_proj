import unittest
from fact import fact

class FactorialTest(unittest.TestCase):
    def test_factorial1(self):
        self.assertEqual(fact(2), 2)

    def test_factorial2(self):
        self.assertEqual(fact(3), 6)

    def test_factorial3(self):
        self.assertEqual(fact(4), 24)

    def test_factorial4(self):
        self.assertEqual(fact(5), 120)

    def test_factorial5(self):
        self.assertEqual(fact(6), 720)

    def test_factorial6(self):
        self.assertEqual(fact(7), 5040)
    
    def test_factorial7(self):
        self.assertEqual(fact(8), 40320)

    def test_factorial8(self):
        self.assertEqual(fact(9), 362880)

    def test_factorial9(self):
        self.assertEqual(fact(10), 3628800)

if __name__ == '__main__':
    unittest.main()