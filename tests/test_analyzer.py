from analyzer import SentimentAnalyzer


def test_positive_sentiment():
    analyzer = SentimentAnalyzer()
    assert analyzer.analyze("I love this") == "POSITIVE"


def test_negative_sentiment():
    analyzer = SentimentAnalyzer()
    assert analyzer.analyze("This is bad") == "NEGATIVE"


def test_neutral_sentiment():
    analyzer = SentimentAnalyzer()
    assert analyzer.analyze("Hello") == "NEUTRAL"
    