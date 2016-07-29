import logging
import sys

log_format = '[%(asctime)s] %(name)s {%(filename)s:%(lineno)d} %(levelname)s - %(message)s'
logging.basicConfig(
    filename='logger.log', 
    level=logging.DEBUG, stream=sys.stdout, 
    format= log_format,
    datefmt='%H:%M:%S')

def createLogger(name):
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    formatter = logging.Formatter(log_format)
    console.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.addHandler(console)
    return logger