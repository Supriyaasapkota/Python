print(True and True)
print(2==2 and 1>=1)

print("Test"=="hello" and True)
      

logged_in=False 
print(not(logged_in))       
      
''' if condition
'''

if(2==2): #condition true bhaye true print
    print("this is true")
    print("this is also true block")
else:
    print("this is else")    


logged_in=True 
if logged_in:
    print("User is logged in")    


gpa=3.60
if (gpa<0 and gpa>4):
    print("Invalid GPA")    
elif(gpa<4 and gpa>=3.65):
    print("A+")
elif(gpa<3.65 and gpa>=3.25):
    print("A") 
elif(gpa<3.25 and gpa>=3.10):
    print("B+")
elif(gpa<3.10 and gpa>=2.80):
    print("B") 
elif(gpa<2.80 and gpa>=2.65):
    print("C+")    
else:
    print("Fail")       


        