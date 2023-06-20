#Remove all occurances of a specified item from a given list.
a=[10,20,10,30,10,40,10,50]
#Remove 10
b=[]
for i in range(8):
    if i%2!=0:
        b.append(a[i])
print("The new list is....",b)     