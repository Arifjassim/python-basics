fruits={'apple','grape','jack fruit'}
print(fruits)
print(len(fruits))
fruits.add('orange')# to add single items
print(fruits)
fruits2={1,2,3}
fruits2.update(fruits)#to join
print(fruits2)
fruits.remove('grape')
print(fruits)
fruits.discard('grape')# to delete a items multiple time without error
print(fruits)
fruits.pop()# to delete random items
print(fruits)
set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}
set3=set1.union(set2)# 2 setilthe ella elemant kittan
print(set3)
set4=set1.intersection(set2)#comman
print(set4)
set5=set1.issubset(set3)# subset kittan
print(set5)
set6=set1.issuperset(set3)
print(set6)
for i in set1:
    print(i)