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

def firehose_envelope(func2):
    def inner_fi(*args,**kwargs):
        print("Before playing Pasoori ")
        returned_value = func2(*args,**kwargs)
        print("After playing Pasoori")
        return returned_value
    return inner_fi

@func_time_calculator
def play_alexa():
    time.sleep(2)
    log.debug("Hello Aaron, how are you?")
    print("Play Pasoori")

@firehose_envelope
def two_music_time_addition(a,b):
    print("Song time calculation")
    return (float(a) + float(b))

a,b = "1","0.0003"

play_alexa()
print("Sum of two music time is {}".format(two_music_time_addition(a,b)))
