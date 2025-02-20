ospf_route = 'O 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

parts = ospf_route.split()

protocol = "OSPF"
prefix = parts[1]
ad_metric = parts[2].strip('[]')
next_hop = parts[4].strip(',')
last_update = parts[5].strip(',')
outbound_interface = parts[6]

output = f"""Protocol: {protocol}
Prefix: {prefix}
AD/Metric: {ad_metric}
Next-Hop: {next_hop}
Last update: {last_update}
Outbound Interface: {outbound_interface}"""

print(output)
