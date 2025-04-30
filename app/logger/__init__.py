import logging

def setup_logging(name: str = __name__, level: int = logging.ERROR):
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s: %(message)s')
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    if logger.hasHandlers():
        logger.handlers.clear()
    logger.addHandler(stream_handler)
    return logger

logger = setup_logging()