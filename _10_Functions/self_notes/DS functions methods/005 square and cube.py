
# 1.buitin method

num = int(input('enter any number :'))
square = num*num
print('square of given no is :',square)
cube = num*num*num
print('cube of given no is :',cube)

#2. decision making
num = int(input('enter any number:'))
f= 0
for i in range(1,num):
    if i*i == num:
        f = 1
        break
if f==1:
    print('number is perfect square ')
else:
    print('number is not perfect square')
