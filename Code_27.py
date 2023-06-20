#Write to program to update the first set with items that do not exits in the second set.
s1={10,20,30,40,50}
s2={40,50,60,70,80}
s3=set()
s3=s1.intersection(s2)
s4=set()
s4=s1-s3
print("The updated first set is given as......",s4)
