file1 = open("aclinput.txt","w") 

ip = raw_input("Enter IP list:").split(" ")

tpl = """acl ip{index} myip {ip}
tcp_outgoing_address {ip} ip{index}
"""

for index, line in enumerate(ip):
    file1.write(tpl.format(index=index, ip=line.strip()))


print("Thanks for using created by LULU HOC")