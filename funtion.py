def my_name():
    print("hello")
my_name()


def names(fname,lname):#firs
    print(fname+" "+lname)
names("jassim","arif")


def arbitrary(*kids):
    print(kids[2])
arbitrary("tom","jerry","oggy","jack")
arbitrary("a","b","c","d","e")

def keyword(a,b,c):
    print(b)
keyword(a=1,b=2,c=3)


def arbitrary_keyword(**kids):
    print(kids["b"])
arbitrary_keyword(a=0,b=8,c=7)
fruits=["mango","grape","apple","orange"]


def frui(foods):
    for i in foods:
     print(i) 
frui(fruits)  


d=int(input("enter a number"))
def number(f):
    if (f%2)==0:
        print("even")
    else:
        print("odd")
number(d)  
        

f=int(input("enter a number"))
def number(s):
    if(s>1):
        for i in range(2,s):
            if (s%i)==0:
                print("not a prime")
                break
        else:
                print("prime number")
    else:
        print("not a prime")
number(f)


maximum=[1,5,10,15]
print(maximum)
def max(b):
    for i in b:
        c=0
        c=c+i
    return c
max(maximum)


    


