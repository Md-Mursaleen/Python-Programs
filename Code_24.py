#Swap the two given tuple.
t1=(10,20,30,40)
t2=(50,60,70,80)
a=list(t1)
b=list(t2)
for i in range(4):
    temp=a[i]
    a[i]=b[i]
    b[i]=temp
print("t1=",tuple(a)) 
print("t2=",tuple(b))   