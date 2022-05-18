

#1.method
str = 'COMPUTER'
print(str)
print(str[-1:])
print(str[1:])
print(str[1:-1])
print(str[-1:]+str[1:-1]+str[:1])



#2. method               #input is hell0
def change_str(str):
    return str[-1:]+str[1:-1]+str[:1]
na = input('enter any string::')
print(change_str(na))


#3.method with loop
mes = 'code'
new = " "
n = len(mes)
new += mes[n-1]

while (i < n-1):
    new += mes[i]
    i = i+1
new += mes[0]
print(new)