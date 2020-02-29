import time
import logging

def get_timestamp():
    return time.strftime("%Y%m%d-%H%M%S")

def create_logger(file=""):
    filepath = time.strftime("%Y%m%d")
    filepath = f".//logs//{file}{filepath}.log"
    logging.basicConfig(filename=filepath,
                        level=logging.INFO, 
                        format='%(levelname)s %(asctime)s - %(message)s', 
                        filemode='w')
    return logging.getLogger()