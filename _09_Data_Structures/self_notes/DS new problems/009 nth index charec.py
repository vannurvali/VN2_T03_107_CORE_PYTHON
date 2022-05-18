

#1. method           check the 2nd position of index value
str = input('enter any string::')
str1 = " "
for i in range(len(str)):
    if i == 2:
        continue
    else:
        str1=str1+str[i]
print(str1)



#2.method       check the exact index position of charac
str = input('enter any string::')
str1 = " "
n = int(input('enter any position to remove character:' ))
for i in range(len(str)):
    if i == n:
        continue
    else:
        str1=str1+str[i]
print(str1)