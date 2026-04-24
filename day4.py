# '''Nested if ''' #if bhitra if but elif bhitra ni if rakhna milxa
# per=100

# if (per<0 and per>100):
#     print("Invalid number")

# elif(per>=80 and per<=100):
#     if per==80:
#         print("Lucky")
#     elif per==100:
#         print("Topper")
#     print("Dis") 

# elif(per>=60 and per>79):
#     print("first")  

# else:
#     print("failed")                



# '''Gender'''
# gender="F" 
# if gender=="M":
#     print("Male")
# else:
#     print("Female")

# '''another way'''
# data= "Female" if gender=="F" else "Male" 
# print(data)


# '''Type Casting/Conversion-euta type bata arko ma laijane'''
# a =input("Enter a number") #user input jaile string hunxa
# b=input("Enter a 2nd number")
# print(type(a))
# #print(a+b) gare concat hunxa add hudaina kinaki yo string ho so int ma laijane
# print(int(a)+int(b))
# print("User enter",a)



# a=input("Enter a number")
# b=input("Enter 2nd number")
# print(float(a)+float(b))

# print("User enter",a)

# a=12
# print(type(a))

# a="12"
# print(str(a)) #change hudaina  12 already string ma xa

# COMMENT GARNA CLT+/ GARNE ANI HATAUNA LAI NI TEI GARNE 


'''List-ordered collection''' #mutable ho-change garna milxa
#kun type bhanyo bhane square bracket dekhesi list ho 
print("-----------List----------")
a=[1,2,3,4,5]
print(type(a))
data=["hello",1,True,1.5]
print(data)
#print(data[10]) gare error aauxa index error :List out of range bhanera data ma xaina teibhayera
print(data[1]) #positive ma 0,1,2,3 hunxa agadi bata count garxa
print(data[-1]) # negative ma -1,-2,-3,-4 hunxa paxadi bata count garxa

print(len(data)) #list ko length count hunxa ra esma length count 1 dekhi start hunxa not 0 like index 



'''SLICING IN LIST'''
teachers=['Naisr','Ifran','Haris','Sheraz','Farhan','Khalil','Haris','Ihsan']
print(teachers[1:5]) #slicing bhaneko katne ho ani 1 dekhi 4 samma hunxa paxadi ko lidaina
print(teachers[1:])  #1 dekhi sab whole linxa
print(teachers[:5])  #agadi ko purai 0 dekhi 4 samma linxa
print(teachers[:])   #whole leko -no slicing
