def get_int_vlan_map(config_file):
    access_ports = {}
    trunk_ports = {}

    with open(config_file) as file:
        for line in file:
            line = line.strip()
            if line.startswith('interface'):
                interface = line.split()[1]
            elif 'access vlan' in line:
                vlan = int(line.split()[-1])
                access_ports[interface] = vlan
            elif 'mode access' in line and 'access vlan' not in line:
                access_ports[interface] = 1  # Добавляем информацию о VLAN 1
            elif 'trunk allowed vlan' in line:
                vlans = line.split()[-1].split(',')
                vlans = [int(vlan) for vlan in vlans]
                trunk_ports[interface] = vlans

    return access_ports, trunk_ports

access_dict, trunk_dict = get_int_vlan_map('config_sw2.txt')

print('Access ports:', access_dict)
print('Trunk ports:', trunk_dict)
