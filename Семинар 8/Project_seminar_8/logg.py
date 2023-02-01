import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="logs.log",
    format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s - %(message)s",
    datefmt='%d-%m-%Y %H:%M:%S',
)
