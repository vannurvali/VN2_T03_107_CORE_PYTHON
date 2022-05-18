



print('------------remove odd values in charecter-------')
s = input('enter any number :')
s1 = ' '
for i in range(0,len(s)):
    if i%2 == 0:
        s1+=s[i]
print(s1)
