#decorator learning

import time
import logging

log = logging.getLogger(__name__)

def func_time_calculator(func):
    def inner_fo(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Total time taken for: ", func.__name__, end - begin)
    return inner_fo

@func_time_calculator
def play_alexa():
    time.sleep(2)
    log.debug("Hello Aaron, how are you?")
    print("Play Pasoori")

play_alexa()
