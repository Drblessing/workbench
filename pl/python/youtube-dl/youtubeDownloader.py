#!/usr/bin/env python3
# Youtube Downloader

import argparse
import importlib
import logging
import os
import shutil
import subprocess
import sys
import webbrowser
from dataclasses import dataclass
from enum import Enum
from pathlib import Path


class YoutubeDownloader:
    """Youtube Downloader

    Download youtube files in the best quality and specify output
    format and filename.
    """

    def parse_args(self):
        """Parse command line arguments."""
        parser = argparse.ArgumentParser(
            description="Download youtube files in the best quality and specify output format and filename."
        )

        # File directory.
        parser.add_argument(
            "-d",
            "--directory",
            dest="directory",
            default=os.getcwd(),
            help="Directory to download files to.",
        )

        # Output file name.
        parser.add_argument(
            "-o",
            "--output",
            dest="output",
            default=None,
            help="Output file name.",
        )

        # Youtube url
        parser.add_argument(
            "-u",
            "--url",
            dest="url",
            default=None,
            help="Youtube url.",
        )

        args = parser.parse_args()
        return args

    def __init__(self):
        """Initialize."""
        self.args = self.parse_args()
        self.download()

    @staticmethod
    def run_command(command: list[str]):
        """Run a command and handle errors"""
        try:
            subprocess.check_call(command)
        except subprocess.CalledProcessError as e:
            print(
                f"Command '{' '.join(command)}' failed with error code {e.returncode}"
            )
            sys.exit(1)

    def download(self):
        """Download the youtube file."""

        command_list = [
            "youtube-dl",
            "-f",
            "'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'",
            "-o",
            f"{self.args.directory}/{self.args.output}.%(ext)s",
        ]

        YoutubeDownloader.run_command(command_list)


def setup_logging():
    """Setup logging for the application."""

    # Get the cwd of this file.
    cwd = Path(__file__).parent
    # Create logs dir if it doesn't exist.
    log_dir = cwd / "logs"
    if not log_dir.exists():
        log_dir.mkdir()
    # Create a path to the log file.
    log_file = cwd / "logs" / "youtubeDownloader.log"
    # Configure root logger with a file handler.
    # Also, my preferred log format and level.
    # Overwrite the log file each time the file is run.
    logging.basicConfig(
        filename=log_file,
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s",
        # format="%(message)s",
        datefmt="%m/%d/%Y %I:%M:%S %p",
        filemode="w",
    )
    # Optionaly add a console handler.
    # This will print to the console in addition to the log file.
    # Useful for debugging.
    log_console = True
    if log_console:
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        logging.getLogger("").addHandler(console)
        # Format for console logging.
        # This is different than the format for the log file.
        formatter = logging.Formatter(
            "%(filename)s:%(lineno)d - %(levelname)s - %(message)s"
        )
        console.setFormatter(formatter)

    # Start logging.
    logging.info("Started Youtube Downloader.")


if __name__ == "__main__":
    setup_logging()
    YoutubeDownloader()
