#Create a dictionary and print the items of the dictionary.
a={"one":1,"two":2,"three":3,"four":4}
b=a.keys()
c=a.values()
print("The keys is.....",b)
print("The values is....",c)
print("The corresponding values of the keys of dictionary is given as....\n")
#for i in range(1,4):
for b in a:
     print(b)
     print(a.get(b))
        
   
