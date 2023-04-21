import logging
import datetime
import time 
import typing

def log(level=logging.WARNING, **kwargs):
    logging.basicConfig(level=level)

    def logs(func):
        def wrapper(*args, **kwargs):
            # start time and logging start time 
            __start: float = time.time()
            logging.warning(f"started func {func.__name__} ==> {__start}")
            
            # run function
            result: typing.Any = func(*args, **kwargs)
            
            # end time and logging end time
            __end: float = time.time()
            logging.warning(f"ended func {func.__name__} ==> {__end}")
            
            return result
        return wrapper
    return logs
    