import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


# Turn this into a class and use OOP to make it more modular
class HeadlineScraper:
    def __init__(self, url="https://news.ycombinator.com/"):
        # Check if url is valid
        if not self.is_valid_url(url):
            raise ValueError("Invalid URL")
        

    @staticmethod
    def is_valid_url(url: str) -> bool:
        """Check if url is valid."""
        parsed_url = urlparse(url)
        # Check for http or https
        if parsed_url.scheme not in ["http", "https"]:
            return False

        # Check for domain name
        if not parsed_url.netloc or "." not in parsed_url.netloc:
            return False

        return True


if __name__ == "__main__":
    HeadlineScraper("https://newsasdfasdfcom")


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
