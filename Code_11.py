#File Handling in Python.
ptr=open("student.txt",mode="w")
for i in range(1,3):
    name=input("Enter the name.....")
    ptr.write(name)
    ptr.write("*")
    ptr.write("\n")
ptr.close()
ptr=open("student.txt",mode="rb")
print(ptr.read(12))
print(ptr.read(5))
print(ptr.read())
