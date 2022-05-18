
'''
#print the numbers between 1 to 100
#print even numbers
#get only first 7 numbers only
#break the loop


num = 1
count = 0
while num < 100 :
    if num %2 == 0:
        print ( num )
        count += 1
        if count == 7 :
            break
    num += 1
print("while loop is close ")


#print the numbers bw 1 to 100
#print even numbers
#get only frst 7 even numbers
#break the loop


num1 = 1
count = 0
while num1 <= 100:
    if num1 % 2 == 0:
        print (num1)
        count += 1
        if count == 7:
            break
    num += 1
print ( "while loop is closed")



#print (------------ for looop--------)


#print numbers between 1 to 100
#print even numbers
#ger only frst 7 even numbers
#break the loop

count = 0
for val in range (1,100):
    if val % 2 == 0 :
        print(val)
        count += 1
        if count == 7:
            break
print ( "for loop is closed")


# print(--------enter another for loop -------)
#print even numbers bw 50 to 80

for val in range (1,101):
    if val >= 50 and val<= 80:
        if val % 2 == 0:
            print (val)
    elif val > 80:
        break
print ( "end for loop")




#print (------------continue----------)

#print between 1 to 50
#find the number divisible by 5
#if the same number divisible by 10 dont do anything


for val in range (1,51):
    if val % 5 == 0:
        if val % 10 == 0:
            continue
        print (val)
print("continue type for loop is closed")



#print only frst 3 even numbers between to 10 to 50
count = 1
for val in range (10,50):
    if val % 2 == 0:
        if count > 3:
            break
        print(each)
        count += 1


#print even numbers .skip first 3 even numbers and after 7 even numbers onwords
count = 1
for val in range (1,51):
    if val % 2 == 0:
        count += 1
        if val <= 4:
            continue
            print(each)
        if val > 7:
            break

# print even numbers in the list and print it
#p  rint ( even numbers count)
list1 = [1,2,3,4,5]

count = 0
for val in list1:
    if val % 2 == 0:
        count += 1
        print (val)

print("total even numbers :",count)


print (   "even numbers count" )
tup1 = (1,2,3,4,5,6,7,8,9,10)
count = 0
for val in tup1:
    if val % 2 == 0:
        count += 1
        print(val)
print("even number:",count)


#print first 7 bw 1 to 10
num1 = 1
num2 = 20
count = 0
while num1 <= num2:
    print (num1)
    count += 1
    if count == 7:
        break
    count += 1
print ("end of loop")

'''

x = 1
while  x <= 1:
    print (x)
    x += 1
print ("end of the program")


n1 = 100
n2 = 50
if n1 <= n2:
    while n1 <= n2:
        print (n1)
        n1 += 1
else:
    print( "n1 should < be n2")
    print("end program")


#print ("odd numbers)
n1 = 1 #int(input(enter any number)
n2 = 100#int(input(enter any number)
while n1 <= n2:
    if n1 % 2 == 1:
        print ( n1)
    n1 += 1
print ("correct value")


x = 1
y = 100
while x <= y:
    if x % 5 == 00:
        print ( x )
        if x % 10 == 0:
            break
    x += 1

print (" while loop closed")


print ( "divisible by 3 and 7")
m1 = 1
m2 = 100
while m1 <= m2:
    if m1 % 3 ==0 and m1 % 7 == 0:
        print ( m1 )
    m1 += 1
print ( "while loop closed")