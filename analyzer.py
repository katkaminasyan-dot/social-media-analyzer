class SentimentAnalyzer:

    def analyze(self, text):
        if not text:
            return "NEUTRAL"

        text = text.lower()

        if "good" in text or "love" in text or "great" in text:
            return "POSITIVE"

        if "bad" in text or "hate" in text or "terrible" in text:
            return "NEGATIVE"

        return "NEUTRAL"