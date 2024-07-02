
maximum=[1,5,10,15]
print(maximum)
def max(b):
    c=0
    for i in b:  
        c=c+i
    print(c)
max(maximum)
  


multi=[5,5,5,5,5]
print(multi)
def mul(o):
    d=1
    for i in o:
        d=d*i
    print(d)
mul(multi)


largest=[1,2,3,4,5,6,7,4,6,9,6,10,3,4]
print(largest)
largest.sort()
print(largest)
print(largest[-1])


large=[9,8,7,6,5,4,3]
print(large)
def larg(list):
    max=list[0]
    for i in list:
            if (i>max):
                max=i
    print(max)
larg(large)

small=[1,2,3,4,5,6]
print(small)
def smal(list):
    max=list[0]
    for i in list:
            if (i<max):
                max=i
    print(max)
smal(small)

check="hello world"
print(check)
def chec():
  vowels=0
vowels=("A","E","I","O","U","a","e","i","o","u")