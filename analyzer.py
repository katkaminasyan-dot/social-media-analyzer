POSITIVE_WORDS = {"good", "love", "great"}
NEGATIVE_WORDS = {"bad", "hate", "terrible"}

class SentimentAnalyzer:
    def analyze(self, text):
        if not text:
            return "NEUTRAL"

        normalized_text = text.lower()

        if any(word in normalized_text for word in POSITIVE_WORDS):
            return "POSITIVE"

        if any(word in normalized_text for word in NEGATIVE_WORDS):
            return "NEGATIVE"

        return "NEUTRAL"

