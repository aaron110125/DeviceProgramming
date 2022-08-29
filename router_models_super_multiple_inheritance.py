
class RouterModels:
    def __init__(self,RouterModels):
        print(RouterModels,'is a Router')

class Cisco(RouterModels):
    def __init__(self,ciscoModelname):
        print(ciscoModelname,'is a Cisco product')
        super().__init__(ciscoModelname)

class Cisco_Meraki(RouterModels):
    def __init__(self,Cisco_Meraki):
        print(Cisco_Meraki,"is a Cisco Integrated service Router")
        super().__init__(Cisco_Meraki)

class JuniperRouters(RouterModels):
    def __init__(self,JuniperRouters):
        print(JuniperRouters,"is tightly aligned with SDN")
        super().__init__(JuniperRouters)

class NetCademy(JuniperRouters,Cisco_Meraki):
    def __init__(self):
        print("**Routers used in Netcad**")
        super().__init__('Cisco5000')

Model = NetCademy()
print('')
sr = JuniperRouters('SR')

