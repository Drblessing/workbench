import unittest
from package1.module1 import function1
from package2.module2 import function2

class TestImports(unittest.TestCase):
    def test_function1(self):
        self.assertEqual(function1(), "Expected output from function1")

    def test_function2(self):
        self.assertEqual(function2(), "Expected output from function2")

if __name__ == '__main__':
    unittest.main()