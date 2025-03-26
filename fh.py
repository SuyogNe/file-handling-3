with open("sample.txt","w") as f:
    f.write("Hello World! I am Suyog, a Python Developer.")
f.close()

with open("sample.txt","r") as f1:
    data=f1.readlines()
    print("words are splitted in file...")
    for line in data:
        words=line.split()
        print(words)
f1.close()

