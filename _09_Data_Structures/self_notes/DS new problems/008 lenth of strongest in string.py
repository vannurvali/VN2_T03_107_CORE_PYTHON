#1. method
x = 'happy new year'
print('max lengh of string :',max(x))           # check the largest letter in charecter


#2. method
str = input('enter a line of string:')          # check the largest word in(hello how are you)
word = str.split()
largest=small=word[0]
for i in range (0,len (word)):
    if len(largest)<len(word[i]):
        largest = word[i]
print(largest)



#3.method
str = input('enter a line of string:')          # check the largest word in(hello how are you)
word = str.split()                                 # and check the small word
largest=small=word[0]
for i in range (0,len (word)):
    if len(largest)<len(word[i]):
        largest = word[i]
    if len(small)>len(word[i]):
        small = word[i]
print(largest)
print(small)






