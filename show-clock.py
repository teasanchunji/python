
import netmiko

devices = '''
172.16.171.101
172.16.171.102
172.16.171.103
172.16.171.104
172.16.171.105
'''.strip().splitlines()

device_type = 'cisco_ios'
username = 'cisco'
password = 'cisco'


netmiko_exception = (netmiko.ssh_exception.NetMikoAuthenticationException,
                     netmiko.ssh_exception.NetMikoTimeoutException)

for device in devices:
    try:
        print("~" * 79)
        print("Connecting to device", device)
        connection = netmiko.ConnectHandler(ip=device, device_type=device_type, username=username, password=password)
        print(connection.send_command("show ip int brie\n"))
        print(connection.send_command("enable\n"))
        print(connection.send_command("configure terminal\n"))
        print(connection.send_command("int loop 0\n"))
        print(connection.send_command("ip address 1.1.1.1 255.255.255.255\n"))
        print(connection.send_command("end\n"))
        print(connection.send_command("show ip int brie\n"))
        connection.disconnect()

    except netmiko_exception as e:
        print("Failed to ", device, e)
