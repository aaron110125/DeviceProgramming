#Nested functions along with fixtures devices and closures code
import logging
logging.basicConfig(filename = 'vmos.log', level = logging.INFO)

def OuterTest(portland):
    vixen = portland
    def innnerTest():
        print(vixen)
    return innnerTest

def logger(trili):
    def device_logger(*args):
        logging.info('Running "{}" with arguments {}'.format(trili.__name__,args))
        print(trili(*args))
    return device_logger

def powerst(x,y):
    return x ** y

def modulost(x,y):
    return x % y

power_logger = logger(powerst)
modulo_logger = logger(modulost)

power_logger(3,4)
modulo_logger(20,3)

if __name__ == '__main__':
    myDeviceState = OuterTest("Device Reboot ongoing")
    myDeviceState()
