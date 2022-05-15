import logging
logger = logging.getLogger(__name__)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('logs/app.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

formatter2 = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
file_handler2 = logging.FileHandler('logs/app2.log',mode='w')
file_handler2.setLevel(logging.CRITICAL)
file_handler2.setFormatter(formatter2)
logger.addHandler(file_handler2)

logger.error("error message here")
logger.critical("critical message here")

