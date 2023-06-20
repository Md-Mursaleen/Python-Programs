#Create a tupple and print it in both reverse and non-reverse order.
a=()
n=int(input("Enter the range for a tuple....\n"))
b=list(a)
for i in range(1,n):
    val=int(input("Enter the element in the tuple...."))
    b.append(val)
print("The non-reverse order of the tuple is....",tuple(b))
c=[]
for i in range(n-2,-1,-1):
    c.append(b[i])
print("The reverse order of the tuple is....",tuple(c))    



