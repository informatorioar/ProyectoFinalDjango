from django.test import TestCase


class SampleTestCase(TestCase):
    """A simple test case to demonstrate unittest functionality."""

    def test_example(self):
        self.assertEqual(1 + 1, 2)

    def test_failure(self):
        self.assertEqual(1 + 1, 3)
