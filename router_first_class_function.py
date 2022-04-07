def device1(text):
    return text.upper()

def device2(text):
    return text.lower()

def group_of_devices(protocol):
    router = protocol(""" Arista Router 7280CR3-96 is a feature of 7280R3 Series """)
    print(router)

group_of_devices(device1)
group_of_devices(device2)
