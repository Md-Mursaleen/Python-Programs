#Two dictionary are given then WAP to merge them.
d1={"one":1,"two":2,"three":3}
d2={"four":4,"five":5,"six":6}
d3={}
d3=d1.copy()
#a=d2.keys()
#b=d2.values()
#for i in range(1,4):
    #d3[a]=b
#print(d3)
for a in d2:
    d1[a]=d2[a]
print(d1)