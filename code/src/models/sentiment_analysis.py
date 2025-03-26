# sentiment_analysis.py
from models.gpt_neo_model import load_model

def analyze_sentiment(post_text):
    model, tokenizer = load_model()
    print(post_text)
    # Create the sentiment analysis prompt
    prompt = f"Classify the sentiment of the following social media post as Positive, Negative, or Neutral:\n\nPost: {post_text}\nSentiment:"

    # Tokenize the input and generate a prediction
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Extract sentiment from model's response
    if "Positive" in response:
        return "Positive"
    elif "Negative" in response:
        return "Negative"
    else:
        return "Neutral"