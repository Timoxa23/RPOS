def is_valid_ip(ip):
    octets = ip.split('.')
    if len(octets) != 4:
        return False
    for octet in octets:
        if not octet.isdigit():
            return False
        if int(octet) < 0 or int(octet) > 255:
            return False
    return True

def determine_ip_class(ip):
    first_octet = int(ip.split('.')[0])
    if first_octet >= 1 and first_octet <= 127:
        return 'unicast'  # Class A
    elif first_octet >= 128 and first_octet <= 191:
        return 'unicast'  # Class B
    elif first_octet >= 192 and first_octet <= 223:
        return 'unicast'  # Class C
    elif first_octet >= 224 and first_octet <= 239:
        return 'multicast'  # Class D
    elif ip == '255.255.255.255':
        return 'local broadcast'
    elif ip == '0.0.0.0':
        return 'unassigned'
    else:
        return 'unused'

while True:
    ip_address = input("Введите IP-адрес в формате 10.0.1.1: ")
    if is_valid_ip(ip_address):
        break
    else:
        print('Incorrect IPv4 address, пожалуйста, попробуйте снова.')
print(determine_ip_class(ip_address))
