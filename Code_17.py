#OOPs Concept in Python.
class parrot:
    #class attributes
    species="Bird"
    #instance attributes
    def __int__(self,name,age):
        self.name=name
        self.age=age

blu=parrot("Blu",12)
print(blu.__class__.species)
#print(blu.name,blu.age)
        