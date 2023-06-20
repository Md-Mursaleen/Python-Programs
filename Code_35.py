#OOPs Concept in Python.
class parrot:
    #class attributes
    species="Bird"
    #instance attributes
    def __init__(self,name,age):
        self.name=name
        self.age=age
obj=parrot("Mitthu",10)
#accessing the class attributes

print(obj.__class__.species)
#accessing the instance attributes

print(obj.name)
print(obj.age)

