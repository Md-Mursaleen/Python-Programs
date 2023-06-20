#OOPs Concept in Python.
class parrot:
    #instance attributes
    def __init__(self,name,age):
        self.name=name
        self.age=age
    #instance method    
    def sing(self,song):
        return (self.name,song)    
obj=parrot("Mitthu",10)
print(obj.sing("Happy"))
