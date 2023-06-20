#5th Star Pattern.
a=1
n=1
for i in range(1,4):
    for k in range(a,3):
        print(" ",end=" ")
    for j in range(1,i*2):
        print(n,end=" ")
        n=n+1
    print("\n")
    a=a+1
b=2
m=8
c=2     
for i in range(1,3):
    for k in range(b,3):
        print(" ",end=" ")
    for j in range(1,c*2):
        print(m,end=" ")
        m=m-1
    print("\n")
    b=b-1
    c=c-1            
