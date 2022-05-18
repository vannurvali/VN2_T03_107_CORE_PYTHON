
'''



#print ('--traversing method in for loop--')


print('-----------traversing method------------')
l = ['p','y','t','h','o','n']                # traversing means reverse the entaire program
for a in l:
    print (a)

#traversing with refer the index value



print('-----------------for loop--------------')
l = ['p','y','t','h','o','n']
length = len(l)
for a in range (length):   #a variable is going to read elements in the list
    print (a,l[a])




print('----------------while loop----------')
# traversing with while loop
l = ['p','y','t','h','o','n']
i = 0
while i < len(l):
    print(l[i])
    i = i + 1



print('------------find even--------')
#find the even no or odd
num = []
n = 10
for i in range (0,n):
    if i%2 ==0:
        print(i ,'is a even number')
    else:
        print(i,'is odd number')



print('-------------------append-------')
list = [1,2,3,4,5,6]
list.append(10)
print('after append :',list)     # adding of element to existing list is calld append..



print('------------extend------------')
list1 = [10,20,30,4,5,6]
print('before extend :',list)
list1.extend([10, 20, 30, ['a', 'v']])  #adding the elements end of the list
print('after extend :',list1)



print('--------------append and extend-------')
list1 = [1,2,3,4]
list1.append([10,20])    #adding the element of existing list
list1.extend([200,400])   # adding the elements end of the list
print('after appand & extend :',list1)



print('------------pop-----------')
list1 = [ 12,25,12,13,14,15,25,36]
print('before pop:',list1)  # removing of one element in the specified position
list1.pop(4)
print('after apply :',list1)



print('-------------remove-------------')
list1 = [10,2,20,30,41,52,63]
print('before remove :',list1)    # removing of element into the specified value
list1.remove(20)
print('after apply remove :',list1)



print('-----------insert-----------')
list1 = [14,25,12,15,14,16,20]
print('before :',list1)
list1.insert(0,100)
print('after :',list1)        # adding of element in to the index position
list1.insert(3,120)
print('after :',list1)



print('----------------reverse-------')
list1 = [1,2,3,4,5,6]
list1.reverse()
print('after reverse :',list1)


print('------------sort-------------')
list1 = [12,56,1,2,5,4,6,3,7,8,9]
list1.sort()   #acendig order
print('after acendig :',list1)



print('----------length ----------')
list1 = [1,2,3,4,5,7,8]
print('before :',list1)
print('after len :',len(list1))


print('----------count------------')
list1 = [1,5,6,7,8,9,10,12,2,2,2,23]
print ('befor :',list1)
print('after :',list1.count(2))


print(-----------index value---------')
list1 = [1,2,4,5,7,8,9,6,3]
print('before :',list1)
print('list index :',list1.index(9))



#Aliasing list
#print('-------------variable value can be assigned to the another variable-----')
#aliasing and cloning method
list1 = [81,82,83]
list2 = list1
print(list2)

'''

#cloning list
print('-------------create the copy of original list-------')
list1 = [1,2,3]
list3 = list1[:]
print(list3)











