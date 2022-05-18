

# 1. replace using builtin methods
str ='hello bangalore is in india'
print('replace() : replace with given char')
print(str.replace("a", "@", 1))
print(str.replace("a", "@"))
print((str.replace("a", "@")).replace("i", "!"))



#2. using loop and desion making method       # check the index position of (hello balgalore)
str = input('enter the string :')
str1 = input('enter substring:')
for i in range (len(str)):
    for j in range (len(str1)):                     #finding the index position of world or element
        if str[i] == str1[j]:
            j =j +1
        else:
            j = 0
    if j == len(str1):
        f = 1
        print('substrig found at :',i- len(str1)+1)
if f == 0:
    print('not found')
