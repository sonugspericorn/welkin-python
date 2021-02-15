import logging

logger = logging.getLogger("welkin")
logger.setLevel(logging.DEBUG)

# create handlers and set level to debug
ch = logging.StreamHandler()
fh = logging.FileHandler('welkin.log')
ch.setLevel(logging.DEBUG)
fh.setLevel(logging.DEBUG)


# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# add handlers to logger
logger.addHandler(ch)
logger.addHandler(fh)

__all__ = [
    "log_info",
    "log_debug",
]

def log_info(message, **params):
    logger.info(message)

def log_debug(message, **params):
    logger.debug(message)
