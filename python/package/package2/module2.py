import logging

logger = logging.getLogger("package")


def function2():
    logger.warning("function2 in module2 in package2")
    return "Hello from module2 in package2"
