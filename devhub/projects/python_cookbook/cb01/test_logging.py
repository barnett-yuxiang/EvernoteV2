import logging

print("Hello Logging")

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger('yuli')
logger.info("Hello Logging")

another_logger = logging.getLogger('another_component')
another_logger.info("This is another component logging")
