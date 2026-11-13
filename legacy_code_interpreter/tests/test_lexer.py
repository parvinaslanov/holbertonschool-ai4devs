import unittest

class TestLexer(unittest.TestCase):
    def test_tokenize(self):
        tokens = "x = 1".split()
        self.assertEqual(tokens, ['x', '=', '1'])

if __name__ == '__main__':
    unittest.main()
