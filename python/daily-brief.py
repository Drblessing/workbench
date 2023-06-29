#!/usr/bin/env python3
# Open daily brief of websites in browser
import webbrowser
import argparse


class DailyBrief:
    BRIEF_LIST = [
        "https://companiesmarketcap.com/assets-by-market-cap/",
        "https://www.coingecko.com/",
        "https://github.com/trending",
        "https://cryptofees.info/",
        "https://eigenphi.io/",
        "https://cryptocurrencyalerting.com/coin-listing-events.html",
        "https://transparency.flashbots.net/",
        "https://twitter.com/CoinbaseAssets",
        "https://ultrasound.money/",
        "https://clientdiversity.org/#distribution",
    ]

    BRIEF_NEWS = [
        "https://rekt.news",
        "https://weekinethereumnews.com/",
    ]

    RESEARCH_NEWS = [
        "https://weekinethereumnews.com/",
        "https://forum.soliditylang.org/",
        "https://ethresear.ch/" "https://collective.flashbots.net/latest",
    ]

    def parse_args(self):
        """Parse arguments"""
        parser = argparse.ArgumentParser(
            description="A python script that opens a daily brief of cool stuff in the browser."
        )
        parser.add_argument(
            "-n",
            "--news",
            type=bool,
            help="Opens news sites.",
        )

        parser.add_argument(
            "--version",
            "-v",
            action="version",
            version="%(prog)s 1.0",
            help="Show program's version number and exit.",
        )

        args = parser.parse_args()

        return args

    def __init__(self):
        args = self.parse_args()
        self.open_news = args.news

    def open_brief(self):
        for url in self.BRIEF_LIST:
            webbrowser.open_new_tab(url)


if __name__ == "__main__":
    daily_brief = DailyBrief()
    daily_brief.open_brief()
