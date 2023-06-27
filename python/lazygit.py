# Lazy Git
# A python script that runs `git add .`, `git commit -m "Lazy Git Commit"`, and `git push` in one command. Useful for quickly committing changes to a repo.

# 1. Get funny commit message from whatthecommit, add default message if it fails
# 2. Pull from remote to make sure we're up to date
# 3. Add all files to staging
# 4. Commit with funny message
# 5. Push to remote

# Import libraries
import random
import subprocess
import requests
import sys
import argparse


class LazyGit:
    # 1. Get funny commit message from whatthecommit, add default message if it fails, as a property
    # Class property
    COMMIT_MESSAGES_MAIN = "https://raw.githubusercontent.com/Drblessing/notes/master/References/commit_messages.txt"
    COMMIT_MESSAGES_FALLBACK = "https://raw.githubusercontent.com/ngerakines/commitment/main/commit_messages.txt"
    DEFAULT_COMMIT_MESSAGE = "Lazy Git Commit"

    @staticmethod
    def parse_args():
        """Parse arguments"""
        parser = argparse.ArgumentParser(
            description="A python script that runs `git add .`, `git commit -m <random funny git message>`, and `git push` in one command. Useful for quickly committing changes to a repo."
        )
        parser.add_argument(
            "-m",
            "--message",
            type=str,
            help="Commit message",
            default=LazyGit.DEFAULT_COMMIT_MESSAGE,
        )

        parser.add_argument(
            "--version",
            "-v",
            action="version",
            version="%(prog)s 1.0",
            help="Show program's version number and exit.",
        )

        args = parser.parse_args()

        if args.message:
            LazyGit.DEFAULT_COMMIT_MESSAGE = args.message

        return args

    @classmethod
    def get_commit_message_from_url(cls, url: str = COMMIT_MESSAGES_MAIN) -> str | None:
        """Get commit message from url"""
        try:
            r = requests.get(url)
            r.raise_for_status()
            text = r.text
            text = text.split("\n")
            # Get random commit message from text
            commit_message = random.choice(text)
            return commit_message

        except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError):
            return

    @classmethod
    def get_commit_message(cls) -> str:
        """Get commit message"""
        commit_message = (
            cls.get_commit_message_from_url()
            or cls.get_commit_message_from_url(cls.COMMIT_MESSAGES_FALLBACK)
            or cls.DEFAULT_COMMIT_MESSAGE
        )
        return commit_message

    # 2. Pull from remote to make sure we're up to date
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

    @staticmethod
    def pull_from_remote():
        """Pull from remote to make sure we're up to date"""
        LazyGit.run_command(["git", "pull"])

    # 3. Add all files to staging
    @staticmethod
    def add_all_files_to_staging():
        """Add all files to staging"""
        LazyGit.run_command(["git", "add", "."])

    # 4. Commit with funny message
    @classmethod
    def commit_with_funny_message(cls):
        """Commit with funny message"""
        commit_message = cls.get_commit_message()
        LazyGit.run_command(["git", "commit", "-m", commit_message])

    # 5. Push to remote
    @staticmethod
    def push_to_remote():
        """Push to remote"""
        LazyGit.run_command(["git", "push"])

    # 6. Run all commands
    @classmethod
    def run_all_commands(cls):
        """Run all commands"""
        cls.pull_from_remote()
        cls.add_all_files_to_staging()
        cls.commit_with_funny_message()
        cls.push_to_remote()
        print("Done!")


if __name__ == "__main__":
    args = LazyGit.parse_args()
    LazyGit.run_all_commands()
