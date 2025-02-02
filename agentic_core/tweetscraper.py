import asyncio
from pyppeteer import launch
import nest_asyncio

nest_asyncio.apply()  # Allows asyncio to work in Flask/Gunicorn

async def scrape_tweets(handle, limit=20):
    """Scrapes recent tweets from a Twitter/X profile using headless Chrome."""
    try:
        browser = await launch(
            headless=True,
            args=["--no-sandbox", "--disable-setuid-sandbox", "--disable-blink-features=AutomationControlled"]
        )

        page = await browser.newPage()
        await page.setUserAgent(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )

        profile_url = f'https://twitter.com/{handle}'
        await page.goto(profile_url, {'waitUntil': 'networkidle2', 'timeout': 60000})

        tweet_selector = 'div[data-testid="tweetText"]'
        await page.waitForSelector(tweet_selector, timeout=30000)

        tweets = []

        for _ in range(15):  # Scroll to load more tweets
            await page.evaluate("window.scrollBy(0, 4000);")
            await asyncio.sleep(2)

            new_tweets = await page.evaluate('''() => {
                return Array.from(document.querySelectorAll('div[data-testid="tweetText"]'))
                .map(tweet => tweet.innerText.trim());
            }''')

            tweets.extend(new_tweets)
            tweets = list(set(tweets))  # Remove duplicates

            if len(tweets) >= limit:
                break

        await browser.close()
        return tweets[:limit] if tweets else ["No tweets found or access blocked."]

    except Exception as e:
        return [f"🔥 Scraping Error: {str(e)}"]
