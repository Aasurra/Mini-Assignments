#Student Name: Michael Lin
#Student ID: 101484021

from netmiko import ConnectHandler

for i in range(1, 4):
    with open(f"ospf_routing_protocol_{i}.txt", "w") as file:
        file.write(f"Host of router: router_{i}\n")
        file.write(f"Username to connect to router: admin\n")
        file.write(f"Password to connect to router: admin123\n")
        file.write(f"Port of router: 22\n")

with open("ospf_routing_protocol.txt", "w") as file:
    file.write("router ospf 1\n")
    file.write("network 0.0.0.0 0.0.0.0 area 0\n")
    file.write("distance 110\n")
    file.write("default-information originate\n")

for i in range(1, 4):
    with open(f"router_{i}.txt", "w") as file:
        lines = file.readlines()
        hostname = lines [0].split(":")[1].strip()
        username = lines [1].split(":")[1].strip()
        password = lines [2].split(":")[1].strip()
        port = int(lines [3].split(":")[1].strip())

    router = {
        "device_type": "cisco_ios",
        "host": hostname,
        "username": username,
        "password": password,
        "port": port,
    }

try:
    print(f"Connecting to {hostname}. . .")
    connection = ConnectHandler(**router)
    connection.enable()

    with open("ospf_routing_protocol.txt") as ospf_file:
        ospf_commands = ospf_file.readlines()

    output = connection.send_config_set(ospf_commands)
    print(f"OSPF configuration applied to {hostname}: \n{output}")

    connection.disconnect()

except Exception as e:
    print(f"Failed to connect to {hostname}: {e}")