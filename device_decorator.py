from functools import wraps

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper

def device_name(device):
    def router(*args, **kwargs):
        print('Wrapper ran before {}'.format(device.__name__))
        return device(*args, **kwargs)
    return router

class decorator_device(object):
    def __init__(self, device_name):
        self.device_name = device_name

    def __call__(self, *args, **kwargs):
        print('Call occured before {}'.format(self.device_name.__name__))
        return self.device_name(*args, **kwargs)

@device_name
def display_device():
    print('Display of the device is cisco-xe300')

@my_logger
def display_info(regard, switch):
    print(f'Display ran with arguments ({regard },{switch})')

display_info('cisco-xe300','bond24')
