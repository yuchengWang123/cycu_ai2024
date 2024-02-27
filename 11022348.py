import feedparser

url = "https://news.pts.org.tw/xml/newsfeed.xml"

def parse_rss(url):
    feed = feedparser.parse(url)
    if 'title' in feed.feed:
        print("Feed Title:", feed.feed.title)
        print("Feed Description:", feed.feed.description)
        print("\nEntries")
        for entry in feed.entries:
            if 'title' in entry:
                print(entry.title)

parse_rss(url)

