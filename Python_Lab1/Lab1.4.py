command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'

vlan_list1 = set(command1.split()[-1].split(','))
vlan_list2 = set(command2.split()[-1].split(','))
common_vlans = list(vlan_list1 & vlan_list2)
common_vlans = sorted(common_vlans, key=int)
print(common_vlans)
