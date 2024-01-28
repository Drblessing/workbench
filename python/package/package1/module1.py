import logging

logger = logging.getLogger("package")


def function1():
    logger.info("function1 in module1 in package1")
    return "Hello from module1 in package1"
