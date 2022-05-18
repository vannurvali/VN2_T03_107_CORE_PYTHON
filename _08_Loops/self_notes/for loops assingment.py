



'''

# 5 write a program to prient first 10 even numbers ?
i = 1
for i in range(20,0,-2):
    print (i,end=" ")

'''




'''
# 6 write the program to print table of a number accepted from the user ?

n = int(input("enter the number:"))
for i in range (1,21):
    c = n*i
    print(n,"*",i,"=",c)
    
    
'''
'''
# 9  write the program to find the sum of digits of the number accepted from the user ?

a=10
b=20
c=30
for i in range(a,b,c):
    sum = a+b+c
    print(sum, end='')
print()

'''



'''
# 8 write the program to find the factorial number ?

num = int(input("enter any number::"))
factorial = 1
if num < 0 :
    print ("sorry factorial doest exist")
elif num == 0:
    print ("print the factorial 0 is 1")
else:
    for i in range(1,num + 1):
         factorial = factorial*i
    print("the factorial of",num,"is",factorial)
    
'''


'''
#7 write the program to display the product of digits of a number accepted from the user ?
num = int(input("enter a number:"))
product = 1
while num != 0:
    rem = num % 10
    product = product * rem
    num = num // 10
print(product)
'''

'''
#5 write the program to check the whether a number is prime or not ?


num = int(input("enter a number::"))
if num > 1:
    for i in range (2,num):
        if (num % i) == 0:
            print(num,"is not a prime number")
            print(i,"times",num//i,"is",num)

    else:
        print(num,"number is a prime number")


'''

'''
# 11.write the program to display the sum of odd nymbers and even numbers that fall between 12 and 37(including both numbers)
x = 0
for i in range (12,37):
    if (i % 2) == 0:
        x = x + i
    for i in range (12,37):
        if (i % 2) != 0:
            x = x + i
print("sum of odd numbers:",x)
print("sum of even numbers:", x)

'''


'''
# 12 write the program to display the numbers which are divisible by 11 but not by 2 between 100and 500 ?


for i in range (100,500):
    if i%11 == 0 and i%2 != 0:
        print(i,end="")


'''


'''
# 13 write a program to print the following pattern?
#print ("nested for loop")
rows = 5
for i in range (1,rows+1):
    for j in range (i):
        print("x",end='')
    print()


#write a program to print the following pattern
#print("program to number pyramid")
rows = 5
for i in range(0,rows +1):
    for j in range(i):
        print(i,end = "")
    print()

'''



'''
#14 write the program to print numbers from 1 to 20 expect multiple of 2&3.
x = 0
for i in range (1,20):
    if x !=

'''


'''
#print ("9 series numbers")
count = 0
for value in range (1,101):
    if value % 9 == 0:
        print (value)
        count += 1
        if count == 4:
            break
print ("end of loop")
'''


# while loop practice problems
#print numbers berween 1 to 100
#print even numbers
#print only first 7 even numbers
#break the loop
num = 1
count = 0
while num <= 100:
    if num % 2 == 0:
        print(num)
        count += 1
        if count == 7:
            break
    num += 1
print("end of while loop")
'''

#find the first 3 numbers which are divisible by 3 between 500 to 1000
#print numbers bw 500 to 1000
#filter divisible by 3
#loop the break once we ger 15 count

i = 500
count = 1
while i <= 1000:
    if i % 3 == 0:
        count += 1
        print(count , " : ",i)
        count += 1
        if count > 15:
            break
'''


names = ['massy','chaithu','arjun']
for x in names:
    print(x)
    if x == 'chaithu':
        break

names = ['massy','chaithu','arjun']
for x in names:
    if x == 'chaithu':
        break
    print(x)

names = ['massy','chaithu','arjun']
key = ['hello','world','india']
for x in names:
    for y in key:
        print(x,y)

names = ['massy','chaithu','arjun']
for x in names:
    if x == 'chaithu':
        continue
    print(x)

names= ['massy','chaithu','arjun']
for x in names:
    if x == 'chaithu':
        continue
    print(x)

for x in range(6):
    print(x)

for x in range (1,10):
    print(x)

for x in range (100,200,40):
    print(x)

names = ['massy','chaithu','arjun']
for x in names:
    if x == 'chaithu': break
    print(x)
else:
    print ('loop is not exicuted')


print('----------------while loopppppppp--------')
i = 1
while i < 6:
    print(i)
    i += 1

i = 0
while i < 5:
    print (i)
    i += 1
else:
    print('i is no longer statement')


names = ('bangalore is a great city')
print ('covert into upper case :',)





