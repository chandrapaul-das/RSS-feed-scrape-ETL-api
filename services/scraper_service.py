import feedparser
import re

def text_clean(text):
    text = str(text)
    text = re.sub(r'[\r\t]', ' ', text)
    text = re.sub(r'\n', '.', text)
    text = re.sub(' +', ' ', text)
    text = re.sub(r'\.(?=[a-zA-Z]|#)', '. ', text)
    return text.replace("..", ".").replace(" .", " ").replace(":. ", ": ").replace('• ', '')

def fetch_rss_article(feed_url):
    feed = feedparser.parse(feed_url)
    articles = []
    for entry in feed.entries:
        try:
            article = {
                "title": entry.title,
                "link": getattr(entry, 'link', ''),
                "description": text_clean(getattr(entry, 'description', '')),
                "published": getattr(entry, 'published', '')
            }
            articles.append(article)
        except Exception as e:
            print(f'Failed in extracting article: {e}')
    return articles

def article_scraper(rss_feeds):
    articles = []
    for rss_feed in rss_feeds:
        articles += fetch_rss_article(rss_feed)
    return articles