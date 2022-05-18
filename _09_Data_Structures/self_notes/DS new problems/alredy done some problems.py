
print('---------------------count -----------')
x = input( 'enter any string :')
ma1 = 1
for i in range (ma1):
    ma1 = ma1 + 1
print('lentth of the charecter :',ma1)





print('------------String slicing----------------')

string = input('enter any number')
def countlettersanddigit(string):

    lcount = dcount = 0

    for c in string:
        if c.isdigit():
            dcount +=1
        elif c.isalpha():
            lcount += 1
    return lcount,dcount

letters,digits = countlettersanddigits(string)
print('no of alphabets/ no of letter :',letters)
print('no of digits  :',digits)



print('---------printt of longest length in python ------------')

def longestwordlength (string):
    l = 0
    w = ' '
    words  = string.split()
    for word in words:
        if (len(word)) > l ) :
            w = words
            l = len(word)
        return (w,l)
string = input('enter the string :')
w , l = longestwordslegth(string)
print ('longest word is :',w )
print ('length of longest word is :' l)


#print('---------------------funtion for the upper case to lower case----------------')
x = input()
new_name  = " "
for i in range (len(x)):
    if x[i].isupper():
        new_name += x[i].lower()
    elif x[i].islower():
        new_name += x[i].upper()
    else:
        new_name += x[i]
print(new_name)

'''
'''

print('------------remove odd values in charecter-------')
s = input('enter any number :')
s1 = ' '
for i in range(0,len(s)):
    if i%2 == 0:
        s1+=s[i]
print(s1)

'''

'''
print('------------Count words in a string------------------')


str = input('enter line of string :')
str = str.split()
i = 0
while i<len(str):
    count = 0
    for j in str:
        if str[i]==j:
            count = count+1
    print(str[i],"present",count,"times")

    i = i+1

#print('---------------------funtion for the upper case to lower case----------------')


x = input()
new_name  = " "
for i in range (len(x)):
    if x[i].isupper():
        new_name += x[i].lower()
    elif x[i].islower():
        new_name += x[i].upper()
    else:
        new_name += x[i]
print(new_name)

'''
'''

print('------------------Last part of string-----------')


str = input('enter the string :')
str1 = input('enter substring:')
for i in range (len(str)):
    for j in range (len(str1)):
        if str[i] == str1[j]:
            j =j +1
        else:
            j = 0
    if j == len(str1):
        f = 1
        print('substrig found at :',i- len(str1)+1)
if f == 0:
    print('not found')





print('------------------slicing method -------------')


def change_str(str):
    return str[-1:]+str[1:-1]+str[:1]
na = input('enter any string::')
print(change_str(na))


str = ('COMPUTER')
print(str)
print(str[-1:]+str[1:-1]+str[:1])



print('---------------------conver given string into upper case---------------')
str = input('enter any string :')
new_name = ''
for i in range (len(str)):
    if str[i].islower() :
        new_name += str[i].isupper()
    else:
        new_name += str[i]
print('new_name')


'''

#8. print sum of list,tuple,set,dictionary
numbers = [2,5,8,4]
def sum(numbers):
    total = 0
    for i in numbers:
        total = total+0
    return total


print(sum(numbers))















