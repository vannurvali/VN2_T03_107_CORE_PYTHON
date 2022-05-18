




#calculate the square of numbers

num = int(input('enter any number :'))
square = num*num
print('square of given no is :',square)



#1. parameters                              # 5 = 5*5 =25
def square(num):
    return num*num
number = int(input("please enter any numaric value :"))
square = square(number)

print("the square of a given number{0} = {1}".format(number,square))




#print('input 2 numbers and return as sum value   ( 4 + 5)')


def sum(x,y):
    return x + y
a = int(input("enter any number 1:"))
b = int(input("enter ant number 2:"))
c = sum(a,b)
print('sum of ',a , 'and',b, 'is',c)




#3. whether the given number is even or odd value

def even_odd(number):                           #even = 4  odd = 5
    if number % 2 == 0:
        return 'even'
    elif number % 2 != 0:
        return 'odd'

num = int(input('enter any number:'))
result = even_odd(int(num))
print(result)


# 4.factorial of a given number
def factorial(a):                                            #4*3*2*1  = 24
    fact = 1
    for p in range(a,0,-1):
        fact = fact*p
    return fact

n =int(input('enter any number '))
res = factorial(n)
print('factorial of ',n,'is',res)


# 5. return the multiple value tuple              #addition 100+ 50 =150
def multiple():                                    #subtraction 100 -50=50
    operation = 'sum'
    total = 50 + 100
    return operation,total ;

operation,total =multiple()
print(operation, total)

def multiple():
    operation = 'subtraction'
    total = 100 - 50
    return operation,total;

operation,total = multiple()
print(operation ,total)

'''
'''

#6. positional arguements method
def add_numbers(n1,n2):               # parameters
    sum = n1+n2
    return sum
result =add_numbers(5.4,2.5)               # arguament  one required positional arguement missing form the function
print(result)

# default arguament function
def add_number(n1=100,n2=1000):
    sum = n1+n2
    return sum

result = add_numbers(5.4,2.4)                 #missing 1 required positional arguement n2 value          #
print(result)

# keyword arguament function
def add_number(n1=100,n2=1000):
    sum = n1+n2
    return sum

result = add_numbers(n2=5.4,n1=2.4,n3=10)                 #missing 1 required positional arguement n2 value          #
print(result)






#7.multipication taple of given number
n = int(input('enter any number :'))
for i in range (0,11):
    print(n ,'*',i,'=',n*i)              # 5th table

'''
'''
#list method

print('-----------------sum of list tuple set dict-----------')
def list(a):
    total = 0
    total2 = 1
    for x in a:
        total = total + x
        total2 = total2 * x
    return total, total2


a = [1,2, 3, 4, 5]
ans = list(a)
print('sum and multipication of all number in list:', ans)


# tuple method
#
print('----------------tuple method-----------------')

def tuple(a):
    total = 0
    total2 = 1
    for x in a:
        total = total + x
        total2 = total2 * x
    return total, total2


a = (1, 2, 3, 4)
solution = tuple(a)
print('sum and multipication of all number in tuple:', solution)



#set method
print('-----------------------------set methiod-----------------')
def set(a):
    total = 0
    total2 = 1
    for x in a:
        total = total + x
        total2 = total2 * x
    return total, total2


a = {1, 2, 3, 4}
solution = set(a)
print('sum and multipication of all number in set:', solution)




#PRINT('------------------------------calculate the upper case and lower case letter given object-----------')


def upper_lower(str1):
    case = {'upper':0,'lower':0}
    for i in str1:
        if i.isupper():
            case['upper'] = case['upper']+1
        if i.islower():
            case['lower'] = case['lower']+1
    print('original :',str1)
    print('upper :',case['upper'])
    print('lower :',case['lower'])

upper_lower('SkillS CafE')


#print('-------------------take list make it unique---------------')
def unique_list( l ):
    x = []
    for a in l:
        if a not in x :          #if one element already present so agin not copy that element
            x.append(a)
    return x
print (unique_list([1,2,3,3,3,3,4,5]))




#print('----------------------check it is palindrome are not-------')
#1.method
def palindrome(x):
    return x== x [::-1]

x = 'malayalam'
res = palindrome(x)
if res:
    print('yes')
else:
    print('no')





#print('---------------given no in the range or not-------------')
def test_range(n):
    if n in range(0,1000):
        print(' number in the range:',str(n))
    else:
        print('the number is out of range.')
test_range(11)



#print('---------------pascal  method-------------')

def solve(n):
    for i in range(n+1):
        for j in range (n-1):
            print(" ", end = " ")
        c = 1
        for j in range(1,i+1):
            print(" ",c ,sep ="", end="")
            c = c * (i-j)//j
        print()

n = 5
solve(n)






