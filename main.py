import requests
from send_email import send_email

topic = "tesla"

api_key = "a364a5dbee934ca6a3b3fc98e2a98bd3"
url = "https://newsapi.org/v2/everything?" \
    f"q={topic}&" \
    "from=2026-02-22&" \
    "sortBy=publishedAt&" \
    "apiKey=a364a5dbee934ca6a3b3fc98e2a98bd3&" \
    "language=en"

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = "Subject: Today's news" + "\n"
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" \
               + article["description"] + "\n" \
               + article["url"] + 2*"\n"


body = body.encode("utf-8")
send_email(message=body)