def predict_sentiment(text):
    text = text.lower()

    positive_words = ["good", "great", "love", "awesome", "happy", "excellent"]
    negative_words = [
        "bad", "hate", "worst", "sad", "terrible", "angry",
        "no", "not", "problem", "issue", "delay", "lack",
        "complaint", "error", "fail", "failure"
    ]

    score = 0

    # Positive check
    for word in positive_words:
        if word in text:
            score += 1

    # Negative check
    for word in negative_words:
        if word in text:
            score -= 1

    # Special case (very important)
    if "no" in text and ("water" in text or "service" in text):
        return "Negative 😡"

    if score > 0:
        return "Positive 😊"
    elif score < 0:
        return "Negative 😡"
    else:
        return "Neutral 😐"