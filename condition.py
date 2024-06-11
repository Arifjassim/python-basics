a=33
b=33
if b<a:
    print("b>a")
elif b>a:
    print('b<a')
elif b==a:
    print("equal")
else:
    print("error")

x=5
y=10
if(x>7 and y<15):
    print("correct")
else:
    print("error")

i=5
j=10
if(i>7 or j<15):
    print("correct")
else:
    print("error")

fruits=("apple","grape","orange")
print(fruits)
if("apple" in fruits):
    print("correct")
else:
    print("error")

d=int(input("enter a number"))
if (d%2)==0:
    print("even")
else:
    print("odd")

f=int(input("enter a prime number"))
if (f>1):
    for i in range(2,f):
        if (f%i)==0:
            print("not a prime")
            break
    else:
         print("prime number")
else:
    print("not a prime")

    
j=[10,20,30,20,30,40,20,50]
j1=set(j)
print(j1)
k=[]
#print(j)
for i in j:
    if i not in k:
        k.append(i)
print(k)

std1={"name":"jassim","age":21,"place":"thalikulam"}
for i,j in std1.items():
    print(i,"-->",j)

f=[1,2,2,3,3,3,4,4,4,4,]
s=[]
print(f)


raw=5
for i in range(raw):
    for j in range(i):
        print(i,end=" ")
    print(' ')

raw=11
for i in range(raw):
    for j in range(i):
        print("*",end=" ")
    print(' ')

        