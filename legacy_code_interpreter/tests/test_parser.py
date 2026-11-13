import unittest

class TestParser(unittest.TestCase):
    def test_parse_expression(self):
        self.assertEqual(2 + 2, 4)

if __name__ == '__main__':
    unittest.main()
