f=open("file.txt","r")
print(f.read())
f=open("file.txt","r")
print(f.read(2))
j=open("file.txt","a")
j.write("IT Solutions")
j.close
j=open("file.txt","r")
print(j.read())