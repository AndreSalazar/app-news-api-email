import requests

api_key = "a364a5dbee934ca6a3b3fc98e2a98bd3"

url = "https://newsapi.org/v2/everything?q=tesla&from=2026-02-19&sortBy=publishedAt&apiKey=a364a5dbee934ca6a3b3fc98e2a98bd3"

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
