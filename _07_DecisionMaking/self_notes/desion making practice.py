
#bus pass

# requirement: deluxe pass= 200
# metro pass= 100
#ordinary pass = 50
# student pass = 10
'''
a=int(input("enter the amount:::"))
if a<10 and a>=201:
  print ("enter valid amount:")
elif a>190:
 print ("deluxe pass:")
elif a>150:
 print ("metro pass:")
elif a>99:
 print ("ordinary pass:")
elif a>11:
 print("student pass")
else:
 print("not valid")
'''

'''
a=int(input("enter the amount bus fare::::"))
if a<100 and a>=1001:
 print("enter amount of bus fare:::")
if a>900:
 print("high class ticket :")
if a>500:
 print("middle class ticket:")
if a>300:
 print ("low class ticlet:")
if a>100:
 print("general pass ticket :")
else:
 print("pass is invalid")
'''
'''
a=int(input("ipl match ticket:::::"))
if a<2000 and a>=10000:
 print("ipl match ticlet fare::::::")
elif a>9000:
 print("back seat:")
elif a>5000:
 print("middle seat:")
else:
 print("ticlet is invalid::::")


'''
'''

a="sachin tendulkar"
if (a=='tendulkar'):
 print("ifcodition:")
'''
'''

if 10+20:
 print("successfully excuted 10+20")
if True:
 print("successfully excuted")
if False:
 print("false condition")
if False:
 print("false condition")
if True or False:
 print("or conditoin")

'''
'''
mark=80
mark=int(input("enter marks:::::"))
if marks >= 0 and marks<=100 :
if marks>=35:
 print ("result is :pass")
else:
 print ("result is :fail")
else:
print("enter valid marks")

'''
'''
marks = int(input("enter marks: "))
if  (marks< 35) :
   print("your fail...write exam again")
elif (marks>70):
   print("FIRST CLASS")
elif (marks>=55):
   print("SECOND CLASS")
else:
    print("THIRD CLASS")
'''
'''
x = int(input("enter your purshace amount limit :"))
if (x <= 50000) and (x>=40000):
    print(" you go with i phone mobile :")
elif (x <= 40000) and (x >= 30000):
    print("you go with one plus mobile :")
elif ( x <= 30000) and (x >= 20000):
    print ( "you go with samsung mobile :")
elif (x <= 20000) and (x >= 10000):
    print ("you go with samsung mobile phone :")
else:
    print("not available:")
'''
'''
x=10
y=20
if x>20:
    print(" hai massy")
if x<20:
    print (" hai hardik")
print("nothing")
'''
'''

marks = int(input("your result is pass::::"))
if marks < 0 and marks > 100 :
    print("please enter valid marks between 0 to 100 :::;")
else:
    if marks >= 60:
        print("result : first class")
        if marks == 100:
            print(" good congratulations::")
        elif marks >= 90:
            print ("good super:;")
    elif marks >= 50 and marks <= 60 :
            print ("result is second class")
    elif marks >= 35 and marks <= 50 :
            print ("result 3rd class")
    else :
        print ("result : fail")
        if marks == 0:
            print (" double super.....")
            

'''
'''
x=10
y=20
if x > y :
    print( "x is big value ")
elif x < y:
    print (" x is smaller value ")
else:
    print (" x is equal to y")
if y==10:
    print(" five ")
elif y > 20:
    print(" seven value ")
else:
    print (" six ")
'''

'''

num = int(input("enter the number:::"))
if num == 1:
    print("monday")
elif num == 2:
    print(" tuesday")
elif num == 3:
    print ("wednesday")
elif num == 4:
    print ("thursday")
elif num == 5:
    print("friday")
elif num == 6:
    print(" satday ")
elif num == 7:
    print("snday ")
else:
    print ("invalid number")

'''
'''
x = int(input("enter the value:::"))
if x % 2 == 0:
    print("even number")
else :
    print(" odd number ")
    
'''

# decision making concept assingment  28/04/2022
'''
#calculate the persontage of class attendance
x =  75
x = int(input("enter persontage::"))
if x >= 75 and x <= 100:
    print(" student qualified for exam ")
elif x <= 75 and x >= 50:
    print("student not qualified for exam")
elif x <= 50 and x >= 40:
    print ("your are not promoted")
else:
    print(" better luck next time")
'''
'''
x= int(input("total number of working days::"))
y= int(input("total number of days absent::"))

per = (x - y)/x * 100
print("attendance in your",per)
if per >= 75 :
    print (" your qualified for exam ")
else:
    print(" your not qualified for exam")
'''
'''
# comapany decided to give bonus to employee according to following criteria
salary = int(input(" monthly salary of employee::: "))
service = int(input("salary and year of experience"))
if salary >= 10 :
    netbounce=0.1*salary
    print("enter bounce for 10 years:", netbounce)
elif service >= 6 and service <= 10 :
    netbounce=0.08*salary
    print (" enter bounce for years:",netbounce)
elif service <= 6 :
    netbounce=0.05*salary
    print("enter bounce fot years:",netbounce)
    
'''
'''

x = int(input("total market price"))
if x < 10000 :
   y =(x/100)*80
   print("your selling price:",y)
elif x <=10000 and x > 7000:
    y = (x/100)*85
    print("your selling price:",y)
elif x <= 7000:




#till five days : rs2/day.
#six to ten days : rs3/day.
#11 to 15 days : rs4/day.
#after 15 days : 5rs/day.
     y = (x/100)*90
     print("your selling price:",y)
     
'''
'''
#accept the number of days from the user and calculate the charge for library according to following:

x = int(input("how many number of days need to required::"))
if x > 15:
    y = x*5
    print("your charge is:",y)
if x <=15 and x >= 11:
    y =x*4
    print("your charge is:",y)
if x <= 10 and x >= 6:
    y = x*3
    print("your charge is:",y)
if x <= 5:
    y = x*2
    print("your charge is:",y)


'''
print('----------------------if statement also called as conditional statement----------------')

a = 50
b = 20
if a < b :
    print('a is lessthan b :')
elif a > b :
    print ('a is grather than b ')
else :
    print ('a is equal to b')


a = 100
b =100
if a > b :
    print ('a is grather than b :')
else:
    print ('a is equal to b')




print('----------------short hand if statement--------------------')
a = 10
b =  5
print (a) if a > b else print (b)

a = 200
b = 200
print (a) if a > b else print (b) if a < b else print (a)


# print('-----------------logical statements-------------')

a = 200
b =20
c =1000
if a > b and c < a :
    print ('both condition are true')


a =100
b = 20
c = 500
if a > b or c < a :
    print ('one condition is true so that statement is true ')


# nested if statement
x = 45
if x > 55:
    print ('yes statement true')
    if x > 63:
        print ('yes statement is true')
else:
    print ('statement is false ')










