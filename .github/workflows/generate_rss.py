import re
from datetime import datetime

with open("news.html", "r", encoding="utf-8") as f:
    html = f.read()

pattern = re.compile(
    r'<div class="news-item">.*?<div class="news-date">(.*?)</div>.*?<strong>(.*?)</strong>.*?</p>.*?<p>(.*?)</p>',
    re.S
)

items = pattern.findall(html)

rss_items = ""

for date, title, desc in items:
    dt = datetime.strptime(date.strip(), "%d %B %Y")
    pub = dt.strftime("%a, %d %b %Y 12:00:00 +0300")

    rss_items += f"""
    <item>
        <title>{title}</title>
        <link>https://threeheadsbot.ru/news.html</link>
        <pubDate>{pub}</pubDate>
        <description>{desc}</description>
    </item>
    """

rss = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
    <title>ThreeHeadsBot — Новости</title>
    <link>https://threeheadsbot.ru/news.html</link>
    <description>Новости сервиса ThreeHeadsBot.</description>
    <language>ru</language>
    {rss_items}
</channel>
</rss>
"""

with open("rss.xml", "w", encoding="utf-8") as f:
    f.write(rss)
