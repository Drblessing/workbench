from package1.module1 import function1
from package2.module2 import function2
import logging

logger = logging.getLogger("package")
# Basic logging configuration
# logging.basicConfig(
#     level=logging.DEBUG,
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     datefmt="%Y-%m-%d %H:%M:%S",
# )


def main():
    function1()
    function2()


if __name__ == "__main__":
    main()

import logging

logging.warning("Watch out!")  # will print a message to the console
logging.info("I told you so")  # will not print anything
