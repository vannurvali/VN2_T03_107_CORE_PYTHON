
#int
x=12
y=12355452
z=-15
print(type(x))
print(type(y))
print(type(z))

#float
x=102.5
y=444585.1
z=7702.1
print(type(x))
print(type(y))
print(type(z))


x = 12e4
y = 36e45
z = -396e456
print(type(x))
print(type(y))
print(type(z))

#complex
x = 3 + 8j
t = 6j
y = -8j
print(type(x))
print(type(t))
print(type(y))

#type_coversion
# complexs numbers not coverted to into another type
x = 10
y = 15.5
z = 5j
a = float(x)
b = complex(y)
c = int(y)
print(a)
print(b)
print(c)

#Import randm
# spicify the type of variable

x = int(53)
y = int(52.45)
z = int("3")
print(type(x))
print(type(y))
print(type(z))
print(x)
print(y)
print(z)

m = float(10.2)
n = float(12.0)
o = float("15.3")
print(type(m))
print(type(n))
print(type(o))
print(m)
print(n)
print(o)

d = str(12)
x = str(125)
f = str("3")
n = str("mani")
print(d)
print(x)
print(f)
print(n)
print(type(d))
print(type(x))
print(type(f))
print(type(n))

#string

v1= "hello world"
v2= "python"
print(v1)
print(v2)
print(v1[3])
print(v2[0:6:2])
print(v2[1:6:2])
print(v1[:5]+ " boom")

#list
list1=[1,2,3,4,5,6]
list2=['axe','ant','apple']
print(list1)
print(list1[3])
print(list2)
print(list2[2])
print(list1[0:3:2])

mylist=("apple", "banana", "cane")
print(mylist)
print(mylist[1])
print(mylist[2])
print(mylist[-2])
print(mylist[-3])

me=["apple", "orange", "mango", "pink", "yellow"]
print(me)
print(me[2:5])
print(me[0:3:5])
print(me[-4:-1])

tup=["tea", "cofee", "milk", "apple"]
print(tup)
print(tup[3])
print(tup[-3])
print(tup[0:3])

set1 = {"coffee", "tea","milk", "cat"}
print(set1)

list=["fan", "ac", "car"]
set1.update(list)
print(set1)


list=["fan", "cooler", "ac", "fridze"]
set1.update(list)
print(set1)
set1.remove("fan")
print(set1)


x=y=z=10
print("x")
print("type of x : "), type(x)
print("type of x : "), type(id)


x=10+20-45*43/2  # BODMAS RULE
print ("final value :",x)
print ("type of x : ", type(x))
print ( "id of x : ", id(x))

i_value= True
print("type of i_value : ",type(i_value))
print("type of i_value : ",id(i_value))

x=10
print("integer : ",type(x))
y=12.0
print("float : ", type(y))
z='14'
print("str : ",type(z) , id(z))

# type of conversations
a=0
print(bool(a))
print("convert int to float")
x=10
print("value : ",(x),type(x))

#covert to float

y=float(x)
print("value : ",(y), type(y))

a=0
print(bool(a))
print("covert int to float")
x=10
print("value : ",x,type(x))
y=float(x)
print("value : ",(y),type(y))

#convert int to boolan
x=10
print((x),type(x))
x=bool(x)
print(y, type(y))

x=14
print(x, type(x))
x=bool(x)
print(x, type(x))

x=0
print(x,type(x))
x=bool(x)

eid="10001"
print((eid,type(eid)))



#data structure
a='madhu nettam'
# 0123456789   n-1 positive index
#-n           -3,-2,-1   negitive index


print(a)
print("0th index value : ", a[0])
print("6th index value : ", a[6])
print("5th negative index value : ", a[-5])
print("4th negative index value : ", a[-4])
print("get partial name :", a[0:7])
print("get reverse string using negative indexing :", a[:-1])
print("get partial name : ", a[10:9])
print("get reverse string using negative indexing :", a[-3:-4])
print(a[-7:-1])

office=("vn solutions pvt ltd")
print(office)

list1=[110,23.5, True, "sachin tendulkar",[1,2,3],(1,2),{1:10,2:20},{1,2,3}]
print("list1 : ", id(list1))
print("index 3rd : ", id(list1[3]) )
print("index : ", id(list1[3][1]))
print("slice : ", list1[3][1:3])

tup1=(110,20.5,True,"massy",[1,2,3,4],(1,2),{1:10,2:20},{1,2,3})
print(tup1)
print("index : ", tup1)
print("index : ", tup1[3])
print("index : ", tup1[3], id(tup1[3][-1]))
