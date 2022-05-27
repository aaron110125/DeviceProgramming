#decorator_learning 2

def serial_number_addition(func):
    def inner_func_addition(*args,**kwargs):
        print("Before serial number addition is done")
        returned_value = func(*args,**kwargs)
        print("After serial number addition is done")
        return returned_value
    return inner_func_addition

@serial_number_addition
def two_devices_serial_number_addition(a,b):
    print("Inside the serial number addition function!!")
    return a + b

a,b = 2350123467, 67820837463
print("Sum of two serial number of devices=",two_devices_serial_number_addition(a,b))
