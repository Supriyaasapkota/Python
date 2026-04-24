a=[1,2,3,4,5]
a[0]=100
 #a[10]=100
print(a) 

#lidai xau bhane error aauxa ,kunai data pathaye error aaudaina

#append -dherai use garxau 

a=[1,2,3] #euta matrai list add garxa paxadi ekai choti 5,6 garna mildaina
a.append(5)
a.append(6)
print(a)

item=[] #list ma kei value xaina so 12 hunxa paxi pheri 13 add gareko so 12,13
item.append(12)
item.append(13)

print(item)


#insert 
teachers=['Nasir','Irfan','Haris', 'Sheraz', 'Farhan', 'Khalil', 'Haris', 'Ihsan']
teachers.insert(1,"Hari")
print(teachers)

teachers.insert(100,"test")
print(teachers)



#extend -naya variable banauna mildaina
a=[1,23,4]
b=[5,6,7]
#[1,23,4,5,6,7]
b.extend(a)
a.extend(b)
print(a)
print(b)


#concat -naya variable banauna milxa concat ma
a=[1,23,4]
b=[5,6,7]
c=a+b
print(c)
print(a,b)


#del
#pop
#remove
#clear 
#yo sab le list ko value hatauxa 

#del
data=[1,23,4,5,6,7]
del data[0]

print(data)

#pop
remove_data=data.pop()
data.pop(1)
print(data)
print(remove_data)

#item=[]
#item.pop()
#print(item)

#remove
a=[1,2,3,4,5]
a.remove(4)
#a.remove(20)-error case
a=[1,1,2,2,3,4]
a.remove(2)
print(a)


#clear
data=['Nasir', 'Hari', 'Irfan', 'Haris', 'Sheraz', 'Farhan', 'Khalil', 'Haris', 'Ihsan', 'test']
data.clear()
print(data)


#Nested List -List bhitra list rakhne
a=[1,2,3]
b=[5,6,7,7,[1,2,3]]
print(len(b))
print(b[4][1])
item=b[4] #another method 
print(item[1])