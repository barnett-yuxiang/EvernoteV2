import logging

print("Hello Logging")

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger('yuli')
logger.info("Hello Logging")

another_logger = logging.getLogger('another_component')
another_logger.info("This is another component logging")

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)

file_handler = logging.FileHandler('run.log')
file_handler.setLevel(logging.DEBUG)
file_formmatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formmatter)
logger.addHandler(file_handler)

logger.info("This message will appear in the console and the file.")
logger.debug("This message will appear only in the file.")
