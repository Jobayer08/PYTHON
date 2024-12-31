f=open("demo1.txt", "r")
data =f.read()
print(data)
line1=f.readline()
print(line1)
f.close()
f=open("demo1.txt", "w")
f.write("i want to learn")
f.close()
f=open("demo1.txt", "a")
f.write("\ni want to learn")
f.close()
f=open("demo1.txt", "r+")
f.write("want")
print(f.read())
f.close()
with open("demo1.txt", "r") as f:
    print(f.read())
with open("demo2.txt", "w") as f:
    pass
import os
os.remove("demo2.txt")    
