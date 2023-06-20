#WAP to remove the elements from the given set.
a={10,20,30,40,50}
#Remove 10,20 and 30.
b=list(a)
print(b)
for i in range(3):
    b.remove(b[i])
print("The updated set is.....",set(b))
#This method is not good because list ke andar elements randomly aa jayenge.
for i in range(1,4):
    a.remove(10*i)
print(a)    
