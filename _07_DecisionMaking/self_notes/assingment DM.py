
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

# calculate persontage of the student
x = int(input("calculate the percentage student"))
if x >= 80 and x <= 100:
    print("persontage of the student is A+")
elif x >= 60 and x <= 80:
    print(" persontage of the student is A")
elif x>=50 and x <= 60:
    print(" persontage of the student is B+")
elif x >= 45 and x <= 50:
    print(" persontage of the student is B")
elif x >= 25 and x <= 45:
    print(" persontage of the student is c")
else:
    print(" student not qualified")

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

#calculate the net amount as marked prize and discount to pay according to the critiria


x = int(input("total market price"))
if x < 10000 :
   y =(x/100)*80
   print("your selling price:",y)
elif x <=10000 and x > 7000:
    y = (x/100)*85
    print("your selling price:",y)
elif x <= 7000:
     y = (x/100)*90
     print("your selling price:",y)


'''

#accept the number of days from the user and calculate the charge for library according to following:
#till five days : rs2/day.
#six to ten days : rs3/day.
#11 to 15 days : rs4/day.
#after 15 days : 5rs/day.

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













