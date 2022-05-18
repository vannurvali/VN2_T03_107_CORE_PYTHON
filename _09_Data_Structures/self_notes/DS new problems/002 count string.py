

#for loop method

print('---------------------count -----------')
x = input( 'enter any string :')
ma1 = 1
for i in range (ma1):
    ma1 = ma1 + 1
print('lentth of the charecter :',ma1)


# decision making method




# string count builtin method
str1 = 'hello bangalore'
print(str1.count ('e',0,len(str1)))
print(str1.count('o',0,len(str1)))



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
