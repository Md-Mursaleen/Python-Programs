#Write to program to get only the unique elements from the given two sets.
s1={10,20,30,40,50}
s2={40,50,60,70,80}
s3=set()
s3=s1.union(s2)-s1.intersection(s2)
print("The set of unique elements is.....",s3)
