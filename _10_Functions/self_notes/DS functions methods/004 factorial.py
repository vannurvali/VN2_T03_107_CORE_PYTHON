


#1.loop method
fact = 1
num = int(input('enter any number :'))
org = num
while num > 0:
    fact = fact*num
    num =num - 1
print('the factorial of ',ord,'is',fact)
#
#
# # 2.function method
# def factorial(a):
#     fact = 1
#     for p in range(a,0,-1):
#         fact = fact*p
#     return fact
#
# n =int(input('enter any number '))
# res = factorial(n)
# print('factorial of ',n,'is',res)
#
#
# #3.decision making method
# num = 5
# if num < 0:
#     print('factorial does not exists for nagative number')
# elif num == 0:
#     print('the factorial of 0 is 1')
# else:
#     for i in range(1,num+1):
#         factorial= num + i
#
#     print('factorial of',num,'is',factorial)
