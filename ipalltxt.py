file = open("ip.txt", "r")
file1 = open("acl.list.txt", "w")

tpl = """acl ip{index} myip {ip}
tcp_outgoing_address {ip} ip{index}
"""

for index, line in enumerate(file):
    file1.write(tpl.format(index=index, ip=line.strip()))



print("Thanks for using created by LULU HOC")