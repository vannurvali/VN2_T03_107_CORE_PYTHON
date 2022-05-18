


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
