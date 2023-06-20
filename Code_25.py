#Copy specific item from one tuple to another tuple.
a=(10,20,30,40)
#Only even numbers:example(20,40)
b=()
c=list(b)
for i in range(4):
    if i%2!=0:
          c.append(a[i])
print("The new tuple is....",tuple(c))          

  