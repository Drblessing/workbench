"""
Testing out how python package and modules work.
"""
from package1.module1 import function1
from package2.module2 import function2
from utils.log_manager import init_logger, get_logger


def main():
    init_logger(__file__)
    function1()
    function2()


if __name__ == "__main__":
    main()
