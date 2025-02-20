CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'
vlan_list = CONFIG.split()[-1].split(',')
print(vlan_list)