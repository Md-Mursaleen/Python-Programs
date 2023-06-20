#WAP to remove items from set1 that are not common to both set1 and set2.
s1={10,20,30,40,50}
s2={40,50,60,70,80}
s3=set()
s3=s1.union(s2)-s1.intersection(s2)
s4=set()
s4=s1-s3
print(s4)