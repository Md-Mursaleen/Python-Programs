#Create a list and print it in both reverse and non-reverse order.
a=[]
n=int(input("Enter the range of a list....\n"))
for i in range(1,n):
    val=int(input("Enter a value in the list....."))
    a.append(val)

print("The non-reverse order of the list is.....",a)
b=[]
for i in range(n-2,-1,-1):
    b.append(a[i])
print("The reverse order of the list is......",b)    


