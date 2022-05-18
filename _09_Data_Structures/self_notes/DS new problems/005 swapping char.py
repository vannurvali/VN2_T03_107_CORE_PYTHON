



# using while loop method
message = 'code'
new =' '
n = len(message)
new += message[n-1]

i = 1
while (i < n-1):
    new += message[i]
    i = i +1
new += message[0]
print(new)




# using desion making statements
x = input()
new_name  = " "
for i in range (len(x)):
    if x[i].isupper():
        new_name += x[i].lower()
    elif x[i].islower():
        new_name += x[i].upper()
    else:
        new_name += x[i]
print(new_name)



#buitin method

str = 'hello bangalore'
print('after swapcase  method :',str.swapcase())