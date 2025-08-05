from transformers import pipeline

_summarizer = None


def get_summarizer():
    global _summarizer
    if _summarizer is None:
        _summarizer = pipeline(
            "summarization", model="sshleifer/distilbart-cnn-12-6", framework="pt"
        )
    return _summarizer


def summrize_text(text):
    summarizer = get_summarizer()
    return summarizer(text, max_length=100, min_length=25, do_sample=False)[0][
        "summary_text"
    ]
