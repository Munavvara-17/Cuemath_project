def predict_sarcasm(text):
    text = text.lower()

    sarcasm_keywords = [
        "yeah right",
        "sure",
        "as if",
        "wow great",
        "nice job"
    ]

    for phrase in sarcasm_keywords:
        if phrase in text:
            return "Sarcastic 😏"

    return "Not Sarcastic 🙂"