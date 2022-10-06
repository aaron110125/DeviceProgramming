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

## Second class to find out capacity in the network

class addition_traffic_load:
    first_router_load = 0
    second_router_load = 0
    third_router_load = 0

    def __init__(self,first,second):
        self.first = first
        self.second = second

    def display(self):
        print("Traffic displayed on first_router is {} Gbps".format(str(self.first)))
        print("Traffic displayed on first_router is {} Gbps".format(str(self.second)))
        print("Total traffic in the network is {} Gbps".format(str(self.total_capacity)))

    def calculate_total_capacity(self):
        self.total_capacity = self.first + self.second

cap = addition_traffic_load(12800,25600)
cap.calculate_total_capacity()
cap.display()




