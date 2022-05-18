

list = [10,1.2,False,'hello',[1,2,3,],(1,2,3,),{1:1,2:2},{1,2,3}]
print('----------hetiro--------------')
list1 = [1,2,2,3,4,4]
print('allow the duplicate :',list1)

list2 = [1,2,5,3,4,6,9,8]
print('insertion order :',list2)

list3 = [10,50,20,12,10,11]
print('insertion order :',list3)

print('----------------list is mutable---------')
list5 = [ 1,2,5,6,3,4]
print('mutable   :',list5)
list5[2] = 500
print('after replacing one element:',list5)




print('-----------------sequence operations-------------------')
list6 = [1,2.5,False,'hello massy',255]

print('indexing of 2nd ::',list6[2])
print ('indexing of 5th position :',list6[4])
print ('index of :', list6[3][4])

print('slicling of :',list6)
print ('slicing :',list6[0:3])
print ('slicing :',list6[:-1])

print('adding of two lists :',[1,2,3]+[4,5,6])
print('adding of two lists :',[12,15,10]+[1,2,3])

print ('multiplying :',[1,2,3]*3)
print ('multiplying :',('chaithu')*5)

print ('check the value :',10 in [10,20,30])
print ('check the value :',500 in [100,200,300])

print ('lenth of object:',len(list6))
print('lenth of object :',len(list6))

list7 = [1,2,4,6,8,9]
print('max value:',max(list7))
print('min value :',min(list7))



print('-------------------conversion-----------------')
x = 10
print('float of x :',float(x),type(x))
y = 20.4
print('int of y :',int(y),type(y))
z=0
print('bool :',bool(z),type(z))

xy = 12345
print(xy,type(xy))

xyz = [1,2,3,4,5,6,7,8,9]
print(xyz,type(xyz))

list5 = [ 30,15,12,47,86,23,54,21,13]
print(id(list5))
list5[2] = 500
print(list5)


print('before list :',list5,id(list5),id(list5[0]),id(list5[1]),id(list5[2]))
list5[1] = 1000
print('aftere list:',list5,id(list5),id(list5[0]),id(list5[1]),id(list5[2]))



print('-------------------------------------crud functions---------------')
list = (1,2,3,4,5,6)

list1 = (1,2,3,[12,30,20],(10,20,30),{12,13,14},{12:12,20:22})
print('list value:',list1)
print('list value :',list1[2])
print('list value :',list1[3])

print('---------------append------------'
      )