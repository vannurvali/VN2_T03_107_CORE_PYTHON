print('-------------capitalize method-------------')

str1 = "hello premier league"
print ("normal sharing           :", str1)
print("after capitalize :",str1.capitalize())

ma = "deveoloped country"
print("after capitalize    :",ma.capitalize())


print('------------------center function------------')
ma1 = "bangalore"
ma2 = "hyderabd"
ma3 = "massy"
print(len(ma1.center(20,'$')))
print("after center functions   :", ma1.center(20, '$'))
print("after center fuctions    :", ma2.center(50, '#'))
print("after center fuctions    :", ma3.center(50 , '*'))


print('--------------count functionc---------')

str1 = "bangaloregoodcity"
print(str1[0:10])
print(str1[0:5])
print(str1[:5])
print(str1.count('o'))
print(str1.count('a'))
print(str1.count('y'))
print(str1.count('good'))
print(str1.count('bangalore'))
print('number of o in the strings     :',str1.count('o',0,17))


print('----------------encode---------')
str1 = 'hello bangalore'
str2 = str1.encode()
print('after encoded :',str2)
print('after decoded  :',str2.decode())

ma1 = 'hello hyderabad'
ma2 = str1.encode()
print('after encoded  :',ma2)
print('after decoded  :',ma2.decode())

x1 = 'hello australia'
x2 = x1.encode()
print('after encoded :',x2)
print('after decoded :',x2.decode())

print('-------upper------')

str1 = 'hello bangalore'
print(str1.upper())
str2 = 'hello massy'
print(str2.upper())

print('------------endswith and endpandtabs----------')
str1 = 'hello world'
print('if the normal string end with pe  :',str1.endswith('ld'))
print('if the normal string end with ld or not :',str1.endswith('l'))

print('-------------lower----------------------------')

str3 = 'MASSY'
print(str3.lower())
str3 = 'CHAITANYA AVILIGONDA'
print(str3.lower())



print('------------ljust------------------------')
str1 = 'massy'
print(str1.ljust(20,'$'))

str2 = 'maheshbabu'
print(str2.ljust(20,'*'))




print('-------------------join------------------------')
str4 = '****'
str5 = ['sky','is','blue']
print(str4.join(str5))



print('------------------------strioip-----------------')





print('---------------convertions--------')

x = 10
print(x,type(x),id(x))
x = 12.4
print(x,type(x),id(x))

# int----int()
x = 12.4
print("before  :",x, type(x))
print(int(x))
print("after  :",x, type(x))

# float ------float()
y = 2
print('before :',y, type(y))
print(float(y))
print('after  :',y ,type(y))

# bool----bool()
z = 0
print('before :',z,type(z))
print(bool(z))
print('after :',z ,type(z))

# string-----string
phone_no = 9849896744
print('before  :',phone_no,type(phone_no))
phone_no = str(phone_no)
print('after :',phone_no,type(phone_no))



print('-----------------------sequence operations------------------------------------------------')

msg = 'hello massy'
print('-------string with for loop--------')
for char in msg:
    print(char)


print('---------------string with for loop--------')
for char in msg[0:4]:
    print(char)

print('------------------string with for loop-----------')
for char in msg[: : -1]:
    print(char)



# sequence operations
print('----------------index method--------------')
msg = 'hello massy'
print('indexing of 2nd position of string::',msg[1])
print('print indexing of 9 and 10 position of string :',msg[9])
print('print indexing of -1 position :',msg[-1])

print('-----------------slicing method=---------------')
msg = 'hello massy'
print('slicing position of 2 to 5 :',msg[2:9])
print('slincing position of 1 to 5 :',msg[1:5])
print('slincing position of -1 to 5:',msg[-8:7])

print('----------------adding--------')
msg1 = 'massy'
msg2 = 'chaithu'
print('adding of two variable  :',msg1+msg2)
print('adding of two variable ::',msg2+msg1)

print('----------------multiplication method---------')
msg1 = 'massy'
print('multiply of two objects :',msg1 * 10)
msg2 = 'chaithu'
print('multiply of two objects:',msg2*5)

print('------------------------membership method----------------')
msg1 = 'hello massy'
print('h :','h' in msg1)
print('m :','m'in msg1)
print('z :','z'in msg1)


print('----------------------------lenth ------------------')
msg1 = 'hello massy'
print('length of object :',len(msg1))
msg2 = 'python project'
print('lenth of object :',len(msg2))


print('-----------max---------------')
msg1 = 'hello massy'
print(max(msg1))
msg2 = 'hello chaithu'
print(min(msg2))





