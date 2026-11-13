import unittest

class TestMain(unittest.TestCase):
    def test_entrypoint(self):
        self.assertIsNotNone("main")

if __name__ == '__main__':
    unittest.main()
