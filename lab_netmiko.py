from netmiko import ConnectHandler
#create data router 
R1={
    'device_type':'cisco_ios',
    'host':'172.23.15.203',
    'username':'cisco',
    'password':'cisco',
    'port':22,
    'secret':'cisco'
}

list_config=['int lo99',
            'description create by netmiko',
            'ip add 19.19.19.19 255.255.255.255',
            'do show ip int brief']

net_connect=ConnectHandler(**R1)
net_connect.enable()
output=net_connect.send_config_set(list_config)
print(output)

