import unittest


class SampleTestCase(unittest.TestCase):
    def test_example(self):
        self.assertEqual(1 + 1, 2)

    def test_failure(self):
        self.assertEqual(1 + 1, 3)
