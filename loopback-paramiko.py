import paramiko
import time

ip_address = "172.16.171.101"
username = "cisco"
password = "cisco"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)

print ("success connection", ip_address)
remote_connection = ssh_client.invoke_shell()
remote_connection.send("conf t\n")
remote_connection.send("int loop 1\n")
remote_connection.send("ip address 2.2.2.2 255.255.255.255")
remote_connection.send("router opsf 1 \n")
remote_connection.send("network 0.0.0.0 255.255.255.255 area 0\n")
