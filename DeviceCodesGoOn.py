class networkTopology:

    device1 = "ciena6500"

    def __init__(self,device_name):
        self.device_name = device_name

NetDevice = networkTopology("Router1")
NetDevice2 = networkTopology("Router2")

print("Router1 belongs to the family of {}".format(NetDevice.__class__.device1))
print("Router2 belongs to the family of {}".format(NetDevice2.__class__.device1))

print("L2 routing will be done by {}".format(NetDevice.device_name))
print("L3 routing will be done by {}".format(NetDevice2.device_name))
