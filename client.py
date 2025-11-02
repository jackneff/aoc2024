import requests
import re
from bs4 import BeautifulSoup

from dotenv import dotenv_values

env = dotenv_values(".env")

s = requests.Session()
s.cookies.set("session", env["MY_AOC_SESSION_COOKIE"], domain="adventofcode.com")
r = s.get("https://adventofcode.com/2024/day/2")
t = r.text
html = r.content
soup = BeautifulSoup(html, "html.parser")
articles = soup.find_all("article")

with open("challenge.md", "w") as f:
    for article in articles:
        f.write(article.get_text())


def extract_text_between(text, start, end):
    context = f"{start}(.*){end}"
    result = re.search(context, text)
    return result.group(1)


# article = extract_text_between(t, '<article class="day-desc">', "</article>")
# code = extract_text_between(t, "<code>", "</code>")
# print("article", article)
# print("code", code)
