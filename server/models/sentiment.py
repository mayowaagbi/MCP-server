from transformers import pipeline

_classifier = None


def get_classifier():
    global _classifier
    if _classifier is None:
        _classifier = pipeline(
            "sentiment-analysis",
            model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
        )
    return _classifier


def get_sentiment(text):
    classifier = get_classifier()
    return classifier(text)[0]
