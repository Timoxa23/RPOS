mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']
mac_cisco = []

for address in mac:
    cisco_address = address.replace(':', '.')
    mac_cisco.append(cisco_address)

print(mac_cisco)
