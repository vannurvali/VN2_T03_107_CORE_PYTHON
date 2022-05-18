

#1.method
def palindrome(x):
    return x== x [::-1]

x = 'malayalam'
res = palindrome(x)
if res:
    print('yes')
else:
    print('no')


#2.method
x = 'malayalam'
c =''
for i in x:
    c = i+c
if (x==c ):
    print('yes')
else:
    print('no')


#3.method
p = ['happy','new','year']
result = list(filter(lambda x : (x == ''.join(reversed(x))),p))
print(result)

