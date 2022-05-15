import logging

logging.basicConfig(filename='logs/basic.log',level=logging.ERROR, filemode='a', format='%(name)s - %(levelname)s - %(message)s')

logging.error('This will get logged to a file')

a = 5
b = 0

try:
    mysub = a /b
except Exception as e:
    logging.info("info level: ",exc_info=True)
    logging.warning("warning level: ",exc_info=True)
    logging.error("error level",exc_info=True)
    logging.critical("critical level: ",exc_info=True)
    print(e)
