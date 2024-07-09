class person:#classinte constract anne "init" (nb)
    def __init__(self,fname,lname):
        self.firstname=fname 
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
x=person("jassim","arif")
x.printname()

#child class 

class student(person):
    pass 
y=student("tom","jerry")
y.printname()

#polymorphisam
#inheritanse


#method of overloading("last define chayynathe mathramme print avallo")
def product(a,b):
    p=a*b
    print(p)
def product(a,b,c):
    p=a*b*c
    print(p)
product(2,3,4)

#over riding
class parent():
    def __init__(self):
        self.value="inside"
    def show(self):
        print(self.value)
class child(parent):
    def __init__(self):
        self.value="inside chid"
    def show(self):
        print(self.value)
obj1=parent()
obj2=child()
obj1.show()
obj2.show()


