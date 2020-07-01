import logging
from util import get_script_path


def get_logger():
    logger = logging.getLogger(__name__)
    file_handler = logging.FileHandler('{}/logs.log'.format(get_script_path()))
    file_handler.setFormatter(logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)
    return logger
