


#print("----------2. Slicing---------")
# 2. Slicing :
message = 'HELLO-WORLD'
print("2 to 5 : ", message[2:5])
print("3 to 7 : ", message[3:7])
print("-9 to 5 : ", message[-9:5])


print('------------String slicing----------------')

string = input('enter any number')
def countlettersanddigit(string):

    lcount = dcount = 0

    for c in string:
        if c.isdigit():
            dcount +=1
        elif c.isalpha():
            lcount += 1
    return lcount,dcount

letters,digits = countlettersanddigit(string)
print('no of alphabets/ no of letter :',letters)
print('no of digits  :',digits)

