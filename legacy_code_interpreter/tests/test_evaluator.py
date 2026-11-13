import unittest

class TestEvaluator(unittest.TestCase):
    def test_evaluation(self):
        self.assertEqual(eval("2 * 3"), 6)

if __name__ == '__main__':
    unittest.main()
