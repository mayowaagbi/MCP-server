from models.summarizer import summrize_text
from models.sentiment import get_sentiment


async def handle_mcp_request(data):
    action = data.get("action")
    model = data.get("model")
    input_text = data.get("input")

    if action == "predict":
        if model == "summarize":
            return {"summary": summrize_text(input_text)}
        elif model == "sentiment":
            return {"sentiment": get_sentiment(input_text)}
        else:
            return {"error": "Unknown model"}
    else:
        return {"error": "Unsupported action"}
