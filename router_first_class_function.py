def device1(text):
    return text.upper()

def device2(text):
    return text.lower()

def group_of_devices(protocol):
    router = protocol(""" Arista Router 7280CR3-96 is a feature of 7280R3 Series """)
    print(router)

def create_adder(x):
    def akamai_bar_raiser(y):
        return x**y
    return akamai_bar_raiser

migeot = create_adder(3)
print(migeot(3))

group_of_devices(device1)
group_of_devices(device2)
