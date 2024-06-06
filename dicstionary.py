student={'name':"jassim",'age':21,'place':"nattiga"}
print(student)
print(len(student))
print(student['name'])
x=student.get('place')#to the selected value
print(x)
y=student.keys() #to display every key
print(y)
z=student.values()#to diplace every values
print(z)
s=student.items()# full items kanaan
print(s)
student['name']="arif"# to change 
print(student)
student.update({"age":20})#to change and add
print(student)
student.update({"course":"bca"})#to add
print(student)
student.pop('place') # to delete 
print(student)
student.popitem()# to delete last item
print(student)
student1=student.copy()#copy cheyyan
print(student1)
family={'child1':{'name':'jassim','age':21},
        'child2':{'name':'arif','age':22},
        'child3':{'name':'haleem','age':23}
        }
print(family)
for i in student.values():
    print(i)
for i,j in student.items():#to find the key and values
    print(i,j)


