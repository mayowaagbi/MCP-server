from transformers import pipeline

summerizer = pipeline("summerizer", model="sshleifer/distilbart-cnn-12-6")


def summerize_text(text):
    return summerizer(text, max_lenght=100, min_lenght=25, do_sample=false)[0][
        "summary_text"
    ]
