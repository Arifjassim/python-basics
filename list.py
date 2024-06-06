fruits=['apple',1,'orange',2]
print(type(fruits))# to find the type
print(fruits)
print(fruits[0])
print(fruits[2])
print(len(fruits))
print(fruits[-1])#negative intext (to pick last element)
print(fruits[1:3])
print(fruits[:3])
fruits[0]='banana'#to changing element
print(fruits)
fruits[2:4]=[12,14]
print(fruits)
fruits.append('cherry')#to add iteam last
print(fruits)
fruits.insert(2,16)# to add item without delete
print(fruits)
fruits2=[1,2,'chaya',5]
fruits.extend(fruits2) #to add new list(extend)
print(fruits) 
fruits.remove('chaya')#to remove 
print(fruits)
fruits.pop(2) # to remove position with number
print(fruits)
fruits.clear()# to clear everthing
print(fruits)
del fruits2[3]
print(fruits2)
del fruits # list complet ayi delete akan
#print(fruits)
fruit=["apple","orange","cherry"]
fruit.sort()# to alphabatic order
print(fruit)
fruit.sort(reverse=True)# reverse order
print(fruit)
veg=fruit.copy()#
print(veg)
fruits3=veg+fruits2#
print(fruits3)
for i in fruit:
    print(i)
for x in range(len(fruit)):
    print(fruit[x])