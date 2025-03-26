op=open("d.txt","w")
ip=open("c.txt","r")

lines=set()
print("checking for duplicate lines...")
for line in ip:
    newline=line.strip()
    if newline not in lines:
        op.write(line)
    lines.add(newline)


ip.close()
op.close()