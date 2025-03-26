import openai
import os

# Set up the OpenAI API key

def analyze_sentiment(post_text):
    # Define the prompt to ask the model to classify sentiment
    prompt = f"Type ONLY the sentiment of this social media post as positive or negative:{post_text}"
    #prompt="How are you"
    client = openai.OpenAI(
        base_url = "https://openrouter.ai/api/v1",
        api_key = os.getenv("OPENROUTER_MISTRAL_KEY")
    )
    # Call OpenAI's API to generate a response based on the prompt
    try:
        print(os.getenv("OPENROUTER_MISTRAL_KEY"))
        print(client.api_key)
        response = client.chat.completions.create(
            model="meta-llama/llama-3.3-70b-instruct:free",
            messages=[
                {
                    "role": "user",
                    "content":[
                        {
                            "type":"text",
                            "text":prompt
                        }
                    ]
                }
            ],            
            temperature=0,  # Temperature 0 for deterministic answers,
            max_completion_tokens=1
        )

        # Extract and return the sentiment
        print(response.choices)
        sentiment = response.choices[0].message.content
        return sentiment

    except Exception as e:
        print(f"Error analyzing sentiment: {e}")
        return "Error"
