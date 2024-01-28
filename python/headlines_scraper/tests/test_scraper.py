import pytest
import requests_mock
from headliens- import HeadlineScraper


def test_is_valid_url():
    """Test if url is valid."""
    assert HeadlineScraper.is_valid_url("https://news.ycombinator.com/") == True
    assert HeadlineScraper.is_valid_url("http://example.com/") == True
    assert HeadlineScraper.is_valid_url("ftp://example.com/") == False
    assert HeadlineScraper.is_valid_url("example.com") == False


def test_init():
    """Test if url is set correctly."""
    with requests_mock.Mocker() as m:
        m.get(
            "https://news.ycombinator.com/",
            text="<html><span class='titleline'><a>Headline 1</a></span></html>",
        )
        scraper = HeadlineScraper("https://news.ycombinator.com/")
        assert scraper.url == "https://news.ycombinator.com/"


def test_init_invalid_url():
    """Test if url is invalid."""
    with pytest.raises(ValueError):
        HeadlineScraper("ftp://example.com/")


def test_get_headlines():
    """Test if headlines are set correctly."""
    with requests_mock.Mocker() as m:
        m.get(
            "https://news.ycombinator.com/",
            text="<html><span class='titleline'><a>Headline 1</a></span></html>",
        )
        scraper = HeadlineScraper("https://news.ycombinator.com/")
        assert scraper.headlines == ["Headline 1"]


def test_get_headlines_no_headlines():
    """Test if headlines are empty."""
    with requests_mock.Mocker() as m:
        m.get("https://news.ycombinator.com/", text="<html></html>")
        with pytest.raises(ValueError):
            HeadlineScraper("https://news.ycombinator.com/")


def test_other_website_multiple_headlines():
    """Test othe website with multiple headlines."""
    with requests_mock.Mocker() as m:
        m.get(
            "http://important-news.com",
            text="<html><span class='titleline'><a>Headline 1</a><a>Subheadline1 </a></span><span class='titleline'><a>Headline 2</a></span></html>",
        )
        scraper = HeadlineScraper("http://important-news.com")
        assert scraper.headlines == ["Headline 1", "Headline 2"]
