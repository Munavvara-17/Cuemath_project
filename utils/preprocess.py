import re
import string

# Basic stopwords list (you can expand later)
STOPWORDS = {
    "the", "is", "in", "and", "to", "of", "a", "an", "on", "for",
    "with", "as", "by", "at", "from", "that", "this", "it"
}

def clean_text(text):
    """
    Basic text cleaning:
    - Lowercase
    - Remove punctuation
    - Remove numbers
    """
    text = text.lower()
    
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    return text


def remove_stopwords(text):
    """
    Remove common stopwords
    """
    words = text.split()
    filtered_words = [word for word in words if word not in STOPWORDS]
    return " ".join(filtered_words)


def preprocess_text(text):
    """
    Full preprocessing pipeline
    """
    text = clean_text(text)
    text = remove_stopwords(text)
    return text