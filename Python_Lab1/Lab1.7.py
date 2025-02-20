MAC = 'AAAA:BBBB:CCCC'

mac_str = MAC.replace(':', '')
binary_mac = ''.join(format(int(char, 16), '04b') for char in mac_str)

print(binary_mac)
