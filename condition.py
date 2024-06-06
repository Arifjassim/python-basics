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