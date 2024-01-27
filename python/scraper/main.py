"""
This module contains the HeadlineScraper class, which is used to scrape headlines from a website.

The HeadlineScraper class takes a URL as input and uses the BeautifulSoup library to parse the HTML of the webpage. It looks for 'span' elements with the class 'titleline', and extracts the text of the 'a' elements within these 'span' elements as headlines.

The HeadlineScraper class has the following methods:
- is_valid_url: Checks if a URL is valid.
- get_headlines: Extracts headlines from the HTML of a webpage.
- print_headlines: Prints the extracted headlines.

Example usage:
    scraper = HeadlineScraper("https://news.ycombinator.com/")
    scraper.print_headlines()
"""
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


# Turn this into a class and use OOP to make it more modular
class HeadlineScraper:
    def __init__(self, url: str = "https://news.ycombinator.com/"):
        # Check if url is valid
        if not self.is_valid_url(url):
            raise ValueError("Invalid URL")
        self.url = url

        # Send a request to the website
        response = requests.get(url)
        response.raise_for_status()

        # Get headlines
        self.get_headlines(response)

        # Print headlines
        self.print_headlines(self.headlines)

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

    def get_headlines(self, response: requests.Response):
        """Get headlines from url.

        The expected structure of the html is:
        <html>
            <span class="titleline">
                <a>Headline 1</a>
                <a> Skip this headline </a>
            </span>
            <span class="titleline">
                <a>Headline 2</a>
            </span>
        </html>
        """

        soup = BeautifulSoup(response.text, "html.parser")
        headlines = soup.select("span.titleline")
        # Some span elements don't have a headline, so
        # we need to check if the span has a headline.
        headlines_text = [
            headline.a.get_text() if headline.a else "" for headline in headlines
        ]

        # Check if headlines are empty
        if not headlines_text:
            raise ValueError("No headlines found")

        self.headlines = headlines_text

    def print_headlines(self, headlines: list[str]):  
        """Print headlines."""
        for headline in headlines:
            print(headline)


if __name__ == "__main__":
    HeadlineScraper("https://news.ycombinator.com/")
