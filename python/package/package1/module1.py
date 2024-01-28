# import get from the utils package, and use it to get the logger.
from utils.log_manager import get_logger


def function1():
    logger = get_logger()
    logger.critical("function1 called")
    return "Hello from module1 in package1"
