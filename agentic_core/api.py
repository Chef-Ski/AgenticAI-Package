from flask import Flask, request, jsonify
from flask_cors import CORS
from asgiref.sync import async_to_sync
import os

from agentic_tweets.scraper import scrape_tweets
from agentic_tweets.generator import generate_tweets_in_style

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "https://agenticai.onl"}})

@app.route('/api/generate-tweets', methods=['POST'])
def generate_tweets():
    """API Endpoint to scrape and generate tweets."""
    data = request.json
    twitter_handle = data.get('twitterHandle')
    tweet_count = data.get('tweetCount', 5)

    if not twitter_handle:
        return jsonify({'error': "Missing 'twitterHandle'"}), 400

    tweets = async_to_sync(scrape_tweets)(twitter_handle, 20)

    if not tweets or tweets == ["No tweets found or access blocked."]:
        return jsonify({'error': "Could not scrape tweets. Try again later."}), 500

    ai_tweets = generate_tweets_in_style(twitter_handle, tweets)

    if not ai_tweets:
        return jsonify({'error': "Failed to generate tweets."}), 500

    return jsonify({'tweets': ai_tweets})

@app.route('/')
def index():
    return "✅ Server is running. Use POST /api/generate-tweets to generate tweets."

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True, use_reloader=False)
