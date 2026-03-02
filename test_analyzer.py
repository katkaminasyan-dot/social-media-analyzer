import unittest
from analyzer import SentimentAnalyzer

class TestSentimentAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = SentimentAnalyzer()

    def test_positive(self):
        result = self.analyzer.analyze("I love this product")
        self.assertEqual(result, "POSITIVE")

    def test_negative(self):
        result = self.analyzer.analyze("This is terrible")
        self.assertEqual(result, "NEGATIVE")

    def test_neutral(self):
        result = self.analyzer.analyze("This is a table")
        self.assertEqual(result, "NEUTRAL")

    def test_empty(self):
        result = self.analyzer.analyze("")
        self.assertEqual(result, "NEUTRAL")


if __name__ == "__main__":
    unittest.main()