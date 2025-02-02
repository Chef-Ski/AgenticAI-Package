# `pip install agentic-core` 🧠  
**AI-powered toolkit for scraping and generating tweets in a user's style.**

`agentic-core` enables **tweet scraping** (without the Twitter API) and **AI-powered tweet generation**. This package is designed for developers looking to build intelligent AI agents for social media content analysis, simulation, and generation.

---

## 🚀 **Installation**  
`agentic-core` requires **Python 3.7+**. To install:  

```sh
pip install agentic-core
```

To upgrade to the latest version:
```sh
pip install --upgrade agentic-core
```

---

## 🔥 **Usage**
### 1️⃣ **Scrape Tweets from a Public Twitter/X Profile**
```python
from agentic_core.scraper import scrape_tweets

# Scrape recent tweets from a user (no API required)
tweets = scrape_tweets("elonmusk", limit=10)

print("Scraped Tweets:", tweets)
```

---

### 2️⃣ **Generate AI-Powered Tweets in a User’s Style**
```python
from agentic_core.generator import generate_tweets_in_style

# Use scraped tweets to generate AI-powered tweets
generated_tweets = generate_tweets_in_style("elonmusk", tweets)

print("Generated AI Tweets:", generated_tweets)
```

---

## 📚 **API Reference**
### **🔍 `scraper.py` (Tweet Scraper)**
#### `scrape_tweets(handle: str, limit: int = 20) -> list`
**Description:**  
Scrapes recent tweets from a **public** Twitter/X profile using headless browsing (without the Twitter API).  

**Parameters:**
- `handle` _(str)_: Twitter username (e.g., `"elonmusk"`).
- `limit` _(int, optional)_: Number of tweets to scrape (default is `20`).

**Returns:**
- A **list of tweets** _(list[str])_ or an error message if scraping fails.

---

### **🤖 `generator.py` (AI-Powered Tweet Generator)**
#### `generate_tweets_in_style(handle: str, scraped_tweets: list) -> list`
**Description:**  
Generates **new tweets** in the same writing style as the provided user's past tweets using OpenAI GPT.

**Parameters:**
- `handle` _(str)_: Twitter username (for reference).
- `scraped_tweets` _(list[str])_: A list of scraped tweets to use as training data.

**Returns:**
- A **list of AI-generated tweets** _(list[str])_.

---

## 🌍 **Running the API Server**
`agentic-core` provides a built-in Flask API for seamless integration.

### **Start the API Server**
```sh
python -m agentic_core.api
```

### **Available API Endpoints**
#### 🔹 `POST /api/generate-tweets`
**Description:**  
Scrapes tweets and generates AI-powered tweets in a user's style.

**Request Body (JSON)**:
```json
{
  "twitterHandle": "elonmusk",
  "tweetCount": 5
}
```

**Response Example (JSON)**:
```json
{
  "tweets": [
    "SpaceX is going to change everything.",
    "Tesla AI Day is coming soon. Big updates ahead!"
  ]
}
```

---

## 🔑 **Environment Variables**
To use the **OpenAI GPT model** for tweet generation, set up your API key in an `.env` file:

```sh
OPENAI_API_KEY=your_api_key_here
```

Or export it directly in your terminal:
```sh
export OPENAI_API_KEY="your_api_key_here"
```

---

## 🛠️ **Development Setup**
### **Clone the Repository**
```sh
git clone https://github.com/your-username/agentic-core.git
cd agentic-core
```

### **Install Dependencies**
```sh
pip install -r requirements.txt
```

### **Run Tests**
```sh
pytest tests/
```

---

## 🚀 **Why Use `agentic-core`?**
✅ **No Twitter API required** – Scrape tweets **without** API keys.  
✅ **AI-Powered** – Generates **tweets in the same writing style** as a given user.  
✅ **Fast & Scalable** – Designed for **developers & AI projects**.  
✅ **Modular & Open-Source** – Use it as a **standalone tool** or as part of a larger AI system.  

---

## 🤝 **Contributing**
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Open a pull request.

For major changes, please open an issue first to discuss your proposal.

---

## 📝 **License**
`agentic-core` is licensed under the **MIT License** – free for personal and commercial use.

---

## 📩 **Contact & Support**
Need help or have suggestions? Reach out via:  
📧 **Email:** [your-email@example.com](mailto:your-email@example.com)  
🐦 **Twitter:** [@yourhandle](https://twitter.com/yourhandle)  
🌐 **Website:** [yourwebsite.com](https://yourwebsite.com)  

---

### ⭐ **Like `agentic-core`? Consider giving it a star on GitHub!** ⭐

