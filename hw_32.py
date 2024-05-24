import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

html_response = requests.get(url)

if html_response.status_code != 200:
    print(f"Failed to retrieve the article. Status code: {html_response.status_code}")
else:
    soup = BeautifulSoup(html_response.content, "html.parser")
    content = soup.find("div", {"class": "mw-parser-output"})

    if content is None:
        print("Could not find the main content of the article.")
    else:
        paragraphs = content.find_all("p")
        article_text = "\n".join([para.get_text() for para in paragraphs])

        print(article_text)
