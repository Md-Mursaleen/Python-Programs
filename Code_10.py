#File Handling in Python.
ptr=open("student.txt",mode="w")
for i in range(1,3):
    name=input("Enter the name.....")
    roll_no=input("Enter the roll no....")
    marks=input("Enter the marks of student in math subject.....")
    ptr.write(name)
    ptr.write(roll_no)
    ptr.write(marks)
ptr.close()
ptr=open("student.txt",mode="r")
print(ptr.read(12))
print(ptr.read(2))
marks1=int(ptr.read(2))
print("Marks of first student is",marks1)
print(ptr.read(5))
print(ptr.read(2))
marks2=int(ptr.read(2))
print("Marks of second student is",marks2)
total_marks=marks1+marks2
print("Total marks of both student is",total_marks)

ptr.close()


