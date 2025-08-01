from transformers import pipeline

classifier = pipeline("sentiment-analysis")


def get_sentiment(text):
    return classifier(text)[0]
