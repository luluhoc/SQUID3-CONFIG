file = open("ip.txt", "r")

tpl = """acl ip{index} myip {ip}
tcp_outgoing_address {ip} ip{index}"""

for index, line in enumerate(file):
    print(tpl.format(index=index, ip=line.strip()))

print
print
print

print("Thanks for using created by LULU HOC")