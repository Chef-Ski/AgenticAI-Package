import openai
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_tweets_in_style(handle, scraped_tweets):
    """Uses OpenAI to generate tweets in the same style."""
    if not scraped_tweets or scraped_tweets == ["No tweets found or access blocked."]:
        return None

    prompt = f"""
    You are an AI assistant analyzing a Twitter user's style. 
    Generate 5 tweets mimicking their style, length, and vocabulary.
    Only use vocabulary they have used before.
    
    {' '.join(f"- {tweet}" for tweet in scraped_tweets)}
    
    Now generate 5 new tweets in the same style.
    """

    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": "Generate 5 tweets mimicking their style."}
            ],
            max_tokens=300,
            temperature=0.7
        )
        return response.choices[0].message.content.strip().split('\n')
    except Exception as e:
        return [f"🔥 OpenAI API Error: {str(e)}"]
