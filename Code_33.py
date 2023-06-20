#WAP to create a new dictionary from a given dictionary by extracting the mentioned keys.
d1={"name":"deepak","age":19,"city":"delhi"}
#Keys are name and city only.

print(d1)
d2={}
for a in d1:
    d2[a]=d1[a]

#print(d2)