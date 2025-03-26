import os
print("checking with file existance...")
if os.path.exists("f1.txt"):
    print("file exists")

else:
    print("file does not exists")

myfile=open("f1.txt","w")
myfile.write("Hello World! I am Suyog, a Python Developer.")
myfile.close()

os.remove("f2.txt")