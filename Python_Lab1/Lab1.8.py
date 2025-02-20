IP = '192.168.3.1'

octets = IP.split('.')
binary_octets = [format(int(octet), '08b') for octet in octets]
decimal_line = ' '.join(octet.ljust(10) for octet in octets)
binary_line = ' '.join(binary_octet.ljust(10) for binary_octet in binary_octets)

print(decimal_line)
print(binary_line)
