#https://blog.router-switch.com/2017/04/upgrade-your-cisco-routers/

cisco_2800_series = ['Cisco 2801 ISR','Cisco 2811 ISR','Cisco 2821 ISR','Cisco 2851 ISR']
cisco_4300_series = ['Cisco 4321 ISR','Cisco 4351 ISR','Cisco 4351 ISR','Cisco 4431 ISR']
durand = len(cisco_2800_series)

for router in range(0,durand):
    print("{} is being replaced by cisco device {}".format(cisco_2800_series[router],cisco_4300_series[router]))