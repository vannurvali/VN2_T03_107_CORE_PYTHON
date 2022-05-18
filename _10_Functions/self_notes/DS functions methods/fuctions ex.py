

# i = 1
# while i<=5:
#     print(i)
#     i = i+1

#
# i = 0
# while i<= 5:
#     i = i+1
#     if (i ==3):
#         break
#     print(i)


# i = 5
# while i >= 5:
#     if (i!=5):
#         break
#         print(i)
#         i = i-1

#
# for i in range (1,10):
#     print(i+5)
#     if (i==3):
#         break
#
# i = 5
# while i <= 9:
#     i = i+1
#     if (i == 7):
#         continue
#     print(i)

# i = 1
# while i<=3:
#     i = i+1
#     if (i==1):
#         continue
#     print(i)

# i = 1
# while i <= 10:
#     i = i+1
#     if (i%2==0):
#         continue
#     print(i)


# i = 10
# while True:
#     i = i+1
#     if (i%2 == 0):
#         continue
#     else:
#         break
#  print(i)

x = int(input('enter any number ::'))
prime = True
for i in range(2,x):
    if x % i == 0:
        prime = False
        break
print(prime)