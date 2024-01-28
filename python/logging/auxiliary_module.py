import logging

# create logger
module_logger = logging.getLogger("spam_application")


class Auxiliary:
    def __init__(self):
        self.logger = logging.getLogger("spam_application")
        self.logger.info("creating an instance of Auxiliary")

    def do_something(self):
        self.logger.info("doing something")
        a = 1 + 1
        self.logger.info("done doing something")


def some_function():
    module_logger.info('received a call to "some_function"')
