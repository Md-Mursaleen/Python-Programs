#3rd Star Pattern.
ascii_value=65
for i in range(1,6):
    for j in range(i):
        a=chr(ascii_value)
        print(a,end=" ")
    ascii_value+=1    
    print("\n") 


ascii_value=70
for i in range(6,0,-1):
    for j in range(i):
        a=chr(ascii_value)
        print(a,end=" ")
    ascii_value-=1    
    print("\n")        