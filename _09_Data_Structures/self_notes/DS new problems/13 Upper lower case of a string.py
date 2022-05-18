


#print('---------------------funtion for the upper case to lower case----------------')
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