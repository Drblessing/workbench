import requests
from bs4 import BeautifulSoup

# Turn this into a class and use OOP to make it more modular
class HeadlineScraper: 
    def __init__(self, url="https://news.ycombinator.com/"):
        # Check if url 
        self.url = url


# # Replace the URL below with the website you want to scrape
# url = "https://news.ycombinator.com/"

# # Send a request to the website
# response = requests.get(url)

# # Parse the page content
# soup = BeautifulSoup(response.text, "html.parser")

# # Find the elements containing the info you want to scrape
# # For example, let's scrape the news headlines
# # The specific element and class will depend on the website's structure
# headlines = soup.select("span.titleline")

# # Get the text from the first a tag of each headline
# headlines_text = [headline.a.get_text() if headline.a else "" for headline in headlines]

# # Print the headlines
# for headline in headlines_text:
#     print(headline)
