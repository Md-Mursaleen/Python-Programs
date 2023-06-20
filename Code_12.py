#Modules in Python.
#NumPy Module in Python.
#import numpy as np
#print(dir(np))
import sys
print(sys.path)
import numpy as np
a=[]
n=int(input("Enter the range....."))
for i in range(n):
    b=int(input("Enter the elements in the list....."))
    a.append(b)
print(a)    
my_arr=np.array(a)
print(my_arr)
print(my_arr.size) 

a=[{1,2,3},{4,5,6}]
print(a)    
my_arr=np.array(a)
print(my_arr)
print(my_arr.size) 


